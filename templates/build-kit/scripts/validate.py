#!/usr/bin/env python3
"""Check the manuscript against a journal profile.

    python3 scripts/validate.py --journal generic-icmje
    python3 scripts/validate.py --compare                # every profile, side by side
    python3 scripts/validate.py --journal x --json       # machine-readable

Three levels, never mixed:
    ERROR  objective non-compliance; the build stops unless --force.
    WARN   likely problem, or something the code cannot decide alone.
    HUMAN  judgement the code cannot make; listed so nobody forgets it.

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
        order = {"ERROR": 0, "WARN": 1, "HUMAN": 2}
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
    C.die(f"unknown limit unit '{unit}' (words, characters_with_spaces, characters_without_spaces)")


def check_limit(rep, where, text, limit):
    if not limit or limit.get("max") is None:
        return None
    unit = limit.get("unit", "words")
    n = measure(text, unit)
    if n > limit["max"]:
        rep.error(where, f"{n} {unit.replace('_', ' ')}; limit {limit['max']} (over by {n - limit['max']})")
    return n


def validate(prof: dict, doc: dict) -> tuple[Report, dict]:
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
    lim = mt.get("limit") or {}
    count_ids = lim.get("count_sections") or [sd["id"] for sd in mt.get("sections", [])]
    body_txt = "\n".join(C.text_of_blocks(secs[i]["blocks"], include_floats=lim.get("include_floats", False))
                         for i in count_ids if i in secs)
    stats["main_text_words"] = C.count_words(body_txt)
    n = check_limit(rep, "main text", body_txt, lim)
    if n is not None:
        stats["main_text_counted"] = f"{n} {lim.get('unit', 'words')} in " + ", ".join(count_ids)
    for sid, slim in (prof.get("section_limits") or {}).items():
        if sid in secs:
            check_limit(rep, f"section {sid}", C.text_of_blocks(secs[sid]["blocks"]), slim)

    # ---- declarations
    for d in prof.get("required_declarations", []):
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
    rmax = prof.get("references", {}).get("max")
    if rmax and len(uniq) > rmax:
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

    # abbreviations the journal bans outright in the title and abstract
    if style.get("no_abbreviations_in_title_abstract"):
        roman = {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"}
        for scope, txt in (("title", meta.get("title") or ""), ("title-alt", meta.get("title-alt") or ""),
                           ("abstract", full.get("abstract", "")), ("abstract-alt", full.get("abstract-alt", ""))):
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

    # numbers in the abstract must appear in the rest of the manuscript
    if "abstract" in full:
        rest = " ".join(v for k_, v in full.items() if k_ not in ("abstract", "abstract-alt"))
        norm = lambda s: s.replace(",", "")
        rest_nums = set(re.findall(r"\d+(?:\.\d+)?", norm(rest)))
        for num in dict.fromkeys(re.findall(r"\d+(?:\.\d+)?", norm(full["abstract"]))):
            if num not in rest_nums and len(num.replace(".", "")) > 1:
                rep.warn("abstract", f"number {num} does not appear in the main text or tables")

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
    a = ap.parse_args()

    doc = C.ast()
    atype = a.article_type or C.metadata(doc).get("article-type")
    names = C.list_profiles() if a.compare else [a.journal or C.metadata(doc).get("journal") or "generic-icmje"]

    results = []
    for name in names:
        rep, stats = validate(C.load_profile(name, atype), doc)
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
