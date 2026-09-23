"""Revision rounds: word-level marking and the full journal round trip.

    python3 -m unittest discover -s scripts/tests -v

The end-to-end test needs git and pandoc; it copies the kit into a temporary
git repository, simulates a journal that returns our file with a tracked
insertion, a reviewer comment and an untracked copy-edit, and runs
start -> import -> reconcile -> base -> revise -> check -> build.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE.parent.parent
sys.path.insert(0, str(HERE.parent))

import revdiff  # noqa: E402


def para(*inlines):
    return {"t": "Para", "c": list(inlines)}


def words(text):
    out = []
    for k, w in enumerate(text.split()):
        if k:
            out.append({"t": "Space"})
        out.append({"t": "Str", "c": w})
    return out


def cite(key, note=1):
    return {"t": "Cite", "c": [[{"citationId": key, "citationPrefix": [], "citationSuffix": [],
                                 "citationMode": {"t": "NormalCitation"}, "citationNoteNum": note,
                                 "citationHash": note}], [{"t": "Str", "c": f"[@{key}]"}]]}


def doc(*blocks):
    return {"meta": {}, "blocks": list(blocks)}


def spans(d, style):
    found = []

    def walk(n):
        if isinstance(n, list):
            for x in n:
                walk(x)
        elif isinstance(n, dict):
            if n.get("t") == "Span" and ["custom-style", style] in n["c"][0][2]:
                found.append(n["c"][1])
            if isinstance(n.get("c"), (list, dict)):
                walk(n["c"])

    walk(d["blocks"] if isinstance(d, dict) and "blocks" in d else d)
    return found


class MarkingTests(unittest.TestCase):
    def test_citation_renumbering_is_not_a_change(self):
        old = doc(para(*words("First"), {"t": "Space"}, cite("a", 1)), para(*words("Second"), cite("b", 2)))
        new = doc(para(*words("First")), para(*words("Second"), cite("b", 1)))
        _, m = revdiff.annotate(new, old, "color", "strike", "A", "D")
        self.assertEqual(m.deleted_words, 1)   # only the removed citation
        self.assertEqual(m.inserted_words, 0)  # the second paragraph did not change

    def test_deleted_citation_is_neutralised(self):
        old = doc(para(*words("Known fact"), {"t": "Space"}, cite("a")))
        new = doc(para(*words("Known fact")))
        out, _ = revdiff.annotate(new, old, "color", "strike", "A", "D")
        deleted = spans(out, revdiff.DEL_STYLE)
        self.assertTrue(deleted)
        self.assertNotIn("Cite", json.dumps(deleted))
        self.assertIn("[citation]", json.dumps(deleted))

    def test_insertion_marked_and_word_level(self):
        old = doc(para(*words("adjusted for age and sex.")))
        new = doc(para(*words("adjusted for age, sex and diabetes.")))
        out, m = revdiff.annotate(new, old, "color", "strike", "A", "D")
        ins = " ".join(revdiff_text(x) for x in spans(out, revdiff.INS_STYLE))
        self.assertIn("diabetes", ins)
        self.assertNotIn("adjusted", ins)

    def test_omit_mode_drops_deletions(self):
        old = doc(para(*words("Keep this.")), para(*words("Drop this paragraph.")))
        new = doc(para(*words("Keep this.")))
        out, m = revdiff.annotate(new, old, "color", "omit", "A", "D")
        self.assertEqual(len(out["blocks"]), 1)
        self.assertGreater(m.deleted_words, 0)

    def test_tracked_mode_uses_insertion_class(self):
        old = doc(para(*words("A.")))
        new = doc(para(*words("A. B.")))
        out, _ = revdiff.annotate(new, old, "tracked", "strike", "Authors", "2026-01-01T00:00:00Z")
        self.assertIn('"insertion"', json.dumps(out))

    def test_superscript_citation_keeps_no_space(self):
        old = doc(para(*words("ends here.")))
        new = doc(para(*words("ends here"), {"t": "Space"}, cite("a"), {"t": "Str", "c": "."}))
        out, _ = revdiff.annotate(new, old, "color", "strike", "A", "D", superscript=True)
        ins = spans(out, revdiff.INS_STYLE)
        self.assertEqual(ins[0][0]["t"], "Cite")


def revdiff_text(inlines):
    return " ".join(i["c"] for i in inlines if i.get("t") == "Str")


# A throwaway identity, so the test never depends on the machine's git config.
GIT_ENV = {**{k: v for k, v in os.environ.items() if k != "MANUSCRIPT_CONTENT_ROOT"},
           "GIT_AUTHOR_NAME": "Test", "GIT_AUTHOR_EMAIL": "test@example.org",
           "GIT_COMMITTER_NAME": "Test", "GIT_COMMITTER_EMAIL": "test@example.org",
           "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}


@unittest.skipUnless(shutil.which("git") and shutil.which("pandoc"), "needs git and pandoc")
class RoundTripTest(unittest.TestCase):
    def run_kit(self, *args, cwd=None, ok=True):
        r = subprocess.run([sys.executable, *args], cwd=cwd or self.repo, capture_output=True, text=True, env=GIT_ENV)
        if ok:
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return r

    def edit(self, root, name, old, new):
        p = Path(root) / "manuscript" / name
        s = p.read_text(encoding="utf-8")
        self.assertIn(old, s)
        p.write_text(s.replace(old, new), encoding="utf-8")

    def test_round_trip(self):
        tmp = Path(tempfile.mkdtemp())
        self.repo = tmp / "kit"
        shutil.copytree(KIT, self.repo, ignore=shutil.ignore_patterns("outputs", "build", "__pycache__", "revision",
                                                                      ".git"))
        (self.repo / "revision").mkdir()
        shutil.copy(KIT / "revision" / "_responses-template.md", self.repo / "revision")
        git = lambda *a: subprocess.run(["git", "-C", str(self.repo), *a], capture_output=True, check=True,
                                        env=GIT_ENV)
        git("init", "-q")
        git("add", "-A")
        git("commit", "-qm", "submitted")
        git("tag", "submission-1")

        # The journal's copy: tracked insertion, a comment, and an untracked copy-edit.
        journal = tmp / "journal"
        shutil.copytree(self.repo, journal, ignore=shutil.ignore_patterns(".git"))
        self.edit(journal, "04-discussion.md", "prespecified confounders.",
                  'prespecified confounders[, including CEAP class]{.insertion author="Copyeditor" '
                  'date="2026-09-20T00:00:00Z"}.')
        self.edit(journal, "04-discussion.md", "Confounding by indication",
                  '[Please discuss adherence.]{.comment-start id="0" author="Reviewer 2" '
                  'date="2026-09-20T00:00:00Z"}Confounding by indication[]{.comment-end id="0"}')
        self.edit(journal, "01-introduction.md", "most disabling complication", "most severe complication")
        self.run_kit("scripts/build.py", "--journal", "jvb", cwd=journal)
        returned = tmp / "returned.docx"
        shutil.copy(journal / "outputs" / "jvb" / "statins-ulcer_jvb_manuscript.docx", returned)

        # The exact uploaded file can be given at start (it was only accepted by `import`).
        sent = tmp / "sent.docx"
        subprocess.run([sys.executable, "scripts/build.py", "--journal", "jvb"], cwd=self.repo, capture_output=True,
                       env=GIT_ENV)
        shutil.copy(next((self.repo / "outputs" / "jvb").glob("*_manuscript.docx")), sent)
        shutil.rmtree(self.repo / "outputs")
        r = self.run_kit("scripts/revision.py", "start", "--round", "1", "--submitted-tag", "submission-1",
                         "--journal", "jvb", "--returned", str(returned), "--submitted-docx", str(sent))
        self.assertIn("the submitted file (sent.docx)",
                      (self.repo / "revision" / "round-1" / "journal-changes.md").read_text())
        self.assertIn("1 tracked change(s), 1 comment(s), 1 untracked difference(s)", r.stdout)
        report = (self.repo / "revision" / "round-1" / "journal-changes.md").read_text()
        self.assertIn("including CEAP class", report)
        self.assertIn("Please discuss adherence", report)
        self.assertIn("[-disabling-] {+severe+}", report)

        # Base refuses to move while the journal edits are missing from the source...
        r = self.run_kit("scripts/revision.py", "reconcile", "--round", "1")
        self.assertIn("difference(s)", r.stdout)
        # ...accept them, and the source matches the returned file.
        self.edit(self.repo, "04-discussion.md", "prespecified confounders.",
                  "prespecified confounders, including CEAP class.")
        self.edit(self.repo, "01-introduction.md", "most disabling complication", "most severe complication")
        r = self.run_kit("scripts/revision.py", "reconcile", "--round", "1")
        self.assertIn("ready for", r.stdout)
        git("commit", "-qam", "accept journal edits")
        self.run_kit("scripts/revision.py", "base", "--round", "1")

        # The revision itself, and a letter that explains only part of it.
        self.edit(self.repo, "04-discussion.md", "Randomized trials are needed",
                  "Adherence to statins was not measured. Randomized trials are needed")
        self.edit(self.repo, "02-methods.md", "body mass index (BMI), and", "body mass index (BMI), diabetes, and")
        letter = self.repo / "revision" / "round-1" / "responses.md"
        s = letter.read_text()
        s = s.replace("> [Paste the editor's comment here, verbatim.]\n\n[Response: what was done, or why not.]",
                      "> Address the reviewers.\n\nDone below.")
        s = s.replace("> [Paste the comment here, verbatim.]\n\n[Response: what was done, or why not.]\n\n"
                      "Changed: methods-statistics", "> Discuss adherence.\n\nAdded.\n\nChanged: discussion")
        letter.write_text(s)
        r = self.run_kit("scripts/revision.py", "check", "--round", "1")
        self.assertIn("methods-statistics` changed but no response lists it", r.stdout)
        self.assertNotIn("`results` changed", r.stdout)

        self.run_kit("scripts/build.py", "--journal", "jvb", "--revision", "1")
        out = self.repo / "outputs" / "jvb" / "revision-1"
        name = lambda part: f"statins-ulcer_jvb_rev1_{part}.docx"
        for part in ("manuscript-clean", "manuscript-marked", "response-letter", "title-page"):
            self.assertTrue((out / name(part)).exists(), name(part))
        xml = zipfile.ZipFile(out / name("manuscript-marked")).read("word/document.xml").decode()
        marked = "".join(re.findall(r'w:rStyle w:val="RevisionInserted".*?<w:t[^>]*>([^<]*)', xml, re.S))
        self.assertIn("diabetes", marked)
        self.assertIn("Adherence", marked)
        self.assertNotIn("CEAP class", marked)  # a journal edit accepted into the base is not ours
        plain = lambda f: subprocess.run(["pandoc", str(out / f), "-t", "plain"], capture_output=True, text=True).stdout
        refs = lambda t: t[t.find("\nReferences"):]
        self.assertEqual(refs(plain(name("manuscript-clean"))), refs(plain(name("manuscript-marked"))))
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
