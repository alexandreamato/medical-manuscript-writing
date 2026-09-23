#!/usr/bin/env python3
"""Reference management. The agent never types bibliographic data by hand.

    python3 scripts/refs.py add 10.1016/S0140-6736(07)61602-X     # by DOI
    python3 scripts/refs.py add PMID:18064739                     # by PMID
    python3 scripts/refs.py add 10.1136/bmj.c332 --key schulz2010consort
    python3 scripts/refs.py verify            # Crossref / PubMed, retractions
    python3 scripts/refs.py list

`references.json` holds complete CSL-JSON for each reference; the journal's
CSL style decides how it is printed. Changing journal never touches it.

`verify` writes references.verified.json with a fingerprint of the fields it
checked; editing a reference invalidates its verification and validate.py
warns until it is re-run. Retractions and corrections come from Crossref's
`updated-by` (Retraction Watch data).

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
    key, n = base, 1
    while key in taken:
        n += 1
        key = f"{base}{chr(96 + n)}"
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
    out["author"] = [{k: v for k, v in a.items() if k in ("family", "given", "literal", "suffix",
                                                           "non-dropping-particle", "dropping-particle")}
                     for a in out.get("author", [])]
    return out


def cmd_add(args):
    refs = C.load_references()
    taken = {r["id"] for r in refs}
    have_doi = {(r.get("DOI") or "").lower(): r["id"] for r in refs}
    have_pmid = {str(r.get("PMID")): r["id"] for r in refs if r.get("PMID")}
    for ident in args.ids:
        if ident.upper().startswith("PMID:") or ident.isdigit():
            pmid = ident.split(":")[-1]
            if pmid in have_pmid:
                print(f"= already present as {have_pmid[pmid]}")
                continue
            ref = fetch_pmid(pmid)
            if not ref:
                print(f"! PMID {pmid} not found in PubMed", file=sys.stderr)
                continue
            ref["PMID"] = pmid
        else:
            doi = norm_doi(ident)
            if doi.lower() in have_doi:
                print(f"= already present as {have_doi[doi.lower()]}")
                continue
            ref = fetch_doi(doi)
            if not ref:
                print(f"! DOI {doi} not found in Crossref", file=sys.stderr)
                continue
            pmid = pmid_for_doi(doi)
            if pmid:
                ref["PMID"] = pmid
                pm = fetch_pmid(pmid)
                if pm and pm.get("container-title-short"):
                    ref["container-title-short"] = pm["container-title-short"]
        ref = clean(ref)
        key = args.key if args.key and len(args.ids) == 1 else make_key(ref, taken)
        if key in taken:
            C.die(f"key {key} already exists")
        ref["id"] = key
        taken.add(key)
        refs.append(ref)
        print(f"+ @{key}  {ref.get('title', '')[:80]}")
    C.save_references(refs)


def similar(a: str, b: str) -> float:
    f = lambda s: re.sub(r"[^a-z0-9 ]", "", re.sub(r"<[^>]+>", "", (s or "").lower()))
    return difflib.SequenceMatcher(None, f(a), f(b)).ratio()


def verify_one(ref: dict) -> dict:
    notes, status = [], "ok"
    year = str((ref.get("issued", {}).get("date-parts") or [[""]])[0][0])
    fam = ascii_slug((ref.get("author") or [{}])[0].get("family", ""))
    doi, pmid = ref.get("DOI"), ref.get("PMID")
    if not doi and not pmid:
        return {"status": "unverifiable", "notes": "no DOI or PMID"}
    if doi:
        w = get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
        if not w:
            return {"status": "not_found", "notes": f"DOI {doi} not in Crossref"}
        m = w["message"]
        t = (m.get("title") or [""])[0]
        if similar(t, ref.get("title", "")) < 0.85:
            status, _ = "mismatch", notes.append(f"title differs: Crossref has '{t[:90]}'")
        cy = str(((m.get("issued") or {}).get("date-parts") or [[""]])[0][0])
        if year and cy and year != cy:
            notes.append(f"year {year} vs Crossref {cy}")
            status = "mismatch"
        cf = ascii_slug(((m.get("author") or [{}])[0]).get("family", ""))
        if fam and cf and fam != cf:
            notes.append(f"first author {fam} vs Crossref {cf}")
            status = "mismatch"
        for u in m.get("updated-by", []) or []:
            typ = (u.get("type") or "").lower()
            if "retraction" in typ or "withdrawal" in typ:
                status = "retracted"
                notes.append(f"retraction {u.get('DOI')}")
            elif typ in ("correction", "erratum", "expression_of_concern", "expression-of-concern"):
                if status == "ok":
                    status = "corrected"
                notes.append(f"{typ} {u.get('DOI')}")
        if t.upper().startswith("RETRACTED"):
            status = "retracted"
    if pmid:
        s = get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id={pmid}")
        res = (s or {}).get("result", {}).get(str(pmid))
        if not res or res.get("error"):
            notes.append(f"PMID {pmid} not found")
            status = "not_found" if status == "ok" else status
        else:
            if similar(res.get("title", ""), ref.get("title", "")) < 0.85:
                notes.append(f"PubMed title differs: '{res.get('title', '')[:90]}'")
                status = "mismatch" if status in ("ok", "corrected") else status
            if "Retracted Publication" in (res.get("pubtype") or []):
                status = "retracted"
                notes.append("PubMed: Retracted Publication")
        time.sleep(0.34)  # NCBI allows 3 requests/s without an API key
    return {"status": status, "notes": "; ".join(notes)}


def cmd_verify(args):
    refs = C.load_references()
    ver = C.load_verified()
    bad = 0
    for r in refs:
        if args.only and r["id"] not in args.only:
            continue
        fp = C.ref_fingerprint(r)
        if not args.all and ver.get(r["id"], {}).get("fingerprint") == fp:
            continue
        try:
            res = verify_one(r)
        except Exception as e:  # network trouble must not look like a bad reference
            print(f"? {r['id']}: could not check ({e})", file=sys.stderr)
            continue
        res.update(fingerprint=fp, checked_at=dt.date.today().isoformat())
        ver[r["id"]] = res
        flag = {"ok": "ok ", "corrected": "cor"}.get(res["status"], "BAD")
        bad += flag == "BAD"
        print(f"{flag} {r['id']:<32} {res['status']} {res['notes']}")
    C.VERIFIED.write_text(json.dumps(ver, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    sys.exit(1 if bad else 0)


def cmd_list(_):
    ver = C.load_verified()
    for r in C.load_references():
        v = ver.get(r["id"], {})
        st = v.get("status", "unverified") if v.get("fingerprint") == C.ref_fingerprint(r) else "unverified"
        year = (r.get("issued", {}).get("date-parts") or [[""]])[0][0]
        print(f"@{r['id']:<32} {year}  {st:<11} {r.get('title', '')[:70]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add", help="add references by DOI or PMID")
    a.add_argument("ids", nargs="+")
    a.add_argument("--key", help="citation key (single reference only)")
    a.set_defaults(fn=cmd_add)
    v = sub.add_parser("verify", help="check against Crossref / PubMed")
    v.add_argument("--all", action="store_true", help="re-check even unchanged references")
    v.add_argument("only", nargs="*", help="limit to these keys")
    v.set_defaults(fn=cmd_verify)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
