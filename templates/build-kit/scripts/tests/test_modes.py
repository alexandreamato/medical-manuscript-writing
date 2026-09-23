"""Draft vs submission mode, sign-off, and estimate/CI consistency.

    python3 -m unittest discover -s scripts/tests -v
"""

from __future__ import annotations

import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent))

import validate as V  # noqa: E402


class TripleTests(unittest.TestCase):
    def test_forms_that_must_match(self):
        forms = ["adjusted hazard ratio 0.72, 95% confidence interval 0.55 to 0.94",
                 "razão de risco ajustada 0,72, intervalo de confiança de 95% 0,55 a 0,94",
                 "HR 0.72, 95% CI 0.55 to 0.94", "| 0.72 (0.55 to 0.94) |"]
        for f in forms:
            self.assertEqual(V.ci_triples(f), {("0.72", "0.55", "0.94")}, f)

    def test_ranges_and_years_are_not_estimates(self):
        self.assertEqual(V.ci_triples("recruited from 2018 to 2020, aged 40 to 60"), set())


@unittest.skipUnless(shutil.which("pandoc"), "needs pandoc")
class SubmissionGateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.kit = self.tmp / "kit"
        shutil.copytree(KIT, self.kit, ignore=shutil.ignore_patterns("outputs", "build", "__pycache__", "signoff"))
        # Verification results of the bundled example, dated today so they are fresh.
        vp = self.kit / "references.verified.json"
        ver = json.loads(vp.read_text())
        for v in ver.values():
            v["checked_at"] = dt.date.today().isoformat()
        vp.write_text(json.dumps(ver))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def validate(self, *extra):
        r = subprocess.run([sys.executable, "scripts/validate.py", "--journal", "jvb", *extra], cwd=self.kit,
                           capture_output=True, text=True)
        return r.returncode, r.stdout

    def test_draft_passes_submission_blocks_until_resolved(self):
        code, out = self.validate()
        self.assertEqual(code, 0, out)

        code, out = self.validate("--submission")
        self.assertNotEqual(code, 0)
        self.assertIn("example: true", out)
        self.assertIn("not ticked in signoff/jvb.md", out)

        # Tick every item and sign; only the example flag remains.
        so = self.kit / "signoff" / "jvb.md"
        text = so.read_text().replace("- [ ] ", "- [x] ").replace("[name], [YYYY-MM-DD]", "A. Author, 2026-09-23")
        so.write_text(text)
        code, out = self.validate("--submission")
        self.assertEqual(re.findall(r"^ERROR.*$", out, re.M), [
            next(l for l in out.splitlines() if l.startswith("ERROR  example"))])

        # Removing the flag changes the content: the sign-off no longer vouches for it.
        md = self.kit / "manuscript" / "metadata.yaml"
        md.write_text(re.sub(r"^example: true.*\n", "", md.read_text(), flags=re.M))
        code, out = self.validate("--submission")
        self.assertNotEqual(code, 0)
        self.assertIn("content changed since the sign-off (manuscript/metadata.yaml)", out)
        self.assertNotIn("- [x]", so.read_text())  # every tick cleared

        # Review again, sign again: now it passes.
        so.write_text(so.read_text().replace("- [ ] ", "- [x] ").replace("[name], [YYYY-MM-DD]",
                                                                         "A. Author, 2026-09-24"))
        code, out = self.validate("--submission")
        self.assertEqual(code, 0, out)

    def test_unverified_reference_blocks_submission_only(self):
        (self.kit / "references.verified.json").write_text("{}")
        code, out = self.validate()
        self.assertEqual(code, 0)
        self.assertIn("WARN   references", out)
        code, out = self.validate("--submission")
        self.assertIn("[blocks submission]", out)


if __name__ == "__main__":
    unittest.main()
