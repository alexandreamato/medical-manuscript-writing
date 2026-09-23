---
name: medical-manuscript-writing
description: Write, revise and translate medical manuscripts (RCTs, observational, diagnostic and prediction studies, systematic, scoping and narrative reviews, case reports). Use for reporting guidelines (CONSORT, STROBE, PRISMA, STARD, CARE, TRIPOD+AI), formatting references (Vancouver default), claim-evidence audits, translating abstracts, cover letters, journal choice, submission and responding to reviewers, including for Portuguese-speaking and other non-native English authors.
license: CC-BY-4.0
metadata:
  author: Alexandre Campos Moraes Amato
  version: 1.11.1
---
# Medical Manuscript Writing

Turn a medical manuscript, or part of one, into clear, honest text that meets its journal's expectations and its reporting guideline. Priorities, in order: faithfulness to the data and protocol; clarity of the question, design and claims; compliance with the reporting guideline. Load only the file the task needs (map at the end).

## Match the Work to the Request

| Mode | Typical request | Do |
| --- | --- | --- |
| **Point edit** | "Improve this paragraph" | Integrity Rules and the relevant guide, on that text only |
| **Section revision** | "Revise my Methods" | Core Workflow for that section |
| **Submission preparation** | "Is this ready?", "prepare for journal X" | Full Core Workflow and `paper-review.md` |

When unclear, use the smaller mode and offer the larger. What each mode delivers: Output Contract.

## When Information Is Missing

- **Design:** infer it from the text and state the inference ("read as a retrospective cohort").
- **Target journal:** ask only in submission preparation, where it changes the deliverable. In the other modes apply the defaults (Vancouver; J Vasc Bras in the build kit) and flag them. Never assume either silently.
- **Language:** answer in the user's language; write the manuscript in the journal's language (English when no journal is known; keep the language of a draft the user is revising); for a bilingual journal, title, abstract and keywords in both. Translation requests: `non-native-authors.md` §6.

## Integrity Rules (obligatory)

No journal, deadline or preference overrides these.

1. **Never fabricate references, data or results.** Every citation points to a real source you verified. With no verifiable source, write `[CITATION NEEDED]`; never invent an author, year, journal, DOI, number or finding. A source without DOI or PMID (guideline page, software manual, book) is fine once checked against the source and recorded with its URL or ISBN. A reference you could not check is unverified, not fabricated: classify it (`paper-review.md`, four categories).
2. **Every claim has the evidence its type requires.** Prior knowledge: a citation that says it. This study's findings: the Results, tables and figures, with the same numbers, from the prespecified analysis or labelled exploratory. Interpretation: both, in language proportional to the design. Source, weaken or remove what lacks its evidence; never delete well-sourced background because the Results do not test it.
3. **Stay faithful to the data and the protocol.** Do not change numbers, outcomes, populations or the primary question for style. Propose scientific changes to the authors; never make them silently. Numbers you derive from raw data (e.g., a CSV) are a new analysis, not reporting: label them as such, never present them as prespecified results, and have the authors confirm them before they enter Results.

## Conditional Rules (when the design, mode or journal calls for them)

1. In section revision and submission preparation, identify the design and its reporting guideline first (`study-types.md`, `reporting-standards.md`). A point edit does not need it.
2. Ethics approval, consent, registration and data sharing apply as the design and journal require (`ethics-and-integrity.md`).
3. Define the terms the target reader may not know; the journal's audience sets the bar (`scientific-writing-principles.md`).
4. Causal verbs only for designs that support them (`study-types.md`).

## Submission Conventions (defaults; the journal's instructions override)

1. Tables and figures cited in numerical order; references in the journal's style, Vancouver when none is chosen (`manuscript-conventions.md` §1.2, §2.1; `citation-styles.md`).
2. No em-dash or en-dash in sentences, table cells, figure captions or the abstract; ranges as `12 to 18`. Journal exceptions: `manuscript-conventions.md` §3.1.
3. Deliver what the author works in: revised text for pasted text; stay in an existing Word file. For a new manuscript, many revisions or several journals, offer the build kit (`docx-build.md`; journal profiles in `templates/build-kit/journals/`).
4. Within the text you were asked to change, apply these conventions; outside it, change nothing and list any violations you notice in the notes. A point edit on one paragraph never rewrites the rest of the manuscript.

## Core Workflow

1. Mode, and (conditional rule 1) design and guideline.
2. The clinical question (PICO/PECO) and the single take-home message.
3. Rewrite with the section guide, one message per paragraph (`paragraph-flow.md`).
4. Check each claim against its evidence (Integrity Rule 2) and the cross-section consistency checks (`paper-review.md`).
5. Submission preparation only: the adversarial review in `paper-review.md`, then the Stopping Rule.

## Stopping Rule

Writing fixes writing, not a design limitation or a missing analysis. Stop when every editorial problem is fixed in the text, and list the rest for the authors, separately from the manuscript, under the status each needs: `needs new data`, `needs new analysis`, `needs author decision`, `needs author information` (a fact only the authors have). Same four in `paper-review.md`. State an unfixable limitation in the Limitations paragraph and leave it.

## Output Contract

- **Point edit:** revised text and at most a few lines of notes, only those the author must know (a weakened claim, an unverifiable citation, a conflicting number). No outline, labels or checklist.
- **Section revision:** the revised section and its open issues. Add, only when they earn their place: an outline (3 to 7 bullets mapped to the guideline items) when the structure changed or the section is long; paragraph role labels when asked or when structure was the problem; a claim-evidence map (`Claim | Type: prior knowledge / own finding / interpretation | Evidence | Status: supported / needs evidence / overstated`) when claims were added, changed or are doubtful. A light copy-edit of a section needs none of them.
- **Submission preparation:** the manuscript, and a separate audit: claim-evidence map of major claims, guideline mapping, remaining problems under the four Stopping Rule statuses.

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
| Formatting references in a given style | `citation-styles.md` → `citation-styles-detail.md` (non-Vancouver) |
| Figures, tables, forest plots | `figures-and-tables.md` → `statistical-figures.md` |
| Translating an abstract or manuscript | `non-native-authors.md` §6 |
| Letter to the editor, conference abstract | Closest guides (`abstract.md`, `discussion.md`, `cover-letter.md`), flagged as partial coverage. Not a small manuscript: follow the journal's or congress's own limits and structure (a letter: a few hundred words, 350 to 500 in the journals profiled in the build kit, no IMRaD headings, few references, one published article or one point; a congress abstract follows the congress template and character limit) |
| Non-native English author | `non-native-authors.md` → `scientific-writing-principles.md` |
| Polishing a draft | `read-as-reader.md` → `paragraph-flow.md` → `scientific-writing-principles.md` → `common-mistakes.md` |
| Pre-submission final pass | `paper-review.md` → `reporting-standards.md` → `ethics-and-integrity.md` |
| Reviewer comments; revision | `responding-to-reviewers.md`; with the kit, `docx-build.md` (Revision round) |
| Source files and generated .docx; changing journal | `docx-build.md` → `templates/build-kit/README.md` → `templates/build-kit/journals/README.md` |
| Flow diagram (CONSORT, STROBE, PRISMA, STARD) | `diagrams.md` |
| Ready scaffold | `templates/` |

Out of scope: grant applications, posters and theses. Say so, and help only with the parts the guides cover.

**Files, one line each**

- Sections: `abstract.md`, `introduction.md`, `method.md`, `results.md`, `discussion.md`; background and prior evidence `related-work.md`; `title.md`.
- Article types: `case-report.md` (CARE), `systematic-review.md` (PRISMA 2020), `narrative-review.md`.
- Standards: `reporting-standards.md` (all guidelines, selector); `study-types.md` (designs, PICO, causal language); `statistical-reporting.md` (estimates, CIs, missing data, noninferiority); `ethics-and-integrity.md` (what applies to which design).
- Literature and references: `pubmed-essentials.md`; `research-apis.md` (Crossref, OpenAlex, E-utilities); `citation-styles.md` (Vancouver) and `citation-styles-detail.md` (AMA, APA, Harvard, Chicago, CSE).
- Presentation: `manuscript-conventions.md` (citation and figure order, dashes, file format); `figures-and-tables.md`; `diagrams.md` (flows, timelines, schemas, DAG); `statistical-figures.md` (forest, KM, funnel, ROC, calibration); `docx-build.md` (build kit, revision rounds, file names).
- Process and quality: `writing-process.md`; `paragraph-flow.md` (flow, clarity check, reverse outline); `scientific-writing-principles.md`; `non-native-authors.md`; `read-as-reader.md`; `common-mistakes.md` (five-minute audit); `paper-review.md` (the full pre-submission checklist); `responding-to-reviewers.md`; `cover-letter.md`; `journal-selection.md`; `glossary.md`.
- Examples: `examples/index.md` (all sections; fictional).
- Scaffolds: `templates/` (RCT, observational, case report, systematic review) and `templates/build-kit/`.
