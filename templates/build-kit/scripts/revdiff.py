"""Mark what changed between two versions of the manuscript, on the pandoc AST.

Used by build.py --revision N to produce the "marked" manuscript that
journals ask for with a revision. The comparison runs on the source AST
(before citeproc and the cross-reference filter), so the marked file and the
clean file get exactly the same reference and figure/table numbers.

Marking modes (journal profile, "revision.marking"):
    color      inserted text in a colour (e.g. red); deleted text struck
               through in the same colour, or omitted ("revision.deleted")
    highlight  inserted text highlighted; deletions as above
    tracked    real Word tracked changes (w:ins / w:del), author and date set
    none       no marked file

Citations inside deleted text are replaced by a neutral placeholder: a
deleted citation must not take a number in the reference list, or the
marked and clean files would be numbered differently.
"""

from __future__ import annotations

import copy
import difflib
import json
import re

INS_STYLE = "Revision Inserted"
DEL_STYLE = "Revision Deleted"
INLINE_BLOCKS = ("Para", "Plain")


class Marker:
    def __init__(self, marking: str, deleted: str, author: str, date: str, superscript: bool = False):
        self.marking, self.deleted, self.author, self.date = marking, deleted, author, date
        self.superscript = superscript
        self.inserted_words = 0
        self.deleted_words = 0
        self.changed_sections: set[str] = set()
        self.section = "_front"

    # ---- inline level

    def _span(self, inlines: list, kind: str) -> list:
        if not inlines:
            return []
        if self.marking == "tracked":
            attr = ["", ["insertion" if kind == "ins" else "deletion"], [["author", self.author], ["date", self.date]]]
        else:
            attr = ["", [], [["custom-style", INS_STYLE if kind == "ins" else DEL_STYLE]]]
        return [{"t": "Span", "c": [attr, inlines]}]

    def mark(self, inlines: list, kind: str) -> list:
        if all(i.get("t") in ("Space", "SoftBreak", "LineBreak") for i in inlines):
            return inlines if kind == "ins" else []
        words = sum(1 for i in inlines if i.get("t") in ("Str", "Cite"))
        self.changed_sections.add(self.section)
        if kind == "ins":
            self.inserted_words += words
            return self._span(inlines, "ins")
        self.deleted_words += words
        if self.deleted == "omit" and self.marking != "tracked":
            return []
        return self._span(neutralize(inlines), "del")

    def diff_inlines(self, new: list, old: list) -> list:
        new, old = split_punct(new), split_punct(old)
        sm = difflib.SequenceMatcher(None, [key(x) for x in old], [key(x) for x in new], autojunk=False)
        out: list = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                out += new[j1:j2]
                continue
            if op in ("delete", "replace"):
                out += self.mark(old[i1:i2], "del")
            if op in ("insert", "replace"):
                seg = new[j1:j2]
                # citeproc drops the space before a superscript number, but not across
                # the marking span: drop it here, for superscript styles only.
                if self.superscript:
                    seg = [x for k, x in enumerate(seg) if not (
                        x.get("t") == "Space" and k + 1 < len(seg) and seg[k + 1].get("t") == "Cite")]
                    if seg and seg[0].get("t") == "Cite" and out and out[-1].get("t") == "Space":
                        out.pop()
                out += self.mark(seg, "ins")
        return out

    # ---- block level

    def mark_block(self, b: dict, kind: str) -> dict | None:
        """Whole block inserted or deleted."""
        if kind == "del" and (self.deleted == "omit" and self.marking != "tracked"):
            self.deleted_words += count_words(b)
            self.changed_sections.add(self.section)
            return None
        b = copy.deepcopy(b)
        if kind == "del":
            strip_ids(b)
        map_inline_blocks(b, lambda inl: self.mark(inl, kind))
        return b

    def diff_blocks(self, new: list, old: list) -> list:
        sm = difflib.SequenceMatcher(None, [key(b) for b in old], [key(b) for b in new], autojunk=False)
        out: list = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                for b in new[j1:j2]:
                    self._track_section(b)
                    out.append(b)
                continue
            olds, news = old[i1:i2], new[j1:j2]
            for k in range(max(len(olds), len(news))):
                ob = olds[k] if k < len(olds) else None
                nb = news[k] if k < len(news) else None
                if nb is not None:
                    self._track_section(nb)
                if ob is not None and nb is not None and pairable(nb, ob):
                    out.append(self.diff_pair(nb, ob))
                    continue
                if ob is not None:
                    d = self.mark_block(ob, "del")
                    if d is not None:
                        out.append(d)
                if nb is not None:
                    out.append(self.mark_block(nb, "ins"))
        return out

    def _track_section(self, b: dict):
        if b.get("t") == "Header" and b["c"][0] <= 2 and b["c"][1][0]:
            self.section = b["c"][1][0]

    def diff_pair(self, nb: dict, ob: dict) -> dict:
        t = nb["t"]
        nb = copy.deepcopy(nb)
        if t in INLINE_BLOCKS:
            nb["c"] = self.diff_inlines(nb["c"], ob["c"])
        elif t == "Header":
            nb["c"][2] = self.diff_inlines(nb["c"][2], ob["c"][2])
        elif t in ("Div", "BlockQuote"):
            i = 1 if t == "Div" else None
            if i is None:
                nb["c"] = self.diff_blocks(nb["c"], ob["c"])
            else:
                nb["c"][1] = self.diff_blocks(nb["c"][1], ob["c"][1])
        elif t in ("BulletList", "OrderedList"):
            ni = nb["c"] if t == "BulletList" else nb["c"][1]
            oi = ob["c"] if t == "BulletList" else ob["c"][1]
            items = self.diff_items(ni, oi)
            if t == "BulletList":
                nb["c"] = items
            else:
                nb["c"][1] = items
        else:
            # Tables and figures: pair their text blocks in order when the shape is the same.
            n_slots, o_slots = inline_slots(nb), inline_slots(ob)
            if len(n_slots) == len(o_slots):
                for (holder, idx), (oh, oi) in zip(n_slots, o_slots):
                    holder[idx] = self.diff_inlines(holder[idx], oh[oi])
            else:
                map_inline_blocks(nb, lambda inl: self.mark(inl, "ins"))
        return nb

    def diff_items(self, new_items: list, old_items: list) -> list:
        sm = difflib.SequenceMatcher(None, [key(i) for i in old_items], [key(i) for i in new_items], autojunk=False)
        out = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                out += new_items[j1:j2]
                continue
            olds, news = old_items[i1:i2], new_items[j1:j2]
            for k in range(max(len(olds), len(news))):
                if k < len(olds) and k < len(news):
                    out.append(self.diff_blocks(news[k], olds[k]))
                elif k < len(news):
                    out.append([self.mark_block(b, "ins") for b in news[k]])
                else:
                    kept = [self.mark_block(b, "del") for b in olds[k]]
                    kept = [b for b in kept if b is not None]
                    if kept:
                        out.append(kept)
        return out


# ---------------------------------------------------------------- helpers

PUNCT = re.compile(r"^([(\[]*)(.*?)([.,;:!?)\]]*)$", re.S)


def split_punct(inlines: list) -> list:
    """'ulcer.' -> 'ulcer', '.': adding a citation before a full stop then marks
    only the citation, not the word. Rendering is unchanged (adjacent Str)."""
    out = []
    for i in inlines:
        if i.get("t") == "Str" and len(i["c"]) > 1:
            m = PUNCT.match(i["c"])
            parts = [x for x in m.groups() if x] if m else [i["c"]]
            out += [{"t": "Str", "c": x} for x in parts]
        else:
            out.append(i)
    return out

# pandoc numbers every citation in document order (note number, hash): removing
# one citation renumbers all later ones, which is not a change in the text.
CITE_BOOKKEEPING = ("citationNoteNum", "citationHash")


def norm(n):
    """Soft line breaks are layout, not content; citation counters are bookkeeping."""
    if isinstance(n, dict):
        if n.get("t") in ("SoftBreak", "LineBreak"):
            return {"t": "Space"}
        return {k: norm(v) for k, v in n.items() if k not in CITE_BOOKKEEPING}
    if isinstance(n, list):
        return [norm(x) for x in n]
    return n


def key(n) -> str:
    return json.dumps(norm(n), sort_keys=True, ensure_ascii=False)


def pairable(nb: dict, ob: dict) -> bool:
    if nb.get("t") != ob.get("t"):
        return False
    if nb["t"] in ("Div", "Figure", "Table"):
        return (nb["c"][0][0] or None) == (ob["c"][0][0] or None)
    if nb["t"] == "Header":
        return nb["c"][0] == ob["c"][0]
    return True


def neutralize(inlines: list) -> list:
    """Deleted citations must not be numbered: replace them with plain text."""
    out = []
    for i in inlines:
        if i.get("t") == "Cite":
            ids = [c["citationId"] for c in i["c"][0]]
            xref = all(x.split(":")[0] in ("fig", "tbl", "sfig", "stbl") for x in ids)
            out.append({"t": "Str", "c": "[cross-reference]" if xref else "[citation]"})
        elif isinstance(i.get("c"), list) and i.get("t") in ("Emph", "Strong", "Span", "Superscript",
                                                                "Subscript", "Underline", "SmallCaps",
                                                                "Strikeout", "Quoted", "Link"):
            j = copy.deepcopy(i)
            # the inline list is the last element for Span/Link/Quoted, or the whole content
            if i["t"] in ("Span", "Link", "Quoted"):
                j["c"][1 if i["t"] != "Link" else 1] = neutralize(j["c"][1])
            else:
                j["c"] = neutralize(j["c"])
            out.append(j)
        else:
            out.append(i)
    return out


def map_inline_blocks(b, fn):
    """Apply fn(inlines) -> inlines to every Para/Plain/Header inside block b."""
    if isinstance(b, list):
        for x in b:
            map_inline_blocks(x, fn)
        return
    if not isinstance(b, dict) or "t" not in b:
        return
    t = b["t"]
    if t in INLINE_BLOCKS:
        b["c"] = fn(b["c"])
    elif t == "Header":
        b["c"][2] = fn(b["c"][2])
    elif isinstance(b.get("c"), (list, dict)):
        map_inline_blocks(b["c"], fn)


def inline_slots(b) -> list:
    """(container, index) of every inline list in text blocks, in order."""
    slots = []

    def walk(n):
        if isinstance(n, list):
            for x in n:
                walk(x)
        elif isinstance(n, dict) and "t" in n:
            if n["t"] in INLINE_BLOCKS:
                slots.append((n, "c"))
            elif n["t"] == "Header":
                slots.append((n["c"], 2))
            elif isinstance(n.get("c"), (list, dict)):
                walk(n["c"])

    walk(b)
    return slots


def strip_ids(b):
    """A deleted copy must not reuse ids (figures, tables, sections)."""
    if isinstance(b, list):
        for x in b:
            strip_ids(x)
    elif isinstance(b, dict) and "t" in b:
        if b["t"] in ("Div", "Figure", "Table"):
            b["c"][0][0] = ""
        elif b["t"] == "Header":
            b["c"][1][0] = ""
        if isinstance(b.get("c"), (list, dict)):
            strip_ids(b["c"])


def count_words(b) -> int:
    n = 0

    def walk(x):
        nonlocal n
        if isinstance(x, list):
            for y in x:
                walk(y)
        elif isinstance(x, dict):
            if x.get("t") in ("Str", "Cite"):
                n += 1
            if isinstance(x.get("c"), (list, dict)):
                walk(x["c"])

    walk(b)
    return n


def annotate(new_doc: dict, old_doc: dict, marking: str, deleted: str, author: str, date: str,
             superscript: bool = False):
    """Return (marked AST, Marker with statistics)."""
    m = Marker(marking, deleted, author, date, superscript)
    out = copy.deepcopy(new_doc)
    out["blocks"] = m.diff_blocks(new_doc["blocks"], old_doc["blocks"])
    return out, m
