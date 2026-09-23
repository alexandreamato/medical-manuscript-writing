#!/usr/bin/env python3
"""Build the submission files for one journal.

    python3 scripts/build.py --journal generic-icmje
    python3 scripts/build.py --journal generic-icmje --force     # build despite ERRORs
    python3 scripts/build.py --all                               # every profile

Output in outputs/<journal>/:
    manuscript.docx         (title page + text, or blinded text if the journal
                             reviews blind)
    title-page.docx         (when the journal wants it separate)
    figures/Figure1.png ... (numbered by first mention, for separate upload)
    validation-report.txt   (what was checked, against which profile version)
    build-info.json         (pandoc version, profile, git commit: traceability)

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

import common as C
import refdocx
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


def run_pandoc(out_file, runtime_meta, csl, refdoc, number_sections, lang):
    C.BUILD.mkdir(exist_ok=True)
    rt = C.BUILD / "runtime-meta.json"
    rt.write_text(json.dumps(runtime_meta, ensure_ascii=False), encoding="utf-8")
    cmd = [C.require_pandoc(), "-f", "markdown", "-t", "docx",
           "--metadata-file", str(C.METADATA), "--metadata-file", str(rt),
           "--resource-path", f"{C.KIT}:{C.MANUSCRIPT_DIR}",
           "--lua-filter", str(C.FILTERS / "crossref.lua"),
           "--lua-filter", str(C.FILTERS / "journal.lua"),
           "--citeproc", "--csl", csl, "--bibliography", str(C.REFERENCES),
           "--reference-doc", str(refdoc),
           "-M", f"lang={lang}", "-M", "link-citations=false",
           "-o", str(out_file), *map(str, C.section_files())]
    if number_sections:
        cmd.insert(3, "--number-sections")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        C.die(f"pandoc failed:\n{res.stderr}")
    for line in res.stderr.splitlines():
        # citeproc reports unknown keys here; validate.py should already have caught them.
        print("  pandoc:", line)


def build(name: str, atype: str | None, force: bool) -> bool:
    doc = C.ast()
    meta = C.metadata(doc)
    atype = atype or meta.get("article-type")
    prof = C.load_profile(name, atype)
    out = C.OUTPUTS / name
    print(f"== {name}" + (f" / {atype}" if atype else ""))

    rep, stats = V.validate(prof, doc)
    print(f"  validation: {rep.count('ERROR')} error(s), {rep.count('WARN')} warning(s)")
    if rep.count("ERROR") and not force:
        print(rep.text())
        print(f"  not built: fix the errors or pass --force (draft build).")
        return False

    if out.exists():
        shutil.rmtree(out)
    (out / "figures").mkdir(parents=True)
    (out / "validation-report.txt").write_text(rep.text() + "\n", encoding="utf-8")

    csl = resolve_csl(prof.get("csl", "nlm-citation-sequence"))
    rd = prof.get("reference_docx", {})
    refdoc = (C.KIT / rd["file"]) if rd.get("file") else refdocx.ensure(prof["id"], rd)

    abs_cfg = prof.get("abstract", {})
    headings = {f"abstract-{p['id']}": p["heading"] for p in abs_cfg.get("structure", []) if p.get("heading")}
    headings.update({s["id"]: s["heading"] for s in prof.get("main_text", {}).get("sections", [])
                     if s.get("heading")})
    headings.update(prof.get("headings", {}))
    sub = prof.get("submission", {})
    base = {
        "headings": headings,
        "unstructured": not abs_cfg.get("structure"),
        "word-counts": {"abstract": stats.get("abstract_words"), "main": stats.get("main_text_words")},
    }
    xref = {"tables": prof.get("tables", {}).get("placement", "inline"),
            "figures": prof.get("figures", {}).get("placement", "inline")}
    lang = meta.get("lang") or prof.get("lang", "en-US")
    ns = sub.get("number_sections", False)

    if sub.get("separate_title_page"):
        run_pandoc(out / "title-page.docx", {"journal-build": {**base, "mode": "titlepage"}, "xref": xref},
                   csl, refdoc, False, lang)
        mode = "blinded" if sub.get("blinded") else "full"
    else:
        mode = "blinded" if sub.get("blinded") else "full"
    omit = sub.get("omit_in_blinded", []) if mode == "blinded" else []
    run_pandoc(out / "manuscript.docx", {"journal-build": {**base, "mode": mode, "omit": omit}, "xref": xref},
               csl, refdoc, ns, lang)

    # Figures as separate files, renamed by their number.
    nums = C.float_numbers(doc)
    for fid, src in C.image_targets(doc).items():
        p = C.KIT / src if (C.KIT / src).exists() else C.MANUSCRIPT_DIR / src
        if p.exists():
            prefix = "SupplementaryFigure" if fid.startswith("sfig:") else "Figure"
            shutil.copy2(p, out / "figures" / f"{prefix}{nums.get(fid, 0)}{p.suffix}")

    (out / "build-info.json").write_text(json.dumps({
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
    a = ap.parse_args()
    meta = C.metadata(C.ast())
    names = C.list_profiles() if a.all else [a.journal or meta.get("journal") or "generic-icmje"]
    ok = [build(n, a.article_type, a.force) for n in names]
    sys.exit(0 if all(ok) else 1)


if __name__ == "__main__":
    main()
