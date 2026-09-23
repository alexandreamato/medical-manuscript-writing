#!/usr/bin/env python3
"""Revision rounds: reconcile the journal's copy first, then mark our changes.

    python3 scripts/revision.py start  --round 1 --submitted-tag submission-1 --journal jvb
    python3 scripts/revision.py import --round 1 returned.docx [--submitted-docx sent.docx]
    #   -> revision/round-1/journal-changes.md: what the journal changed in our file
    #      (tracked changes, comments, and silent edits made without tracking)
    #   apply the accepted ones to manuscript/*.md, then:
    python3 scripts/revision.py reconcile --round 1   # journal edits still missing from the source
    python3 scripts/revision.py base --round 1        # tag revision-1-base (clean git tree)
    #   now make the revision itself in manuscript/*.md and answer in
    #   revision/round-1/responses.md, then:
    python3 scripts/revision.py check --round 1       # response letter vs actual changes
    python3 scripts/build.py --journal jvb --revision 1
    #   -> outputs/jvb/revision-1/: clean, marked (journal's marking rule), letter

Why this order. The journal often sends back a .docx that its staff or the
reviewers edited. If we marked our changes against what we *submitted*, their
edits would show up as ours, or our file would silently undo them. So the
base of the revision is "submitted + the journal edits we accept", tagged in
git; the marked file shows exactly what the authors changed after that.

The returned .docx is never converted back into the source: citations come
back as plain numbers. Its changes are listed and applied to the Markdown.
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from io import BytesIO
from pathlib import Path

import common as C


# ---------------------------------------------------------------- state

def round_dir(n: int) -> Path:
    return C.REVISION_DIR / f"round-{n}"


def load_state(n: int) -> dict:
    p = round_dir(n) / "state.json"
    if not p.exists():
        C.die(f"revision round {n} not started (python3 scripts/revision.py start --round {n} ...)")
    st = json.loads(p.read_text(encoding="utf-8"))
    return st


def save_state(n: int, st: dict):
    round_dir(n).mkdir(parents=True, exist_ok=True)
    (round_dir(n) / "state.json").write_text(json.dumps(st, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def git(*args, check=True) -> str:
    r = subprocess.run(["git", "-C", str(C.TOOLS), *args], capture_output=True, text=True)
    if check and r.returncode:
        C.die(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout.strip()


def export_tag(tag: str) -> Path:
    """Content of the kit at `tag`, extracted to a temporary folder.
    Remove it with cleanup(path)."""
    if not git("rev-parse", "--verify", "--quiet", f"{tag}^{{commit}}", check=False):
        C.die(f"git tag or commit '{tag}' not found")
    prefix = git("rev-parse", "--show-prefix")
    tmp = Path(tempfile.mkdtemp(prefix="kit-"))
    data = subprocess.run(["git", "-C", str(C.TOOLS), "archive", "--format=tar", tag, "--", prefix or "."],
                          capture_output=True, check=True).stdout
    with tarfile.open(fileobj=BytesIO(data)) as t:
        try:
            t.extractall(tmp, filter="data")
        except TypeError:  # Python < 3.12 has no extraction filters
            t.extractall(tmp)
    return tmp / prefix if prefix else tmp


def cleanup(root: Path):
    """Remove the temporary folder made by export_tag (root may be a subfolder of it)."""
    tmp = Path(tempfile.gettempdir()).resolve()
    p = root.resolve()
    while p.parent != tmp and p.parent != p:
        p = p.parent
    if p.name.startswith("kit-"):
        shutil.rmtree(p, ignore_errors=True)


def base_ast(st: dict) -> dict:
    if not st.get("base_tag"):
        C.die(f"no base yet for round {st['round']}: reconcile the journal's edits, commit, then "
              f"`python3 scripts/revision.py base --round {st['round']}`")
    root = export_tag(st["base_tag"])
    try:
        return C.ast(root)
    finally:
        cleanup(root)


# ---------------------------------------------------------------- docx text

def docx_paragraphs(path: Path, track: str) -> list[str]:
    """Paragraph texts of a .docx, tracked changes accepted/rejected/kept."""
    r = subprocess.run([C.require_pandoc(), str(path), f"--track-changes={track}", "-t", "plain", "--wrap=none"],
                       capture_output=True, text=True)
    if r.returncode:
        C.die(f"pandoc could not read {path}: {r.stderr}")
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", r.stdout)]
    return [p for p in paras if p]


def without_comments(inlines: list) -> list:
    """Paragraph text without the comment bodies Word stores inline."""
    return [i for i in inlines if not (isinstance(i, dict) and i.get("t") == "Span"
                                       and "comment-start" in i["c"][0][1])]


def tracked_items(path: Path) -> list[dict]:
    """Tracked insertions/deletions and comments in a .docx, with context."""
    r = subprocess.run([C.require_pandoc(), str(path), "--track-changes=all", "-t", "json"],
                       capture_output=True, text=True)
    doc = json.loads(r.stdout)
    items: list[dict] = []
    heading = ""

    def spans(inlines, para_text):
        for i in inlines:
            if not isinstance(i, dict):
                continue
            if i.get("t") == "Span":
                attr, content = i["c"]
                kv = dict(attr[2])
                kind = next((c for c in attr[1] if c in ("insertion", "deletion", "comment-start")), None)
                if kind:
                    items.append({"kind": {"comment-start": "comment"}.get(kind, kind),
                                  "author": kv.get("author", "?"), "date": kv.get("date", ""),
                                  "text": C.stringify(content), "section": heading,
                                  "context": para_text[:300]})
                spans(content, para_text)
            elif i.get("t") in ("Emph", "Strong", "Underline", "Strikeout", "Superscript", "Subscript",
                                "SmallCaps"):
                spans(i["c"], para_text)
            elif i.get("t") in ("Link", "Quoted", "Cite"):
                spans(i["c"][1], para_text)

    def walk(node):
        nonlocal heading
        if isinstance(node, list):
            for x in node:
                walk(x)
            return
        if not isinstance(node, dict) or "t" not in node:
            return
        t = node["t"]
        if t == "Header":
            heading = C.stringify(node["c"][2])
            spans(node["c"][2], heading)
        elif t in ("Para", "Plain"):
            spans(node["c"], C.stringify(without_comments(node["c"])))
        elif isinstance(node.get("c"), (list, dict)):
            walk(node["c"])

    walk(doc["blocks"])
    return items


def word_diff(a: str, b: str) -> str:
    """'old [-removed-] {+added+} text' at word level."""
    aw, bw = a.split(), b.split()
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, aw, bw, autojunk=False).get_opcodes():
        if op == "equal":
            seg = aw[i1:i2]
            out.append(" ".join(seg) if len(seg) <= 12 else " ".join(seg[:5]) + " … " + " ".join(seg[-5:]))
        if op in ("delete", "replace"):
            out.append("[-" + " ".join(aw[i1:i2]) + "-]")
        if op in ("insert", "replace"):
            out.append("{+" + " ".join(bw[j1:j2]) + "+}")
    return " ".join(out)


def paragraph_diff(old: list[str], new: list[str]) -> list[dict]:
    out = []
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        a, b = old[i1:i2], new[j1:j2]
        for k in range(max(len(a), len(b))):
            pa = a[k] if k < len(a) else ""
            pb = b[k] if k < len(b) else ""
            kind = "changed" if pa and pb else ("removed" if pa else "added")
            out.append({"kind": kind, "before": pa, "after": pb, "diff": word_diff(pa, pb) if pa and pb else ""})
    return out


def render_current(journal: str, env_root: Path | None = None) -> Path:
    """Build the manuscript docx with today's tools (for `env_root`, an old tag)."""
    env = dict(os.environ)
    if env_root:
        env["MANUSCRIPT_CONTENT_ROOT"] = str(env_root)
    r = subprocess.run([sys.executable, str(C.TOOLS / "scripts" / "build.py"), "--journal", journal, "--force"],
                       capture_output=True, text=True, env=env)
    root = env_root or C.KIT
    found = sorted((root / "outputs" / journal).glob("*_manuscript.docx"))
    out = found[0] if found else root / "outputs" / journal / "manuscript.docx"
    if r.returncode or not out.exists():
        C.die(f"could not build {journal} from {root}:\n{r.stdout}\n{r.stderr}")
    return out


# ---------------------------------------------------------------- commands

def cmd_start(a):
    d = round_dir(a.round)
    if (d / "state.json").exists() and not a.force:
        C.die(f"round {a.round} already started ({d}); --force to reset its state")
    git("rev-parse", "--verify", f"{a.submitted_tag}^{{commit}}")
    save_state(a.round, {"round": a.round, "journal": a.journal, "submitted_tag": a.submitted_tag,
                         "submitted_docx": None, "returned_docx": None, "base_tag": None,
                         "started_at": dt.date.today().isoformat()})
    tpl = C.TOOLS / "revision" / "_responses-template.md"
    resp = d / "responses.md"
    if not resp.exists() and tpl.exists():
        shutil.copy(tpl, resp)
    print(f"round {a.round} started from {a.submitted_tag} for {a.journal}: {d.relative_to(C.TOOLS)}/")
    if a.returned:
        a.file = a.returned
        a.submitted_docx = None
        cmd_import(a)


def cmd_import(a):
    st = load_state(a.round)
    d = round_dir(a.round)
    src = Path(a.file).expanduser()
    if not src.exists():
        C.die(f"{src} not found")
    returned = d / "returned.docx"
    shutil.copy(src, returned)
    st["returned_docx"] = returned.name
    if a.submitted_docx:
        sent = d / "submitted.docx"
        shutil.copy(Path(a.submitted_docx).expanduser(), sent)
        st["submitted_docx"] = sent.name
        what = f"the submitted file ({Path(a.submitted_docx).name})"
    else:
        root = export_tag(st["submitted_tag"])
        sent = d / "submitted-rebuilt.docx"
        shutil.copy(render_current(st["journal"], root), sent)
        cleanup(root)
        what = f"a rebuild of tag {st['submitted_tag']}"
    save_state(a.round, st)

    tracked = tracked_items(returned)
    silent = paragraph_diff(docx_paragraphs(sent, "accept"), docx_paragraphs(returned, "reject"))
    lines = [f"# Journal changes, round {a.round}", "",
             f"Returned file: `{src.name}`; compared with {what}.", "",
             "Decide each item, apply the accepted ones to `manuscript/*.md` (never paste the returned "
             "file back: its citations are plain numbers), then run `revision.py reconcile`.", ""]
    ins = [t for t in tracked if t["kind"] in ("insertion", "deletion")]
    com = [t for t in tracked if t["kind"] == "comment"]
    lines += [f"## Tracked changes ({len(ins)})", ""]
    for i, t in enumerate(ins, 1):
        verb = "inserted" if t["kind"] == "insertion" else "deleted"
        lines += [f"{i}. [ ] accept  [ ] reject: **{verb}** \"{t['text']}\" ({t['author']}, section "
                  f"\"{t['section'] or '?'}\")", f"   Context: {t['context']}", ""]
    lines += [f"## Comments ({len(com)})", ""]
    for i, t in enumerate(com, 1):
        lines += [f"{i}. **{t['author']}** (section \"{t['section'] or '?'}\"): {t['text']}",
                  f"   On: {t['context']}", "   Answer in `responses.md` if it is a reviewer or editor comment.", ""]
    lines += [f"## Changes made without tracking ({len(silent)})", "",
              "Differences between what we sent and the returned file with its tracked changes rejected: "
              "edits by the journal that Word does not show. `[-removed-]` `{+added+}`. Layout differences "
              "(numbering, headers) also appear here; ignore them.", ""]
    for i, s in enumerate(silent, 1):
        if s["kind"] == "changed":
            lines += [f"{i}. [ ] accept  [ ] reject: changed paragraph", f"   {s['diff']}", ""]
        elif s["kind"] == "added":
            lines += [f"{i}. [ ] accept  [ ] reject: paragraph added by the journal", f"   {s['after'][:400]}", ""]
        else:
            lines += [f"{i}. [ ] accept  [ ] reject: paragraph removed by the journal", f"   {s['before'][:400]}", ""]
    report = d / "journal-changes.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    (d / "journal-changes.json").write_text(json.dumps({"tracked": tracked, "untracked": silent}, indent=2,
                                                       ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{len(ins)} tracked change(s), {len(com)} comment(s), {len(silent)} untracked difference(s)")
    print(f"-> {report.relative_to(C.TOOLS)}")


def cmd_reconcile(a):
    st = load_state(a.round)
    returned = round_dir(a.round) / (st.get("returned_docx") or "")
    if not returned.is_file():
        C.die("no returned file imported for this round (revision.py import)")
    ours = docx_paragraphs(render_current(st["journal"]), "accept")
    theirs = docx_paragraphs(returned, "accept")
    diffs = paragraph_diff(theirs, ours)
    if not diffs:
        print("source matches the returned file with its changes accepted: ready for `revision.py base`")
        return
    print(f"{len(diffs)} difference(s) between the returned file (changes accepted) and the current source.")
    print("Each must be a journal edit you rejected on purpose, or layout; otherwise apply it first.\n")
    for i, s in enumerate(diffs, 1):
        body = s["diff"] or (("journal only: " + s["before"]) if s["kind"] == "removed" else ("source only: " + s["after"]))
        print(f"{i:>3}. {body[:500]}")


def cmd_base(a):
    st = load_state(a.round)
    dirty = git("status", "--porcelain", "--", "manuscript", "references.json", "figures")
    if dirty:
        C.die("commit the reconciled manuscript first; uncommitted changes:\n" + dirty)
    tag = a.tag or f"revision-{a.round}-base"
    if git("rev-parse", "--verify", "--quiet", f"refs/tags/{tag}", check=False):
        if not a.force:
            C.die(f"tag {tag} exists; --force to move it")
        git("tag", "-d", tag)
    git("tag", "-a", tag, "-m", f"Revision {a.round} base: submitted {st['submitted_tag']} + accepted journal edits")
    st["base_tag"] = tag
    st["base_commit"] = git("rev-parse", "--short", "HEAD")
    save_state(a.round, st)
    print(f"base of round {a.round}: {tag} ({st['base_commit']}). Make the revision now; "
          f"`build.py --journal {st['journal']} --revision {a.round}` marks everything after this point.")


# ---------------------------------------------------------------- response letter

def letter_ast(n: int) -> dict | None:
    p = round_dir(n) / "responses.md"
    if not p.exists():
        return None
    r = subprocess.run([C.require_pandoc(), str(p), "-f", "markdown", "-t", "json"], capture_output=True, text=True)
    if r.returncode:
        C.die(f"could not parse {p}: {r.stderr}")
    return json.loads(r.stdout)


def check_letter(n: int, doc: dict | None = None):
    """Every comment has a response; every `Changed:` section really changed;
    every changed section is explained somewhere in the letter."""
    import validate as V
    import revdiff
    rep = V.Report(f"response letter, round {n}")
    la = letter_ast(n)
    if la is None:
        rep.error("letter", f"revision/round-{n}/responses.md not found")
        return rep
    st = load_state(n)
    doc = doc or C.ast()
    changed: set[str] = set()
    if st.get("base_tag"):
        _, m = revdiff.annotate(doc, base_ast(st), "tracked", "strike", "x", "x")
        changed = m.changed_sections
    ids = {s["id"] for s in C.sections(doc)} | {ss["id"] for s in C.sections(doc) for ss in s["subsections"]}
    comments, cur = [], None
    for b in la["blocks"]:
        if b["t"] == "Header" and b["c"][0] == 2:
            cur = {"title": C.stringify(b["c"][2]), "quote": False, "response": "", "changed": []}
            comments.append(cur)
        elif cur is None:
            continue
        elif b["t"] == "BlockQuote":
            cur["quote"] = True
        elif b["t"] in ("Para", "Plain"):
            txt = C.stringify(b["c"])
            m = re.match(r"(?i)changed?\s*:\s*(.*)", txt)
            if m:
                cur["changed"] += [x.strip().lstrip("#") for x in re.split(r"[,;\s]+", m.group(1)) if x.strip()]
            else:
                cur["response"] += " " + txt
    if not comments:
        rep.error("letter", "no comments found (one `## ...` heading per reviewer comment)")
    explained = set()
    for c in comments:
        where = f"comment \"{c['title']}\""
        if not c["quote"]:
            rep.warn(where, "reviewer's comment not quoted (`> ...`)")
        resp = c["response"].strip()
        if not resp or re.search(r"\[(?:response|resposta|todo)[^\]]*\]", resp, re.I):
            rep.error(where, "no response written")
        for sid in c["changed"]:
            if sid.lower() in ("none", "nenhuma", "-"):
                continue
            explained.add(sid)
            if sid not in ids:
                rep.error(where, f"`Changed: {sid}`: no section with that id in the manuscript")
            elif st.get("base_tag") and sid not in changed:
                rep.error(where, f"says `{sid}` changed, but it is identical to {st['base_tag']}")
    for sid in sorted(changed - explained - {"_front"}):
        rep.warn("manuscript", f"section `{sid}` changed but no response lists it under `Changed:`")
    return rep


LETTER_LABELS = {
    "en": ("Changes in the manuscript", "No change to the manuscript."),
    "pt": ("Alterações no manuscrito", "Sem alteração no manuscrito."),
    "es": ("Cambios en el manuscrito", "Sin cambios en el manuscrito."),
}


def build_letter(n: int, out: Path, refdoc: Path, lang: str, meta: dict, headings: dict | None = None):
    """responses.md -> .docx. `Changed: <ids>` lines become readable locations
    ("Changes in the manuscript: Methods, Statistical analysis")."""
    la = letter_ast(n)
    if la is None:
        return
    doc = C.ast()
    names = {}
    for s_ in C.sections(doc):
        names[s_["id"]] = s_["title"]
        for ss in s_["subsections"]:
            names[ss["id"]] = ss["title"]
    names.update(headings or {})
    label, none = LETTER_LABELS.get((lang or "en").split("-")[0], LETTER_LABELS["en"])
    blocks = []
    for b in la["blocks"]:
        if b["t"] in ("Para", "Plain"):
            m = re.match(r"(?i)changed?\s*:\s*(.*)", C.stringify(b["c"]))
            if m:
                ids = [x.strip().lstrip("#") for x in re.split(r"[,;\s]+", m.group(1)) if x.strip()]
                ids = [i for i in ids if i.lower() not in ("none", "nenhuma", "-")]
                text = f"{label}: " + ", ".join(names.get(i, i) for i in ids) + "." if ids else none
                b = {"t": "Para", "c": [{"t": "Emph", "c": [{"t": "Str", "c": w} if k % 2 == 0 else {"t": "Space"}
                                                           for k, w in enumerate(sum(([w, " "] for w in text.split()), [])[:-1])]}]}
        blocks.append(b)
    la["blocks"] = blocks
    src = C.BUILD / "letter-ast.json"
    C.BUILD.mkdir(exist_ok=True)
    src.write_text(json.dumps(la, ensure_ascii=False), encoding="utf-8")
    cmd = [C.require_pandoc(), str(src), "-f", "json", "-t", "docx", "--reference-doc", str(refdoc),
           "-M", f"lang={lang}", "-o", str(out)]
    if meta.get("title"):
        cmd += ["-M", f"subtitle={meta['title']}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        C.die(f"could not build the response letter: {r.stderr}")


def cmd_check(a):
    rep = check_letter(a.round)
    print(rep.text())
    sys.exit(1 if rep.count("ERROR") else 0)


def cmd_status(_):
    if not C.REVISION_DIR.exists():
        print("no revision rounds")
        return
    for d in sorted(C.REVISION_DIR.glob("round-*")):
        st = json.loads((d / "state.json").read_text()) if (d / "state.json").exists() else {}
        print(f"{d.name}: journal {st.get('journal')}, submitted {st.get('submitted_tag')}, "
              f"returned {st.get('returned_docx') or '-'}, base {st.get('base_tag') or 'not yet'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("start")
    s.add_argument("--round", type=int, required=True)
    s.add_argument("--submitted-tag", required=True, help="git tag of what was submitted")
    s.add_argument("--journal", required=True)
    s.add_argument("--returned", help="the .docx the journal sent back (runs import)")
    s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_start)
    i = sub.add_parser("import")
    i.add_argument("--round", type=int, required=True)
    i.add_argument("file", help="the .docx returned by the journal")
    i.add_argument("--submitted-docx", help="the exact file we uploaded (default: rebuild the tag)")
    i.set_defaults(fn=cmd_import)
    r = sub.add_parser("reconcile")
    r.add_argument("--round", type=int, required=True)
    r.set_defaults(fn=cmd_reconcile)
    b = sub.add_parser("base")
    b.add_argument("--round", type=int, required=True)
    b.add_argument("--tag")
    b.add_argument("--force", action="store_true")
    b.set_defaults(fn=cmd_base)
    c = sub.add_parser("check")
    c.add_argument("--round", type=int, required=True)
    c.set_defaults(fn=cmd_check)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
