"""Regression tests for checks that must never pass silently.

    python3 -m unittest discover -s scripts/tests -v

Each test is a case where an earlier version gave false confidence:
intervals dropped instead of flagged, estimates matched in the wrong
section, a CI divergence that did not block submission, author data in
document properties, and a renderer failure that went unreported.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
KIT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent))

import preview as P  # noqa: E402
import validate as V  # noqa: E402


class IntervalExtractionTests(unittest.TestCase):
    def test_integer_estimates_are_extracted(self):
        self.assertEqual(V.ci_triples("HR 2, 95% CI 1 to 3"), {("2", "1", "3")})

    def test_suspicious_intervals_are_kept_and_flagged(self):
        inverted = V.ci_extract("HR 0.72 (0.94 to 0.55)")
        outside = V.ci_extract("HR 1.20 (0.55 to 0.94)")
        self.assertEqual(inverted[0]["issue"], "lower limit above upper limit")
        self.assertEqual(outside[0]["issue"], "estimate outside its interval")

    def test_equal_values_compare_equal(self):
        self.assertEqual(V.ci_triples("0.720 (0.55 to 0.940)"), V.ci_triples("0,72 (0,55 a 0,94)"))


@unittest.skipUnless(shutil.which("pandoc"), "needs pandoc")
class KitCopy(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.kit = self.tmp / "kit"
        shutil.copytree(KIT, self.kit, ignore=shutil.ignore_patterns("outputs", "build", "__pycache__", "signoff"))
        vp = self.kit / "references.verified.json"
        ver = json.loads(vp.read_text())
        for v in ver.values():
            v["checked_at"] = dt.date.today().isoformat()
        vp.write_text(json.dumps(ver))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def edit(self, name, old, new):
        p = self.kit / "manuscript" / name
        s = p.read_text()
        self.assertIn(old, s)
        p.write_text(s.replace(old, new))

    def run_py(self, *args):
        r = subprocess.run([sys.executable, *args], cwd=self.kit, capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr


class EstimateConsistencyTests(KitCopy):
    def diverge(self):
        # The Results and the table now report 0.70; the abstract still says 0.72.
        self.edit("03-results.md", "HR 0.72, 95% CI 0.55 to 0.94", "HR 0.70, 95% CI 0.55 to 0.94")
        self.edit("03-results.md", "0.72 (0.55 to 0.94)", "0.70 (0.55 to 0.94)")

    def test_estimate_only_in_discussion_does_not_count(self):
        self.diverge()
        self.edit("04-discussion.md", "In this cohort,", "In this cohort (HR 0.72, 95% CI 0.55 to 0.94),")
        code, out = self.run_py("scripts/validate.py", "--journal", "jvb")
        self.assertIn("estimate 0.72 (95% CI 0.55 to 0.94) not found", out)

    def test_divergence_blocks_submission_until_resolved_with_reason(self):
        self.diverge()
        code, out = self.run_py("scripts/validate.py", "--journal", "jvb")
        self.assertIn("WARN   abstract: estimate 0.72", out)            # a draft only warns
        code, out = self.run_py("scripts/validate.py", "--journal", "jvb", "--submission")
        self.assertRegex(out, r"ERROR  abstract: estimate 0\.72.*resolve it with a reason")
        so = self.kit / "signoff" / "jvb.md"
        text = so.read_text()
        self.assertIn("## Warnings to resolve", text)
        # Ticking without a reason is not enough...
        text = re.sub(r"- \[ \] (abstract: estimate 0\.72[^\n]*\| because:)", r"- [x] \1", text)
        so.write_text(text)
        code, out = self.run_py("scripts/validate.py", "--journal", "jvb", "--submission")
        self.assertRegex(out, r"ERROR  abstract: estimate 0\.72")
        # ...a reason without a location is not enough either...
        text = so.read_text()
        text = re.sub(r"- \[[ x]\] (abstract: estimate 0\.72[^\n]*?\| because:)[^\n]*",
                      r"- [x] \1 checked, it is fine", text)
        so.write_text(text)
        code, out = self.run_py("scripts/validate.py", "--journal", "jvb", "--submission")
        self.assertIn("the reason must say where the checked value is", out)
        # ...a located reason resolves it (the sign-off is rewritten each run: tick it again).
        text = so.read_text()
        text = re.sub(r"- \[[ x]\] (abstract: estimate 0\.72[^\n]*?\| because:)[^\n]*",
                      r"- [x] \1 abstract gives the adjusted estimate, Table 2 the crude one", text)
        so.write_text(text)
        code, out = self.run_py("scripts/validate.py", "--journal", "jvb", "--submission")
        self.assertIn("[resolved in sign-off: abstract gives the adjusted estimate", out)
        self.assertNotRegex(out, r"ERROR  abstract: estimate 0\.72")

    def test_suspicious_interval_reported(self):
        self.edit("03-results.md", "HR 0.72, 95% CI 0.55 to 0.94", "HR 0.72, 95% CI 0.94 to 0.55")
        code, out = self.run_py("scripts/validate.py", "--journal", "jvb")
        self.assertIn("suspicious interval", out)
        self.assertIn("lower limit above upper limit", out)


class LevelAndSpreadTests(unittest.TestCase):
    def test_confidence_levels_captured(self):
        for lvl in ("90", "95", "99"):
            x = V.ci_extract(f"HR 0.72, {lvl}% CI 0.55 to 0.94")
            self.assertEqual((x[0]["triple"], x[0]["level"]), (("0.72", "0.55", "0.94"), lvl))

    def test_median_iqr_is_not_an_estimate(self):
        self.assertEqual(V.ci_triples("Median 12 (8 to 18)"), set())
        self.assertEqual(V.ci_extract("age, median (IQR) 63 (55 to 70)")[0]["kind"], "spread")


class BibliographyAfterOmissionTests(KitCopy):
    def test_reference_cited_only_in_omitted_section_is_dropped(self):
        # Vandenbroucke cited only in the acknowledgments, which the blinded JVB file omits.
        self.edit("05-declarations.md", "We thank the clinic nurses.",
                  "We thank the clinic nurses [@vandenbroucke2007strengthening].")
        self.edit("01-introduction.md", "[@vonelm2007strengthening; @vandenbroucke2007strengthening]",
                  "[@vonelm2007strengthening]")
        code, out = self.run_py("scripts/build.py", "--journal", "jvb", "--force")
        self.assertEqual(code, 0, out)
        ms = next((self.kit / "outputs" / "jvb").glob("*_manuscript.docx"))
        text = subprocess.run(["pandoc", str(ms), "-t", "plain", "--wrap=none"], capture_output=True, text=True).stdout
        refs = [l for l in text.splitlines() if re.match(r"^\d+\. ", l)]
        self.assertEqual(len(refs), 2, refs)
        self.assertFalse(any("Vandenbroucke JP, von Elm E" in r for r in refs))
        self.assertIn("statement¹", text.replace(" ", ""))  # first visible citation is number 1


class AnonymityTests(KitCopy):
    def test_no_metadata_in_document_properties(self):
        code, out = self.run_py("scripts/build.py", "--journal", "jvb")
        self.assertEqual(code, 0, out)
        ms = self.kit / "outputs" / "jvb" / "statins-ulcer_jvb_manuscript.docx"
        with zipfile.ZipFile(ms) as z:
            props = " ".join(z.read(n).decode() for n in z.namelist() if n.startswith("docProps/"))
        self.assertNotIn("/Users/", props)
        self.assertNotIn(str(self.kit), props)
        self.assertNotIn("Ana Example", props)

    def test_identity_found_outside_the_body(self):
        # A footnote naming an author, in a blinded manuscript.
        self.edit("04-discussion.md", "baseline.", "baseline.^[Data from Placeholder's clinic.]")
        code, out = self.run_py("scripts/build.py", "--journal", "jvb")
        self.assertEqual(code, 0, out)
        code, out = self.run_py("scripts/preview.py", "--journal", "jvb")
        self.assertIn("author identity in word/footnotes.xml: Placeholder", out)
        self.assertNotEqual(code, 0)

    def test_local_path_pattern(self):
        self.assertTrue(P.LOCAL_PATH.search("csl /Users/someone/Dropbox/x.csl"))
        self.assertTrue(P.LOCAL_PATH.search(r"C:\Users\someone\x.docx"))


class ReferenceDocxTests(KitCopy):
    def test_styles_applied_or_loud_failure(self):
        sys.path.insert(0, str(self.kit / "scripts"))
        import importlib
        import common as Cm
        import refdocx as R
        importlib.reload(Cm)
        importlib.reload(R)
        R.C.BUILD = self.kit / "build"
        out = R.ensure("t", {"font": "Arial", "line_spacing": 1.5, "paper": "letter"})
        xml = zipfile.ZipFile(out).read("word/styles.xml").decode()
        self.assertIn('w:ascii="Arial"', xml)
        self.assertIn('w:line="360"', xml)
        # A reference.docx whose styles no longer match the patches must stop the build.
        with mock.patch.object(R, "_styles", lambda x, s: x), mock.patch.object(R.C, "die", side_effect=SystemExit):
            (self.kit / "build").mkdir(exist_ok=True)
            for f in (self.kit / "build").glob("reference-*"):
                f.unlink()
            with self.assertRaises(SystemExit):
                R.ensure("u", {"font": "Arial"})


class RefsAddTests(unittest.TestCase):
    def test_group_author_kept_and_key_suffix(self):
        import refs as RF
        a = RF.clean({"title": "T", "author": [{"family": "Smith", "given": "J"}, {"name": "for the X Group"}]})
        self.assertEqual(a["author"][1], {"literal": "for the X Group"})
        taken = {"smith2020trial"}
        ref = {"author": [{"family": "Smith"}], "issued": {"date-parts": [[2020]]}, "title": "Trial outcomes"}
        self.assertEqual(RF.make_key(ref, taken), "smith2020outcomes")
        ref2 = {"author": [{"family": "Smith"}], "issued": {"date-parts": [[2020]]}, "title": "Outcomes"}
        self.assertEqual(RF.make_key(ref2, {"smith2020outcomes"}), "smith2020outcomesa")

    def test_network_failure_on_add_is_reported(self):
        import refs as RF
        tmp = Path(tempfile.mkdtemp())
        with mock.patch.object(RF.C, "REFERENCES", tmp / "r.json"), \
                mock.patch.object(RF, "fetch_doi", side_effect=RF.urllib.error.URLError("offline")), \
                mock.patch.object(sys, "argv", ["refs.py", "add", "10.1000/x"]):
            with self.assertRaises(SystemExit) as cm:
                RF.main()
        self.assertEqual(cm.exception.code, 3)
        shutil.rmtree(tmp, ignore_errors=True)


class OrcidTests(unittest.TestCase):
    def test_check_digit(self):
        self.assertTrue(V.orcid_checksum_ok("0000-0002-1825-0097"))
        self.assertFalse(V.orcid_checksum_ok("0000-0002-1825-0098"))


class CliRegressionTests(KitCopy):
    def test_duplicate_orcid_is_an_error(self):
        md = self.kit / "manuscript" / "metadata.yaml"
        md.write_text(md.read_text().replace("0000-0001-2345-6789", "0000-0002-1825-0097"))
        code, out = self.run_py("scripts/validate.py", "--journal", "jvb")
        self.assertIn("have the same ORCID 0000-0002-1825-0097", out)
        self.assertEqual(code, 1)

    def test_compare_exit_code(self):
        code, out = self.run_py("scripts/validate.py", "--compare")
        self.assertEqual(code, 1)          # the example has gaps in several profiles by design
        for p in (self.kit / "journals").glob("*.json"):
            if p.stem not in ("jvb", "generic-icmje", "example-journal-b"):
                p.unlink()
        code, out = self.run_py("scripts/validate.py", "--compare")
        self.assertEqual(code, 0, out)     # no profile with errors: exit 0

    def test_refs_add_not_found_and_bad_json(self):
        import refs as RF
        tmp = Path(tempfile.mkdtemp())
        with mock.patch.object(RF.C, "REFERENCES", tmp / "r.json"), mock.patch.object(RF, "fetch_doi", return_value=None), \
                mock.patch.object(sys, "argv", ["refs.py", "add", "10.1000/none"]):
            with self.assertRaises(SystemExit) as cm:
                RF.main()
        self.assertEqual(cm.exception.code, 1)
        with mock.patch.object(RF.C, "REFERENCES", tmp / "r.json"), \
                mock.patch.object(RF, "fetch_doi", side_effect=json.JSONDecodeError("html", "<html>", 0)), \
                mock.patch.object(sys, "argv", ["refs.py", "add", "10.1000/x"]):
            with self.assertRaises(SystemExit) as cm:
                RF.main()
        self.assertEqual(cm.exception.code, 3)
        shutil.rmtree(tmp, ignore_errors=True)


class RenderStatusTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.docx = self.tmp / "a.docx"
        self.docx.write_bytes(b"not really a docx")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_missing_renderer_is_a_warning(self):
        rep = V.Report("t")
        with mock.patch.object(P.shutil, "which", lambda name: None):
            self.assertIsNone(P.render(self.docx, self.tmp, rep, "a.docx"))
        self.assertEqual([lv for lv, _, _ in rep.items], ["WARN"])

    def test_failing_renderer_is_an_error(self):
        fake = self.tmp / "soffice"
        fake.write_text("#!/bin/sh\necho 'conversion failed' >&2\nexit 1\n")
        fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
        rep = V.Report("t")
        with mock.patch.object(P.shutil, "which", lambda name: str(fake) if name == "soffice" else None):
            self.assertIsNone(P.render(self.docx, self.tmp, rep, "a.docx"))
        self.assertTrue(any(lv == "ERROR" and "LibreOffice failed" in m for lv, _, m in rep.items), rep.items)


if __name__ == "__main__":
    unittest.main()
