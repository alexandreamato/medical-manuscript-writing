"""Shared helpers for the manuscript build kit.

Only the Python standard library is used, plus the `pandoc` executable.
The manuscript is parsed through pandoc's JSON AST, so every check sees the
document exactly as pandoc will render it (citations, headers, figures,
tables), with no regex parsing of Markdown.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
MANUSCRIPT_DIR = KIT / "manuscript"
METADATA = MANUSCRIPT_DIR / "metadata.yaml"
REFERENCES = KIT / "references.json"
VERIFIED = KIT / "references.verified.json"
JOURNALS = KIT / "journals"
CSL_DIR = KIT / "csl"
FILTERS = KIT / "filters"
OUTPUTS = KIT / "outputs"
BUILD = KIT / "build"

# Prefixes that belong to the cross-reference filter, not to the bibliography.
XREF_PREFIXES = ("fig", "tbl", "sfig", "stbl")

# Study design (metadata `study-design`) -> reporting guideline.
GUIDELINES = {
    "rct": "CONSORT 2025",
    "trial-protocol": "SPIRIT 2025",
    "cohort": "STROBE",
    "case-control": "STROBE",
    "cross-sectional": "STROBE",
    "diagnostic-accuracy": "STARD 2015",
    "prediction-model": "TRIPOD+AI 2024",
    "systematic-review": "PRISMA 2020",
    "case-report": "CARE 2013",
    "quality-improvement": "SQUIRE 2.0",
    "qualitative": "SRQR / COREQ",
    "economic-evaluation": "CHEERS 2022",
    "animal": "ARRIVE 2.0",
}


def die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(2)


def require_pandoc() -> str:
    exe = shutil.which("pandoc")
    if not exe:
        die("pandoc not found. Install it (macOS: `brew install pandoc`).")
    out = subprocess.run([exe, "--version"], capture_output=True, text=True).stdout
    m = re.search(r"pandoc(?:\.exe)? (\d+)\.(\d+)", out)
    if m and (int(m.group(1)), int(m.group(2))) < (3, 1):
        die(f"pandoc >= 3.1 required, found {m.group(0)}")
    return exe


def pandoc_version() -> str:
    out = subprocess.run([require_pandoc(), "--version"], capture_output=True, text=True).stdout
    return out.splitlines()[0] if out else "unknown"


def section_files() -> list[Path]:
    """Manuscript files in build order: the numeric prefix sets the order."""
    files = sorted(p for p in MANUSCRIPT_DIR.glob("*.md") if not p.name.startswith("_"))
    if not files:
        die(f"no .md files in {MANUSCRIPT_DIR}")
    return files


# ---------------------------------------------------------------- profiles

def _deep_merge(base: dict, over: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in over.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def load_profile(name: str, article_type: str | None = None, _seen=None) -> dict:
    """Load journals/<name>.json, resolving `extends` and the article type.

    Keys starting with "_" are comments and are ignored.
    """
    _seen = _seen or set()
    if name in _seen:
        die(f"circular `extends` in journal profiles: {name}")
    _seen.add(name)
    path = JOURNALS / f"{name}.json"
    if not path.exists():
        avail = ", ".join(p.stem for p in JOURNALS.glob("*.json") if not p.stem.startswith("_"))
        die(f"journal profile '{name}' not found. Available: {avail}")
    raw = json.loads(path.read_text(encoding="utf-8"))
    raw = {k: v for k, v in raw.items() if not k.startswith("_")}
    parent = raw.pop("extends", None)
    prof = _deep_merge(load_profile(parent, None, _seen), raw) if parent else raw
    types = prof.pop("article_types", {}) or {}
    if article_type:
        if article_type in types:
            prof = _deep_merge(prof, {k: v for k, v in types[article_type].items() if not k.startswith("_")})
        prof["article_type"] = article_type
        prof["_article_type_known"] = article_type in types or not types
    prof["id"] = name
    return prof


def list_profiles() -> list[str]:
    return sorted(p.stem for p in JOURNALS.glob("*.json") if not p.stem.startswith("_"))


# ---------------------------------------------------------------- AST

def ast() -> dict:
    """Pandoc JSON AST of metadata + all manuscript files."""
    cmd = [require_pandoc(), "--metadata-file", str(METADATA), "-f", "markdown", "-t", "json",
           *map(str, section_files())]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        die(f"pandoc could not parse the manuscript:\n{res.stderr}")
    return json.loads(res.stdout)


def meta_value(m):
    """Convert a pandoc MetaValue into plain Python."""
    if m is None:
        return None
    t, c = m.get("t"), m.get("c")
    if t == "MetaMap":
        return {k: meta_value(v) for k, v in c.items()}
    if t == "MetaList":
        return [meta_value(v) for v in c]
    if t in ("MetaInlines", "MetaBlocks"):
        return stringify(c)
    if t in ("MetaString", "MetaBool"):
        return c
    return c


def metadata(doc: dict) -> dict:
    return {k: meta_value(v) for k, v in doc.get("meta", {}).items()}


def stringify(node, skip_cites: bool = False) -> str:
    """Plain text of any AST fragment."""
    parts: list[str] = []

    def walk(n):
        if isinstance(n, list):
            for x in n:
                walk(x)
            return
        if not isinstance(n, dict):
            return
        t, c = n.get("t"), n.get("c")
        if t == "Str":
            parts.append(c)
        elif t in ("Space", "SoftBreak", "LineBreak"):
            parts.append(" ")
        elif t == "Cite":
            if not skip_cites:
                walk(c[1])
        elif t in ("Code", "Math"):
            parts.append(c[1] if t == "Code" else c[1])
        elif t in ("Para", "Plain", "Header"):
            walk(c if t != "Header" else c[2])
            parts.append("\n")
        elif c is not None:
            walk(c)

    walk(node)
    return re.sub(r"[ \t]+", " ", "".join(parts)).strip()


WORD_RE = re.compile(r"[0-9A-Za-zÀ-ÿ]")


def count_words(text: str) -> int:
    return sum(1 for tok in text.split() if WORD_RE.search(tok))


def block_id(b: dict) -> str | None:
    """Identifier of a Div, Figure, Table or Header block."""
    t, c = b.get("t"), b.get("c")
    if t == "Header":
        return c[1][0] or None
    if t in ("Div", "Figure", "Table"):
        return c[0][0] or None
    return None


def is_float(b: dict, kinds=("fig", "tbl", "sfig", "stbl")) -> bool:
    bid = block_id(b) or ""
    if b.get("t") == "Header":
        return False
    return b.get("t") in ("Figure", "Table") or bid.split(":")[0] in kinds


def sections(doc: dict) -> list[dict]:
    """Split the body into level-1 sections.

    Each item: {id, title, level, blocks, subsections:[{id,title,blocks}]}.
    Blocks before the first level-1 header go into a section with id "_front".
    """
    out = [{"id": "_front", "title": "", "blocks": [], "subsections": []}]
    for b in doc["blocks"]:
        if b["t"] == "Header" and b["c"][0] == 1:
            out.append({"id": b["c"][1][0], "title": stringify(b["c"][2]), "blocks": [], "subsections": []})
            continue
        if b["t"] == "Header" and b["c"][0] == 2:
            out[-1]["subsections"].append({"id": b["c"][1][0], "title": stringify(b["c"][2]), "blocks": []})
        elif out[-1]["subsections"]:
            out[-1]["subsections"][-1]["blocks"].append(b)
        out[-1]["blocks"].append(b)
    return out


def text_of_blocks(blocks: list, include_floats: bool = False, skip_cites: bool = True) -> str:
    keep = [b for b in blocks if include_floats or not is_float(b)]
    return stringify([b for b in keep if b["t"] != "Header"], skip_cites=skip_cites)


def walk_inlines(node, fn):
    """Call fn(inline) for every inline element, in document order."""
    if isinstance(node, list):
        for x in node:
            walk_inlines(x, fn)
    elif isinstance(node, dict):
        if "t" in node:
            fn(node)
        c = node.get("c")
        if isinstance(c, (list, dict)):
            walk_inlines(c, fn)


def citations(doc: dict) -> list[str]:
    """All citation ids in document order (bibliographic and cross-reference)."""
    ids: list[str] = []

    def fn(n):
        if n.get("t") == "Cite":
            ids.extend(cit["citationId"] for cit in n["c"][0])

    walk_inlines(doc["blocks"], fn)
    return ids


def floats(doc: dict) -> list[str]:
    """Identifiers of figures/tables in definition order."""
    found: list[str] = []

    def walk(blocks):
        for b in blocks:
            bid = block_id(b)
            if bid and bid.split(":")[0] in XREF_PREFIXES and b["t"] != "Header" and bid not in found:
                found.append(bid)
            if b["t"] == "Div":
                walk(b["c"][1])

    walk(doc["blocks"])
    return found


def float_numbers(doc: dict) -> dict[str, int]:
    """Number figures and tables by first mention in the text (ICMJE rule).

    Mirrors filters/crossref.lua so file names and captions agree.
    """
    nums: dict[str, int] = {}
    counters: dict[str, int] = {}
    order = [c for c in citations(doc) if c.split(":")[0] in XREF_PREFIXES]
    for fid in order + floats(doc):
        if fid in nums:
            continue
        kind = fid.split(":")[0]
        counters[kind] = counters.get(kind, 0) + 1
        nums[fid] = counters[kind]
    return nums


def image_targets(doc: dict) -> dict[str, str]:
    """Figure id -> image path."""
    out: dict[str, str] = {}

    def find_img(node):
        hit = []
        walk_inlines(node, lambda n: hit.append(n["c"][2][0]) if n.get("t") == "Image" else None)
        return hit[0] if hit else None

    def walk(blocks):
        for b in blocks:
            bid = block_id(b)
            if bid and bid.startswith(("fig:", "sfig:")) and b["t"] != "Header":
                img = find_img(b["c"])
                if img:
                    out[bid] = img
            if b["t"] == "Div":
                walk(b["c"][1])

    walk(doc["blocks"])
    return out


# ---------------------------------------------------------------- references

def load_references() -> list[dict]:
    if not REFERENCES.exists():
        return []
    data = json.loads(REFERENCES.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        die("references.json must be a CSL-JSON array")
    return data


def save_references(refs: list[dict]) -> None:
    refs = sorted(refs, key=lambda r: r.get("id", ""))
    REFERENCES.write_text(json.dumps(refs, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ref_fingerprint(ref: dict) -> str:
    """Hash of the fields verification depends on; a change invalidates it."""
    fields = {k: ref.get(k) for k in ("title", "DOI", "PMID", "issued", "author", "container-title")}
    return hashlib.sha256(json.dumps(fields, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


def load_verified() -> dict:
    if VERIFIED.exists():
        return json.loads(VERIFIED.read_text(encoding="utf-8"))
    return {}
