#!/usr/bin/env python3
"""Look at the generated files before anyone uploads them.

    python3 scripts/preview.py --journal jvb               # outputs/jvb/
    python3 scripts/preview.py --journal jvb --revision 1  # outputs/jvb/revision-1/

For every .docx to upload it writes, in <outputs>/_preview/:
    <name>.pdf          rendered by LibreOffice (as close to Word as a script gets)
    <name>-sheet.png    all pages side by side: open it and look at every page
and _preview/_inspection.txt with checks that only the finished file allows:

    ERROR  an author's name or e-mail in a blinded manuscript
    ERROR  a revision "marked" file with no marked text at all
    WARN   line numbers missing when the profile wants them; figure files and
           legends that do not match; placeholder text in the rendered file
    INFO   pages, tables, images, fonts

Validation (validate.py) checks the source; this checks the product. Neither
replaces opening the file: tables, images, page breaks and colours are judged
by eye. Needs LibreOffice (`soffice`) for the PDF and poppler (`pdftoppm`) for
the page images; without them only the XML checks run.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import common as C
import validate as V


def docx_text(path: Path) -> str:
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    return " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", xml))


def render(docx: Path, outdir: Path) -> tuple[Path | None, list[Path]]:
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        return None, []
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(outdir), str(docx)],
                   capture_output=True, text=True, timeout=180)
    pdf = outdir / (docx.stem + ".pdf")
    if not pdf.exists():
        return None, []
    pages: list[Path] = []
    if shutil.which("pdftoppm"):
        prefix = outdir / f"{docx.stem}-page"
        subprocess.run(["pdftoppm", "-r", "60", "-png", str(pdf), str(prefix)], capture_output=True)
        pages = sorted(outdir.glob(f"{docx.stem}-page*.png"),
                       key=lambda p: int(re.search(r"(\d+)\.png$", p.name).group(1)))
        magick = shutil.which("magick") or shutil.which("montage")
        if pages and magick:
            cmd = [magick, "montage"] if magick.endswith("magick") else [magick]
            subprocess.run(cmd + [*map(str, pages), "-tile", "4x", "-geometry", "+6+6", "-background", "#888888",
                                  str(outdir / f"{docx.stem}-sheet.png")], capture_output=True)
            for p in pages:
                p.unlink()
    return pdf, pages


def pdf_pages(pdf: Path) -> int | None:
    if shutil.which("pdfinfo"):
        m = re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                                                        text=True).stdout)
        return int(m.group(1)) if m else None
    return len(re.findall(rb"/Type\s*/Page[^s]", pdf.read_bytes()))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--journal")
    ap.add_argument("--revision", type=int)
    a = ap.parse_args()
    doc = C.ast()
    meta = C.metadata(doc)
    journal = a.journal or meta.get("journal") or "generic-icmje"
    prof = C.load_profile(journal, meta.get("article-type"))
    outdir = C.OUTPUTS / journal / (f"revision-{a.revision}" if a.revision else "")
    files = sorted(p for p in outdir.glob("*.docx") if not p.name.startswith("_"))
    if not files:
        C.die(f"nothing to preview in {outdir}: run build.py first")
    prev = outdir / "_preview"
    if prev.exists():
        shutil.rmtree(prev)
    prev.mkdir()

    rep = V.Report(f"preview of {outdir.relative_to(C.KIT)}")
    authors = [x for x in (meta.get("author") or []) if isinstance(x, dict)]
    names = set()
    for au in authors:
        parts = (au.get("name") or "").split()
        if parts:
            names.add(parts[-1])
            names.add(" ".join(parts))
        if au.get("email"):
            names.add(au["email"])
    blinded = prof.get("submission", {}).get("blinded")
    want_ln = prof.get("reference_docx", {}).get("line_numbers", True)
    rendered = False

    for f in files:
        part = f.stem.split("_")[-1]
        xml = zipfile.ZipFile(f).read("word/document.xml").decode("utf-8")
        text = docx_text(f)
        pdf, _ = render(f, prev)
        rendered |= pdf is not None
        pages = pdf_pages(pdf) if pdf else None
        rep.add("INFO", f.name, f"{pages if pages is not None else '?'} page(s), "
                               f"{xml.count('<w:tbl>')} table(s), {xml.count('<pic:pic')} image(s)")
        if part.startswith("manuscript") and blinded:
            leaked = sorted(n for n in names if re.search(rf"\b{re.escape(n)}\b", text))
            if leaked:
                rep.error(f.name, "blinded manuscript contains author identity: " + ", ".join(leaked))
        if part.startswith("manuscript") and want_ln and "<w:lnNumType" not in xml:
            rep.warn(f.name, "no line numbers, but the profile asks for them")
        if part == "manuscript-marked":
            n = len(re.findall(r'w:rStyle w:val="RevisionInserted"|w:rStyle w:val="RevisionDeleted"|<w:ins |<w:del ',
                               xml))
            if not n:
                rep.error(f.name, "marked revision file has no marked text")
            else:
                rep.add("INFO", f.name, f"{n} marked run(s)")
        for m in V.PLACEHOLDER_RE.finditer(text):
            rep.warn(f.name, f"placeholder in the rendered file: {m.group(0)!r}")

    # Figure files vs legends in the manuscript.
    figs = sorted(outdir.glob("*_figure-*"))
    ms = [f for f in files if f.stem.endswith(("_manuscript", "_manuscript-clean"))]
    if ms:
        legends = set(re.findall(r"Figure (\d+)\.", docx_text(ms[0])))
        numbers = {re.search(r"figure-(\d+)", p.name).group(1) for p in figs}
        if legends and numbers and legends != numbers:
            rep.warn("figures", f"legends for figure(s) {sorted(legends)} but files for {sorted(numbers)}")

    rep.human("look", f"open each {prev.relative_to(C.KIT)}/*-sheet.png (or the PDF) and check every page: "
                      "tables, images, page breaks, headings, colours of marked text"
              if rendered else "LibreOffice not found: open every .docx in Word and check every page by eye")
    (prev / "_inspection.txt").write_text(rep.text().replace("INFO  ", "INFO   ") + "\n", encoding="utf-8")
    print(rep.text())
    sys.exit(1 if rep.count("ERROR") else 0)


if __name__ == "__main__":
    main()
