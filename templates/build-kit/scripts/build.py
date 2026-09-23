#!/usr/bin/env python3
"""Build the submission files for one journal.

    python3 scripts/build.py --journal generic-icmje
    python3 scripts/build.py --journal generic-icmje --force     # build despite ERRORs
    python3 scripts/build.py --all                               # every profile
    python3 scripts/build.py --journal jvb --revision 1          # revised files (clean,
                                                                 # marked, response letter)

With --revision N, outputs/<journal>/revision-N/ holds the clean manuscript,
the marked one (the journal's rule: red text, highlight or tracked changes,
against the tag made by `revision.py base`), the response letter built from
revision/round-N/responses.md, and _letter-check.txt. See revision.py.

Output in outputs/<journal>/, named <short-name>_<journal>[_rev<N>]_<part>.<ext>
(common.file_name):
    ..._manuscript.docx       title page + text, or blinded text if the journal
                              reviews blind
    ..._title-page.docx       when the journal wants it separate
    ..._figure-1.png ...      numbered by first mention, for separate upload
    _validation-report.txt    internal: what was checked, against which profile
    _build-info.json          internal: pandoc version, profile, git commit

Pipeline: validate -> resolve CSL -> reference.docx -> pandoc
          (crossref.lua -> journal.lua -> citeproc).
Citations are numbered by citeproc on every build, so moving a paragraph can
never leave the reference list out of sequence.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

import common as C
import refdocx
import revdiff
import validate as V

CSL_REPO = "https://raw.githubusercontent.com/citation-style-language/styles/master/"


def resolve_csl(name: str) -> str:
    """Local csl/<name>.csl, else download from the CSL repository.

    Journal styles are often "dependent" (only a pointer to a parent style);
    pandoc needs the independent parent, so it is fetched and used instead.
    """
    if name.endswith(".csl") and (C.KIT / name).exists():
        return str(C.KIT / name)
    path = C.CSL_DIR / f"{name}.csl"
    if not path.exists():
        for sub in ("", "dependent/"):
            try:
                with urllib.request.urlopen(CSL_REPO + sub + name + ".csl", timeout=30) as r:
                    path.write_bytes(r.read())
                print(f"  fetched CSL style {sub}{name}")
                break
            except Exception:
                continue
        else:
            C.die(f"CSL style '{name}' not found locally or in the CSL repository "
                  "(browse https://www.zotero.org/styles for the exact file name)")
    xml = path.read_text(encoding="utf-8")
    m = re.search(r'<link href="https?://www\.zotero\.org/styles/([^"]+)" rel="independent-parent"', xml)
    if m:
        print(f"  {name} is a dependent style; using parent {m.group(1)}")
        return resolve_csl(m.group(1))
    return str(path)


def pick(value, lang: str):
    """A heading given per language ({"pt": "Métodos", "en": "Methods"}) or as a plain string."""
    if not isinstance(value, dict):
        return value
    code = (lang or "").split("-")[0]
    return value.get(lang) or value.get(code) or next(iter(value.values()))


def git_commit() -> str | None:
    try:
        r = subprocess.run(["git", "-C", str(C.KIT), "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True)
        if r.returncode:
            return None
        dirty = subprocess.run(["git", "-C", str(C.KIT), "status", "--porcelain"],
                               capture_output=True, text=True).stdout.strip()
        return r.stdout.strip() + ("-dirty" if dirty else "")
    except FileNotFoundError:
        return None


def run_pandoc(out_file, runtime_meta, csl, refdoc, number_sections, lang, ast_input=None):
    """Markdown sources -> docx; or, with `ast_input`, a pandoc JSON AST (the
    marked revision) through exactly the same filters and citeproc."""
    C.BUILD.mkdir(exist_ok=True)
    rt = C.BUILD / "runtime-meta.json"
    rt.write_text(json.dumps(runtime_meta, ensure_ascii=False), encoding="utf-8")
    if ast_input is not None:
        src = C.BUILD / "input-ast.json"
        src.write_text(json.dumps(ast_input, ensure_ascii=False), encoding="utf-8")
        inputs, fmt = [str(src)], "json"
    else:
        inputs, fmt = [str(f) for f in C.section_files()], "markdown"
    cmd = [C.require_pandoc(), "-f", fmt, "-t", "docx",
           "--metadata-file", str(C.METADATA), "--metadata-file", str(rt),
           "--resource-path", f"{C.KIT}:{C.MANUSCRIPT_DIR}",
           # Order matters: cross-references, then citations, then the journal layer,
           # which also strips every metadata field from the file (docProps/custom.xml
           # would otherwise carry local paths and author data into blinded files).
           "--lua-filter", str(C.FILTERS / "crossref.lua"),
           "--citeproc", "--csl", csl, "--bibliography", str(C.REFERENCES),
           "--lua-filter", str(C.FILTERS / "journal.lua"),
           "--reference-doc", str(refdoc),
           "-M", f"lang={lang}", "-M", "link-citations=false",
           "-o", str(out_file), *inputs]
    if number_sections:
        cmd.insert(3, "--number-sections")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        C.die(f"pandoc failed:\n{res.stderr}")
    for line in res.stderr.splitlines():
        # citeproc reports unknown keys here; validate.py should already have caught them.
        print("  pandoc:", line)


def build(name: str, atype: str | None, force: bool, revision: int | None = None,
          submission: bool = False) -> bool:
    doc = C.ast()
    meta = C.metadata(doc)
    atype = atype or meta.get("article-type")
    prof = C.load_profile(name, atype)
    out = C.OUTPUTS / name / (f"revision-{revision}" if revision else "")
    print(f"== {name}" + (f" / {atype}" if atype else "") + (f" / revision {revision}" if revision else ""))

    rep, stats = V.validate(prof, doc, "submission" if submission else "draft")
    print(f"  validation: {rep.count('ERROR')} error(s), {rep.count('WARN')} warning(s)")
    if rep.count("ERROR") and not force:
        print(rep.text())
        print(f"  not built: fix the errors or pass --force (draft build).")
        return False

    # Replace this build's files but keep revision-N/ folders of earlier rounds.
    if out.exists():
        for p in out.iterdir():
            if not p.name.startswith("revision-"):
                shutil.rmtree(p) if p.is_dir() else p.unlink()
    out.mkdir(parents=True, exist_ok=True)
    (out / "_validation-report.txt").write_text(rep.text() + "\n", encoding="utf-8")
    fname = lambda part, ext: C.file_name(meta, name, part, ext, revision)

    csl = resolve_csl(prof.get("csl", "nlm-citation-sequence"))
    rd = prof.get("reference_docx", {})
    rev = prof.get("revision", {})
    refdoc = (C.KIT / rd["file"]) if rd.get("file") else refdocx.ensure(prof["id"], rd, rev if revision else None)

    abs_cfg = prof.get("abstract", {})
    lang = meta.get("lang") or prof.get("lang", "en-US")
    lang_alt = meta.get("lang-alt") or ""
    bilingual = bool(abs_cfg.get("bilingual"))
    headings = {f"abstract-{p['id']}": pick(p["heading"], lang) for p in abs_cfg.get("structure", [])
                if p.get("heading")}
    if abs_cfg.get("title"):
        headings["abstract"] = pick(abs_cfg["title"], lang)
    if bilingual:
        headings.update({f"abstract-alt-{p['id']}": pick(p["heading"], lang_alt)
                         for p in abs_cfg.get("structure", []) if p.get("heading")})
        if abs_cfg.get("title"):
            headings["abstract-alt"] = pick(abs_cfg["title"], lang_alt)
    headings.update({s["id"]: pick(s["heading"], lang) for s in prof.get("main_text", {}).get("sections", [])
                     if s.get("heading")})
    headings.update({k: pick(v, lang) for k, v in prof.get("headings", {}).items()})
    sub = prof.get("submission", {})
    kw_labels = {"pt": "Palavras-chave", "en": "Keywords", "es": "Palabras clave"}
    kw_labels.update(prof.get("keywords", {}).get("labels", {}))
    base = {
        "headings": headings,
        "unstructured": not abs_cfg.get("structure"),
        "word-counts": {"abstract": stats.get("abstract_words"), "main": stats.get("main_text_words")},
        "keywords-after-abstract": bool(prof.get("keywords", {}).get("after_abstract")),
        "keywords-label": pick(kw_labels, lang),
        "keywords-label-alt": pick(kw_labels, lang_alt) if lang_alt else "",
        "titlepage-sections": sub.get("title_page_sections", []),
    }
    xref = {"tables": prof.get("tables", {}).get("placement", "inline"),
            "figures": prof.get("figures", {}).get("placement", "inline")}
    ns = sub.get("number_sections", False)

    if sub.get("separate_title_page"):
        run_pandoc(out / fname("title-page", ".docx"), {"journal-build": {**base, "mode": "titlepage"}, "xref": xref},
                   csl, refdoc, False, lang)
        mode = "blinded" if sub.get("blinded") else "full"
    else:
        mode = "blinded" if sub.get("blinded") else "full"
    omit = sub.get("omit_in_blinded", []) if mode == "blinded" else []
    if sub.get("separate_title_page"):
        # What the journal wants on the title page is not repeated in the manuscript.
        omit = list(dict.fromkeys(omit + sub.get("title_page_sections", [])))
    runtime = {"journal-build": {**base, "mode": mode, "omit": omit}, "xref": xref}
    if not revision:
        run_pandoc(out / fname("manuscript", ".docx"), runtime, csl, refdoc, ns, lang)
    else:
        import revision as R  # local import: only revision builds need git and the base tag
        state = R.load_state(revision)
        run_pandoc(out / fname("manuscript-clean", ".docx"), runtime, csl, refdoc, ns, lang)
        marking = rev.get("marking", "tracked")
        if marking != "none":
            old = R.base_ast(state)
            marked, stats_m = revdiff.annotate(doc, old, marking, rev.get("deleted", "strike"),
                                               rev.get("author") or "Authors",
                                               dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                                               superscript='vertical-align="sup"' in Path(csl).read_text(encoding="utf-8"))
            run_pandoc(out / fname("manuscript-marked", ".docx"), runtime, csl, refdoc, ns, lang,
                       ast_input=marked)
            stats["revision"] = {"base": state["base_tag"], "marking": marking,
                                 "inserted_words": stats_m.inserted_words, "deleted_words": stats_m.deleted_words,
                                 "changed_sections": sorted(stats_m.changed_sections)}
            print(f"  marked ({marking}): +{stats_m.inserted_words} / -{stats_m.deleted_words} words in "
                  + ", ".join(sorted(stats_m.changed_sections)))
        letter_rep = R.check_letter(revision, doc)
        for item in prof.get("revision_checks", []):
            letter_rep.human("journal", item)
        (out / "_letter-check.txt").write_text(letter_rep.text() + "\n", encoding="utf-8")
        print(f"  response letter: {letter_rep.count('ERROR')} error(s), {letter_rep.count('WARN')} warning(s)")
        R.build_letter(revision, out / fname("response-letter", ".docx"), refdoc, lang, meta, headings)

    # Figures as separate files, renamed by their number.
    nums = C.float_numbers(doc)
    for fid, src in C.image_targets(doc).items():
        p = C.KIT / src if (C.KIT / src).exists() else C.MANUSCRIPT_DIR / src
        if p.exists():
            part = ("supplementary-figure" if fid.startswith("sfig:") else "figure") + f"-{nums.get(fid, 0)}"
            shutil.copy2(p, out / fname(part, p.suffix.lower()))

    (out / "_build-info.json").write_text(json.dumps({
        "built_at": dt.datetime.now().isoformat(timespec="seconds"),
        "profile": prof["id"], "article_type": atype,
        "profile_verified_at": prof.get("verified_at"), "profile_source": prof.get("source_url"),
        "csl": csl.replace(str(C.KIT) + "/", ""), "pandoc": C.pandoc_version(),
        "git_commit": git_commit(), "forced": bool(force and rep.count("ERROR")), "stats": stats,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  wrote {out.relative_to(C.KIT)}/ ({', '.join(sorted(p.name for p in out.iterdir()))})")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--journal")
    ap.add_argument("--article-type")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--force", action="store_true", help="build even with validation errors (draft)")
    ap.add_argument("--submission", action="store_true",
                    help="final build: the submission gate of validate.py must pass (no --force)")
    ap.add_argument("--revision", type=int, help="revision round: clean + marked files and response letter")
    a = ap.parse_args()
    meta = C.metadata(C.ast())
    names = C.list_profiles() if a.all else [a.journal or meta.get("journal") or "generic-icmje"]
    if a.submission and a.force:
        C.die("--submission cannot be forced: the gate exists to stop an unready upload")
    ok = [build(n, a.article_type, a.force, a.revision, a.submission) for n in names]
    sys.exit(0 if all(ok) else 1)


if __name__ == "__main__":
    main()
