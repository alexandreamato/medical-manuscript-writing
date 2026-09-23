---
name: medical-manuscript-writing
description: Write and revise medical and biomedical manuscripts (RCTs, cohort, case-control, diagnostic accuracy and prediction studies, systematic and narrative reviews, case reports), from title to conclusion. Use for reporting guidelines (CONSORT, STROBE, PRISMA, STARD, CARE, TRIPOD+AI), citations (Vancouver default), claim-evidence audits, journal choice, submission, revision and responses to reviewers.
license: CC-BY-4.0
metadata:
  author: Alexandre Campos Moraes Amato
  version: 1.10.0
---
# Medical Manuscript Writing

Turn a medical manuscript, or part of one, into clear, honest text that meets its journal's expectations and its reporting guideline. Priorities, in order: faithfulness to the data and protocol; clarity of the question, design and claims; compliance with the reporting guideline. Load only the reference file the task needs (map at the end).

## Match the Work to the Request

| Mode | Typical request | Do | Deliver |
| --- | --- | --- | --- |
| **Point edit** | "Improve this paragraph" | Integrity Rules and the relevant guide, on that text only | The revised text, plus only the notes the author must know (a weakened claim, an unverifiable citation, a number that conflicts elsewhere) |
| **Section revision** | "Revise my Methods" | Core Workflow for that section | Output Contract, section revision |
| **Submission preparation** | "Is this ready?", "prepare for journal X" | Full Core Workflow and `paper-review.md` | The manuscript, and the audit as a separate document |

When unclear, use the smaller mode and offer the larger. Answer in the format the user asked for: revised text for pasted text; a Word file only when delivering a manuscript file.

## Integrity Rules (obligatory)

No journal, deadline or preference overrides these.

1. **Never fabricate references, data or results.** Every citation points to a real source you verified. With no verifiable source, write `[CITATION NEEDED]`; never invent an author, year, journal, DOI, number or finding. A source without DOI or PMID (guideline page, software documentation, book, report) is fine once checked against the source and recorded with its URL or ISBN. A reference you could not check is unverified, not fabricated: classify it (`paper-review.md`, four categories).
2. **Every claim has the evidence its type requires.** Prior knowledge: a citation that says it. This study's findings: the Results, tables and figures, with the same numbers, from the prespecified analysis or labelled exploratory. Interpretation: both, in language proportional to the design. Source, weaken or remove what lacks its evidence; never delete well-sourced background because the Results do not test it.
3. **Stay faithful to the data and the protocol.** Do not change numbers, outcomes, populations or the primary question for style. Propose scientific changes to the authors; never make them silently.

## Conditional Rules (when the design, mode or journal calls for them)

1. In section revision and submission preparation, identify the design and its reporting guideline first (`study-types.md`, `reporting-standards.md`). A point edit does not need it.
2. Ethics approval, consent, registration and data sharing apply as the design and journal require (`ethics-and-integrity.md`).
3. Define the terms the target reader may not know; the journal's audience sets the bar (`scientific-writing-principles.md`).
4. Causal verbs only for designs that support them (`study-types.md`).

## Submission Conventions (defaults; the journal's instructions override)

1. Tables and figures cited in numerical order; references in the journal's style, Vancouver when none is chosen (`manuscript-conventions.md` §1.2, §2.1; `citation-styles.md`).
2. No em-dash or en-dash inside body sentences; ranges as `12 to 18`. If the journal prints dashes (`95% CI 0.55–0.94`), follow it consistently, never with a negative bound, never mixed (§3.1).
3. Deliver what the author works in. Revising an existing Word file: stay in it. New manuscript, many revisions or several journals: offer the build kit (`docx-build.md`, `templates/build-kit/`), which generates the .docx per journal profile (J Vasc Bras by default; also J Vasc Surg, Phlebology, Obesity, Obesity Facts, Clinical Obesity, Int J Obes, J Clin Med, Cureus), marks revisions as the journal asks and names files `<short-name>_<journal>[_rev<N>]_<part>`.

## Core Workflow

1. Mode, and (conditional rule 1) design and guideline.
2. The clinical question (PICO/PECO) and the single take-home message.
3. Rewrite with the section guide, one message per paragraph (`paragraph-flow.md`).
4. Check each claim against its evidence (Integrity Rule 2) and the cross-section consistency checks (`paper-review.md`).
5. Submission preparation only: the adversarial review in `paper-review.md`, then the Stopping Rule.

## Stopping Rule

Writing fixes writing, not a design limitation or a missing analysis. Stop when every editorial problem is fixed in the text, and list the rest for the authors, separately from the manuscript, by what it needs: new data, new analysis, an author decision, or information only the authors have. State an unfixable limitation in the Limitations paragraph and leave it.

## Output Contract

- **Point edit:** revised text and at most a few lines of notes. No outline, labels or checklist.
- **Section revision:** the revised section and its open issues. Add, only when they earn their place: an outline (3 to 7 bullets mapped to the guideline items) when the structure changed or the section is long; paragraph role labels when asked or when structure was the problem; a claim–evidence map (`Claim | Type: prior knowledge / own finding / interpretation | Evidence | Status: supported / needs evidence / overstated`) when claims were added, changed or are doubtful. A light copy-edit of a section needs none of them.
- **Submission preparation:** the manuscript, and a separate audit: claim–evidence map of major claims, guideline mapping, remaining problems grouped as in the Stopping Rule.

## Where to Look

Files are in `references/` unless another path is given.

| Scenario | Read |
| --- | --- |
| New RCT or observational manuscript | `study-types.md` → `reporting-standards.md` → `writing-process.md` → section guides → `paper-review.md` |
| Case report | `case-report.md` → `diagrams.md` (CARE timeline) → `ethics-and-integrity.md` |
| Systematic review or meta-analysis | `systematic-review.md` → `pubmed-essentials.md` → `reporting-standards.md` → `statistical-figures.md` |
| Narrative review | `narrative-review.md` → `related-work.md` |
| Diagnostic accuracy or prediction model | `study-types.md` → `reporting-standards.md` (STARD, TRIPOD+AI) → `statistical-figures.md` |
| Title and keywords | `title.md` |
| Choosing a journal, checking it is legitimate, preprints | `journal-selection.md` |
| Initial submission cover letter | `cover-letter.md` |
| Non-native English author | `non-native-authors.md` → `scientific-writing-principles.md` |
| Polishing a draft | `read-as-reader.md` → `paragraph-flow.md` → `scientific-writing-principles.md` → `common-mistakes.md` |
| Pre-submission final pass | `paper-review.md` → `reporting-standards.md` → `ethics-and-integrity.md` |
| Reviewer comments; revision | `responding-to-reviewers.md`; with the kit, `docx-build.md` (Revision round) |
| Source files and generated .docx; changing journal | `docx-build.md` → `templates/build-kit/README.md` → `templates/build-kit/journals/README.md` |
| Flow diagram (CONSORT, STROBE, PRISMA, STARD) | `diagrams.md` |
| Ready scaffold | `templates/` |

**Files, one line each**

- Sections: `abstract.md`, `introduction.md`, `method.md`, `results.md`, `discussion.md`; background and prior evidence `related-work.md`; `title.md`.
- Article types: `case-report.md` (CARE), `systematic-review.md` (PRISMA 2020), `narrative-review.md`.
- Standards: `reporting-standards.md` (all guidelines, selector); `study-types.md` (designs, PICO, causal language); `statistical-reporting.md` (estimates, CIs, missing data, noninferiority); `ethics-and-integrity.md` (what applies to which design).
- Literature and references: `pubmed-essentials.md`; `research-apis.md` (Crossref, OpenAlex, E-utilities); `citation-styles.md` (Vancouver) and `citation-styles-detail.md` (AMA, APA, Harvard, Chicago, CSE).
- Presentation: `manuscript-conventions.md` (citation and figure order, dashes, file format); `figures-and-tables.md`; `diagrams.md` (flows, timelines, schemas, DAG); `statistical-figures.md` (forest, KM, funnel, ROC, calibration); `docx-build.md` (build kit, revision rounds, file names).
- Process and quality: `writing-process.md`; `paragraph-flow.md` (flow, clarity check, reverse outline); `scientific-writing-principles.md`; `non-native-authors.md`; `read-as-reader.md`; `common-mistakes.md` (five-minute audit); `paper-review.md` (the full pre-submission checklist); `responding-to-reviewers.md`; `cover-letter.md`; `journal-selection.md`; `glossary.md`.
- Examples: `examples/index.md` (abstracts, introductions, methods, results, discussions; all fictional).
- Scaffolds: `templates/` (RCT, observational, case report, systematic review) and `templates/build-kit/`.
