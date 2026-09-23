# Manuscript Templates

Ready-to-fill scaffolds for the four most common medical-manuscript types. Each template contains the standard section structure, placeholder text indicating what each paragraph should contain, and inline references to the reporting-standard items being addressed.

| Template | Article type | Reporting standard | Typical body words |
| --- | --- | --- | --- |
| [`rct-manuscript.md`](rct-manuscript.md) | Randomized controlled trial (parallel) | CONSORT 2025 | 2,500 to 4,000 |
| [`observational-study.md`](observational-study.md) | Cohort / case-control / cross-sectional | STROBE | 2,500 to 4,000 |
| [`case-report.md`](case-report.md) | Case report or small case series | CARE 2013 (case series: PROCESS for surgical series, JBI checklist otherwise; `references/reporting-standards.md`) | 1,000 to 1,500 |
| [`systematic-review.md`](systematic-review.md) | Systematic review with or without meta-analysis | PRISMA 2020 | 4,000 to 6,000 |

For writing the manuscript as source files and generating the `.docx` per journal, use [`build-kit/`](build-kit/) (Markdown + CSL-JSON + journal profiles + pandoc). The four templates above are content scaffolds: their sections can be pasted into the kit's `manuscript/` files.

## How to use

1. Copy the template to your working folder and rename it with your manuscript's working title.
2. Replace placeholder text (everything in `[BRACKETS]`) with your content.
3. Inline comments (`<!-- CONSORT 5; see references/reporting-standards.md -->`) point to the matching reporting-standard item; consult that file when filling the section.
4. After filling, generate the `.docx` with the build kit (`build-kit/README.md`; workflow in `references/docx-build.md`) rather than formatting Word by hand. Formatting conventions: `references/manuscript-conventions.md`.

## What's included in each template

- Title page block (title, authors, affiliations, corresponding author, word counts, registration ID, conflicts, funding).
- Structured abstract aligned to the reporting standard.
- Section headings in the recommended order, with placeholder paragraphs.
- Reporting-checklist anchors as inline comments: locate them later when filling the supplementary checklist with page/line numbers.
- Adherence statement template.
- Cross-references to the relevant section guides in `references/`.

## What's NOT included

- The actual content (you write that).
- Tables and figures (build separately; insert at the end of the document or as separate files).
- Reference list (in the build kit, added by DOI/PMID with `scripts/refs.py` and formatted by the journal's CSL style; otherwise Zotero, EndNote, or Mendeley, see `references/citation-styles.md`).
- Reporting-standard PDF checklist (download from EQUATOR Network and complete with page/line numbers).
