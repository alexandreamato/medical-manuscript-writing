# Manuscript Conventions (Medical Research)

These are the formatting and integrity conventions that catch most desk-rejections in medical journals. Apply them at the end of every revision pass.

## 1. Citations

### 1.1 Never invent a citation

1. Every reference is a real, verifiable publication. PubMed ID, DOI, or journal page is required.
2. Do not infer a likely author or year. If a fact lacks a known source, mark it `[CITATION NEEDED]` and stop.
3. Do not cite a review when the claim should be tied to the primary source.
4. Verify every citation in the final manuscript against PubMed or the journal record. Run a final pass before submission.

### 1.2 Order of citations

**Choose the citation style by checking the target journal's Instructions to Authors. If the journal has not yet been chosen, default to Vancouver (ICMJE).** For full guidance on Vancouver, AMA, APA, Harvard, Chicago, and reference-manager workflow, see `references/citation-styles.md`.

For Vancouver-style numeric citations (the dominant style for medical journals: NEJM, JAMA, Lancet, BMJ, Ann Intern Med, Nature Medicine, etc.):

1. References are numbered in order of first appearance in the text.
2. After every revision, scan the manuscript top to bottom and verify ascending order.
3. When you move a sentence, the citations move with it; renumber the reference list accordingly.
4. Tables and figures count for citation order: a citation that first appears in a table caption is numbered at the position of that table's first text mention.

For author-date styles (APA, Harvard, Chicago Author-Date, Cell, some specialty journals): list references alphabetically by first author surname, with multiple works by the same author chronologically.

### 1.3 Reference-list checks

1. Every in-text citation has a matching entry in the reference list.
2. Every reference-list entry has at least one in-text citation.
3. Author names, year, journal, volume, issue, pages, and DOI all match the journal record.
4. For preprints: include the version and DOI; mark `(preprint)`.
5. For online-only resources (registries, datasets): include the access URL and the date accessed.

## 2. Tables and Figures

### 2.1 Cite each one in the text in order of appearance

1. Tables and figures are numbered by the order of their first mention in the body text.
2. If you reorganize the manuscript, renumber tables and figures so that Table 1 is mentioned before Table 2, Figure 1 before Figure 2, and so on.
3. After every revision pass, run a top-to-bottom check.

### 2.2 Self-contained captions

1. Every table and figure stands alone. Caption explains the design, the variables, the units, the time horizon, and any abbreviations.
2. Place table captions above the table and figure captions below the figure (most journals: verify in the journal's instructions for authors).
3. Spell out abbreviations in the caption even if defined in the body text.

### 2.3 Forest plots and flow diagrams

1. The participant-flow diagram is required by CONSORT, PRISMA, and STARD, and recommended by STROBE (item 13c: "consider use of a flow diagram").
2. Forest plots in meta-analyses must report the model (fixed / random effects), the heterogeneity statistic, and the test for overall effect.

## 3. Punctuation and Style

### 3.1 No em-dash or en-dash inside body sentences

1. Replace `—` (em-dash) with a comma, semicolon, parenthesis, or full stop.
2. Replace `–` (en-dash) with `to` for ranges. Write `12 to 18 months`, not `12–18 months`.
3. Hyphens (`-`) are fine in compound terms (`placebo-controlled`, `well-tolerated`, `intention-to-treat`).
4. This rule applies to body sentences, table cells, figure captions, and the abstract. Numeric ranges in tables can use a hyphen if the journal style allows; check the instructions for authors.

Examples:

| Avoid | Prefer |
| --- | --- |
| `Patients with diabetes — including type 2 — were eligible.` | `Patients with diabetes, including type 2, were eligible.` |
| `The follow-up period was 12—18 months.` | `The follow-up period was 12 to 18 months.` |
| `The intervention reduced mortality — a finding consistent with prior trials.` | `The intervention reduced mortality, a finding consistent with prior trials.` |

#### Exception: the journal's own style wins

The rule is the house default, used when the journal has not said otherwise. It yields in three cases:

1. **The journal prints ranges with an en-dash.** Many do, especially for confidence intervals and ranges inside parentheses (`95% CI 0.55–0.94`, `IQR 12–18`). When the Instructions for Authors or recent articles of the target journal use the en-dash, follow them, and apply the same form everywhere in the manuscript, tables included. Two traps survive the exception: never write a range with a negative bound as `-0.4–0.2` (use `to`: `-0.4 to 0.2`), and never mix `12–18` and `12 to 18` in one manuscript.
2. **The journal's style sheet uses the em-dash** (some print it in titles, for example `Statins and venous ulcer—a cohort study`). Use it only where the style sheet does, never as a general punctuation habit in body sentences.
3. **Fixed names and quotations** keep their original punctuation: a guideline title, a scale, a quoted sentence, a reference title.

In the build kit, this is a per-journal switch: `"style": {"allow_en_dash_ranges": true, "allow_em_dash": false}` in the journal profile. The validator then stops warning about en-dash ranges for that journal only.

### 3.2 Numbers, units, and abbreviations

1. Spell out numbers under 10 except in measurements, statistics, ages, and doses.
2. Use SI units. Use a non-breaking space between number and unit (`5 mg`, `60 kg`, `12 weeks`).
3. Define every abbreviation at first use, then use the abbreviation. Avoid more than 6 to 8 abbreviations in the abstract.
4. Use one decimal place for percentages with denominators under 1000 (`42.3%`); two decimal places for hazard ratios and odds ratios; report 95% CIs to the same precision as the point estimate.
5. Report p values to 2 significant figures, except very small (`p < 0.001`) and borderline (`p = 0.054`).

### 3.3 Tense

1. Methods: past tense (`We enrolled ...`).
2. Results: past tense (`Mortality was lower in the intervention group ...`).
3. Discussion: present tense for established knowledge (`Aspirin reduces ...`); past tense for the present study's findings.

## 4. Manuscript File Format

### 4.1 Default format: Microsoft Word (.docx)

Most medical journals require Word `.docx` submission. When revising an author's existing Word file, keep working in it. For a new manuscript, or when the author asks, generate the .docx from source files instead of formatting it by hand: `references/docx-build.md` explains the workflow, and `templates/build-kit/` is a ready-to-copy scaffold that applies every setting below automatically. The settings, for when a journal gives no template:

1. **Page setup:** A4 or US Letter, 2.5 cm margins.
2. **Font:** Times New Roman 12 pt for body text, 10 pt for tables and captions. (Some journals accept Arial 11 pt: check.)
3. **Line spacing:** double-spaced throughout, including references and table captions.
4. **Line numbering:** continuous, starting at 1 on the first page of the body text.
5. **Page numbers:** bottom right.
6. **Headings:** numbered (1, 1.1, 1.2) only when the journal asks for it; most medical journals use unnumbered headings. Either way, use Word's heading styles (Heading 1, Heading 2) so the table of contents and journal style sheet can map them.
7. **Tables:** native Word tables (not images). One table per page or all tables at the end of the manuscript, depending on journal style.
8. **Figures:** placed at the end of the manuscript or submitted as separate files. Resolution: 300 dpi minimum for raster images; vector format (.eps, .pdf) preferred for line art.
9. **References:** cited by stable key and formatted by the journal's CSL style at build time (`references/docx-build.md`), or managed in Zotero, EndNote, or Mendeley with live fields. Never type reference numbers by hand.

### 4.2 Suggested file structure for a journal submission

1. `Manuscript.docx`: title page, abstract, body text, references, figure legends.
2. `Tables.docx` (if separate per journal style) or appended at end of `Manuscript.docx`.
3. `Figure1.tif`, `Figure2.tif`, ... (one figure per file).
4. `Supplementary.docx` or `Supplementary.pdf`: full search strategy, statistical analysis plan, additional tables and figures.
5. `CONSORT_Checklist.pdf` (or STROBE / PRISMA / STARD as applicable).
6. `Title_page.docx` (if the journal requires a separate title page with author information removed from the main file for blinded review).

### 4.3 Title page content

1. Full title (descriptive, not a question, no abbreviations).
2. Short running title (40 to 50 characters).
3. Author list with affiliations and ORCID IDs.
4. Corresponding author with full address, email, and phone.
5. Word counts: abstract, body text, references, tables, figures.
6. Funding statement.
7. Conflict-of-interest statement.
8. Trial / review registration number.
9. Data sharing statement.

## 5. Final Pre-Submission Pass

The full pre-submission checklist is `references/paper-review.md`. The conventions in this file add only the mechanical pass:

1. Reference format matches the journal's style (or Vancouver); journal abbreviations consistent.
2. Dash and range style consistent (§3.1).
3. File format and file names as the journal requires: `.docx` body, separate figure files at the required resolution.
4. Spell-check and grammar pass.
