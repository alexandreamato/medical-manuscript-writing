#!/usr/bin/env python3
"""Reference management. The agent never types bibliographic data by hand.

    python3 scripts/refs.py add 10.1016/S0140-6736(07)61602-X     # by DOI
    python3 scripts/refs.py add PMID:18064739                     # by PMID
    python3 scripts/refs.py add 10.1136/bmj.c332 --key schulz2010consort
    python3 scripts/refs.py verify            # Crossref / PubMed, retractions
    python3 scripts/refs.py add-manual --key who2023guideline --type report \
        --org "World Health Organization" --title "..." --year 2023 --url https://... \
        --by "A. Amato" --evidence "title page and imprint of the official PDF"
    python3 scripts/refs.py confirm KEY --by NAME --evidence "..."   # manual check of an entry
    python3 scripts/refs.py list

`references.json` holds complete CSL-JSON for each reference; the journal's
CSL style decides how it is printed. Changing journal never touches it.

`verify` checks title, year and first author against every source the
reference has (Crossref for a DOI, PubMed for a PMID) and flags retractions
and corrections (Crossref `updated-by`, Retraction Watch data; PubMed
publication type). Results go to references.verified.json with a
fingerprint and a date: editing a reference, or letting the check grow older
than --max-age days (default 90), sends it back for re-checking, because
retractions happen after publication.

Statuses: ok | corrected | check (look by eye: one-year gap, missing field)
| incomplete (a source did not answer) | mismatch | not_found | retracted |
manual (checked by a person, see add-manual/confirm) | stale | unverifiable.
Exit code: 0 all verified, 1 a reference is wrong, 3 nothing wrong found
but verification is incomplete. Never read a non-zero exit as "all good".

Set CROSSREF_MAILTO=you@example.org to join Crossref's polite pool (optional).
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

import common as C

UA = "manuscript-build-kit/1.0" + (f" (mailto:{os.environ['CROSSREF_MAILTO']})"
                                   if os.environ.get("CROSSREF_MAILTO") else "")
# CSL fields that are bulky or change without meaning a different work.
DROP = {"reference", "reference-count", "references-count", "is-referenced-by-count", "license", "link",
        "deposited", "indexed", "content-domain", "score", "relation", "resource", "member", "prefix",
        "source", "subject", "funder", "assertion", "update-policy", "alternative-id", "created",
        "published-print", "published-online", "published", "journal-issue", "short-container-title",
        "original-title", "short-title", "subtitle", "archive", "archive_location", "abstract"}


def get(url: str, accept: str = "application/json", retries: int = 3) -> dict | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    for i in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code in (429, 500, 502, 503) and i < retries - 1:
                time.sleep(2 ** i)
                continue
            raise
        except urllib.error.URLError:
            if i < retries - 1:
                time.sleep(2 ** i)
                continue
            raise
    return None


def norm_doi(s: str) -> str:
    s = s.strip()
    s = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", s, flags=re.I)
    return s


def ascii_slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


STOP = {"a", "an", "the", "of", "in", "on", "and", "for", "to", "with", "by", "from", "at", "is", "are",
        "effect", "effects", "study", "studies", "trial", "randomized", "randomised", "use"}


def make_key(ref: dict, taken: set[str]) -> str:
    fam = ""
    if ref.get("author"):
        a = ref["author"][0]
        fam = a.get("family") or a.get("literal") or ""
    fam = ascii_slug(fam) or "anon"
    year = str((ref.get("issued", {}).get("date-parts") or [[""]])[0][0] or "nd")
    words = [w for w in re.findall(r"[A-Za-z]+", ref.get("title", "")) if w.lower() not in STOP]
    base = f"{fam}{year}{ascii_slug(words[0]) if words else ''}"
    key, n = base, 0
    while key in taken:
        n += 1
        key = f"{base}{chr(96 + n)}"  # base, basea, baseb, ...
    return key


def pmid_for_doi(doi: str) -> str | None:
    q = urllib.parse.quote(f"{doi}[doi]")
    r = get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&term={q}")
    ids = (r or {}).get("esearchresult", {}).get("idlist", [])
    return ids[0] if len(ids) == 1 else None


def fetch_doi(doi: str) -> dict | None:
    r = get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}/transform/application/"
            "vnd.citationstyles.csl+json")
    return r


def fetch_pmid(pmid: str) -> dict | None:
    r = get(f"https://pmc.ncbi.nlm.nih.gov/api/ctxp/v1/pubmed/?format=csl&id={pmid}", accept="*/*")
    if isinstance(r, list):
        r = r[0] if r else None
    return r


def clean_author(a: dict) -> dict:
    """Keep the name parts CSL uses. Crossref sends group authors as {"name": ...}:
    that becomes CSL's `literal`, so "for the STROBE Initiative" is not lost."""
    keep = {k: v for k, v in a.items() if k in ("family", "given", "literal", "suffix",
                                                 "non-dropping-particle", "dropping-particle")}
    if not keep.get("family") and not keep.get("literal") and a.get("name"):
        keep["literal"] = a["name"]
    return keep


def clean(ref: dict) -> dict:
    out = {k: v for k, v in ref.items() if k not in DROP and not k.startswith("_")}
    if isinstance(out.get("container-title"), list):
        out["container-title"] = out["container-title"][0] if out["container-title"] else ""
    # CSL wants scalars here; Crossref sends lists (print and electronic ISSN).
    for k in ("ISSN", "ISBN", "URL", "container-title-short"):
        if isinstance(out.get(k), list):
            out[k] = out[k][0] if out[k] else ""
    if isinstance(out.get("title"), list):
        out["title"] = out["title"][0] if out["title"] else ""
    if out.get("title"):
        out["title"] = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", out["title"])).strip()
    if out.get("type") == "article-journal" or out.get("type") == "journal-article":
        out["type"] = "article-journal"
    # Vancouver prints the NLM journal abbreviation; keep it when the source has it.
    if ref.get("container-title-short") or ref.get("journalAbbreviation"):
        out["container-title-short"] = ref.get("container-title-short") or ref.get("journalAbbreviation")
    out["author"] = [clean_author(a) for a in out.get("author", [])]
    out["author"] = [a for a in out["author"] if a]
    return out


def cmd_add(args):
    refs = C.load_references()
    taken = {r["id"] for r in refs}
    have_doi = {(r.get("DOI") or "").lower(): r["id"] for r in refs}
    have_pmid = {str(r.get("PMID")): r["id"] for r in refs if r.get("PMID")}
    failed = 0
    for ident in args.ids:
        try:
            ref = add_one(ident, have_doi, have_pmid)
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            print(f"! {ident}: could not reach Crossref/PubMed ({getattr(e, 'reason', e)}); nothing added",
                  file=sys.stderr)
            failed += 1
            continue
        if ref is None:
            continue
        ref = clean(ref)
        key = args.key if args.key and len(args.ids) == 1 else make_key(ref, taken)
        if key in taken:
            C.die(f"key {key} already exists")
        ref["id"] = key
        taken.add(key)
        refs.append(ref)
        print(f"+ @{key}  {ref.get('title', '')[:80]}")
    C.save_references(refs)
    if failed:
        sys.exit(3)


def add_one(ident: str, have_doi: dict, have_pmid: dict) -> dict | None:
    """Fetch one record; None when it is already present or not found."""
    if ident.upper().startswith("PMID:") or ident.isdigit():
        pmid = ident.split(":")[-1]
        if pmid in have_pmid:
            print(f"= already present as {have_pmid[pmid]}")
            return None
        ref = fetch_pmid(pmid)
        if not ref:
            print(f"! PMID {pmid} not found in PubMed", file=sys.stderr)
            return None
        ref["PMID"] = pmid
    else:
        doi = norm_doi(ident)
        if doi.lower() in have_doi:
            print(f"= already present as {have_doi[doi.lower()]}")
            return None
        ref = fetch_doi(doi)
        if not ref:
            print(f"! DOI {doi} not found in Crossref", file=sys.stderr)
            return None
        pmid = pmid_for_doi(doi)
        if pmid:
            ref["PMID"] = pmid
            pm = fetch_pmid(pmid)
            if pm and pm.get("container-title-short"):
                ref["container-title-short"] = pm["container-title-short"]
    return ref


def similar(a: str, b: str) -> float:
    f = lambda s: re.sub(r"[^a-z0-9 ]", "", re.sub(r"<[^>]+>", "", (s or "").lower()))
    return difflib.SequenceMatcher(None, f(a), f(b)).ratio()


class Unreachable(Exception):
    """A source could not be queried; the reference is neither good nor bad."""


def fetch(url: str) -> dict | None:
    """get() for verification: None = the source says 'not found';
    Unreachable = no answer (network, timeout, server error, bad JSON)."""
    try:
        return get(url)
    except Exception as e:
        raise Unreachable(f"{url.split('/')[2]}: {e}") from e


def ref_year(ref: dict) -> str:
    return str((ref.get("issued", {}).get("date-parts") or [[""]])[0][0] or "")


def ref_first_family(ref: dict) -> str:
    a = (ref.get("author") or [{}])[0]
    return ascii_slug(a.get("family") or a.get("literal") or "")


def pubmed_family(name: str) -> str:
    """'von Elm E' -> 'vonelm'; 'STROBE Initiative' (collective) -> 'strobeinitiative'."""
    parts = name.split()
    if len(parts) > 1 and re.fullmatch(r"[A-Z]{1,4}", parts[-1]):
        parts = parts[:-1]
    return ascii_slug(" ".join(parts))


# Ordered by severity: a later status never downgrades an earlier, worse one.
SEVERITY = ["ok", "corrected", "check", "incomplete", "mismatch", "not_found", "retracted"]


class Result:
    def __init__(self):
        self.status, self.notes, self.checked = "ok", [], []

    def raise_to(self, status: str, note: str | None = None):
        if SEVERITY.index(status) > SEVERITY.index(self.status):
            self.status = status
        if note:
            self.notes.append(note)

    def compare(self, source: str, field: str, ours: str, theirs: str):
        """Year and first author: a missing value on either side is 'check',
        a one-year gap is 'check' (online vs print date), anything else 'mismatch'."""
        if not ours or not theirs:
            self.raise_to("check", f"{field}: not comparable with {source} (ours '{ours}', {source} '{theirs}')")
        elif ours != theirs:
            if field == "year" and ours.isdigit() and theirs.isdigit() and abs(int(ours) - int(theirs)) == 1:
                self.raise_to("check", f"year {ours} vs {source} {theirs} (online vs print date?)")
            else:
                self.raise_to("mismatch", f"{field} '{ours}' vs {source} '{theirs}'")
        self.checked.append(f"{source}:{field}")

    def as_dict(self) -> dict:
        return {"status": self.status, "notes": "; ".join(self.notes), "checked": self.checked}


def check_crossref(ref: dict, res: Result):
    doi = ref["DOI"]
    w = fetch(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
    if not w:
        res.raise_to("not_found", f"DOI {doi} not in Crossref")
        return
    m = w["message"]
    t = (m.get("title") or [""])[0]
    if similar(t, ref.get("title", "")) < 0.85:
        res.raise_to("mismatch", f"title differs: Crossref has '{t[:90]}'")
    res.checked.append("crossref:title")
    res.compare("Crossref", "year", ref_year(ref),
                str(((m.get("issued") or {}).get("date-parts") or [[""]])[0][0] or ""))
    res.compare("Crossref", "first author", ref_first_family(ref),
                ascii_slug(((m.get("author") or [{}])[0]).get("family", "")))
    for u in m.get("updated-by", []) or []:
        typ = (u.get("type") or "").lower()
        if "retraction" in typ or "withdrawal" in typ:
            res.raise_to("retracted", f"retraction {u.get('DOI')}")
        elif typ in ("correction", "erratum", "expression_of_concern", "expression-of-concern"):
            res.raise_to("corrected", f"{typ} {u.get('DOI')}")
    if t.upper().startswith("RETRACTED"):
        res.raise_to("retracted", "title marked RETRACTED")
    res.checked.append("crossref:updates")


def check_pubmed(ref: dict, res: Result):
    pmid = str(ref["PMID"])
    s = fetch(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id={pmid}")
    time.sleep(0.34)  # NCBI allows 3 requests/s without an API key
    rec = (s or {}).get("result", {}).get(pmid)
    if not rec or rec.get("error"):
        res.raise_to("not_found", f"PMID {pmid} not found")
        return
    if similar(rec.get("title", "").rstrip("."), ref.get("title", "").rstrip(".")) < 0.85:
        res.raise_to("mismatch", f"PubMed title differs: '{rec.get('title', '')[:90]}'")
    res.checked.append("pubmed:title")
    m = re.match(r"\d{4}", rec.get("pubdate") or rec.get("epubdate") or "")
    res.compare("PubMed", "year", ref_year(ref), m.group(0) if m else "")
    names = [a.get("name", "") for a in rec.get("authors") or [] if a.get("authtype", "Author") == "Author"]
    res.compare("PubMed", "first author", ref_first_family(ref), pubmed_family(names[0]) if names else "")
    if "Retracted Publication" in (rec.get("pubtype") or []):
        res.raise_to("retracted", "PubMed: Retracted Publication")
    res.checked.append("pubmed:pubtype")


def verify_one(ref: dict) -> dict:
    """Check every identifier the reference has. A source that does not answer
    makes the result 'incomplete', never 'ok'."""
    res = Result()
    if not ref.get("DOI") and not ref.get("PMID"):
        return {"status": "unverifiable", "notes": "no DOI or PMID: use `refs.py confirm` after checking "
                                                   "the source by hand", "checked": []}
    for has, fn in ((ref.get("DOI"), check_crossref), (ref.get("PMID"), check_pubmed)):
        if not has:
            continue
        try:
            fn(ref, res)
        except Unreachable as e:
            res.raise_to("incomplete", f"not checked, source unreachable ({e})")
    return res.as_dict()


def is_stale(v: dict, fp: str, max_age: int) -> bool:
    if not v or v.get("fingerprint") != fp:
        return True
    try:
        age = (dt.date.today() - dt.date.fromisoformat(v.get("checked_at", ""))).days
    except ValueError:
        return True
    return age > max_age


def cmd_verify(args):
    refs = C.load_references()
    ver = C.load_verified()
    counts = {"bad": 0, "incomplete": 0, "check": 0, "skipped": 0, "checked": 0}
    for r in refs:
        if args.only and r["id"] not in args.only:
            continue
        fp = C.ref_fingerprint(r)
        prev = ver.get(r["id"], {})
        manual = prev.get("method") == "manual" and not r.get("DOI") and not r.get("PMID")
        fresh = not is_stale(prev, fp, args.max_age)
        # Re-check anything stale, changed, or not fully verified last time; `--all` forces.
        if not args.all and fresh and prev.get("status") in ("ok", "corrected", "manual"):
            counts["skipped"] += 1
            continue
        if manual:
            if fresh:
                counts["skipped"] += 1
                continue
            res = {"status": "stale", "method": "manual", "notes": "manual verification expired: re-check the "
                   "source and run `refs.py confirm`", "checked": []}
        else:
            res = verify_one(r)
            res["method"] = "automatic"
        res.update(fingerprint=fp, checked_at=dt.date.today().isoformat())
        ver[r["id"]] = res
        counts["checked"] += 1
        st = res["status"]
        if st in ("mismatch", "not_found", "retracted"):
            counts["bad"] += 1
        elif st in ("incomplete", "stale", "unverifiable"):
            counts["incomplete"] += 1
        elif st == "check":
            counts["check"] += 1
        flag = {"ok": "ok ", "corrected": "cor", "check": "chk", "incomplete": "???", "stale": "old",
                "unverifiable": "man"}.get(st, "BAD")
        print(f"{flag} {r['id']:<32} {st} {res['notes']}")
    C.VERIFIED.write_text(json.dumps(ver, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(f"-- checked {counts['checked']}, skipped {counts['skipped']} (verified in the last {args.max_age} days); "
          f"{counts['bad']} bad, {counts['incomplete']} incomplete, {counts['check']} to check by eye")
    # 1 = a reference is wrong; 3 = nothing wrong found, but verification is not complete.
    sys.exit(1 if counts["bad"] else 3 if counts["incomplete"] else 0)


def record_manual(key: str, by: str, evidence: str, source_url: str | None):
    refs = {r["id"]: r for r in C.load_references()}
    if key not in refs:
        C.die(f"@{key} is not in references.json")
    if not by or not evidence:
        C.die("manual verification needs --by (who checked) and --evidence (what was compared, where)")
    ver = C.load_verified()
    ver[key] = {"status": "manual", "method": "manual", "verified_by": by, "evidence": evidence,
                "source_url": source_url or refs[key].get("URL"), "notes": "",
                "fingerprint": C.ref_fingerprint(refs[key]), "checked_at": dt.date.today().isoformat()}
    C.VERIFIED.write_text(json.dumps(ver, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def cmd_add_manual(args):
    """For sources without DOI/PMID: software documentation, guidelines on an
    institutional site, books, reports. The record is typed from the source in
    front of you, never from memory, and the check is logged as manual."""
    if not args.url and not args.isbn:
        C.die("a manual reference needs an official --url or an --isbn, so a reader can find it")
    refs = C.load_references()
    taken = {r["id"] for r in refs}
    if args.key in taken:
        C.die(f"key {args.key} already exists")
    rec = {"id": args.key, "type": args.type, "title": args.title}
    authors = []
    for a in args.author or []:
        fam, _, given = a.partition(",")
        authors.append({"family": fam.strip(), "given": given.strip()} if given else {"literal": fam.strip()})
    if args.org:
        authors.append({"literal": args.org})
    if authors:
        rec["author"] = authors
    if args.year:
        rec["issued"] = {"date-parts": [[int(args.year)]]}
    for fld, val in (("URL", args.url), ("publisher", args.publisher), ("publisher-place", args.place),
                     ("container-title", args.container), ("version", args.version), ("ISBN", args.isbn),
                     ("edition", args.edition), ("number", args.number)):
        if val:
            rec[fld] = val
    if args.accessed:
        y, m, d = (int(x) for x in args.accessed.split("-"))
        rec["accessed"] = {"date-parts": [[y, m, d]]}
    elif args.url:
        t = dt.date.today()
        rec["accessed"] = {"date-parts": [[t.year, t.month, t.day]]}
    refs.append(rec)
    C.save_references(refs)
    record_manual(args.key, args.by, args.evidence, args.url)
    print(f"+ @{args.key}  {args.title[:70]}  (manual, verified by {args.by})")


def cmd_confirm(args):
    record_manual(args.key, args.by, args.evidence, args.url)
    print(f"= @{args.key} marked as manually verified by {args.by}")


def cmd_list(_):
    ver = C.load_verified()
    for r in C.load_references():
        v = ver.get(r["id"], {})
        st = v.get("status", "unverified") if v.get("fingerprint") == C.ref_fingerprint(r) else "unverified"
        print(f"@{r['id']:<32} {ref_year(r):<5} {st:<12} {v.get('checked_at', ''):<11} {r.get('title', '')[:60]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add", help="add references by DOI or PMID")
    a.add_argument("ids", nargs="+")
    a.add_argument("--key", help="citation key (single reference only)")
    a.set_defaults(fn=cmd_add)
    v = sub.add_parser("verify", help="check against Crossref / PubMed")
    v.add_argument("--all", action="store_true", help="re-check every reference, however recent")
    v.add_argument("--max-age", type=int, default=90,
                   help="days a verification stays valid (default 90); older ones are re-checked")
    v.add_argument("only", nargs="*", help="limit to these keys")
    v.set_defaults(fn=cmd_verify)
    m = sub.add_parser("add-manual", help="add a source without DOI/PMID, checked by hand")
    m.add_argument("--key", required=True)
    m.add_argument("--type", required=True, choices=["webpage", "report", "book", "chapter", "software",
                                                     "dataset", "legislation", "standard", "document"])
    m.add_argument("--title", required=True)
    m.add_argument("--author", action="append", help="'Family, Given' (repeat); or use --org")
    m.add_argument("--org", help="corporate author, e.g. 'World Health Organization'")
    m.add_argument("--year")
    m.add_argument("--url", help="official URL of the source")
    m.add_argument("--accessed", help="YYYY-MM-DD (default today when --url is given)")
    for f in ("publisher", "place", "container", "version", "isbn", "edition", "number"):
        m.add_argument(f"--{f}")
    m.add_argument("--by", required=True, help="who checked the source")
    m.add_argument("--evidence", required=True, help="what was compared, e.g. 'title page and imprint, PDF v2.1'")
    m.set_defaults(fn=cmd_add_manual)
    c = sub.add_parser("confirm", help="record a manual check of an existing entry")
    c.add_argument("key")
    c.add_argument("--by", required=True)
    c.add_argument("--evidence", required=True)
    c.add_argument("--url")
    c.set_defaults(fn=cmd_confirm)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
