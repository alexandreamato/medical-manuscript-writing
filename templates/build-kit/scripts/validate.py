#!/usr/bin/env python3
"""Check the manuscript against a journal profile.

    python3 scripts/validate.py --journal generic-icmje
    python3 scripts/validate.py --compare                # every profile, side by side
    python3 scripts/validate.py --journal x --json       # machine-readable

Three levels, never mixed:
    ERROR  objective non-compliance; the build stops unless --force.
    WARN   likely problem, or something the code cannot decide alone.
    HUMAN  judgement the code cannot make; listed so nobody forgets it.

Two modes. `draft` (default) is for writing: problems that are normal in a
draft are WARN. `submission` (--submission) is the gate before upload:
example content, unverified or doubtful references, unverified journal
profiles and every HUMAN item not signed off in signoff/<journal>.md become
ERROR. Passing in draft mode means "valid draft", never "ready to submit".

The validator never edits the manuscript. Shortening a section or
restructuring an abstract is editorial work for the authors (or an agent,
as a reviewable change), never a silent cut by the exporter.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys

import common as C

# Tokens that are conventionally left undefined in medical journals.
ABBR_WHITELIST = {
    "CI", "SD", "SE", "IQR", "HR", "OR", "RR", "US", "USA", "UK", "EU", "DNA", "RNA", "HIV",
    "AIDS", "ID", "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII", "ORCID", "DOI",
    "PMID", "ICMJE", "CONSORT", "STROBE", "PRISMA", "STARD", "CARE", "TRIPOD", "SPIRIT", "AI",
}
PLACEHOLDER_RE = re.compile(
    r"\[(?:CITATION NEEDED|N|n|X+|TBD|TODO|REF|\.\.\.|…)\]|\bTODO\b|\bTBD\b|\bXX+\b|\?\?\?"
    # template slots such as [number], [exposure], [reason 1: n]
    r"|\[(?:[a-z][a-z0-9 ,:/]{1,40})\]")


NUM = r"-?\d+(?:[.,]\d+)?"
_SEP = r"(?:to|a|–|-|,\s)"
_LEVEL = r"(?:(?P<lvl>\d{2}(?:[.,]\d+)?)\s*%\s*)?"
_LABEL = (r"(?:CI|confidence interval|IC|intervalo de confian[cç]a(?:\s+de\s+(?P<lvl2>\d{2}(?:[.,]\d+)?)\s*%)?|"
          r"intervalo de confianza(?:\s+del?\s+(?P<lvl3>\d{2}(?:[.,]\d+)?)\s*%)?)")
# Labelled ("HR 2, 95% CI 1 to 3", "0.72, 90% CI 0.55 to 0.94", "0,72, intervalo de
# confiança de 95% 0,55 a 0,94") or parenthesised ("0.72 (0.55 to 0.94)", a table cell).
CI_RE = re.compile(
    rf"(?P<est>{NUM})\s*[,;(]?\s*\(?\s*{_LEVEL}{_LABEL}\s*[,:]?\s*\(?\s*(?P<lo>{NUM})\s*{_SEP}\s*(?P<hi>{NUM})\s*\)?"
    rf"|(?P<est2>{NUM})\s*\(\s*(?P<lo2>{NUM})\s*{_SEP}\s*(?P<hi2>{NUM})\s*\)", re.I)
# An unlabelled "12 (8 to 18)" after these words is a spread, not a confidence interval.
SPREAD_RE = re.compile(r"\b(median|IQR|interquartile|range|mediana|intervalo interquartil|amplitude|"
                       r"min(?:imum)?[-–\s]*max(?:imum)?|p25|p75|percentil)", re.I)


def _num(x: str) -> str:
    """'0,720' -> '0.72', '2.0' -> '2': equal values compare equal."""
    from decimal import Decimal, InvalidOperation
    try:
        d = Decimal(x.replace(",", "."))
    except InvalidOperation:
        return x
    t = format(d.normalize(), "f")
    return "0" if t in ("-0", "") else t


def ci_extract(text: str) -> list[dict]:
    """Every estimate with an interval, kept even when it looks wrong: extraction
    and validation are separate so a suspicious interval is reported, not lost.

    kind: "ci" (labelled; `level` is its confidence level when stated), "interval"
    (unlabelled, parenthesised: assumed to be a CI, e.g. a table cell), or
    "spread" (unlabelled after median/IQR/range: not compared as an estimate)."""
    out = []
    for m in CI_RE.finditer(text):
        if m.group("est"):
            est, lo, hi = m.group("est"), m.group("lo"), m.group("hi")
            level = m.group("lvl") or m.group("lvl2") or m.group("lvl3")
            kind = "ci"
        else:
            est, lo, hi = m.group("est2"), m.group("lo2"), m.group("hi2")
            level = None
            kind = "spread" if SPREAD_RE.search(text[max(0, m.start() - 60):m.start()]) else "interval"
        e, l, h = _num(est), _num(lo), _num(hi)
        issue = None
        try:
            fe, fl, fh = float(e), float(l), float(h)
            if fl > fh:
                issue = "lower limit above upper limit"
            elif kind != "spread" and not fl <= fe <= fh:
                issue = "estimate outside its interval"
        except ValueError:
            issue = "not a number"
        out.append({"triple": (e, l, h), "raw": m.group(0).strip(), "issue": issue, "kind": kind,
                    "level": _num(level) if level else None})
    return out


def interval_label(x: dict) -> str:
    if x.get("level"):
        return f"{x['level']}% CI"
    return "interval" if x.get("kind") == "interval" else "CI"


def ci_triples(text: str) -> set[tuple[str, str, str]]:
    """Estimates with confidence intervals (spreads such as median (IQR) excluded)."""
    return {x["triple"] for x in ci_extract(text) if x["kind"] != "spread"}


class Report:
    def __init__(self, profile_id: str):
        self.profile_id = profile_id
        self.items: list[tuple[str, str, str]] = []

    def add(self, level: str, where: str, msg: str):
        self.items.append((level, where, msg))

    def error(self, where, msg):
        self.add("ERROR", where, msg)

    def warn(self, where, msg):
        self.add("WARN", where, msg)

    def human(self, where, msg):
        self.add("HUMAN", where, msg)

    def count(self, level):
        return sum(1 for lv, _, _ in self.items if lv == level)

    def text(self) -> str:
        order = {"ERROR": 0, "WARN": 1, "INFO": 2, "HUMAN": 3}
        lines = [f"Validation against profile: {self.profile_id}"]
        for lv, where, msg in sorted(self.items, key=lambda x: order[x[0]]):
            lines.append(f"{lv:<6} {where}: {msg}")
        lines.append(f"-- {self.count('ERROR')} error(s), {self.count('WARN')} warning(s), "
                     f"{self.count('HUMAN')} item(s) for human review")
        return "\n".join(lines)


def measure(text: str, unit: str) -> int:
    if unit == "words":
        return C.count_words(text)
    if unit == "characters_with_spaces":
        return len(text)
    if unit == "characters_without_spaces":
        return len(re.sub(r"\s", "", text))
    if unit == "items":
        C.die("unit 'items' is only valid in section_limits (it counts list items in a section)")
    C.die(f"unknown limit unit '{unit}' (words, characters_with_spaces, characters_without_spaces)")


def count_items(blocks: list) -> int:
    """List items (bullets or numbered) in a section: "up to three bullet points"."""
    n = 0
    for b in blocks:
        if b.get("t") == "BulletList":
            n += len(b["c"])
        elif b.get("t") == "OrderedList":
            n += len(b["c"][1])
    return n


def check_limit(rep, where, text, limit):
    if not limit or (limit.get("max") is None and limit.get("min") is None):
        return None
    if limit.get("max") is None:
        limit = {**limit, "max": float("inf")}
    unit = limit.get("unit", "words")
    n = measure(text, unit)
    # "soft": the journal gives the number as guidance only; exceeding it is a WARN.
    flag = rep.warn if limit.get("soft") else rep.error
    note = " (guidance only)" if limit.get("soft") else ""
    if limit.get("min") is not None and n < limit["min"]:
        flag(where, f"{n} {unit.replace('_', ' ')}; minimum {limit['min']}{note}")
    if n > limit["max"]:
        flag(where, f"{n} {unit.replace('_', ' ')}; limit {limit['max']} (over by {n - limit['max']}){note}")
    return n


def validate(prof: dict, doc: dict, mode: str = "draft") -> tuple[Report, dict]:
    rep, stats = _validate(prof, doc)
    if mode == "submission":
        gate(rep, prof, C.metadata(doc))
    return rep, stats


# Warnings that must be fixed before upload (a sign-off cannot waive them).
GATED = ("references", "profile", "short-name", "authors", "language", "title", "keywords")
# Warnings that block upload unless fixed or explicitly resolved, with a reason, in the sign-off.
RESOLVABLE = ("abstract", "abstract-alt", "results")


LOCATION_RE = re.compile(r"\b(results?|resultados|methods?|métodos|abstract|resumo|table|tabela|figure|figura|"
                         r"paragraph|parágrafo|page|página|line|linha|section|seção|supplement\w*|appendix|"
                         r"apêndice)\b|§", re.I)


def resolvable(where: str, msg: str) -> bool:
    if where == "wording":  # a banned term may be legitimate in a quotation or a title
        return True
    return where in RESOLVABLE and ("estimate" in msg or "interval" in msg)


def signoff_path(journal: str):
    return C.KIT / "signoff" / f"{journal}.md"


def content_files() -> list:
    """What a sign-off vouches for: the text, metadata, references and figures."""
    files = sorted(C.MANUSCRIPT_DIR.glob("*.md")) + [C.METADATA, C.REFERENCES]
    fig = C.KIT / "figures"
    if fig.exists():
        files += sorted(p for p in fig.rglob("*") if p.is_file())
    return [p for p in files if p.exists()]


def fingerprints() -> dict[str, str]:
    import hashlib
    return {str(p.relative_to(C.KIT)): hashlib.sha256(p.read_bytes()).hexdigest()[:12] for p in content_files()}


def combined(fps: dict) -> str:
    import hashlib
    return hashlib.sha256(json.dumps(fps, sort_keys=True).encode()).hexdigest()[:16]


def read_signoff(journal: str) -> dict:
    p = signoff_path(journal)
    text = p.read_text(encoding="utf-8") if p.exists() else ""
    fp = re.search(r"^Content fingerprint:\s*([0-9a-f]{16})", text, re.M)
    files = re.search(r"<!-- files: (.*?) -->", text, re.S)
    checked, reasons = set(), {}
    for l in text.splitlines():
        if l.lower().startswith("- [x] "):
            item, _, why = l[6:].partition(" | because:")
            checked.add(item.strip())
            reasons[item.strip()] = why.strip()
    return {"exists": p.exists(), "fingerprint": fp.group(1) if fp else None,
            "files": dict(x.split("=") for x in files.group(1).split("; ") if "=" in x) if files else {},
            "checked": checked, "reasons": reasons,
            "signer": re.search(r"Signed off by:\s*(?!\[name\])(\S.*\d{4}-\d{2}-\d{2})", text)}


def write_signoff(rep: Report, journal: str, warns: list | None = None) -> str:
    """signoff/<journal>.md: one checkbox per HUMAN item and per resolvable warning.
    Ticks survive only while the content they vouch for is unchanged."""
    p = signoff_path(journal)
    p.parent.mkdir(exist_ok=True)
    old = read_signoff(journal)
    fps = fingerprints()
    same = old["fingerprint"] == combined(fps)
    checked = old["checked"] if same else set()
    signer = old["signer"].group(1) if (same and old["signer"]) else "[name], [YYYY-MM-DD]"
    lines = [f"# Sign-off before submission: {journal}", "",
             "Tick an item only after doing it. `validate.py --submission` refuses any unticked item.",
             "The fingerprint below is written by the kit: when the manuscript, metadata, references or",
             "figures change, every tick is cleared and the review starts again.", "",
             f"Signed off by: {signer}", f"Content fingerprint: {combined(fps)}",
             "<!-- files: " + "; ".join(f"{k}={v}" for k, v in fps.items()) + " -->", "",
             "## Human review", ""]
    for lv, where, msg in rep.items:
        if lv == "HUMAN":
            item = f"{where}: {msg}"
            lines.append(f"- [{'x' if item in checked else ' '}] {item}")
    if warns is None:
        warns = [f"{w}: {m}" for lv, w, m in rep.items if lv == "WARN" and resolvable(w, m)]
    if warns:
        lines += ["", "## Warnings to resolve", "",
                  "Fix each one in the manuscript, or tick it and give the reason after `| because:`.",
                  "The reason must say where the checked value is, so a reader can verify it, e.g.",
                  "`| because: the adjusted HR is in Results, paragraph 3, and Table 3; Table 2 gives crude HRs only`.",
                  "A reason without a location is not a resolution.", ""]
        for item in warns:
            why = old["reasons"].get(item, "") if same else ""
            lines.append(f"- [{'x' if item in checked else ' '}] {item} | because: {why}".rstrip())
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(p.relative_to(C.KIT))


def gate(rep: Report, prof: dict, meta: dict):
    """Submission mode: turn what may stay open in a draft into blocking errors."""
    if meta.get("example"):
        rep.error("example", "metadata.yaml has `example: true`: this is demonstration content "
                             "(fictional authors, ethics approval, declarations). Replace it and remove the flag.")
    if prof.get("generic") or prof.get("illustrative"):
        rep.error("profile", "cannot submit against a generic or illustrative profile")
    so = read_signoff(prof["id"])
    fps = fingerprints()
    stale = so["exists"] and so["fingerprint"] != combined(fps)
    if stale:
        changed = sorted(k for k in set(fps) | set(so["files"]) if fps.get(k) != so["files"].get(k))
        rep.error("sign-off", "content changed since the sign-off (" + (", ".join(changed[:6]) or "unknown")
                  + (", ..." if len(changed) > 6 else "") + "): every tick was cleared, review again")
        so = {**so, "checked": set(), "reasons": {}, "signer": None}
    # Captured before promotion: the sign-off lists them as warnings to resolve.
    to_resolve = [f"{w}: {m}" for lv, w, m in rep.items if lv == "WARN" and resolvable(w, m)]
    for i, (lv, where, msg) in enumerate(list(rep.items)):
        if lv != "WARN":
            continue
        item = f"{where}: {msg}"
        if where in GATED:
            rep.items[i] = ("ERROR", where, msg + " [blocks submission]")
        elif resolvable(where, msg):
            why = so["reasons"].get(item, "")
            located = where == "wording" or LOCATION_RE.search(why)
            if item in so["checked"] and why and not located:
                rep.items[i] = ("ERROR", where, msg + " [the reason must say where the checked value is: "
                                                      "section, paragraph, table, figure or page]")
            elif item in so["checked"] and why:
                rep.items[i] = ("WARN", where, msg + f" [resolved in sign-off: {so['reasons'][item]}]")
            else:
                rep.items[i] = ("ERROR", where, msg + " [fix it, or resolve it with a reason in the sign-off]")
    pending = [f"{w}: {m}" for lv, w, m in rep.items if lv == "HUMAN" and f"{w}: {m}" not in so["checked"]]
    unresolved = [1 for lv, w, m in rep.items if lv == "ERROR" and "resolve it with a reason" in m]
    if pending or unresolved or stale or not so["exists"]:
        rel = write_signoff(rep, prof["id"], to_resolve)
        if pending:
            rep.error("sign-off", f"{len(pending)} human-review item(s) not ticked in {rel}")
    elif not so["signer"]:
        rep.error("sign-off", f"{signoff_path(prof['id']).relative_to(C.KIT)}: fill 'Signed off by: name, YYYY-MM-DD'")


def _validate(prof: dict, doc: dict) -> tuple[Report, dict]:
    rep = Report(prof["id"] + (f" / {prof['article_type']}" if prof.get("article_type") else ""))
    meta = C.metadata(doc)
    secs = {s["id"]: s for s in C.sections(doc)}
    stats: dict = {}

    # ---- profile provenance: rules change; an unverified profile is a guess
    if prof.get("illustrative"):
        rep.warn("profile", "illustrative profile, not a real journal. Do not submit against it.")
    checked = prof.get("verified_at")
    if prof.get("generic"):
        rep.warn("profile", "generic defaults, not a journal: create journals/<target>.json from the "
                            "journal's instructions before submitting (journals/README.md).")
    elif not checked:
        rep.warn("profile", "no `verified_at`: re-read the journal's instructions to authors "
                            f"({prof.get('source_url') or 'no source_url'}) and record the date.")
    else:
        age = (dt.date.today() - dt.date.fromisoformat(checked)).days
        if age > prof.get("reverify_after_days", 180):
            rep.warn("profile", f"verified {age} days ago ({checked}); re-check {prof.get('source_url')}")
    if prof.get("article_type") and not prof.get("_article_type_known", True):
        rep.warn("profile", f"article type '{prof['article_type']}' has no specific rules in this profile; "
                            "using the journal defaults.")

    # ---- title and metadata
    title = meta.get("title") or ""
    if not title:
        rep.error("title", "missing `title` in metadata.yaml")
    t = prof.get("title", {})
    if t.get("max_chars") and len(title) > t["max_chars"]:
        rep.error("title", f"{len(title)} characters with spaces; limit {t['max_chars']}")
    rt = meta.get("running-title") or ""
    if t.get("running_title_allowed") is False and rt:
        rep.warn("running title", "the journal does not accept a running title; it is left out of the files")
    if t.get("running_title_max_chars"):
        if not rt:
            rep.error("running title", "required by the profile but missing (`running-title`)")
        elif len(rt) > t["running_title_max_chars"]:
            rep.error("running title", f"{len(rt)} characters; limit {t['running_title_max_chars']}")

    # file names carry the short name, blinded files included (common.file_name)
    sn = meta.get("short-name")
    if not sn:
        rep.warn("short-name", f"no `short-name` in metadata.yaml; files are named after the running title "
                               f"('{C.short_name(meta)}'). Set a 1-to-5-word name, e.g. `statins-ulcer`.")
    elif not C.SHORT_NAME_RE.fullmatch(sn):
        rep.error("short-name", f"'{sn}': use 1 to 5 lowercase ASCII words joined by hyphens, e.g. statins-ulcer")
    fams = {C.slugify((a or {}).get("name", "").split()[-1] if isinstance(a, dict) and a.get("name") else "", 1)
            for a in (meta.get("author") or [])} - {"manuscript", ""}
    hit = [f for f in fams if f in C.short_name(meta).split("-")]
    if hit:
        lvl = rep.error if prof.get("submission", {}).get("blinded") else rep.warn
        lvl("short-name", f"contains an author's name ({', '.join(hit)}); it goes into every file name, "
                          "including the blinded manuscript")

    kw = meta.get("keywords") or []
    k = prof.get("keywords", {})
    if k.get("min") and len(kw) < k["min"]:
        rep.error("keywords", f"{len(kw)} given; minimum {k['min']}")
    if k.get("max") and len(kw) > k["max"]:
        rep.error("keywords", f"{len(kw)} given; maximum {k['max']}")

    authors = meta.get("author") or []
    need_orcid = prof.get("authors", {}).get("require_orcid")
    for a in authors:
        a = a if isinstance(a, dict) else {"name": a}
        if need_orcid == "all" or (need_orcid == "corresponding" and a.get("corresponding")):
            if not a.get("orcid"):
                rep.error("authors", f"{a.get('name')} has no ORCID")
        if a.get("orcid") and not re.fullmatch(r"\d{4}-\d{4}-\d{4}-\d{3}[\dX]", str(a["orcid"])):
            rep.error("authors", f"{a.get('name')}: malformed ORCID {a['orcid']}")
    if authors and not any(isinstance(a, dict) and a.get("corresponding") for a in authors):
        rep.error("authors", "no corresponding author (`corresponding: true`)")
    amax = prof.get("authors", {}).get("max")
    if amax and len(authors) > amax:
        rep.error("authors", f"{len(authors)} authors; this journal/article type allows {amax}")
    # A commercial threshold (e.g. Cureus: above it the paid editing service becomes
    # mandatory) is the author's decision, never a blocking error: WARN under "limits".
    au = prof.get("authors", {})
    if au.get("max_soft") and len(authors) > au["max_soft"]:
        rep.warn("limits", f"{len(authors)} authors; above {au['max_soft']}: {au.get('soft_note') or 'see the journal'}")
    soft = prof.get("authors", {}).get("max_without_justification")
    if soft and len(authors) > soft:
        rep.warn("authors", f"{len(authors)} authors; above {soft} the journal requires a statement "
                            "justifying each author's inclusion")

    # ---- second language (e.g. J Vasc Bras: title, abstract and keywords in Portuguese and English)
    bilingual = prof.get("abstract", {}).get("bilingual")
    if bilingual:
        if not meta.get("lang-alt"):
            rep.error("language", "journal wants two languages: set `lang-alt` in metadata.yaml (e.g. en-US)")
        if not meta.get("title-alt"):
            rep.error("title", "missing `title-alt` (title in the second language)")
        elif t.get("max_chars") and len(meta["title-alt"]) > t["max_chars"]:
            rep.error("title", f"title-alt: {len(meta['title-alt'])} characters; limit {t['max_chars']}")
        kwa = meta.get("keywords-alt") or []
        if k.get("min") and len(kwa) < k["min"]:
            rep.error("keywords", f"keywords-alt: {len(kwa)} given; minimum {k['min']}")
        if k.get("max") and len(kwa) > k["max"]:
            rep.error("keywords", f"keywords-alt: {len(kwa)} given; maximum {k['max']}")

    # ---- abstract(s): `abstract`, plus `abstract-alt` when the journal is bilingual
    ab = prof.get("abstract", {})
    if ab.get("required", True):
        for sec_id in ["abstract"] + (["abstract-alt"] if bilingual else []):
            s = secs.get(sec_id)
            if not s:
                rep.error(sec_id, f"no `# ... {{#{sec_id}}}` section")
                continue
            txt = C.text_of_blocks(s["blocks"])
            if sec_id == "abstract":
                stats["abstract_words"] = C.count_words(txt)
            check_limit(rep, sec_id, txt, ab.get("limit"))
            want = [x["id"] for x in ab.get("structure", [])]
            have = [ss["id"] for ss in s["subsections"]]
            if want:
                needed = [x["id"] for x in ab.get("structure", []) if x.get("required", True)]
                missing = [w for w in needed if f"{sec_id}-{w}" not in have]
                extra = [h for h in have if h.removeprefix(f"{sec_id}-") not in want]
                if missing:
                    rep.error(sec_id, "missing structured parts: " + ", ".join(missing)
                              + f" (headers `## ... {{#{sec_id}-<part>}}`)")
                if extra:
                    rep.warn(sec_id, "parts not in this journal's structure: " + ", ".join(extra)
                             + ". Merge or rewrite them.")
            elif have:
                rep.warn(sec_id, "journal wants an unstructured abstract; subheadings will be "
                                 "dropped on export but the text still reads as structured.")
        if bilingual and "abstract" in secs and "abstract-alt" in secs:
            n1 = C.count_words(C.text_of_blocks(secs["abstract"]["blocks"]))
            n2 = C.count_words(C.text_of_blocks(secs["abstract-alt"]["blocks"]))
            if n1 and abs(n1 - n2) / n1 > 0.25:
                rep.warn("abstract", f"the two abstracts differ in length ({n1} vs {n2} words); "
                                     "the journal expects the same content in both languages")

    # ---- main text: required sections, total and per-section limits
    mt = prof.get("main_text", {})
    for sd in mt.get("sections", []):
        if sd.get("required", True) and sd["id"] not in secs:
            rep.error("sections", f"missing required section `{{#{sd['id']}}}`")
    for group in mt.get("required_any", []):
        if not any(g in secs for g in group):
            rep.error("sections", "needs at least one of: " + ", ".join(f"`{{#{g}}}`" for g in group))
    lim = mt.get("limit") or {}
    count_ids = lim.get("count_sections") or [sd["id"] for sd in mt.get("sections", [])]
    body_txt = "\n".join(C.text_of_blocks(secs[i]["blocks"], include_floats=lim.get("include_floats", False))
                         for i in count_ids if i in secs)
    stats["main_text_words"] = C.count_words(body_txt)
    n = check_limit(rep, "main text", body_txt, lim)
    if n is not None:
        stats["main_text_counted"] = f"{n} {lim.get('unit', 'words')} in " + ", ".join(count_ids)
    all_subs = {ss["id"]: ss for s_ in secs.values() for ss in s_["subsections"]}
    for sid, slim in (prof.get("section_limits") or {}).items():
        sec = secs.get(sid) or all_subs.get(sid)
        if not sec:
            continue
        if slim.get("unit") == "items":
            n = count_items(sec["blocks"])
            if slim.get("max") is not None and n > slim["max"]:
                rep.error(f"section {sid}", f"{n} list items; limit {slim['max']}")
            if slim.get("min") is not None and n < slim["min"]:
                rep.error(f"section {sid}", f"{n} list items; minimum {slim['min']}")
        else:
            check_limit(rep, f"section {sid}", C.text_of_blocks(sec["blocks"]), slim)

    # ---- declarations: always required, plus those that depend on who was studied
    # (metadata `involves: [humans]`, `[animals]`, or `[]` for reviews and method papers)
    involves = set(meta.get("involves") or [])
    conditional = prof.get("conditional_declarations", {})
    if conditional and meta.get("involves") is None:
        rep.warn("declarations", "set `involves:` in metadata.yaml ([humans], [animals] or []) so the "
                                 "conditional statements (" + ", ".join(conditional) + ") can be checked")
    required = list(prof.get("required_declarations", []))
    required += [d for d, cond in conditional.items() if involves & set(cond) or meta.get("involves") is None]
    for d in dict.fromkeys(required):
        if d not in secs and not any(d == ss["id"] for s in secs.values() for ss in s["subsections"]):
            rep.error("declarations", f"missing `{{#{d}}}` section")

    # ---- citations and references
    refs = {r["id"]: r for r in C.load_references()}
    cited = [c for c in C.citations(doc) if c.split(":")[0] not in C.XREF_PREFIXES]
    uniq = list(dict.fromkeys(cited))
    stats["references_cited"] = len(uniq)
    for c in uniq:
        if c not in refs:
            rep.error("citations", f"@{c} is not in references.json")
    for rid in refs:
        if rid not in uniq:
            rep.warn("references", f"{rid} is never cited (it will not appear in the list)")
    rcfg = prof.get("references", {})
    rmax = rcfg.get("max")
    if rmax and len(uniq) > rmax:
        if rcfg.get("soft"):
            rep.warn("limits", f"{len(uniq)} references; above {rmax}: {rcfg.get('soft_note') or 'guidance only'}")
        else:
            rep.error("references", f"{len(uniq)} cited; limit {rmax}")
    seen_doi: dict[str, str] = {}
    verified = C.load_verified()
    max_age = prof.get("references", {}).get("reverify_after_days", 90)
    for rid in uniq:
        r = refs.get(rid)
        if not r:
            continue
        doi, pmid = (r.get("DOI") or "").lower(), r.get("PMID")
        v = verified.get(rid) or {}
        current = v.get("fingerprint") == C.ref_fingerprint(r)
        st = v.get("status") if current else None
        if doi:
            if doi in seen_doi:
                rep.error("references", f"{rid} and {seen_doi[doi]} are the same DOI (duplicate entry)")
            seen_doi[doi] = rid
        if not doi and not pmid and st != "manual":
            # A source without DOI/PMID is fine once someone has checked it and said how.
            lvl = rep.error if prof.get("references", {}).get("require_identifier") else rep.warn
            lvl("references", f"{rid} has no DOI or PMID and no manual verification "
                              "(`refs.py confirm` after checking the source)")
            continue
        if st is None:
            rep.warn("references", f"{rid} not verified since it was added or edited "
                                   "(run `python3 scripts/refs.py verify`)")
            continue
        try:
            age = (dt.date.today() - dt.date.fromisoformat(v.get("checked_at", ""))).days
        except ValueError:
            age = max_age + 1
        note = f" ({v.get('notes')})" if v.get("notes") else ""
        if st in ("retracted", "mismatch", "not_found"):
            rep.error("references", f"{rid}: {st.upper().replace('_', ' ')}{note}")
        elif st in ("incomplete", "unverifiable", "stale"):
            rep.warn("references", f"{rid}: verification {st}{note}; re-run `refs.py verify`")
        elif st == "check":
            rep.warn("references", f"{rid}: look at it by eye{note}")
        elif st == "corrected":
            rep.warn("references", f"{rid} has a published correction{note}; cite it if relevant")
        if st in ("ok", "corrected", "check", "manual") and age > max_age:
            rep.warn("references", f"{rid}: last verified {age} days ago; re-run `refs.py verify` "
                                   "(retractions happen after publication)")

    # ---- figures and tables
    xcited = [c for c in C.citations(doc) if c.split(":")[0] in C.XREF_PREFIXES]
    defined = C.floats(doc)
    for f in dict.fromkeys(xcited):
        if f not in defined:
            rep.error("cross-refs", f"@{f} is cited but no figure/table has that id")
    for f in defined:
        if f not in xcited:
            rep.error("cross-refs", f"{f} is never cited in the text")
    first = [f for f in dict.fromkeys(xcited) if f in defined]
    for kind in ("fig", "tbl"):
        d_order = [f for f in defined if f.startswith(kind + ":")]
        c_order = [f for f in first if f.startswith(kind + ":")]
        if [f for f in d_order if f in c_order] != c_order:
            rep.warn("cross-refs", f"{kind} blocks are defined in a different order from their first "
                                   "mention; numbering follows first mention, which is correct, "
                                   "but move the blocks so the source reads in order.")
    nfig = sum(1 for f in defined if f.startswith("fig:"))
    ntbl = sum(1 for f in defined if f.startswith("tbl:"))
    stats.update(figures=nfig, tables=ntbl)
    fmax, tmax = prof.get("figures", {}).get("max"), prof.get("tables", {}).get("max")
    comb = prof.get("figures_tables_max")
    if fmax is not None and nfig > fmax:
        rep.error("figures", f"{nfig} figures; limit {fmax}")
    if tmax is not None and ntbl > tmax:
        rep.error("tables", f"{ntbl} tables; limit {tmax}")
    if comb is not None and nfig + ntbl > comb:
        rep.error("figures+tables", f"{nfig + ntbl} in total; limit {comb}")
    for fid, path in C.image_targets(doc).items():
        if not (C.KIT / path).exists() and not (C.MANUSCRIPT_DIR / path).exists():
            rep.error("figures", f"{fid}: image file not found ({path})")

    # ---- text-level rules
    full = {sid: C.text_of_blocks(s["blocks"], include_floats=True, skip_cites=True) for sid, s in secs.items()}
    style = prof.get("style", {})
    for sid, txt in full.items():
        for m in PLACEHOLDER_RE.finditer(txt):
            rep.error(f"section {sid}", f"placeholder left in text: {m.group(0)!r}")
        if not style.get("allow_em_dash", False):
            for m in re.finditer(r"\S+ ?— ?\S+", txt):
                rep.warn(f"section {sid}", f"em-dash inside a sentence: '{m.group(0)}' (SKILL.md, Submission Convention 3)")
        if not style.get("allow_en_dash_ranges", False):
            for m in re.finditer(r"\d\s?–\s?\d", txt):
                rep.warn(f"section {sid}", f"en-dash range '{m.group(0)}': write 'to', or set "
                                           "`style.allow_en_dash_ranges` if the journal uses dashes")
        pv = style.get("p_value")
        if pv:
            bad = r"\bp\s?[<=>]" if pv == "P" else r"\bP\s?[<=>]"
            for m in re.finditer(bad, txt):
                rep.warn(f"section {sid}", f"P-value written '{m.group(0)}'; journal style is '{pv}'")

    # terms the journal does not accept (e.g. person-first language: "obese patients")
    for bt in style.get("banned_terms", []):
        pat = bt["term"] if bt.get("regex") else r"\b" + re.escape(bt["term"]) + r"\b"
        scopes = [("title", meta.get("title") or ""), ("title-alt", meta.get("title-alt") or "")] + \
                 [(sid, txt) for sid, txt in full.items() if sid not in ("references", "_front")]
        for sid, txt in scopes:
            hits = re.findall(pat, txt, flags=re.I)
            if hits:
                use = f"; use: {bt['use']}" if bt.get("use") else ""
                rep.warn("wording", f"'{hits[0]}' in {sid} ({len(hits)}x): not accepted by the journal{use}")

    # abbreviations the journal bans outright in the title and abstract
    # true = title and abstract; or "title" / "abstract" when the journal bans them in one place only
    ban = style.get("no_abbreviations_in_title_abstract")
    if ban:
        roman = {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"}
        scopes = []
        if ban in (True, "title"):
            scopes += [("title", meta.get("title") or ""), ("title-alt", meta.get("title-alt") or "")]
        if ban in (True, "abstract"):
            scopes += [("abstract", full.get("abstract", "")), ("abstract-alt", full.get("abstract-alt", ""))]
        for scope, txt in scopes:
            found = sorted({m.group(0) for m in re.finditer(r"\b[A-Z]{2}[A-Z0-9]{0,5}\b", txt)} - roman)
            if found:
                rep.warn(scope, "journal does not allow abbreviations here: " + ", ".join(found))

    # abbreviations: first use must be the defined form "... (ABBR)"
    abstract_ids = ("abstract", "abstract-alt")
    for scope, ids in (("abstract", ["abstract"]), ("abstract-alt", ["abstract-alt"]),
                       ("main text", [i for i in full if i not in (*abstract_ids, "_front", "declarations",
                                                                  "references")])):
        txt = " ".join(full.get(i, "") for i in ids)
        seen = set()
        for m in re.finditer(r"\b[A-Z]{2}[A-Z0-9]{0,5}s?\b", txt):
            ab_ = m.group(0).rstrip("s") if m.group(0).endswith("s") and m.group(0)[:-1].isupper() else m.group(0)
            if ab_ in seen or ab_ in ABBR_WHITELIST or ab_.isdigit():
                continue
            seen.add(ab_)
            if not re.match(r"\s*[)\]]", txt[m.end():m.end() + 2]) or txt[m.start() - 1:m.start()] not in "([":
                rep.warn(scope, f"'{ab_}' first used without definition, e.g. 'hazard ratio (HR)'")

    # Estimates with confidence intervals: the same (estimate, lower, upper)
    # triple must appear in the Results or in a table, and in both abstracts.
    # Structured, but still a screen: it cannot tell which outcome, group or
    # time point a triple belongs to (that is the claim-evidence map's job).
    if "abstract" in full:
        tables = " ".join(C.text_of_blocks([b for s_ in secs.values() for b in s_["blocks"] if C.is_float(b)],
                                           include_floats=True))
        sources = full.get("results", "") + " " + tables
        body_items = [x for x in ci_extract(sources) if x["kind"] != "spread"]
        body_triples = {x["triple"] for x in body_items}
        body_levels = {x["triple"]: x["level"] for x in body_items if x["level"]}
        for where_, txt in (("abstract", full["abstract"]), ("abstract-alt", full.get("abstract-alt", "")),
                            ("results", sources)):
            for x in ci_extract(txt):
                if x["issue"]:
                    rep.warn(where_, f"suspicious interval '{x['raw']}': {x['issue']}")
        main_items = {x["triple"]: x for x in ci_extract(full["abstract"]) if x["kind"] != "spread"}
        main_triples = set(main_items)
        for tr in sorted(main_triples):
            x = main_items[tr]
            if tr not in body_triples:
                rep.warn("abstract", f"estimate {tr[0]} ({interval_label(x)} {tr[1]} to {tr[2]}) not found with "
                                     "the same interval in the Results or tables")
            elif x["level"] and body_levels.get(tr) and body_levels[tr] != x["level"]:
                rep.warn("abstract", f"estimate {tr[0]} ({tr[1]} to {tr[2]}) is a {x['level']}% CI in the "
                                     f"abstract but a {body_levels[tr]}% CI in the Results")
        if "abstract-alt" in full:
            alt_items = {x["triple"]: x for x in ci_extract(full["abstract-alt"]) if x["kind"] != "spread"}
            alt = set(alt_items)
            for tr in sorted(main_triples ^ alt):
                side = "abstract-alt" if tr in alt else "abstract"
                rep.warn("abstract-alt", f"estimate {tr[0]} ({tr[1]} to {tr[2]}) is only in `{side}`: "
                                         "the two abstracts must report the same results")
            for tr in sorted(main_triples & alt):
                a_lvl, b_lvl = main_items[tr]["level"], alt_items[tr]["level"]
                if a_lvl != b_lvl and (a_lvl or b_lvl):
                    rep.warn("abstract-alt", f"estimate {tr[0]} ({tr[1]} to {tr[2]}) is a "
                                             f"{a_lvl or 'unlabelled'}% CI in `abstract` but "
                                             f"{b_lvl or 'unlabelled'}% in `abstract-alt`".replace("unlabelled%", "unlabelled"))
        rest = " ".join(v for k_, v in full.items() if k_ not in ("abstract", "abstract-alt"))
        # Screening for other numbers (counts, percentages): present somewhere else at all?
        norm = lambda x: x.replace(",", "")
        rest_nums = set(re.findall(r"\d+(?:\.\d+)?", norm(rest)))
        in_triples = {v for tr in main_triples for v in tr}
        for num in dict.fromkeys(re.findall(r"\d+(?:\.\d+)?", norm(full["abstract"]))):
            if num not in rest_nums and num not in in_triples and len(num.replace(".", "")) > 1:
                rep.warn("abstract", f"number {num} does not appear in the main text or tables (screening)")

    # ---- human review
    design = meta.get("study-design")
    guideline = C.GUIDELINES.get(design) if design else None
    want_g = prof.get("reporting_guideline")
    if want_g and guideline and want_g.split()[0] != guideline.split()[0]:
        rep.warn("guideline", f"profile expects {want_g} but study-design '{design}' maps to {guideline}")
    if guideline:
        rep.human("reporting", f"{guideline} checklist: map every item to a page/section and upload it.")
    else:
        rep.warn("reporting", "set `study-design` in metadata.yaml to pick the reporting guideline")
    rep.human("claims", "each claim has the evidence its type needs: prior knowledge a citation, "
                        "own findings the Results, interpretation both (references/paper-review.md)")
    rep.human("citations", "each citation supports the exact sentence it is attached to "
                           "(existence is verified by refs.py, support is not)")
    for extra in prof.get("human_checks", []):
        rep.human("journal", extra)
    return rep, stats


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--journal", help="profile name (file in journals/ without .json)")
    ap.add_argument("--article-type", help="override `article-type` from metadata.yaml")
    ap.add_argument("--compare", action="store_true", help="validate against every profile")
    ap.add_argument("--json", action="store_true", help="print JSON")
    ap.add_argument("--submission", action="store_true",
                    help="submission gate: example content, doubtful references and unsigned human checks are errors")
    ap.add_argument("--write-signoff", action="store_true", help="write signoff/<journal>.md with the human-review items")
    a = ap.parse_args()

    doc = C.ast()
    atype = a.article_type or C.metadata(doc).get("article-type")
    names = C.list_profiles() if a.compare else [a.journal or C.metadata(doc).get("journal") or "generic-icmje"]

    results = []
    for name in names:
        rep, stats = validate(C.load_profile(name, atype), doc, "submission" if a.submission else "draft")
        if a.write_signoff:
            print("wrote", write_signoff(rep, name))
        results.append((name, rep, stats))

    if a.json:
        print(json.dumps([{"profile": n, "stats": s,
                           "items": [dict(level=l, where=w, message=m) for l, w, m in r.items]}
                          for n, r, s in results], ensure_ascii=False, indent=2))
    elif a.compare:
        print(f"{'profile':<28}{'errors':>7}{'warn':>6}  main errors")
        for n, r, _ in results:
            errs = [f"{w}: {m}" for l, w, m in r.items if l == "ERROR"]
            print(f"{n:<28}{r.count('ERROR'):>7}{r.count('WARN'):>6}  " + ("; ".join(errs[:3]) or "-"))
    else:
        print(results[0][1].text())
    sys.exit(1 if any(r.count("ERROR") for _, r, _ in results) and not a.compare else 0)


if __name__ == "__main__":
    main()
