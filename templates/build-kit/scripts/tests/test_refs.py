"""Reference verification with simulated Crossref/PubMed answers (no network).

    python3 -m unittest discover -s scripts/tests -v
"""

from __future__ import annotations

import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import common as C  # noqa: E402
import refs  # noqa: E402
import validate as V  # noqa: E402

REF_PMID = {"id": "smith2020trial", "type": "article-journal", "title": "A trial of something in someone",
            "author": [{"family": "Smith", "given": "J"}], "issued": {"date-parts": [[2020]]}, "PMID": "111"}
REF_DOI = {"id": "jones2019cohort", "type": "article-journal", "title": "A cohort of people",
           "author": [{"family": "Jones", "given": "A"}], "issued": {"date-parts": [[2019]]},
           "DOI": "10.1000/xyz", "PMID": "222"}


def pubmed(pmid, title, year, first, pubtype=("Journal Article",)):
    return {"result": {pmid: {"title": title, "pubdate": f"{year} Jan 5", "pubtype": list(pubtype),
                              "authors": [{"name": first, "authtype": "Author"}]}}}


def crossref(title, year, family, updated_by=()):
    return {"message": {"title": [title], "issued": {"date-parts": [[year]]},
                        "author": [{"family": family}], "updated-by": list(updated_by)}}


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.p = [mock.patch.object(C, "REFERENCES", self.tmp / "references.json"),
                  mock.patch.object(C, "VERIFIED", self.tmp / "references.verified.json"),
                  mock.patch.object(refs.time, "sleep", lambda s: None)]
        for x in self.p:
            x.start()

    def tearDown(self):
        for x in self.p:
            x.stop()

    def write_refs(self, *records):
        C.REFERENCES.write_text(json.dumps(list(records)))

    def verify(self, answers, *argv):
        """Run `refs.py verify`; `answers` maps a URL fragment to a response,
        an Exception instance to raise, or None for 'not found'."""
        def fake_get(url, accept="application/json", retries=3):
            for frag, ans in answers.items():
                if frag in url:
                    if isinstance(ans, Exception):
                        raise ans
                    return ans
            raise AssertionError(f"unexpected URL {url}")

        with mock.patch.object(refs, "get", fake_get), mock.patch.object(sys, "argv", ["refs.py", "verify", *argv]):
            with self.assertRaises(SystemExit) as cm:
                refs.main()
        return cm.exception.code, C.load_verified()


class VerifyTests(Base):
    def test_pmid_only_wrong_year_and_author_is_mismatch(self):
        # Title matches, year and first author do not: this used to pass as "ok".
        self.write_refs(REF_PMID)
        code, ver = self.verify({"esummary": pubmed("111", REF_PMID["title"], 2015, "Brown K")})
        self.assertEqual(ver["smith2020trial"]["status"], "mismatch")
        self.assertIn("year", ver["smith2020trial"]["notes"])
        self.assertIn("first author", ver["smith2020trial"]["notes"])
        self.assertEqual(code, 1)

    def test_pmid_only_correct_is_ok(self):
        self.write_refs(REF_PMID)
        code, ver = self.verify({"esummary": pubmed("111", REF_PMID["title"] + ".", 2020, "Smith J")})
        self.assertEqual(ver["smith2020trial"]["status"], "ok")
        self.assertEqual(code, 0)

    def test_network_failure_is_incomplete_and_nonzero(self):
        self.write_refs(REF_PMID)
        code, ver = self.verify({"esummary": OSError("connection reset")})
        self.assertEqual(ver["smith2020trial"]["status"], "incomplete")
        self.assertEqual(code, 3)

    def test_one_source_unreachable_is_incomplete_even_if_other_ok(self):
        self.write_refs(REF_DOI)
        code, ver = self.verify({"api.crossref.org": crossref(REF_DOI["title"], 2019, "Jones"),
                                 "esummary": TimeoutError("timed out")})
        self.assertEqual(ver["jones2019cohort"]["status"], "incomplete")
        self.assertEqual(code, 3)

    def test_retraction_found_by_crossref(self):
        self.write_refs(REF_DOI)
        code, ver = self.verify({
            "api.crossref.org": crossref(REF_DOI["title"], 2019, "Jones",
                                         [{"type": "retraction", "DOI": "10.1000/ret"}]),
            "esummary": pubmed("222", REF_DOI["title"], 2019, "Jones A")})
        self.assertEqual(ver["jones2019cohort"]["status"], "retracted")
        self.assertEqual(code, 1)

    def test_one_year_gap_is_check_not_mismatch(self):
        self.write_refs(REF_PMID)
        code, ver = self.verify({"esummary": pubmed("111", REF_PMID["title"], 2021, "Smith J")})
        self.assertEqual(ver["smith2020trial"]["status"], "check")
        self.assertEqual(code, 0)

    def test_fresh_verification_is_skipped_stale_is_rechecked(self):
        self.write_refs(REF_PMID)
        fp = C.ref_fingerprint(REF_PMID)
        good = pubmed("111", REF_PMID["title"], 2020, "Smith J")
        for days, expect_calls in ((10, 0), (120, 1)):
            C.VERIFIED.write_text(json.dumps({"smith2020trial": {
                "status": "ok", "fingerprint": fp,
                "checked_at": (dt.date.today() - dt.timedelta(days=days)).isoformat()}}))
            calls = []
            answers = {"esummary": good}
            with mock.patch.object(refs, "fetch", side_effect=lambda u: calls.append(u) or answers["esummary"]):
                self.verify(answers)
            self.assertEqual(len(calls), expect_calls, f"verified {days} days ago")

    def test_manual_reference_and_its_expiry(self):
        self.write_refs()
        argv = ["refs.py", "add-manual", "--key", "who2023report", "--type", "report",
                "--org", "World Health Organization", "--title", "A report", "--year", "2023",
                "--url", "https://www.who.int/example", "--by", "Tester", "--evidence", "official PDF imprint"]
        with mock.patch.object(sys, "argv", argv):
            refs.main()
        ver = C.load_verified()
        self.assertEqual(ver["who2023report"]["status"], "manual")
        # Fresh manual checks are left alone...
        code, ver = self.verify({})
        self.assertEqual(ver["who2023report"]["status"], "manual")
        self.assertEqual(code, 0)
        # ...expired ones are flagged, never silently kept.
        ver["who2023report"]["checked_at"] = (dt.date.today() - dt.timedelta(days=200)).isoformat()
        C.VERIFIED.write_text(json.dumps(ver))
        code, ver = self.verify({})
        self.assertEqual(ver["who2023report"]["status"], "stale")
        self.assertEqual(code, 3)

    def test_manual_requires_url_or_isbn(self):
        self.write_refs()
        argv = ["refs.py", "add-manual", "--key", "x2020", "--type", "book", "--title", "T",
                "--by", "Tester", "--evidence", "e"]
        with mock.patch.object(sys, "argv", argv), self.assertRaises(SystemExit) as cm:
            refs.main()
        self.assertEqual(cm.exception.code, 2)


def cite_doc(*keys):
    """Minimal pandoc AST: one paragraph citing `keys`."""
    cits = [{"citationId": k, "citationPrefix": [], "citationSuffix": [], "citationMode": {"t": "NormalCitation"},
             "citationNoteNum": 0, "citationHash": 0} for k in keys]
    return {"meta": {}, "blocks": [{"t": "Para", "c": [{"t": "Cite", "c": [cits, [{"t": "Str", "c": "[@x]"}]]}]}]}


class ValidatorTests(Base):
    PROFILE = {"id": "t", "generic": True, "abstract": {"required": False}, "main_text": {},
               "required_declarations": [], "references": {}}

    def run_validator(self, status, days=0, ref=REF_PMID):
        self.write_refs(ref)
        C.VERIFIED.write_text(json.dumps({ref["id"]: {
            "status": status, "notes": "n", "fingerprint": C.ref_fingerprint(ref),
            "checked_at": (dt.date.today() - dt.timedelta(days=days)).isoformat()}}))
        rep, _ = V.validate(dict(self.PROFILE), cite_doc(ref["id"]))
        return [(lv, m) for lv, w, m in rep.items if w == "references"]

    def test_levels(self):
        self.assertEqual(self.run_validator("ok"), [])
        self.assertEqual(self.run_validator("mismatch")[0][0], "ERROR")
        self.assertEqual(self.run_validator("retracted")[0][0], "ERROR")
        self.assertEqual(self.run_validator("incomplete")[0][0], "WARN")
        self.assertEqual(self.run_validator("check")[0][0], "WARN")
        old = self.run_validator("ok", days=200)
        self.assertEqual(old[0][0], "WARN")
        self.assertIn("days ago", old[0][1])

    def test_manual_source_without_identifier_is_accepted(self):
        manual = {"id": "r1", "type": "report", "title": "T", "URL": "https://example.org"}
        self.assertEqual(self.run_validator("manual", ref=manual), [])
        self.write_refs(manual)
        C.VERIFIED.write_text("{}")
        rep, _ = V.validate(dict(self.PROFILE, references={"require_identifier": True}), cite_doc("r1"))
        self.assertEqual([lv for lv, w, _ in rep.items if w == "references"], ["ERROR"])


if __name__ == "__main__":
    unittest.main()
