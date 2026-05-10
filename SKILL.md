---
name: medical-manuscript-writing
description: Improve the writing quality of medical and biomedical manuscripts of any type — original research (IMRaD; RCTs, cohort and case-control studies, diagnostic accuracy studies), systematic reviews and meta-analyses, narrative and evidence-based clinical reviews, case reports, and brief reports. Use when drafting or revising Title, Abstract, Introduction, Methods, Results, Discussion, or Conclusion; checking alignment with reporting standards (CONSORT, STROBE, PRISMA, STARD, CARE); formatting citations (Vancouver default; AMA, APA, Harvard, Chicago); auditing claim-evidence fit; or running adversarial pre-submission review.
author: Alexandre Campos Moraes Amato
---
# Medical Manuscript Writing

## Overview

Use this skill to rewrite a medical or biomedical manuscript of any type — original research, systematic review, meta-analysis, narrative or evidence-based clinical review, case report, or brief report — into a reviewer-friendly, high-clarity submission that meets the expectations of biomedical journals and the relevant reporting standard (CONSORT, STROBE, PRISMA, STARD, CARE).

Prioritize three things in this order:

1. Faithfulness to the data and to the prespecified protocol.
2. Clarity of clinical question, study design, and inferential claims.
3. Compliance with the appropriate reporting checklist for the study type.

## Quick Start by Scenario

Find your situation and follow the suggested reading order:

| Scenario | Read in this order |
| --- | --- |
| **Starting an RCT manuscript from scratch** | `study-types.md` → `reporting-standards.md` (CONSORT) → `writing-process.md` → `method.md` → `results.md` → `discussion.md` → `introduction.md` → `abstract.md` → `paper-review.md` |
| **Starting an observational-study manuscript** | `study-types.md` → `reporting-standards.md` (STROBE) → `writing-process.md` → `method.md` → `results.md` → `discussion.md` → `introduction.md` → `abstract.md` → `paper-review.md` |
| **Writing a case report** | `case-report.md` → `diagrams.md` (CARE timeline) → `ethics-and-integrity.md` (consent, anonymization) → `paper-review.md` |
| **Writing a systematic review or meta-analysis** | `systematic-review.md` → `pubmed-essentials.md` → `reporting-standards.md` (PRISMA 2020) → `diagrams.md` (PRISMA flow) → `statistical-reporting.md` → `paper-review.md` |
| **Writing a narrative review or clinical update** | `narrative-review.md` → `pubmed-essentials.md` → `related-work.md` → `paper-review.md` |
| **Looking up references / building a literature framing** | `pubmed-essentials.md` → `citation-styles.md` (Vancouver default) → `manuscript-conventions.md` |
| **Writing a diagnostic-accuracy study** | `study-types.md` (diagnostic) → `reporting-standards.md` (STARD) → `method.md` → `results.md` → `diagrams.md` (STARD flow, ROC) |
| **Writing a prediction-model study** | `study-types.md` → `reporting-standards.md` (TRIPOD) → `statistical-reporting.md` → `diagrams.md` (calibration plot) |
| **Polishing a draft before submission** | `paragraph-flow.md` → `scientific-writing-principles.md` → `read-as-reader.md` → `manuscript-conventions.md` → `figures-and-tables.md` → `common-mistakes.md` → `paper-review.md` |
| **Starting a manuscript from scratch with a ready scaffold** | `templates/` (pick `rct-manuscript.md`, `observational-study.md`, `case-report.md`, or `systematic-review.md`) → `study-types.md` → `reporting-standards.md` → relevant section guides |
| **Looking up an unfamiliar term** | `glossary.md` |
| **Building a citation tool / verifying references at scale** | `research-apis.md` → `citation-styles.md` (Vancouver default) → `manuscript-conventions.md` |
| **Just finished draft 1 — want a critical self-read before refining** | `read-as-reader.md` (three personas) → `scientific-writing-principles.md` → `paragraph-flow.md` → `paper-review.md` |
| **Choosing a citation style and formatting references** | `manuscript-conventions.md` → `citation-styles.md` (Vancouver default) |
| **Building a flow diagram (CONSORT, STROBE, PRISMA, STARD)** | `diagrams.md` → `reporting-standards.md` |
| **Just received reviewer comments — preparing the response** | `responding-to-reviewers.md` → `paper-review.md` (re-audit) → `writing-process.md` (Three-pass self-review) |
| **Pre-submission final pass** | `paper-review.md` → `manuscript-conventions.md` → `reporting-standards.md` (adherence statement) → `ethics-and-integrity.md` |

## Core Workflow

1. Identify the study type and the matching reporting standard before any sentence-level edit (`references/reporting-standards.md`, `references/study-types.md`).
2. Clarify the clinical question (PICO/PECO/PIRD/PIRT) and the single take-home message of the paper.
3. Use section-specific guidance in `references/`.
4. Rewrite paragraph-by-paragraph with one message per paragraph.
5. Run reverse outlining after writing each section.
6. Check every claim in Title/Abstract/Introduction/Discussion against the Results and the prespecified analysis plan.
7. Run an adversarial pre-submission review with `references/paper-review.md`.

## Hard Rules (Never Violate)

These are non-negotiable. They reflect the most common reasons medical manuscripts get desk-rejected or returned for major revision.

1. **Never fabricate or hallucinate references.** Every citation must point to a real, verifiable publication. If a fact is uncertain, mark it `[CITATION NEEDED]` and let the author resolve it; never invent an author, year, journal, or DOI to fill the gap.
2. **Cite every table and figure in the text, in the exact order they appear.** Tables and figures are numbered by their first mention in the body text (Table 1 must be cited before Table 2; Figure 2 must be cited before Figure 3). After drafting, scan the manuscript and verify the order.
3. **References must be numbered or ordered consistently with the citation style.** Always check the target journal's Instructions to Authors first. **If the journal has not yet been chosen, default to Vancouver** (the ICMJE-recommended numeric style used by most major medical journals — NEJM, Lancet, BMJ, Annals, Nature Medicine). For Vancouver, references are numbered in order of first appearance in the text; renumber when sentences move. For AMA, APA, Harvard, Chicago, and other styles, see `references/citation-styles.md`.
4. **Do not use the em-dash (`—`) or en-dash inside body sentences.** Replace with a comma, semicolon, parenthesis, or a full stop. (Hyphens in compound terms such as `placebo-controlled` are fine. Numeric ranges should use `to`: write `12 to 18 months`, not `12—18 months`.)
5. **Default output format is Word (.docx).** Most medical journals require .docx submission. Generate manuscripts as .docx with: numbered headings, double-spaced body, line numbering, references in the journal's required style, and tables/figures placed at the end of the document or in separate files according to the journal's instructions for authors.

See `references/manuscript-conventions.md` for the full list, including dash usage, citation ordering, figure/table referencing, and .docx export guidance.

## Global Principles

1. One paragraph carries one message; the topic sentence states it.
2. Define every clinical and statistical term before reusing it; avoid abbreviation bursts.
3. Maintain sentence-to-sentence flow (cause, contrast, consequence, refinement, example).
4. Treat tables and figures as core content: a reviewer should grasp the main finding from the abstract, the primary outcome figure, and Table 1 alone.
5. Numbers, point estimates, and confidence intervals must match between Abstract, Results, tables, and figures — exactly.
6. Do not overstate causality in observational studies; do not understate uncertainty in trials.
7. Keep terminology stable across sections (e.g., do not switch between "incidence", "rate", and "risk").
8. Acknowledge limitations honestly; reviewers reward visible self-criticism.

## Paragraph Clarity Check

Use this whenever the user asks whether a paragraph "flows" or is clear.

1. Read as a busy clinician-reviewer:
   - Does this paragraph have one explicit message?
   - Does the first sentence state it?
   - Are all clinical, epidemiological, and statistical terms readable without hidden context?
   - Does each sentence connect to the previous one with a clear relation (cause, contrast, consequence, refinement, example)?
2. Run reverse outlining for the current section:
   - Write down thesis / main claim.
   - Write down each paragraph topic sentence.
   - Write down the evidence under each paragraph (study, citation, table/figure pointer, statistic).
   - Check mapping: topic sentence → thesis; evidence → topic sentence.
   - Revise or remove any paragraph that cannot be mapped cleanly.
3. If flow is still weak, add temporary section headers and explicit transitions during revision, then remove unnecessary headers before submission.

Source reference: `references/paragraph-flow.md`.

## Section Guides

Load only the file you need. The references are organized in five groups:

### A. Section guides (IMRaD)

- Title and Abstract: `references/abstract.md`
- Introduction: `references/introduction.md`
- Methods: `references/method.md`
- Results: `references/results.md`
- Discussion and Conclusion: `references/discussion.md`
- Background and prior evidence (inside Introduction or as a narrative review): `references/related-work.md`

### B. Article types (special structures)

- Case report (CARE-aligned, McCarthy & Reilly worksheet): `references/case-report.md`
- Systematic review and meta-analysis (PRISMA-aligned workflow, search, screening, extraction, risk of bias, GRADE): `references/systematic-review.md`
- Narrative review and evidence-based clinical update (POEM vs. DOE, ABC level-of-evidence rating, added-value framework): `references/narrative-review.md`

### C. Cross-cutting standards

- Reporting standards (CONSORT, STROBE, PRISMA, STARD, CARE, TRIPOD): `references/reporting-standards.md`
- Study types and PICO framing (PICO/PECO/PIRD; evidence hierarchy; causal language by design): `references/study-types.md`
- Statistical reporting checklist (effect sizes, CIs, p values, missing data, sensitivity, software): `references/statistical-reporting.md`
- Ethics, registration, conflicts of interest, AI disclosure: `references/ethics-and-integrity.md`
- PubMed essentials for manuscript writers (Boolean, MeSH, field tags, Clinical Queries, NLM journal abbreviations, PMID/DOI extraction): `references/pubmed-essentials.md`
- Open APIs for scientific research (Crossref, OpenAlex, Semantic Scholar, DataCite, NCBI E-utilities, Europe PMC, CORE, arXiv, ORCID, OpenCitations): `references/research-apis.md`

### D. Form, format, and presentation

- Manuscript conventions (dashes, citation order, table/figure referencing, .docx export): `references/manuscript-conventions.md`
- Citation styles — Vancouver (default), comparison table, reference managers, hard rules: `references/citation-styles.md`
- Citation styles — full detail on AMA, APA 7, Harvard, Chicago 18, CSE: `references/citation-styles-detail.md`
- Figures and tables (design principles, types, captions, file formats, accessibility, image-manipulation ethics): `references/figures-and-tables.md`
- Diagrams (Mermaid templates for CONSORT, STROBE, PRISMA, STARD, CARE timeline, trial schema; pointers to PRISMA2020 R package and DAGitty; statistical-figure tooling): `references/diagrams.md`

### E. Writing quality and process

- Writing process and order (drafting sequence, self-criticism, pre-submission passes): `references/writing-process.md`
- Paragraph clarity source (reverse outlining, transitions, "does my writing flow"): `references/paragraph-flow.md`
- Sentence- and word-level scientific-writing principles (six pillars, conciseness, hedging, voice, tense, abbreviations, numbers, common pitfalls): `references/scientific-writing-principles.md`
- Read-as-reader self-reading (three reader personas — methodologist, busy clinician, non-specialist; structured walkthroughs adapted from Greenhalgh): `references/read-as-reader.md`
- Common mistakes — pre-submission speed audit (consolidated cheatsheet of desk-rejection patterns and fixes): `references/common-mistakes.md`
- Adversarial paper review (rejection-dimension matrix, end-of-draft checklist): `references/paper-review.md`
- Responding to reviewers (point-by-point letter, tracked changes, disagreeing respectfully): `references/responding-to-reviewers.md`
- Glossary of statistical, methodological, and reporting terms (~60 entries): `references/glossary.md`
- Example bank index (worked abstracts, introductions, and methods): `references/examples/index.md`
- Manuscript starter templates (RCT, observational study, case report, systematic review): `templates/`

## Pre-Submission Review Core Points

Use `references/paper-review.md` for the full checklist and workflow.

1. Append an end-of-draft self-review across five rejection dimensions:
   - clinical relevance and contribution,
   - writing clarity and reproducibility,
   - methodological rigor (design, bias, confounding, statistics),
   - completeness of reporting against the relevant checklist,
   - safety, ethics, and integrity.
2. Treat claim–evidence alignment as a hard constraint, especially in Title, Abstract, Introduction, and Discussion.
3. Read the manuscript twice as a skeptical methodologist and once as a skeptical clinician.
4. Revise until every high-risk reviewer concern is explicitly addressed in the text or rebutted with prespecified evidence.

## Execution Rules

1. Build a mini-outline before drafting prose; align it to the reporting checklist for the study type.
2. State the prespecified primary outcome and analysis plan early; flag any post-hoc analyses as exploratory.
3. Avoid framing the work as an incremental tweak of a single prior study; place it in the broader evidence base.
4. Keep terminology stable across the full paper (intervention name, exposure definition, outcome definition, analysis population).
5. If a claim cannot be supported by the prespecified analysis, weaken it, move it to "exploratory", or remove it.
6. Before finalizing, append and answer the five-dimension self-review list (`references/paper-review.md`); revise unresolved items.
7. Do not load all section references at once; load only the guide needed for the current edit target.

## Output Contract

When asked to rewrite or draft sections, return:

1. A compact section outline (3–7 bullets) mapped to the relevant reporting checklist items.
2. Revised paragraphs labeled with explicit roles (knowledge gap / aim / hypothesis / design / population / intervention or exposure / outcomes / statistics / primary result / secondary result / sensitivity / strength / limitation / implication).
3. A short self-review checklist covering clarity, terminology, unsupported claims, missing evidence, and reporting-standard items.
4. A claim–evidence map for each major claim using `Claim: ... | Evidence: ... (table/figure/section, statistic) | Status: supported / needs evidence / overstated`.
