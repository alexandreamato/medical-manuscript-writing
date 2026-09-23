# Changelog

All notable changes to the **Medical Manuscript Writing** skill are documented here. Format follows Keep a Changelog (https://keepachangelog.com/) using semantic-style versioning by content scope rather than strict semver.

## [1.9.1] — 2026-09-23

Responds to an external review of 1.9.0.

### Fixed

- **Cureus thresholds are commercial, not editorial.** Its author and reference counts only decide whether the paid Preferred Editing service becomes mandatory; the profile had them as a blocking reference limit and as an authorship justification that `--submission` refused. New `references.soft` and `authors.max_soft` (with `soft_note`) report them as WARN under `limits`, which never blocks.
- **Bilingual abstracts compare the confidence level.** Same estimate and limits with 95% in one abstract and 90% in the other is now reported.
- **CSL download errors say what happened**: HTTP 404 (the style does not exist) versus no network.

### Changed

- **Every bundled profile's CSL style is stored in `templates/build-kit/csl/`** (11 files, including the parents of dependent styles). The kit builds and the whole test suite runs offline, and reference formatting cannot change because an upstream style was edited.
- 3 new tests (48 in total).

## [1.9.0] — 2026-09-23

### Added

- **Six journal profiles**, each rule annotated with its source (read 2026-09-23): `obesity` (Obesity, Silver Spring), `obesity-facts` (Karger), `clinical-obesity` (Wiley), `ijo` (International Journal of Obesity), `jcm` (Journal of Clinical Medicine, MDPI), `cureus`. Summary table in the kit README.
- Profile features the new journals needed:
  - `section_limits` with `unit: "items"` (bullet boxes such as Study Importance or Key Points), `min`, and level-2 sections;
  - `soft: true` limits for journals whose word counts are guidance only (WARN, not ERROR);
  - `main_text.required_any` ("Discussion and/or Conclusion");
  - `style.banned_terms` (person-first language: "obese patients", "morbid obesity"), which blocks submission unless resolved with a reason;
  - `title_page_sections` also for a title page inside the manuscript, and `title_page_copies` for statements required on the title page and in the text;
  - `conditional_declarations` driven by `involves:` in `metadata.yaml` (IRB and consent only when humans or animals are studied);
  - `title.running_title_allowed: false`;
  - `no_abbreviations_in_title_abstract: "title"` or `"abstract"`;
  - `"<type>": null` removes an inherited article type.
- `human_checks` and `revision_checks` now accumulate across `extends` and article types. `_comment` keys are ignored at any depth.

### Fixed

- **Bibliography of omitted sections.** Since 1.8.1, citeproc ran before sections were removed, so a reference cited only in an omitted section (e.g. acknowledgments in a blinded file) stayed in the list and shifted the numbering. The journal layer now selects the content first; citeproc numbers what remains; a new last filter, `scrub.lua`, strips the metadata.
- **Confidence levels and spreads.** 90%, 95% and 99% CIs are recognised and reported with their level (a level mismatch between abstract and Results is flagged); an unlabelled "median 12 (8 to 18)" or IQR is a spread, not an estimate.
- **Resolving a divergence needs a location.** In the sign-off, the reason must say where the checked value is (section, paragraph, table, figure, page); "checked, it is fine" is refused.
- The second-language abstract is left out of files for journals that are not bilingual.

### Changed

- 12 new tests (45 in total), including a build of every profile.

## [1.8.1] — 2026-09-23

Responds to an external review of 1.8.0: no check may pass silently.

### Fixed

- **Blinded files leaked the author's identity.** pandoc wrote every metadata field into `docProps/custom.xml`, including the absolute path of the CSL file (`/Users/<name>/...`). The journal filter now runs after citeproc and strips all metadata except the language.
- **Sign-off tied to one version.** `signoff/<journal>.md` records a fingerprint of the manuscript, metadata, references and figures; any change clears every tick and names the changed files.
- **Estimate/CI divergence blocks submission.** In `--submission` it is an error unless fixed or resolved in the sign-off with a reason (`| because: ...`).
- **Intervals are extracted, then validated.** Integer estimates (`HR 2, 95% CI 1 to 3`) are recognised; inverted limits and estimates outside their interval are reported as suspicious instead of being dropped. Values are compared numerically (`0.720` = `0,72`).
- **Comparison sources.** Abstract estimates are matched only against the Results and tables, not the Introduction or Discussion.
- **Anonymity scan covers the whole file** (body, headers, footers, footnotes, endnotes, comments, document properties) and flags local file paths.
- **Rendering outcomes are checked.** LibreOffice, pdftoppm and ImageMagick results are reported per file: a missing tool is a WARN, a failure an ERROR. ImageMagick's label-font failure fixed by passing a font.

### Changed

- `SKILL.md` Output Contract: for a section revision, the outline, role labels and claim–evidence map are included only when they earn their place.
- `references/docx-build.md`: when to use the revision round and when Word's *Compare Documents*.
- 11 regression tests (33 in total).

## [1.8.0] — 2026-09-23

Responds to two external reviews of 1.6.1 and 1.7.0.

### Added

- `references/title.md` (titles, running titles, keywords, bilingual titles), `references/cover-letter.md` (initial submission), `references/non-native-authors.md` (Portuguese-to-English interference, strategies, AI-editing disclosure), `references/journal-selection.md` (fit, indexing, fees, predatory journals, preprints and ICMJE policy).
- Results and Discussion example banks (`references/examples/results/`, `references/examples/discussion/`, 7 files each, one fictional trial).
- `references/statistical-figures.md`, split from `diagrams.md` (forest, Kaplan-Meier, funnel, ROC, calibration).
- Reporting standards: PRISMA-S, PRISMA-DTA, SWiM, GRRAS, SAMPL, SAGER, TRIPOD-LLM, and the CONSORT noninferiority/equivalence extension; noninferiority section in `statistical-reporting.md` (margin, CI vs margin, assay sensitivity, ITT and per-protocol).
- Build kit: **draft vs submission mode** (`--submission`): example content (`example: true`), unverified or doubtful references, generic or unverified profiles and every human-review item not ticked and signed in `signoff/<journal>.md` become errors; `--force` refused. **`preview.py`** renders each file to PDF and a contact sheet of all pages (LibreOffice, poppler) and checks the product: author identity left in a blinded manuscript, marked revision without marks, line numbers, figure files vs legends. **Estimate/CI consistency**: the same (estimate, lower, upper) must appear in the abstract and the Results or tables, and in both abstracts (decimal comma and Portuguese wording recognised). 4 new tests (22).

### Changed

- `SKILL.md` slimmed from 21 KB to 9 KB: mode selection, Integrity Rules (obligatory), Conditional Rules, Submission Conventions (defaults), minimal workflow, Stopping Rule, Output Contract and one map. Activation description shortened. Answer in the format asked for; Word only when delivering a manuscript file. Frontmatter: `license` added, `author` moved to `metadata` (the official skill validator rejected it).
- CONSORT described as a minimum set of items (not "an upper bound"), with justification for non-applicable items. TRIPOD+AI is the default for all prediction models; TRIPOD 2015 kept as history.
- References: "not verified", "inconsistent", "retracted or corrected" and "apparent fabrication" are distinct categories with proportional actions; only the last raises a misconduct concern (`paper-review.md`, `common-mistakes.md`, `citation-styles.md`).
- `ethics-and-integrity.md` separates universal items from those conditional on design or journal.
- One canonical place per rule: `paper-review.md` is the single full pre-submission checklist with the cross-section consistency checks; `common-mistakes.md` points to it; section guides keep only section-specific items. Four method example files that repeated `method.md` removed.
- The skill's own prose follows its dash rule: 641 em-dashes reduced to 11 (those discussing the character itself); number ranges written with "to". Headings and anchors updated.
- Build kit: footer paragraph excluded from line numbering (it showed a second page number in some renderers).

## [1.7.1] — 2026-09-23

### Added

- **File-name rule** for everything sent to a journal: `<short-name>_<journal>[_rev<N>]_<part>.<ext>` (e.g. `statins-ulcer_jvb_rev1_manuscript-marked.docx`). `short-name` is set once in `metadata.yaml`; the validator rejects a malformed one and flags an author's name in it (an ERROR for blinded journals, since every file carries it). Internal reports are prefixed with `_` (`_validation-report.txt`, `_build-info.json`, `_letter-check.txt`). Documented in the kit README ("File names") and `references/docx-build.md`.

### Changed

- Figures are written next to the manuscript with the same naming rule (`…_figure-1.png`) instead of `figures/Figure1.png`. Revision file names no longer come from the profile (`clean_name`, `marked_name`, `letter_name` removed).
- `test_revision.py` uses a throwaway git identity, so it passes on machines without a global git user.


### Added

- **Revision rounds in the build kit** (`templates/build-kit/scripts/revision.py`, `revdiff.py`). `start`/`import` compare the .docx the journal returns with what was submitted (a rebuild of the submission tag, or the exact uploaded file) and list tracked changes, comments, and edits made without tracking; `reconcile` shows journal edits still missing from the source; `base` tags the reconciled base; `check` verifies the response letter (every comment answered, every `Changed:` section really changed, every changed section explained); `build.py --revision N` writes the clean manuscript, the marked manuscript in the journal's style (red text, highlight, or real Word tracked changes, compared on the pandoc AST so both files have identical reference and figure numbers), and the response letter from `revision/round-N/responses.md`. 7 new tests, including a full round trip in a temporary git repository.
- **Jornal Vascular Brasileiro profile** (`journals/jvb.json`), the kit's default: all article types, limits, bilingual title/abstract/keywords, declarations on the title page, double-blind files, tables after references, legends at the end, superscript Vancouver, revision marked in red, and human checks (Parecer Consubstanciado, CONEP 166/2018, ReBEC, EQUATOR checklist with pages). Every rule annotated with the page it was read on (2026-09-23). `csl/jornal-vascular-brasileiro.csl`: NLM superscript with first three authors + et al. above six, as the journal requires.
- Kit support for **two languages** (`title-alt`, `keywords-alt`, `lang-alt`, `{#abstract-alt}`; headings per language; keywords printed after each abstract), **title-page sections** (declarations moved to the title page and out of the blinded file), **no abbreviations in title/abstract**, **author limit with justification**, **italic subheadings** and bold headings in the generated Word styles, optional parts in structured abstracts, and localized title-page labels (pt, en, es).
- `references/responding-to-reviewers.md` and `references/docx-build.md`: how to handle a journal-edited file and mark changes as the journal asks.

### Fixed

- `references/responding-to-reviewers.md`: removed the claim that a significant result proves the sample was large enough and the advice to run post-hoc power analysis (observed power is a function of the P value; Hoenig and Heisey, Am Stat 2001). Replaced with prespecified sample size, CI width, clinical plausibility, and effect inflation in small studies.
- Factual corrections: SPIRIT participant timeline (item 13 in 2013, 18 in 2025); Naranjo scoring (-4 to +13; three items score +2); updated RUCAM range and RECAM; National Guideline Clearinghouse (closed) and BMJ Clinical Evidence (discontinued) replaced; STROBE flow diagram recommended, not mandatory; en-dash example and range rule aligned with §3.1; EU trials via CTIS, ReBEC listed once, Declaration of Helsinki 2024; broken `experiments.md` link; "ICMJE Uniform Requirements" renamed Recommendations; unsourced search-yield numbers in `systematic-review.md` removed or sourced; glossary count.
- Build kit: an omitted level-1 section reappeared from its first non-omitted subsection; pandoc's internal citation counters made unchanged paragraphs look changed after a citation was removed.
- Packaging: `dist/publish-to-github.sh` reads the version and uses the current branch; `dist/sync-to-installed.sh` excludes `.claude/`, `__pycache__/` and kit build output; README states that zips are built, not versioned; `agents/openai.yaml` documented.

## [1.6.1] — 2026-09-23

Responds to an external review of 1.6.0.

### Changed

- `SKILL.md`: new "Match the Work to the Request" section with three modes (point edit, section revision, submission preparation); the Output Contract scales to the mode, so a paragraph edit returns the paragraph and only the necessary notes.
- `SKILL.md`: "Hard Rules" split into **Integrity Rules** (never violate: no fabricated references, data or results; claims supported by the evidence their type requires; fidelity to data and protocol) and **Submission Conventions** (defaults the journal overrides: figure/table order, reference style, dashes, .docx delivery).
- Claim–evidence rule rewritten by claim type (`SKILL.md` Integrity Rule 2, `references/paper-review.md` rule 1): prior knowledge needs a citation, the study's own findings need the Results, interpretation needs both. The old wording ("supported by the Results", including the Introduction) could lead to deleting well-sourced background. The claim–evidence map gains a `Type` field.
- The build kit is a working mode, not a requirement: revising an existing Word file stays in that file (`SKILL.md` Submission Convention 4, `references/docx-build.md` "When to use it", `references/manuscript-conventions.md` §4.1).
- New **Stopping Rule** (`SKILL.md`, `references/paper-review.md`): stop when editorial problems are fixed; deliver the rest separately, grouped by what it needs (new data, new analysis, author decision, author information). The audit is never appended to the text meant for the journal.

### Fixed

- `refs.py verify`: a PMID-only reference is now checked for year and first author against PubMed, not only the title (a wrong year and author used to pass as `ok`). An unreachable source gives `incomplete` and exit code 3 instead of being skipped with exit 0. Verifications expire after 90 days (`--max-age`) and are re-run, because retractions come after publication. New `check` status for a one-year gap or a missing field.
- `validate.py` reports the new statuses (ERROR for mismatch/not found/retracted; WARN for incomplete, check, expired).

### Added

- `refs.py add-manual` and `refs.py confirm` for real sources without DOI or PMID (guidelines, software documentation, books, reports): official URL or ISBN, metadata from the source, who checked and what was compared; stored as `manual`, expiring like automatic checks. `[CITATION NEEDED]` is kept for statements with no source at all.
- `templates/build-kit/scripts/tests/test_refs.py`: 11 tests with simulated Crossref/PubMed answers (wrong year/author with PMID only, network failure, one source unreachable, retraction, one-year gap, expiry, manual references, validator levels).

## [1.6.0] — 2026-09-23

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
