"""Generate a Word reference document (styles only) from a journal profile.

pandoc copies styles, margins and section settings from the reference .docx.
Starting from pandoc's own default guarantees every style pandoc emits exists;
this module then applies the manuscript conventions most journals ask for:

    "reference_docx": {
        "font": "Times New Roman", "size_pt": 12, "line_spacing": 2.0,
        "line_numbers": true, "margins_cm": 2.5, "page_numbers": true,
        "subheadings": "bold" | "italic"
    }

If the journal supplies its own template, set "reference_docx": {"file":
"templates/journal.docx"} instead and this module is not used.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import zipfile
from pathlib import Path

import common as C

DEFAULTS = {"font": "Times New Roman", "size_pt": 12, "line_spacing": 2.0, "line_numbers": True,
            "margins_cm": 2.5, "page_numbers": True, "subheadings": "bold"}


def _twips(cm: float) -> int:
    return round(cm / 2.54 * 1440)


def _styles(xml: str, s: dict) -> str:
    font = s["font"]
    half_pts = int(s["size_pt"] * 2)
    line = int(240 * s["line_spacing"])
    fonts = f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:eastAsia="{font}" w:cs="{font}" />'
    # Every theme font (body and headings) becomes the manuscript font; code keeps its own.
    xml = re.sub(r"<w:rFonts [^>]*Theme[^>]*/>", fonts, xml)
    xml = re.sub(r'(<w:rPrDefault>\s*<w:rPr>.*?<w:sz w:val=")\d+', rf"\g<1>{half_pts}", xml, flags=re.S)
    xml = re.sub(r'(<w:rPrDefault>\s*<w:rPr>.*?<w:szCs w:val=")\d+', rf"\g<1>{half_pts}", xml, flags=re.S)
    xml = xml.replace('<w:spacing w:after="200" />',
                      f'<w:spacing w:after="0" w:line="{line}" w:lineRule="auto" />', 1)
    # Body paragraphs: no extra space between, the double spacing does the job.
    xml = re.sub(r'(w:styleId="BodyText">.*?)<w:spacing [^>]*/>',
                 rf'\g<1><w:spacing w:before="0" w:after="0" w:line="{line}" w:lineRule="auto" />',
                 xml, count=1, flags=re.S)
    # Headings and captions in black, not the theme blue.
    xml = re.sub(r"<w:color [^>]*/>", '<w:color w:val="000000" />', xml)
    # Heading sizes: journals want plain headings, close to body size.
    for sid, size in (("Heading1", half_pts + 4), ("Heading2", half_pts + 2), ("Heading3", half_pts),
                      ("Title", half_pts + 8)):
        xml = re.sub(rf'(w:styleId="{sid}">.*?<w:sz w:val=")\d+', rf"\g<1>{size}", xml, count=1, flags=re.S)
        xml = re.sub(rf'(w:styleId="{sid}">.*?<w:szCs w:val=")\d+', rf"\g<1>{size}", xml, count=1, flags=re.S)
    # Section headings bold (the common journal default); subheadings bold, or
    # italic when the journal asks for it ("subheadings": "italic").
    sub = '<w:i />' if s.get("subheadings") == "italic" else '<w:b />'
    for sid, mark in (("Heading1", '<w:b />'), ("Heading2", sub), ("Heading3", '<w:i />')):
        xml = re.sub(rf'(w:styleId="{sid}">.*?<w:rPr>)', rf"\g<1>{mark}", xml, count=1, flags=re.S)
    return xml


def _sectpr(s: dict) -> str:
    m = _twips(s["margins_cm"])
    ln = '<w:lnNumType w:countBy="1" w:restart="continuous" />' if s["line_numbers"] else ""
    foot = '<w:footerReference w:type="default" r:id="rIdPageNum" />' if s["page_numbers"] else ""
    return (f'<w:sectPr>{foot}<w:pgSz w:w="11906" w:h="16838" />'
            f'<w:pgMar w:top="{m}" w:right="{m}" w:bottom="{m}" w:left="{m}" w:header="708" '
            f'w:footer="708" w:gutter="0" />{ln}</w:sectPr>')


FOOTER = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
          '<w:p><w:pPr><w:jc w:val="right" /></w:pPr>'
          '<w:r><w:fldChar w:fldCharType="begin" /></w:r>'
          '<w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
          '<w:r><w:fldChar w:fldCharType="separate" /></w:r><w:r><w:t>1</w:t></w:r>'
          '<w:r><w:fldChar w:fldCharType="end" /></w:r></w:p></w:ftr>')


def _revision_styles(rev: dict) -> str:
    """Character styles used by revdiff.py for the marked manuscript."""
    color = rev.get("color", "FF0000")
    ins = f'<w:color w:val="{color}" />'
    if rev.get("marking") == "highlight":
        ins = f'<w:highlight w:val="{rev.get("highlight", "yellow")}" />'
    dele = f'<w:strike /><w:color w:val="{color}" />'
    return (f'<w:style w:type="character" w:customStyle="1" w:styleId="RevisionInserted">'
            f'<w:name w:val="Revision Inserted" /><w:rPr>{ins}</w:rPr></w:style>'
            f'<w:style w:type="character" w:customStyle="1" w:styleId="RevisionDeleted">'
            f'<w:name w:val="Revision Deleted" /><w:rPr>{dele}</w:rPr></w:style>')


def ensure(profile_id: str, settings: dict, revision: dict | None = None) -> Path:
    s = {**DEFAULTS, **{k: v for k, v in (settings or {}).items() if not k.startswith("_")}}
    rev = {k: v for k, v in (revision or {}).items() if not k.startswith("_")}
    digest = hashlib.sha1(json.dumps([s, rev], sort_keys=True).encode()).hexdigest()[:8]
    C.BUILD.mkdir(exist_ok=True)
    out = C.BUILD / f"reference-{profile_id}-{digest}.docx"
    if out.exists():
        return out
    base = C.BUILD / "pandoc-default-reference.docx"
    if not base.exists():
        data = subprocess.run([C.require_pandoc(), "--print-default-data-file", "reference.docx"],
                              capture_output=True, check=True).stdout
        base.write_bytes(data)
    with zipfile.ZipFile(base) as zin, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/styles.xml":
                xml = _styles(data.decode("utf-8"), s)
                if rev.get("marking") in ("color", "highlight"):
                    xml = xml.replace("</w:styles>", _revision_styles(rev) + "</w:styles>")
                data = xml.encode("utf-8")
            elif item.filename == "word/document.xml":
                xml = data.decode("utf-8")
                xml = re.sub(r"<w:sectPr.*?</w:sectPr>", "", xml, flags=re.S)
                xml = xml.replace("</w:body>", _sectpr(s) + "</w:body>")
                data = xml.encode("utf-8")
            elif item.filename == "word/_rels/document.xml.rels" and s["page_numbers"]:
                xml = data.decode("utf-8").replace(
                    "</Relationships>",
                    '<Relationship Id="rIdPageNum" Type="http://schemas.openxmlformats.org/'
                    'officeDocument/2006/relationships/footer" Target="footer-pagenum.xml"/></Relationships>')
                data = xml.encode("utf-8")
            elif item.filename == "[Content_Types].xml" and s["page_numbers"]:
                xml = data.decode("utf-8").replace(
                    "</Types>",
                    '<Override PartName="/word/footer-pagenum.xml" ContentType="application/'
                    'vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>')
                data = xml.encode("utf-8")
            zout.writestr(item, data)
        if s["page_numbers"]:
            zout.writestr("word/footer-pagenum.xml", FOOTER)
    return out
