"""Profile features added for the obesity journals, JCM and Cureus, and a build of every profile.

    python3 -m unittest discover -s scripts/tests -v
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent))


@unittest.skipUnless(shutil.which("pandoc"), "needs pandoc")
class ProfileFeatureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.kit = self.tmp / "kit"
        shutil.copytree(KIT, self.kit, ignore=shutil.ignore_patterns("outputs", "build", "__pycache__", "signoff"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def profile(self, body: dict, name="t"):
        (self.kit / "journals" / f"{name}.json").write_text(json.dumps({"extends": "generic-icmje", **body}))
        return name

    def run_py(self, *args):
        r = subprocess.run([sys.executable, *args], cwd=self.kit, capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    def validate(self, name, *extra):
        return self.run_py("scripts/validate.py", "--journal", name, *extra)[1]

    def edit(self, name, old, new):
        p = self.kit / "manuscript" / name
        p.write_text(p.read_text().replace(old, new))

    def test_soft_limit_warns_hard_limit_errors(self):
        soft = self.validate(self.profile({"main_text": {"limit": {"max": 100, "soft": True}}}))
        self.assertIn("WARN   main text", soft)
        self.assertIn("(guidance only)", soft)
        hard = self.validate(self.profile({"main_text": {"limit": {"max": 100}}}, "h"))
        self.assertIn("ERROR  main text", hard)

    def test_minimum_and_required_any(self):
        out = self.validate(self.profile({"main_text": {"limit": {"min": 9000},
                                                        "required_any": [["summary", "conclusions"]]}}))
        self.assertIn("minimum 9000", out)
        self.assertIn("needs at least one of: `{#summary}`, `{#conclusions}`", out)

    def test_bullet_items_counted(self):
        self.edit("04-discussion.md", "# Discussion {#discussion}",
                  "# Key points {#key-points}\n\n- one\n- two\n- three\n- four\n\n# Discussion {#discussion}")
        out = self.validate(self.profile({"section_limits": {"key-points": {"unit": "items", "max": 3}}}))
        self.assertIn("section key-points: 4 list items; limit 3", out)

    def test_banned_terms(self):
        self.edit("04-discussion.md", "statin use was associated", "obese patients using statins were")
        out = self.validate(self.profile({"style": {"banned_terms": [
            {"term": r"\bobese (?:patients|people)\b", "regex": True, "use": "patients with obesity"}]}}))
        self.assertIn("'obese patients' in discussion", out)
        self.assertIn("use: patients with obesity", out)

    def test_null_removes_inherited_article_type_and_checks_accumulate(self):
        name = self.profile({"human_checks": ["journal-wide check"],
                             "article_types": {"case-report": None,
                                               "review": {"human_checks": ["review-only check"]}}})
        sys.path.insert(0, str(self.kit / "scripts"))
        import importlib
        import common as Cm
        importlib.reload(Cm)
        Cm.JOURNALS = self.kit / "journals"
        p = Cm.load_profile(name, "case-report")
        self.assertFalse(p["_article_type_known"])
        r = Cm.load_profile(name, "review")
        self.assertIn("journal-wide check", r["human_checks"])
        self.assertIn("review-only check", r["human_checks"])

    def test_conditional_declarations(self):
        name = self.profile({"conditional_declarations": {"informed-consent": ["humans"]}})
        self.assertIn("missing `{#informed-consent}`", self.validate(name))
        md = self.kit / "manuscript" / "metadata.yaml"
        md.write_text(md.read_text().replace("involves: [humans]", "involves: []"))
        self.assertNotIn("informed-consent", self.validate(name))

    def test_running_title_forbidden_and_alt_abstract_dropped(self):
        name = self.profile({"title": {"running_title_allowed": False}})
        self.assertIn("does not accept a running title", self.validate(name))
        code, out = self.run_py("scripts/build.py", "--journal", name, "--force")
        self.assertEqual(code, 0, out)
        text = subprocess.run(["pandoc", str(next((self.kit / "outputs" / name).glob("*_manuscript.docx"))),
                               "-t", "plain"], capture_output=True, text=True).stdout
        self.assertNotIn("Running title", text)
        self.assertNotIn("Resumo", text)  # second-language abstract only for bilingual journals

    def test_title_page_sections_inside_manuscript(self):
        name = self.profile({"submission": {"separate_title_page": False, "blinded": False,
                                            "title_page_sections": ["funding"], "title_page_copies": ["ethics"]}})
        code, out = self.run_py("scripts/build.py", "--journal", name, "--force")
        self.assertEqual(code, 0, out)
        text = subprocess.run(["pandoc", str(next((self.kit / "outputs" / name).glob("*_manuscript.docx"))),
                               "-t", "plain"], capture_output=True, text=True).stdout
        head, body = text.split("Introduction", 1)
        self.assertIn("Funding", head)
        self.assertNotIn("Funding", body)   # moved
        self.assertIn("Ethics", head)
        self.assertIn("Ethics", body)       # copied

    def test_every_profile_builds(self):
        for p in sorted((self.kit / "journals").glob("*.json")):
            if p.stem in ("t", "h"):
                continue
            code, out = self.run_py("scripts/build.py", "--journal", p.stem, "--force")
            self.assertEqual(code, 0, f"{p.stem}: {out}")


if __name__ == "__main__":
    unittest.main()
