# Building the .docx Procedurally

A hand-edited .docx is a poor medium for an agent: there is no diff, every edit risks breaking citation fields, and reference numbers drift when paragraphs move. The skill's default is the opposite: the manuscript lives as plain-text source files under git, and the .docx is **generated** for each journal. The ready-to-copy scaffold is `templates/build-kit/` (its `README.md` has the commands).

## Architecture: four layers that never mix

| Layer | Holds | Files |
| --- | --- | --- |
| Content | Text, authors, references, figures, tables, with stable ids | `manuscript/*.md`, `metadata.yaml`, `references.json`, `figures/` |
| Journal profile | Structure, limits, headings, citation style, file requirements, with source and date | `journals/<journal>.json` |
| Exporter | Content + profile → submission files | `scripts/build.py`, `filters/*.lua`, pandoc, citeproc, CSL |
| Validator | Content + profile → ERROR / WARN / HUMAN report | `scripts/validate.py`, `scripts/refs.py verify` |

Consequences:

1. **Reference sequence is solved by construction.** The text cites keys (`[@vonelm2007strengthening]`); citeproc numbers them by first citation at every build. Moving a paragraph cannot leave the list out of order, and figures and tables are renumbered by first mention the same way.
2. **Changing journal is a rebuild.** `references.json` stores complete CSL-JSON; the journal's CSL file decides whether it prints as Vancouver, AMA, or the journal's own variant. Headings (`Results` or `Findings`), table placement, blinding and the title page come from the profile.
3. **Journal rules become checks.** Limits, required sections, declarations, reference caps and ORCIDs are verified before the file is written. `validate.py --compare` shows, for every profile at once, what each candidate journal would require.

## Agent workflow

### Starting from nothing

1. Copy the kit into the project folder (`cp -R templates/build-kit <project>`), `git init`, and replace the fictional example: `metadata.yaml`, the section files, `figures/`.
2. Set `study-design` in `metadata.yaml`; it selects the reporting guideline the report lists for human review.
3. Draft section by section with the other guides of this skill. Cite only keys that exist.
4. For every new reference: find it (PubMed, Crossref, `references/pubmed-essentials.md`), then `python3 scripts/refs.py add <DOI or PMID:n>`. **Never write a CSL record by hand.** If no DOI or PMID can be found, leave `[CITATION NEEDED]` in the text; the validator will not let it through.

### Converting an existing .docx draft (once)

1. `pandoc draft.docx -t markdown -o manuscript/10-body.md --extract-media=figures`, then split it into section files and add the semantic header ids (`{#methods}`, `{#abstract-results}`, declaration ids).
2. The numbered citations become static text such as `(12)` or superscripts. For each, find the entry in the old reference list, add it with `refs.py add` by DOI or PMID, and replace the number with its key. Keep a table of old number → key while doing it and report entries you could not resolve instead of guessing.
3. Rebuild tables as pipe tables inside `::: {#tbl:id}` divs and figures as `::: {#fig:id}` divs; replace "Table 2" in the text with `@tbl:id`.
4. Run `refs.py verify` and `validate.py`; fix every ERROR before the first build.

### Every revision

1. Edit the Markdown. Commit with a message saying what changed and why; separate editorial changes from scientific ones (analysis, exclusions, interpretation).
2. `python3 scripts/validate.py --journal <target>` after each substantive edit.
3. `python3 scripts/build.py --journal <target>` to produce the files for the authors.

### Changing journal

1. Create `journals/<new>.json` from the journal's current instructions (`templates/build-kit/journals/README.md`): record `source_url` and `verified_at`; never fill a limit from memory.
2. `validate.py --journal <new>`. Presentation differences are handled by the build. **Content differences are not:** a 267-word abstract for a 250-word limit, an unstructured abstract turned structured, a shorter Discussion. Propose those as a normal, reviewable edit; the exporter never cuts text.
3. Build, open the .docx, and compare it with the instructions once by eye.

## What the validator does and does not decide

| Level | Examples | Who decides |
| --- | --- | --- |
| ERROR | Over a word limit (with what was counted); missing abstract part, section or declaration; citation key not in the library; duplicate or retracted reference; figure cited but not defined; placeholder left in text; missing ORCID | Objective. The build stops unless `--force` (draft). |
| WARN | Unverified reference; abbreviation used before definition; number in the abstract absent from the text; dash style; profile not verified or out of date | Probably wrong; confirm. |
| HUMAN | Reporting-checklist mapping; claim–evidence fit; whether each citation supports its sentence | Authors. Listed in every report so nobody forgets. |

`refs.py verify` proves that a reference **exists and matches its metadata** (Crossref and PubMed title, year, first author) and flags retractions and corrections. It does not prove that the paper supports the sentence it is attached to. That check is reading the cited abstract or full text against the claim, and it stays a HUMAN item (or an agent task whose output is a list for the authors, never a silent approval).

## Co-authors in Word

The source of truth is the Markdown. Send the generated .docx; co-authors comment or track changes; apply the accepted changes to the Markdown and rebuild. Do not convert an edited .docx back to Markdown after the initial conversion, because citations come back as static text. When co-authors must insert references themselves, have them name the reference in a comment (DOI or PMID) instead of inserting a citation.

Tag each submission in git (`submission-1-<journal>`, `revision-1`). Each build writes `outputs/<journal>/build-info.json` with the profile and its verification date, the CSL, the pandoc version and the commit, so any submitted file can be traced to its exact source. For the tracked-changes version required with a revision, compare the two tagged builds with Word's *Compare Documents*.

## Limits of the kit

1. Numbers in the text are still typed. If the analysis is scripted, export its results (CSV/JSON) and have the tables built from them; Quarto with inline R or Python is the next step when the whole paper should update from the data.
2. The abbreviation and abstract-number checks are heuristics (WARN, never ERROR).
3. Journal templates with unusual layouts (two-column, custom title pages) need the journal's own `reference.docx` (`"reference_docx": {"file": ...}`), and some submission-system fields (Key Points, highlights) are prepared outside the .docx; list them in the profile's `human_checks`.
4. The ICMJE and most journals require disclosure of AI assistance and do not accept AI as an author. Keep the `{#ai-use}` declaration accurate; git history shows which changes came from which pass.
