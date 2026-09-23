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
| **Revision with the build kit (journal returned an edited .docx; changes must be marked, e.g. in red for J Vasc Bras)** | `docx-build.md` (Revision round) → `templates/build-kit/README.md` (Revision rounds) → `responding-to-reviewers.md` |
| **Setting up a manuscript as source files and building the .docx** | `docx-build.md` → `templates/build-kit/README.md` → `templates/build-kit/journals/README.md` (journal profile) |
| **Changing target journal after a rejection** | `docx-build.md` (new profile, `validate.py --compare`) → `paper-review.md` |
| **Pre-submission final pass** | `paper-review.md` → `manuscript-conventions.md` → `reporting-standards.md` (adherence statement) → `ethics-and-integrity.md` |

## Match the Work to the Request

Decide the mode first. The size of the answer follows the size of the request, not the size of this skill.

| Mode | Typical request | Do | Deliver |
| --- | --- | --- | --- |
| **Point edit** | "Improve this paragraph", "fix the flow here", "shorten this sentence" | Apply the Integrity Rules and the relevant section guide to that text only. Do not re-audit the paper. | The revised text, plus only the notes the author needs: a claim you weakened, a citation you could not verify, a number that conflicts with another section. |
| **Section revision** | "Revise my Methods", "draft the Discussion" | Core Workflow steps 1 to 6 for that section. | The Output Contract below. |
| **Submission preparation** | "Is this ready to submit?", "review the whole manuscript", "prepare for journal X" | Full Core Workflow, including the adversarial review (`references/paper-review.md`). | The revised manuscript and, **as a separate document**, the audit (see Stopping Rule). Never append the audit to the text meant for the journal. |

When the mode is unclear, use the smaller one and offer the larger.

## Core Workflow

1. Identify the study type and the matching reporting standard before any sentence-level edit (`references/reporting-standards.md`, `references/study-types.md`).
2. Clarify the clinical question (PICO/PECO/PIRD/PIRT) and the single take-home message of the paper.
3. Use section-specific guidance in `references/`.
4. Rewrite paragraph-by-paragraph with one message per paragraph.
5. Run reverse outlining after writing each section.
6. Check every claim against the evidence its type requires (Integrity Rule 2): prior knowledge against the literature, the study's own findings against the Results and the prespecified analysis plan, interpretations against both.
7. For submission preparation, run the adversarial review with `references/paper-review.md`.

## Integrity Rules (Never Violate)

These protect the science. No journal, deadline, or user preference overrides them.

1. **Never fabricate or hallucinate references, data, or results.** Every citation points to a real, verifiable source. If a statement has no source you can verify, mark it `[CITATION NEEDED]` and let the author resolve it; never invent an author, year, journal, DOI, number, or finding to fill the gap. A source without a DOI or PMID (a guideline on an institutional site, software documentation, a book, a report) is acceptable once checked against the source itself and recorded with its official URL or ISBN.
2. **Every claim is supported by the evidence its type requires.**
   - *Prior knowledge* (context, burden, what earlier studies found; mostly Introduction and Discussion) needs a citation to a source that says it.
   - *This study's findings* (anything "we found"; Abstract, Results, Discussion, Conclusion) must match the Results, tables, and figures exactly, and come from the prespecified analysis or be labelled exploratory.
   - *Interpretation* (what the findings mean, how they compare, implications) must follow from this study's results and the cited literature together, with language proportional to the design (associative for observational studies).

   A claim that lacks its kind of evidence is weakened, sourced, or removed. Do not delete a well-sourced background statement because the Results do not address it.
3. **Stay faithful to the data and the prespecified protocol.** Do not change numbers, outcomes, analysis populations, or the primary question to make the text read better. Editorial changes and scientific changes are different: propose scientific ones to the authors, never make them silently.

## Submission Conventions (Defaults; the Journal's Instructions Override)

These are house defaults. Apply them unless the target journal, or the author, specifies otherwise.

1. **Tables and figures are cited in the text in numerical order.** Table 1 is the first table mentioned, Figure 2 is cited before Figure 3. After drafting, scan the manuscript and verify the order.
2. **Reference style follows the journal; Vancouver when none is chosen** (the ICMJE-recommended numeric style used by NEJM, Lancet, BMJ, Annals, Nature Medicine). For Vancouver, references are numbered in order of first appearance; renumber when sentences move. Other styles: `references/citation-styles.md`.
3. **No em-dash (`—`) or en-dash inside body sentences.** Use a comma, semicolon, parenthesis, or full stop; write ranges as `12 to 18 months`. Hyphens in compound terms (`placebo-controlled`) are fine. **Exception:** the target journal's style wins. If its instructions or recent articles print ranges with an en-dash (`95% CI 0.55–0.94`), follow them consistently; never use the dash with a negative bound (`-0.4 to 0.2`) and never mix the two forms. Details: `references/manuscript-conventions.md` §3.1.
4. **Deliver Word (.docx)** formatted as the journal requires (double spacing, line numbers, reference style, tables and figures placed per its instructions). Two ways to get there, chosen by the situation, not imposed:
   - **Editing an existing Word file** (the common case for revision requests): work in that file's flow. Return revised text or a revised .docx; do not convert the author's document into a new system unless asked.
   - **New manuscript, or when the author asks for it:** use the build kit (`templates/build-kit/`, workflow in `references/docx-build.md`). Text as Markdown, references as CSL-JSON cited by key and added through `scripts/refs.py`, journal rules in a profile, .docx generated by pandoc. It keeps citation and figure numbering correct after every edit and makes changing journal a rebuild. Offer it when a manuscript will go through many revisions or several journals.

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
- Generating the .docx procedurally (Markdown + CSL-JSON + journal profile → pandoc; validator; reference verification; co-author round trip; ready kit in `templates/build-kit/`): `references/docx-build.md`
- Citation styles — Vancouver (default), comparison table, reference managers, hard rules: `references/citation-styles.md`
- Citation styles — full detail on AMA, APA 7, Harvard, Chicago 18, CSE: `references/citation-styles-detail.md`
- Figures and tables (design principles, types, captions, file formats, accessibility, image-manipulation ethics): `references/figures-and-tables.md`
- Diagrams (web generators at enciclopedia.med.br for CONSORT, STROBE, PRISMA 2020, and CARE timeline; Mermaid templates for all flows, STARD, and trial schema; pointers to PRISMA2020 R package and DAGitty; statistical-figure tooling): `references/diagrams.md`

### E. Writing quality and process

- Writing process and order (drafting sequence, self-criticism, pre-submission passes): `references/writing-process.md`
- Paragraph clarity source (reverse outlining, transitions, "does my writing flow"): `references/paragraph-flow.md`
- Sentence- and word-level scientific-writing principles (six pillars, conciseness, hedging, voice, tense, abbreviations, numbers, common pitfalls): `references/scientific-writing-principles.md`
- Read-as-reader self-reading (three reader personas — methodologist, busy clinician, non-specialist; structured walkthroughs adapted from Greenhalgh): `references/read-as-reader.md`
- Common mistakes — pre-submission speed audit (consolidated cheatsheet of desk-rejection patterns and fixes): `references/common-mistakes.md`
- Adversarial paper review (rejection-dimension matrix, end-of-draft checklist): `references/paper-review.md`
- Responding to reviewers (point-by-point letter, tracked changes, disagreeing respectfully): `references/responding-to-reviewers.md`
- Glossary of statistical, methodological, and reporting terms (~90 entries): `references/glossary.md`
- Example bank index (worked abstracts, introductions, and methods): `references/examples/index.md`
- Manuscript starter templates (RCT, observational study, case report, systematic review) and the build kit (`templates/build-kit/`): `templates/`

## Pre-Submission Review Core Points

For submission preparation only. Use `references/paper-review.md` for the full checklist and workflow.

1. Review across five rejection dimensions:
   - clinical relevance and contribution,
   - writing clarity and reproducibility,
   - methodological rigor (design, bias, confounding, statistics),
   - completeness of reporting against the relevant checklist,
   - safety, ethics, and integrity.
2. Treat claim–evidence alignment (Integrity Rule 2) as a hard constraint.
3. Read the manuscript twice as a skeptical methodologist and once as a skeptical clinician.
4. Apply the Stopping Rule below.

## Stopping Rule

Writing can fix writing; it cannot fix a design limitation or a missing analysis. Stop revising when:

1. every editorial problem found (clarity, structure, claim wording, reporting items that the existing data can satisfy, formatting) has been corrected in the text; and
2. every remaining problem is listed for the authors, not argued away in prose.

Deliver the remaining problems separately from the manuscript, grouped by what resolving them requires:

| Needs | Examples |
| --- | --- |
| New data | Missing follow-up, unmeasured confounder, outcome not collected |
| New or changed analysis | Sensitivity analysis a reviewer will ask for, competing-risk model, multiplicity correction |
| An author decision | Which journal, whether to reframe the primary question, whether to report a post hoc finding |
| Information only the authors have | Registration number, ethics approval, funding, author contributions |

A design limitation that cannot be fixed is stated honestly in the Limitations paragraph and then left alone; revising further does not reduce the risk.

## Execution Rules

1. Build a mini-outline before drafting prose; align it to the reporting checklist for the study type.
2. State the prespecified primary outcome and analysis plan early; flag any post-hoc analyses as exploratory.
3. Avoid framing the work as an incremental tweak of a single prior study; place it in the broader evidence base.
4. Keep terminology stable across the full paper (intervention name, exposure definition, outcome definition, analysis population).
5. If a claim cannot be supported by the prespecified analysis, weaken it, move it to "exploratory", or remove it.
6. For submission preparation, answer the five-dimension self-review (`references/paper-review.md`) and deliver it separately from the manuscript, following the Stopping Rule.
7. Do not load all section references at once; load only the guide needed for the current edit target.

## Output Contract

Scaled to the mode (see Match the Work to the Request).

**Point edit:** the revised text, then at most a few lines of notes, only for what the author must know or decide. No outline, no role labels, no checklist.

**Section revision:**

1. A compact section outline (3 to 7 bullets) mapped to the relevant reporting checklist items.
2. The revised section. Label paragraph roles (knowledge gap / aim / hypothesis / design / population / intervention or exposure / outcomes / statistics / primary result / secondary result / sensitivity / strength / limitation / implication) only when the author asks for them or the structure was the problem.
3. A short list of open issues: unsupported claims, missing evidence, reporting items the text cannot yet satisfy.
4. A claim–evidence map for the claims that changed or remain doubtful: `Claim: ... | Type: prior knowledge / own finding / interpretation | Evidence: ... (citation, or table/figure/section and statistic) | Status: supported / needs evidence / overstated`.

**Submission preparation:** the revised manuscript, and a separate audit containing the claim–evidence map for all major claims, the reporting-checklist mapping, and the remaining problems grouped as in the Stopping Rule.
