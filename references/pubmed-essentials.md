# PubMed Essentials for Manuscript Writers

This file covers the parts of PubMed that a manuscript author needs in order to: build the literature framing of an Introduction, verify the uniqueness of a case before writing it up, locate the primary sources for citations, and look up NLM journal abbreviations. It is **not** a guide to systematic-review searching — for that, see `references/systematic-review.md`. For automation of PubMed inside a Claude Code workflow, see the [external tool pointer](#external-tools) at the end of this file.

## Contents

1. [What PubMed indexes (and what it doesn't)](#what-pubmed-indexes-and-what-it-doesnt)
2. [Boolean operators](#boolean-operators)
3. [MeSH vs. free-text](#mesh-vs-free-text)
4. [Field tags (the most useful ones)](#field-tags-the-most-useful-ones)
5. [Filters](#filters)
6. [Clinical Queries (one-click filtered searches)](#clinical-queries-one-click-filtered-searches)
7. [NLM journal abbreviations](#nlm-journal-abbreviations)
8. [Getting PMID, DOI, and citation data for the reference manager](#getting-pmid-doi-and-citation-data-for-the-reference-manager)
9. [My NCBI — saving searches and creating alerts](#my-ncbi--saving-searches-and-creating-alerts)
10. [What is NOT in this file](#what-is-not-in-this-file)
11. [External tools](#external-tools)

## What PubMed Indexes (and What It Doesn't)

1. **MEDLINE** — the curated subset of biomedical literature with full MeSH indexing. ~30 million records.
2. **PubMed Central (PMC)** — open-access full text.
3. **PubMed (broader)** — includes MEDLINE, PMC, in-process records (not yet MeSH-indexed), bookshelf books, NIH-funded preprints.

What PubMed does **not** cover well:

1. Embase-only journals (especially European pharmacology), CINAHL-only nursing journals, PsycINFO-only psychology journals, LILACS / SciELO Latin American literature. For systematic reviews, search those databases too.
2. Conference abstracts (most are not indexed).
3. Grey literature, theses, government reports — outside scope.

## Boolean Operators

PubMed accepts uppercase Boolean operators: `AND`, `OR`, `NOT`. Default behavior: when you type two terms separated by a space, PubMed tries Automatic Term Mapping (ATM), which often inserts `AND` and may expand to MeSH.

```
diabetes AND retinopathy            → both terms present
diabetes OR "diabetes mellitus"     → either term
diabetes NOT type 1                 → exclude type-1 diabetes (use carefully)
(diabetes OR DM) AND retinopathy    → group with parentheses
```

Rules:

1. **Operators must be UPPERCASE.** `and` is treated as a search term, not as an operator.
2. **Group with parentheses.** PubMed evaluates left to right by default; parentheses force the order you want.
3. **Use `NOT` sparingly.** It is easy to over-exclude relevant results.
4. **Quote phrases** to force literal matching: `"systematic review"`. Without quotes, PubMed may break it apart.

## MeSH vs. Free-Text

**MeSH (Medical Subject Headings)** is the controlled vocabulary that NLM indexers assign to each MEDLINE article. Searching by MeSH retrieves all relevant articles regardless of the synonym the author used (e.g., "heart attack", "myocardial infarction", "MI" all map to `Myocardial Infarction[MeSH]`).

**Free-text searching** finds whatever string the author wrote. It catches articles that have not yet been indexed (recent additions are not MeSH-indexed for ~3 weeks to several months) and journals not in MEDLINE.

The robust strategy combines both:

```
("Myocardial Infarction"[MeSH] OR "myocardial infarction"[TIAB] OR "heart attack"[TIAB])
```

### Finding the right MeSH term

1. Open the MeSH Database (top-of-page search → MeSH).
2. Search the entry term you would use naturally (e.g., "heart attack").
3. Click the resulting MeSH heading to see the full record: scope note, entry terms (synonyms), tree position, allowed subheadings (e.g., `/diagnosis`, `/therapy`, `/epidemiology`).
4. Click "Add to search builder" and copy the formatted term.

Useful MeSH features:

1. **Subheadings.** Refine a topic by aspect: `Myocardial Infarction/therapy[MeSH]`.
2. **Major MeSH (`[MAJR]`).** Restrict to articles where the topic is a *major* focus, not just incidental.
3. **Explode** (default ON). A MeSH term automatically retrieves all narrower terms in the tree.

## Field Tags (the most useful ones)

A field tag forces PubMed to search a specific field. Format: `term[tag]`.

| Tag | Meaning | Example |
| --- | --- | --- |
| `[MeSH]` or `[mh]` | MeSH heading (exploded by default) | `"myocardial infarction"[MeSH]` |
| `[MAJR]` | Major MeSH heading | `"myocardial infarction"[MAJR]` |
| `[mh:noexp]` | MeSH without explosion | `"myocardial infarction"[mh:noexp]` |
| `[ti]` | Title only | `troponin[ti]` |
| `[TIAB]` | Title or abstract | `"heart attack"[TIAB]` |
| `[au]` | Author | `solomon sd[au]` |
| `[1au]` | First author | `solomon sd[1au]` |
| `[lastau]` | Last (corresponding) author | `mcmurray jjv[lastau]` |
| `[ad]` | Affiliation | `harvard[ad]` |
| `[ta]` | Journal title abbreviation | `n engl j med[ta]` |
| `[dp]` | Date of publication | `2020:2025[dp]` |
| `[edat]` | PubMed entry date | `2024/01/01:2025/12/31[edat]` |
| `[la]` | Language | `english[la]` |
| `[pt]` | Publication type | `randomized controlled trial[pt]` |
| `[sb]` | Subset (filter set) | `medline[sb]` |
| `[doi]` | Digital Object Identifier | `10.1056/NEJMoa1908655[doi]` |
| `[pmid]` | PubMed identifier | `31475799[pmid]` |
| `[sh]` | Subheading | `therapy[sh]` |
| `[tw]` | Text word (broad) | `troponin[tw]` |

### Practical patterns

```
# All RCTs by a specific author in a specific journal
solomon sd[au] AND "n engl j med"[ta] AND "randomized controlled trial"[pt]

# Recent reviews on a topic
("heart failure"[MeSH]) AND review[pt] AND 2020:2025[dp]

# All papers from one author at one institution
"smith ab"[au] AND harvard[ad]

# Find a specific paper from a partial citation
"Solomon SD" AND "preserved ejection fraction" AND 2019[dp]
```

## Filters

The left sidebar after a search shows preset filters; the most useful for manuscript authors:

1. **Article type** — Randomized Controlled Trial, Systematic Review, Meta-Analysis, Clinical Trial, Review, Case Reports, Practice Guideline.
2. **Publication date** — Custom range, last 1/5/10 years.
3. **Species** — Humans, Other Animals.
4. **Language** — English (default), other.
5. **Sex / Age** — when relevant.
6. **Text availability** — Free full text, Full text, Abstract.
7. **Journal categories** — Core clinical journals (the 119 "Abridged Index Medicus" titles).

You can save a filter combination via "Manage filters" (requires My NCBI account).

## Clinical Queries (One-Click Filtered Searches)

PubMed Clinical Queries (https://pubmed.ncbi.nlm.nih.gov/clinical/) is a focused interface that applies pre-built methodological filters validated by Haynes et al. for evidence-based searching. It is the fastest way to find clinically useful evidence.

Three categories:

1. **Clinical Study Categories** with two scope levels (broad / narrow) for:
   - Therapy
   - Diagnosis
   - Etiology
   - Prognosis
   - Clinical Prediction Guides
2. **Systematic Reviews** — limits to systematic reviews, meta-analyses, and review articles using a validated filter.
3. **Medical Genetics** — gene-related literature filtered by topic.

Use case: when you need a small, high-yield set of articles for the Discussion of an Introduction, run the question first as a Clinical Query (narrow scope) before doing a broader search.

## NLM Journal Abbreviations

Vancouver and AMA require the **NLM-approved abbreviation** of each journal (e.g., `N Engl J Med`, not `New England Journal of Medicine`). Where to find it:

1. Go to https://pubmed.ncbi.nlm.nih.gov/.
2. Click **Journals** under the **Explore** menu (or go directly to the NLM Catalog: https://www.ncbi.nlm.nih.gov/nlmcatalog/journals).
3. Enter the full journal title.
4. The result shows: full title, ISO abbreviation, **NLM Title Abbreviation** (this is the one Vancouver/AMA expect), ISSN, MEDLINE indexing status.

Alternative: append `[ta]` to the search term to verify a journal is indexed in MEDLINE — `"jama netw open"[ta]`.

For a longer list with explanations, see *Citing Medicine* Appendix B: https://www.ncbi.nlm.nih.gov/books/NBK7253/.

## Getting PMID, DOI, and Citation Data for the Reference Manager

For each paper you cite, you need: full author list, full title, journal NLM abbreviation, year, volume, issue, pages, DOI, and PMID.

Three reliable workflows:

### Workflow 1 — From the PubMed paper page

1. Open the paper page on PubMed.
2. Click **Cite** (right side). PubMed offers AMA, MLA, APA, NLM formats — useful for a quick paste.
3. **Copy the PMID** from the citation footer at the bottom of the abstract page.
4. **Click the DOI link** (when present) to verify the article exists at the publisher.

### Workflow 2 — Bulk export to a reference manager

1. Run your search.
2. Select the relevant results (checkboxes).
3. Click **Send to** → **Citation manager** → choose `Format: PubMed` for download as a `.nbib` file, which Zotero, EndNote, Mendeley, and Papers all import natively.
4. Or **Send to** → **Clipboard** to accumulate items across multiple searches before exporting.

### Workflow 3 — From a DOI you already have

1. Append `[doi]` to a PubMed search: `10.1056/NEJMoa1908655[doi]`.
2. The single result gives you the full PubMed-formatted citation including the NLM journal abbreviation.

### Anti-fabrication discipline

The skill's Hard Rule #1 forbids inventing references. Use PubMed (or the publisher record) to verify every citation in your manuscript. If a paper does not appear in PubMed and is not retrievable from CrossRef by DOI, mark it `[CITATION NEEDED]` and resolve before submission. See `references/citation-styles.md`.

## My NCBI — Saving Searches and Creating Alerts

A free NCBI account adds:

1. **Save search.** Reuse a complex Boolean string later without re-typing it.
2. **Email alerts.** PubMed runs your saved search at a chosen frequency (daily / weekly / monthly) and emails new hits. Useful while a manuscript is in revision: keeps you aware of competing publications you may need to cite.
3. **Collections.** Group papers around a project for export later.
4. **Filter customization.** Add or remove the filters that show in the sidebar of every search.

Sign up: top-right "Log in" → register with an institutional login (ORCID, Google, eRA Commons) or email.

## What Is NOT in This File

This file covers what a manuscript author needs for routine literature work. **Out of scope here, covered elsewhere:**

1. **Sensitivity-vs-specificity-balanced search strategy for systematic reviews** (Cochrane Highly Sensitive Search Strategies, PRESS peer review of search strategies, search-string documentation per database, dates of last search). See `references/systematic-review.md`.
2. **Multi-database searching** (Embase, CINAHL, PsycINFO, LILACS, Cochrane CENTRAL). See `references/systematic-review.md` and `references/narrative-review.md`.
3. **Risk-of-bias tools, GRADE, RoB 2, ROBINS-I**. See `references/systematic-review.md`.

## External Tools

### For automation with Claude Code

For programmatic interaction with PubMed inside a Claude Code workflow — keyword search, paper detail extraction, full-text access, and Zotero export with PDF attachment — see the third-party project:

- **`cookjohn/pm-skills`** (https://github.com/cookjohn/pm-skills) — Claude Code skills using Chrome DevTools MCP to call PubMed E-utilities API and integrate with Zotero. Independent project, MIT-licensed.

This is a separate skill from the present manuscript-writing skill; it focuses on **operating** PubMed, while this skill focuses on **writing the manuscript** that emerges from the literature you find.

### Open APIs for programmatic literature work

For scripting and tool-building beyond the interactive PubMed interface — Crossref DOI resolution, OpenAlex graph queries, Europe PMC full text, OpenCitations bibliometrics, and the NCBI E-utilities API — see `references/research-apis.md`. That file lists ten free APIs with authentication notes, rate-limit guidance, and "best API by goal" mapping.

### Other useful NLM resources

1. **MeSH on Demand** (https://meshb.nlm.nih.gov/MeSHonDemand) — paste a paragraph; NLM returns suggested MeSH terms. Useful for verifying you used the right vocabulary.
2. **PubMed user guide** (https://pubmed.ncbi.nlm.nih.gov/help/) — the canonical reference.
3. **NLM Online Training** (https://learn.nlm.nih.gov/) — free interactive tutorials.

## See Also

1. **Systematic-review searching, full strategy, multi-database, risk of bias**: `references/systematic-review.md`.
2. **Narrative review search documentation** (databases, terms, languages, dates, snowballing): `references/narrative-review.md`.
3. **Looking up NLM journal abbreviations for Vancouver/AMA reference list**: `references/citation-styles.md`.
4. **Background literature framing inside an original article**: `references/related-work.md`.
5. **Verifying case-report uniqueness via focused search**: `references/case-report.md`.
