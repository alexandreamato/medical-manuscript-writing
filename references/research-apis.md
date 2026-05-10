# Open APIs for Scientific Research

A curated list of free APIs (or APIs with a real free tier) useful for medical-manuscript work — discovering papers, verifying citations, building reference lists, finding open-access full text, and bibliometric analysis.

For PubMed-specific basics (Boolean operators, MeSH, field tags, Clinical Queries) see `references/pubmed-essentials.md`. This file is the *programmatic* counterpart: when you want to script literature work or build tools rather than search interactively.

## Contents

1. [What this is for](#what-this-is-for)
2. [Article and metadata APIs](#article-and-metadata-apis)
3. [Biomedicine and life-sciences APIs](#biomedicine-and-life-sciences-apis)
4. [Preprints and open access](#preprints-and-open-access)
5. [Author identification](#author-identification)
6. [Open citations and bibliometrics](#open-citations-and-bibliometrics)
7. [Best API by goal](#best-api-by-goal)
8. [Anti-fabrication and rate-limit discipline](#anti-fabrication-and-rate-limit-discipline)

## What This Is For

In medical-manuscript writing, APIs help with concrete tasks:

1. **Verifying that a citation exists** before adding it to the reference list (Hard Rule #1: never invent a reference).
2. **Resolving a DOI to a complete citation** with NLM-correct journal abbreviation, author list, and year.
3. **Building a bibliography from PubMed IDs or DOIs** in bulk.
4. **Discovering related work** when starting a literature review.
5. **Finding open-access full text** for papers you would otherwise have to pay for.
6. **Bibliometric analysis** for a Discussion that quantifies how often a finding has been replicated.
7. **Disambiguating authors** by ORCID for grant or hiring decisions.

A skill can call these from a Node.js script, an R session, or directly from Claude via shell commands.

## Article and Metadata APIs

### 1. Crossref REST API

**URL:** https://api.crossref.org/swagger-ui/index.html
**Documentation:** https://www.crossref.org/documentation/retrieve-metadata/rest-api/
**Authentication:** None required. "Polite pool" available by including your email in the `User-Agent` header — gives you better service-level guarantees.
**Coverage:** ~140 million DOIs across publishers (articles, books, datasets, preprints).
**Best for:**

- **Resolving a DOI to a full citation** (the single most useful operation for manuscript writing).
- Finding all references *cited by* a paper that registered them.
- Looking up the journal title, ISSN, and publisher for a given DOI.

**Example — resolve a DOI:**

```bash
curl "https://api.crossref.org/works/10.1056/NEJMoa1908655" \
  -H "User-Agent: medical-manuscript-skill/1.0 (mailto:you@example.com)"
```

Returns JSON with title, author list, journal, year, volume, issue, pages, references. Map this to Vancouver/AMA format with ~30 lines of code. See `references/citation-styles.md` for the target format.

### 2. OpenAlex API

**URL:** https://api.openalex.org
**Documentation:** https://docs.openalex.org/
**Authentication:** Free; an API key (also free) raises daily quotas.
**Coverage:** Works, authors, sources, institutions, topics, funders, awards. Treats the literature as a graph.
**Best for:**

- Modern literature discovery beyond a single database.
- Finding all works by an author across publishers.
- Mapping institutional output (useful for impact analysis sections).
- Concept-level search with rich topic taxonomy.

**Example — search for a topic:**

```bash
curl "https://api.openalex.org/works?search=heart+failure+preserved+ejection+fraction&per-page=10"
```

### 3. Semantic Scholar API

**URL:** https://api.semanticscholar.org
**Documentation:** https://www.semanticscholar.org/product/api
**Authentication:** Most endpoints public without authentication; an API key gives higher rate limits and access to enriched recommendation endpoints.
**Coverage:** ~200 million papers with extracted abstracts, citations, and references.
**Best for:**

- **Paper-level recommendations** — given a paper, find papers most similar to it.
- Finding which papers cite a specific paper (forward citation tracing).
- Building exploratory literature maps for a narrative review.

**Example — get paper details:**

```bash
curl "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1056/NEJMoa1908655?fields=title,authors,year,references"
```

### 4. DataCite REST API

**URL:** https://api.datacite.org
**Documentation:** https://support.datacite.org/docs/api
**Authentication:** Public API does not require authentication.
**Coverage:** DOIs and metadata for **datasets, software, repositories**, and other research objects (not just articles). Critical when your manuscript cites a dataset DOI or a code repository.
**Best for:**

- Verifying a dataset DOI you reference in the Methods or supplementary materials.
- Citing software (R packages, GitHub releases registered with Zenodo).
- Finding the canonical citation for a deposited dataset.

## Biomedicine and Life-Sciences APIs

### 5. NCBI E-utilities (Entrez)

**URL:** https://eutils.ncbi.nlm.nih.gov
**Documentation:** https://www.ncbi.nlm.nih.gov/books/NBK25500/
**Authentication:** Public; an optional API key raises rate limits from 3 to 10 requests/second.
**Coverage:** PubMed, PMC, Gene, Protein, Nuccore, ClinVar, dbSNP, GenBank, MeSH, BioSample, GEO, and more — the full Entrez ecosystem.
**Best for:**

- **Bulk-fetching PubMed records** by PMID (the most common use case for a reference list).
- Translating between IDs (PMID ↔ DOI ↔ PMCID).
- Querying any NCBI database programmatically.

**Three core operations:**

```bash
# esearch — get PMIDs matching a query
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=dapagliflozin+heart+failure&retmode=json"

# esummary — short metadata for a list of PMIDs
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=31475799,33301246&retmode=json"

# efetch — full record (XML/MEDLINE format with abstracts, MeSH terms)
curl "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=31475799&rettype=abstract&retmode=text"
```

For PubMed search basics (Boolean, MeSH, field tags) see `references/pubmed-essentials.md`.

### 6. Europe PMC REST API

**URL:** https://www.ebi.ac.uk/europepmc/webservices/rest
**Documentation:** https://europepmc.org/RestfulWebService
**Authentication:** None required.
**Coverage:** PubMed mirror plus Europe PMC's own additions: more open-access full text, preprints, agricultural literature, and text-mining annotations.
**Best for:**

- **Open-access full text** when the paper is OA but Crossref / NCBI only return metadata.
- Text-mined entities (genes, diseases, chemicals) extracted from the full text — useful for automated literature analysis.
- An alternative to PubMed when you want a single API across PubMed and PMC.

**Example — search and request JSON:**

```bash
curl "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=dapagliflozin+heart+failure&format=json"
```

### 7. CORE API

**URL:** https://api.core.ac.uk/v3
**Documentation:** https://core.ac.uk/documentation/api
**Authentication:** Free API key required; quotas per endpoint.
**Coverage:** ~280 million open-access works aggregated from repositories worldwide. Provides metadata **and** full-text PDF download URLs when available.
**Best for:**

- **Finding the open-access version** of a paper that exists in a paywalled journal but has been deposited in an institutional repository.
- Bulk OA literature mining.

## Preprints and Open Access

### 8. arXiv API

**URL:** http://export.arxiv.org/api/query
**Documentation:** https://info.arxiv.org/help/api/
**Authentication:** None required.
**Coverage:** physics, mathematics, computer science, statistics, quantitative biology, electrical engineering, economics. Pre-prints — not peer-reviewed.
**Best for:**

- Monitoring preprints in computational and methodological domains (statistics, ML applied to medicine, biostatistics).
- Less useful for clinical-medicine work where bioRxiv / medRxiv are the relevant servers (medRxiv is searchable through Europe PMC and Crossref).

For clinical preprints, use **Europe PMC** (which indexes medRxiv and bioRxiv) instead of arXiv.

## Author Identification

### 9. ORCID Public API

**URL:** https://pub.orcid.org/v3.0
**Documentation:** https://info.orcid.org/documentation/
**Authentication:** Free for non-commercial use; OAuth 2.0 for read-public scope.
**Coverage:** Public records of ~20 million researchers worldwide.
**Best for:**

- **Disambiguating authors with common surnames.**
- Validating an ORCID iD provided by a co-author.
- Reading public works lists for collaboration mapping or hiring decisions.

**Example — resolve an ORCID iD:**

```bash
curl -H "Accept: application/json" "https://pub.orcid.org/v3.0/0000-0002-1825-0097/record"
```

## Open Citations and Bibliometrics

### 10. OpenCitations API

**URL:** https://opencitations.net
**Documentation:** https://api.opencitations.net/index
**Authentication:** Public; tokens recommended for sustained integrations.
**Coverage:** Open citation indexes (COCI, CROCI) — citation links between scholarly works as Linked Open Data.
**Best for:**

- **Open bibliometric analysis** when you cannot or should not pay for proprietary databases (Web of Science, Scopus).
- Self-citation rates, time-from-publication-to-first-citation, OCI (Open Citation Identifier) lookups.

**Example — citations of a paper:**

```bash
curl "https://opencitations.net/index/coci/api/v1/citations/10.1056/NEJMoa1908655"
```

## Best API by Goal

| Goal | Recommended stack |
| --- | --- |
| **General literature review** | OpenAlex + Crossref + Semantic Scholar |
| **Biomedical / clinical search** | NCBI E-utilities + Europe PMC |
| **Preprints in computation / ML / statistics** | arXiv + OpenAlex |
| **Preprints in medicine** | Europe PMC (covers medRxiv and bioRxiv) |
| **Bibliometrics / citation analysis** | OpenCitations + Crossref + OpenAlex |
| **Datasets, software, and other research objects** | DataCite |
| **Open-access full text** | Europe PMC + CORE |
| **Resolving a single DOI to Vancouver-format citation** | Crossref (single best choice) |
| **Bulk PMID-to-citation conversion** | NCBI E-utilities `esummary` or `efetch` |
| **Author disambiguation** | ORCID Public API |
| **Verifying a citation exists before adding to reference list** | Crossref (DOI) or NCBI E-utilities (PMID) |

## Anti-Fabrication and Rate-Limit Discipline

These APIs let you **verify** every citation against an authoritative source, which directly supports the skill's Hard Rule #1: never fabricate a reference.

Operational checklist for any tool that touches these APIs:

1. **Always identify yourself.** Use a `User-Agent: yourtool/version (mailto:you@example.com)` header. Crossref's "polite pool" gives priority to identified clients.
2. **Respect rate limits.** Crossref allows about 50 req/sec for the polite pool; NCBI 3 req/sec without a key, 10 req/sec with one; OpenAlex 100,000 calls/day in the free tier.
3. **Cache locally.** A DOI → citation mapping is stable; cache it (file or SQLite) to avoid re-fetching.
4. **Fail loud, never invent.** When an API returns 404 or no match, surface `[CITATION NEEDED]` to the author rather than synthesising a plausible-looking record.
5. **Cross-validate when stakes are high.** For a critical reference, fetch from two independent APIs (e.g., Crossref + NCBI) and compare the title, author list, year. Mismatches mean stop and inspect.
6. **Mark preprints as such.** Crossref and Europe PMC return a `subtype` field that distinguishes preprints from peer-reviewed articles. Reflect that in the reference list (`[Preprint]`).
7. **Check for retractions.** PubMed adds a `retracted` flag in the record; Crossref Event Data publishes retraction events. Always look before citing.

## Coverage and Free-Tier Honesty

| API | Free without auth? | Free with key? | Notes |
| --- | --- | --- | --- |
| Crossref | Yes (polite pool with email) | n/a | Generally generous |
| OpenAlex | Daily quota | Higher quota | Free key |
| Semantic Scholar | Public endpoints free | Higher rate limits | Free key |
| DataCite | Yes | n/a | |
| NCBI E-utilities | 3 req/sec | 10 req/sec | Free key |
| Europe PMC | Yes | n/a | |
| CORE | No (key required) | Quotas per endpoint | Free key |
| arXiv | Yes | n/a | Be polite — 1 req every 3 seconds is the recommended pace |
| ORCID Public API | Yes (non-commercial) | OAuth 2.0 read-public | |
| OpenCitations | Yes | Token recommended | |

## See Also

1. **PubMed search basics** (interactive use): `references/pubmed-essentials.md`.
2. **Citation styles** that these APIs feed into: `references/citation-styles.md`.
3. **Hard Rule on never inventing references**: `SKILL.md`, `references/manuscript-conventions.md`, `references/common-mistakes.md`.
4. **External skill for Claude Code with Chrome DevTools MCP-based PubMed automation**: https://github.com/cookjohn/pm-skills.
