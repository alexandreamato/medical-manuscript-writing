# Journal profiles

A profile is the machine-readable version of one journal's *Instructions for Authors*. The manuscript never contains journal rules; the profile says how to present it and what to check. Changing journal after a rejection is choosing another profile, rebuilding, and fixing what the validator reports.

Run `python3 scripts/validate.py --compare` to see, before writing a single word more, how much work each candidate journal would need.

## Creating a profile for a real journal

1. Open the journal's current instructions for the article type (original research, case report, review…). Rules differ between article types of the same journal.
2. Copy `generic-icmje.json` to `<journal-id>.json`, or create a small file with `"extends": "generic-icmje"` and only the fields that differ.
3. Fill every field **from the instructions, not from memory**. When a rule is not stated, leave the generic default and note it in a `_comment`.
4. Record `source_url` (the page read) and `verified_at` (today, `YYYY-MM-DD`). The validator warns when a profile has no date or is older than `reverify_after_days` (default 180): instructions change and a stale profile is a guess.
5. Say what each limit counts. "3,000 words" is not a rule until you know whether it includes the abstract, references, legends and tables (`count_sections`, `include_floats`, `unit`).
6. Put anything the code cannot check (a Key Points box, a cover-letter statement, a graphical abstract) in `human_checks`.
7. Run `validate.py --journal <journal-id>` and `build.py --journal <journal-id>`, open the .docx and compare it with the instructions once by eye.

`jvb.json` (Jornal Vascular Brasileiro) is a complete real profile and the model to copy: every rule carries a `_comment` quoting where it was read, and rules the journal does not state are marked as such. Never submit against `generic-icmje` or `example-journal-b`: the first is a set of drafting defaults, the second is illustrative.

## Fields

Keys starting with `_` are comments, at any depth (also inside `headings` or `section_limits`). `null` means "no rule". `human_checks` and `revision_checks` accumulate across `extends` and article types; every other field is replaced.

| Field | Meaning |
| --- | --- |
| `extends` | Parent profile; this file only overrides what differs. |
| `name`, `source_url`, `verified_at`, `reverify_after_days` | Provenance. |
| `generic`, `illustrative` | Flags for non-journal profiles (the validator warns). |
| `csl` | CSL style name from https://www.zotero.org/styles (downloaded on first use; dependent styles resolved), or a path to a local `.csl`. |
| `reference_docx` | `{font, size_pt, line_spacing, line_numbers, margins_cm, page_numbers, subheadings: "bold" \| "italic"}` to generate the Word styles, or `{file: "templates/x.docx"}` to use the journal's own template. |
| `title` | `{max_chars, running_title_max_chars, running_title_allowed}` (characters with spaces). `running_title_allowed: false` leaves the running title out of the files (MDPI). |
| `keywords` | `{min, max, after_abstract, labels}`. `after_abstract: true` prints the keywords after each abstract (in each language) instead of on the title page. |
| `authors` | `{require_orcid: "all" \| "corresponding" \| false, max, max_without_justification, max_soft, soft_note}`. `max_without_justification` is a WARN that blocks submission until justified; `max_soft` is a commercial or guidance threshold, a WARN that never blocks. |
| `abstract` | `{required, bilingual, title, limit: {unit, max}, structure: [{id, heading, required}]}`. `bilingual: true` requires `{#abstract-alt}`, `title-alt`, `keywords-alt` and `lang-alt`. A `heading` (and `title`) may be a string or per language: `{"en": "Background", "pt": "Contexto"}`. `required: false` makes a part optional. `id` matches the manuscript header `{#abstract-<id>}`; `heading` is what this journal calls it. Empty `structure` = unstructured abstract (subheadings dropped on export). |
| `main_text.sections` | `[{id, heading, required}]`: required sections and this journal's heading for each. `main_text.required_any: [["discussion", "conclusions"]]` requires at least one section of each group. |
| `main_text.limit` | `{unit, max, min, soft, count_sections, include_floats}`. `soft: true` when the journal gives the number as guidance only: exceeding it is a WARN, not an ERROR (also valid in `abstract.limit` and `section_limits`). `unit`: `words`, `characters_with_spaces`, `characters_without_spaces`. |
| `section_limits` | `{<section id>: {unit, max, min}}`, e.g. a Discussion cap. `unit: "items"` counts list items (e.g. a key-points box of up to three bullets); works for level-1 and level-2 sections. |
| `references` | `{max, soft, soft_note, require_identifier}` (identifier = DOI or PMID). `soft: true` for a threshold that is not an editorial limit (e.g. a fee above it): a WARN under `limits`, never blocking. |
| `figures`, `tables` | `{max, placement}`. Tables: `inline` or `end` (after references). Figures: `inline` or `legends-at-end` (images shipped as separate numbered files). |
| `figures_tables_max` | Combined cap, when the journal counts them together. |
| `conditional_declarations` | `{<section id>: ["humans", "animals"]}`: required only when `involves` in `metadata.yaml` includes one of them (e.g. `informed-consent` for humans only; nothing for a review with `involves: []`). |
| `required_declarations` | Section ids that must exist: `ethics`, `funding`, `conflicts`, `data-availability`, `author-contributions`, `ai-use`, `trial-registration`, … |
| `submission` | `{separate_title_page, blinded, number_sections, omit_in_blinded: [section ids], title_page_sections: [section ids]}`. `title_page_sections` are printed on the title page and left out of the text, whether the title page is a separate file or the first page of the manuscript (J Vasc Bras: ethics, conflicts, funding, data availability, contributions). `title_page_copies` are printed on the title page and also kept in the text (IJO: competing interests). |
| `style` | `{allow_em_dash, allow_en_dash_ranges, p_value: "P" \| "p" \| null, no_abbreviations_in_title_abstract: true \| "title" \| "abstract", banned_terms: [{term, use, regex}]}`. `banned_terms` warns in drafts and blocks `--submission` unless the sign-off gives a reason (e.g. a quoted title). |
| `revision` | How revised manuscripts are marked: `{marking: "color" \| "highlight" \| "tracked" \| "none", color: "FF0000", deleted: "strike" \| "omit", author}`. File names follow the kit's rule (README, "File names"). |
| `revision_checks` | Free-text items listed in every revision's `_letter-check.txt` (deadlines, submission route). |
| `headings` | Extra `{section id: heading}` renames. |
| `reporting_guideline` | Guideline the journal expects for this article type (checked against `study-design`). |
| `human_checks` | Free-text items listed for human review in every report. |
| `article_types` | `{<article-type>: {…overrides…}}`, selected by `article-type` in `metadata.yaml` or `--article-type`. `"case-report": null` removes a type inherited from the parent profile. |
