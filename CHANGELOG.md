# Changelog

All notable changes to the **Medical Manuscript Writing** skill are documented here. Format follows Keep a Changelog (https://keepachangelog.com/) using semantic-style versioning by content scope rather than strict semver.

## [1.6.0] — 2026

### Added

- `references/diagrams.md`: STROBE Flow Diagram Generator at `enciclopedia.med.br/strobe` integrated as Option 1 (preferred) for observational-study flow diagrams — cohort, case-control, and cross-sectional templates; exposure-group columns; joined final box; arithmetic consistency check for item 13a; documented JSON format for "Load JSON" with a worked cohort example; workflow and citation block. Mermaid template kept as Option 2 fallback.

- `templates/build-kit/` — procedural manuscript build: Markdown sections + CSL-JSON references + per-journal JSON profiles → pandoc → `.docx`. Includes `refs.py` (add by DOI/PMID from Crossref/PubMed; verify title/year/first author; retractions and corrections via Crossref `updated-by` and PubMed), `validate.py` (ERROR / WARN / HUMAN report: limits with explicit counting scope, required sections, structured-abstract parts, declarations, citation keys, duplicate DOIs, figure/table cross-references, placeholders, ORCID, abbreviations, abstract numbers, dash and P-value style; `--compare` across all profiles), `build.py` (CSL resolution including dependent styles, generated reference.docx with double spacing, line numbers, page numbers, margins; separate title page; blinded manuscript; tables at end; figure legends at end with numbered figure files; `build-info.json` for traceability), Lua filters for first-mention figure/table numbering and journal presentation, a generic ICMJE profile, an illustrative second profile, and a fictional cohort example that builds cleanly.
- `references/docx-build.md` — architecture, agent workflow (new manuscript, converting an existing `.docx`, revisions, changing journal), what the validator does and does not decide, co-author round trip, and limits.
- `references/reporting-standards.md`: CONSORT 2025 (30 items, by manuscript section, with changes from 2010 and transition note) replaces CONSORT 2010; SPIRIT 2025 (34 items) replaces SPIRIT 2013. Citations verified against Crossref.
- `references/examples/introduction/`: gap-type example bank (evidence absent, conflicting, other population, low certainty, new condition/test/technology, existing tools inadequate, practice variation) and closing patterns (aim/hypothesis/design), replacing files inherited from a computer-science paper-writing structure.
- `dist/build-zips.sh` — builds the three distribution zips; plugin version read from this changelog.

### Changed

- `templates/observational-study.md`, `references/reporting-standards.md`, `SKILL.md`, and `README.md` now point to the STROBE web tool for Figure 1.
- `templates/rct-manuscript.md` remapped to CONSORT 2025 numbering, with the new items (patient and public involvement, harms, protocol/SAP access, data sharing, intervention delivery). `references/diagrams.md` CONSORT section notes the 2025 box labels ("for primary outcome") and cites CONSORT 2025.
- `references/introduction.md`, `references/abstract.md` and the abstract templates rewritten around clinical logic (known → gap → design → aim; effect size with CI; conclusion proportional to design). "Our innovation / contribution / pipeline" framing removed. `references/examples/method/module-motivation-patterns.md` renamed `rationale-patterns.md`, with a corrected Cox/competing-risk example.
- `SKILL.md` hard rule 4 gains an explicit exception: the target journal's dash style wins (en-dash ranges when the journal uses them, never with negative bounds, never mixed). Detail in `references/manuscript-conventions.md` §3.1.
- `SKILL.md` hard rule 5: the `.docx` is generated from source, never hand-edited; references added only by DOI/PMID. `references/manuscript-conventions.md` §4.1 points to the build kit; numbered headings only when the journal asks.

## [1.5.0] — 2026

### Added

- `references/citation-styles-detail.md` — full per-style detail for AMA, APA 7, Harvard, Chicago / Turabian 18 (Author-Date and Notes-Bibliography variants), and CSE. Split out of `references/citation-styles.md` to keep the core file focused on Vancouver (the default).
- `references/diagrams.md`: CARE Patient Timeline tool at `enciclopedia.med.br/care-timeline` integrated as Option 1 (preferred) for case-report timelines, with three modes (section / hybrid / date), phase-coded color bands, three worked JS examples, anonymization rule, and citation block. Mermaid templates remain as Option 2 fallback.
- `references/paragraph-flow.md` expanded from a 47-line PDF extract to a full reference covering paragraph-, section-, and manuscript-scale flow, reverse-outlining workflow, cross-section consistency, transitions by function, three-persona self-reading, and a symptom → root cause → fix table.
- Variable-to-color consistency rule added to `references/figures-and-tables.md`: a variable assigned a color in Figure 1 must keep that color across Figures 2, 3, 4, etc., with R `scale_color_manual` and Python `GROUP_COLORS` worked examples.
- "See Also" sections with path-style references added to all four templates (`templates/rct-manuscript.md`, `observational-study.md`, `case-report.md`, `systematic-review.md`) so each template explicitly points at the relevant reference files.

### Changed

- `references/citation-styles.md` trimmed of duplicated Book/Chapter blocks and of the AMA / APA / Harvard / Chicago / CSE sections (now in `citation-styles-detail.md`). Legacy anchor IDs preserved for any existing cross-references.
- `SKILL.md` Section Guide D now lists `citation-styles.md` and `citation-styles-detail.md` as two entries.
- `templates/case-report.md` and `references/case-report.md` updated to recommend the CARE Timeline web tool as preferred for Item 7 timelines.

## [1.4.0] — 2026

### Added

- `templates/` folder with four ready-to-fill manuscript scaffolds: `rct-manuscript.md`, `observational-study.md`, `case-report.md`, `systematic-review.md`. Each is aligned to the matching reporting standard (CONSORT / STROBE / CARE / PRISMA 2020).
- `references/glossary.md` — alphabetical glossary of ~60 statistical, methodological, and reporting terms.
- `references/common-mistakes.md` — single-page consolidated cheatsheet of desk-rejection patterns and their fixes.
- `LICENSE` (CC BY 4.0).
- `CHANGELOG.md` (this file).

### Changed

- `SKILL.md` Section Guides updated to reference the new files.
- `README.md` updated to list the templates and glossary.

## [1.3.0] — 2026

### Added

- `references/responding-to-reviewers.md` substantially expanded with the **70% rule**, **three adages** ("rise above the fray", "take the high ground", "play with a straight bat"), the **"sham response"** technique, three common-criticism countermoves (sample size, Discussion scope, Table 1 P-values), repeated-comments handling, editorial-instructions handling, and word-limit strategies. Sources: Efron 2025, Cushman 2023, Hidouri et al. 2024.
- `references/read-as-reader.md` — three reader personas (skeptical methodologist, busy clinician, non-specialist) for structured self-reading. Source: Greenhalgh "How to Read a Paper" series.
- `references/pubmed-essentials.md` — Boolean operators, MeSH, field tags, Clinical Queries, NLM journal abbreviation lookup, anti-fabrication discipline.
- `references/diagrams.md`: CONSORT 2010 generator at `enciclopedia.med.br/consort2010` integrated as Option 1 (preferred) for all five CONSORT trial designs.
- `README.md` with full bibliography organized in 18 thematic categories.

### Changed

- `references/reporting-standards.md` STROBE expanded to full 22-item checklist. STARD expanded to full 30-item checklist plus E&E concepts (single-gate vs. multiple-gate, three-phase test description, prespecified vs. exploratory thresholds, spectrum bias). CONSORT 25-item checklist organized by manuscript section (Falci & Marques 2015 framing). Adherence statement and checklist-completion templates added. Source: Cohen et al. 2016 STARD E&E paper.
- `references/case-report.md` updated with full CARE 2013 checklist as a 30-row table with item numbering 1–13 and sub-items 3a–3d, 5a–5d, 8a–8d, 9a–9c, 10a–10d, 11a–11d.
- `references/diagrams.md`: PRISMA 2020 generator at `enciclopedia.med.br/prisma2020` integrated as Option 1 for systematic reviews.

## [1.2.0] — 2026

### Added

- `references/citation-styles.md` Vancouver section substantially expanded based on the Curtin Vancouver / AMA 11 guide: superscript-numerals as the modern default, multiple-citation rules, page-number citation pattern, all reference-list formats (journal, book, chapter, supplement, eLocator, advanced online publication, organisation report, generative AI), worked examples with real medical citations.
- `references/scientific-writing-principles.md` — the Six Pillars (Clarity, Conciseness, Accuracy, Objectivity, Consistency, Logical Organization), wordy → concise table, hedging vocabulary, anthropomorphism rules, full tense table by section, abbreviation discipline, numbers-and-units rules, commonly confused words, sentence-level revision checklist.
- `references/narrative-review.md` — POEM vs. DOE, ABC level-of-evidence rating, six options for added value, search-strategy specifics including forward vs. backward snowballing, methodological cautions.
- `references/systematic-review.md` — PRISMA-aligned workflow with R package PRISMA2020, search across multiple databases, two-reviewer screening, risk-of-bias tools per design, GRADE certainty.

### Changed

- Table of Contents added to four large files: `citation-styles.md`, `figures-and-tables.md`, `diagrams.md`, `scientific-writing-principles.md`.

## [1.1.0] — 2026

### Added

- `references/figures-and-tables.md` — design principles, types, captions, file formats, accessibility, image-manipulation ethics.
- `references/diagrams.md` — Mermaid templates for CONSORT, STROBE, PRISMA, STARD flows, CARE timeline, trial schemas; pointers to PRISMA2020 R package and DAGitty; statistical-figure tooling.
- `references/manuscript-conventions.md` — em-dash rule, citation-order rule, tables-and-figures-cited-in-order, .docx default format, NLM abbreviation lookup pointer.
- `references/ethics-and-integrity.md` — IRB approval, consent, registration (ClinicalTrials.gov, PROSPERO), ICMJE authorship, conflicts of interest, data sharing, AI disclosure.
- `references/statistical-reporting.md` — effect sizes, CIs, p values, missing data, sensitivity analyses, software documentation.

### Changed

- `SKILL.md` reorganized Section Guides into five thematic groups (A. Section guides, B. Article types, C. Cross-cutting standards, D. Form/format/presentation, E. Writing quality and process).
- Quick Start by Scenario added (12 scenarios mapped to file-reading orders).
- Cross-references added between sibling files; isolated files reduced from 4 to 0.

## [1.0.0] — 2026

### Added

- Initial conversion of a generic ML/CV/NLP research-paper-writing skill into a medical-manuscript-writing skill.
- Eight section guides: `abstract.md`, `introduction.md`, `method.md`, `results.md`, `discussion.md`, `related-work.md`, `paper-review.md`, `paragraph-flow.md`.
- Four article-type guides: `case-report.md`, `systematic-review.md`, `narrative-review.md`, plus the original-article path.
- `references/reporting-standards.md` with the matrix of CONSORT, STROBE, PRISMA, STARD, CARE, TRIPOD, ARRIVE, SPIRIT, CHEERS, SQUIRE, SRQR.
- `references/study-types.md` with PICO/PECO/PIRD framing and evidence hierarchy.
- `references/writing-process.md` with drafting order, three-pass self-review, pre-peer-review tips.
- Worked examples for abstracts, introductions, and methods in `references/examples/`.
- Skill named `medical-manuscript-writing` with Alexandre Campos Moraes Amato as author.
