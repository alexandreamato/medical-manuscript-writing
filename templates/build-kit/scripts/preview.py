#!/usr/bin/env python3
"""Look at the generated files before anyone uploads them.

    python3 scripts/preview.py --journal jvb               # outputs/jvb/
    python3 scripts/preview.py --journal jvb --revision 1  # outputs/jvb/revision-1/

For every .docx to upload it writes, in <outputs>/_preview/:
    <name>.pdf          rendered by LibreOffice (as close to Word as a script gets)
    <name>-sheet.png    all pages side by side: open it and look at every page
and _preview/_inspection.txt with checks that only the finished file allows:

    ERROR  an author's name or e-mail, or a local file path, anywhere in a blinded
           manuscript: body, headers, footers, footnotes, comments and the
           document properties (docProps), which Word shows under File > Info
    ERROR  a revision "marked" file with no marked text at all
    ERROR  a renderer that is installed but failed (the inspection is incomplete)
    WARN   a renderer that is not installed (no PDF or page images)
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
    """Text of the main document only (for legends and placeholders)."""
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    return " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", xml))


def docx_all_text(path: Path) -> dict[str, str]:
    """Every part a reader or Word can show: body, headers, footers, footnotes,
    endnotes, comments, and document properties (creator, custom fields)."""
    parts = {}
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if not name.endswith(".xml"):
                continue
            if name.startswith("docProps/"):
                xml = z.read(name).decode("utf-8", "replace")
                parts[name] = " ".join(re.findall(r">([^<>]+)<", xml))
            elif re.match(r"word/(document|header\d*|footer[^/]*|footnotes|endnotes|comments[^/]*)\.xml$", name):
                xml = z.read(name).decode("utf-8", "replace")
                parts[name] = " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", xml))
    return parts


LOCAL_PATH = re.compile(r"(/Users/[^\s<]+|/home/[^\s<]+|[A-Za-z]:\\[^\s<]+)")


def render(docx: Path, outdir: Path, rep, label: str) -> Path | None:
    """PDF, page images and contact sheet. Each step reports its own outcome:
    a missing tool is a WARN (known gap), a tool that ran and failed an ERROR."""
    def run(cmd, what):
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        except subprocess.TimeoutExpired:
            rep.error(label, f"{what} timed out")
            return False
        if r.returncode != 0:
            rep.error(label, f"{what} failed (exit {r.returncode}): {(r.stderr or r.stdout).strip()[:200]}")
            return False
        return True

    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        rep.warn(label, "LibreOffice not installed: no PDF rendered, open the file in Word and look")
        return None
    pdf = outdir / (docx.stem + ".pdf")
    ok = run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(outdir), str(docx)], "LibreOffice")
    if ok and not pdf.exists():
        rep.error(label, "LibreOffice reported success but wrote no PDF")
    if not pdf.exists():
        return None
    if not shutil.which("pdftoppm"):
        rep.warn(label, "poppler (pdftoppm) not installed: PDF only, no page images")
        return pdf
    prefix = outdir / f"{docx.stem}-page"
    if not run(["pdftoppm", "-r", "60", "-png", str(pdf), str(prefix)], "pdftoppm"):
        return pdf
    pages = sorted(outdir.glob(f"{docx.stem}-page*.png"),
                   key=lambda p: int(re.search(r"(\d+)\.png$", p.name).group(1)))
    if not pages:
        rep.error(label, "pdftoppm wrote no page images")
        return pdf
    magick = shutil.which("magick") or shutil.which("montage")
    if not magick:
        rep.warn(label, "ImageMagick not installed: page images kept, no contact sheet")
        return pdf
    sheet = outdir / f"{docx.stem}-sheet.png"
    cmd = [magick, "montage"] if magick.endswith("magick") else [magick]
    # montage looks up a label font even with no labels; give it one that exists.
    font = next((f for f in ("/System/Library/Fonts/Supplemental/Arial.ttf", "/Library/Fonts/Arial.ttf",
                             "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf") if Path(f).exists()), None)
    r = subprocess.run(cmd + (["-font", font] if font else []) +
                       [*map(str, pages), "-tile", "4x", "-geometry", "+6+6", "-background", "#888888", str(sheet)],
                       capture_output=True, text=True, timeout=300)
    if sheet.exists():
        if r.returncode != 0:
            rep.warn(label, f"contact sheet written, but ImageMagick reported: {r.stderr.strip()[:150]}")
        for p in pages:
            p.unlink()
    else:
        rep.error(label, f"contact sheet not written (exit {r.returncode}: {r.stderr.strip()[:150]}); "
                         "page images kept")
    return pdf


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
        pdf = render(f, prev, rep, f.name)
        rendered |= pdf is not None
        pages = pdf_pages(pdf) if pdf else None
        rep.add("INFO", f.name, f"{pages if pages is not None else '?'} page(s), "
                               f"{xml.count('<w:tbl>')} table(s), {xml.count('<pic:pic')} image(s)")
        if part.startswith("manuscript") and blinded:
            for where, ptext in docx_all_text(f).items():
                leaked = sorted(n for n in names if re.search(rf"\b{re.escape(n)}\b", ptext))
                if leaked:
                    rep.error(f.name, f"blinded manuscript contains author identity in {where}: " + ", ".join(leaked))
                for m in LOCAL_PATH.finditer(ptext):
                    rep.error(f.name, f"blinded manuscript contains a local file path in {where}: {m.group(0)[:80]}")
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
