# Building the .docx Procedurally

A hand-edited .docx is a poor medium for an agent: there is no diff, every edit risks breaking citation fields, and reference numbers drift when paragraphs move. The alternative is to keep the manuscript as plain-text source files under git and **generate** the .docx for each journal. The ready-to-copy scaffold is `templates/build-kit/` (its `README.md` has the commands).

## When to use it

This is a working mode, not a requirement (`SKILL.md`, Submission Convention 3).

| Situation | Mode |
| --- | --- |
| New manuscript, especially one that will go through many revisions or several journals | Build kit. Offer it at the start. |
| The author asks for it, or is resubmitting to another journal after a rejection | Build kit. Converting once pays off. |
| Revising or polishing an existing Word file | Stay in the Word file. Do not convert unless the author agrees; conversion means rebuilding citations and tables. |
| A single section or paragraph | Neither: return the revised text. |

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
4. For every new reference: find it (PubMed, Crossref, `references/pubmed-essentials.md`), then `python3 scripts/refs.py add <DOI or PMID:n>`. Never write a record from memory.
5. For a real source without DOI or PMID (a guideline on an institutional site, software documentation, a book, a report, legislation), open the source itself and register it with `refs.py add-manual`: official URL or ISBN, metadata copied from the source, who checked it and what was compared (`--by`, `--evidence`). It is stored as `manual`, distinct from automatic verification, and expires like any other check. `[CITATION NEEDED]` is only for a statement with no source found at all; the validator will not let it through.

### Converting an existing .docx draft (once)

1. `pandoc draft.docx -t markdown -o manuscript/10-body.md --extract-media=figures`, then split it into section files and add the semantic header ids (`{#methods}`, `{#abstract-results}`, declaration ids).
2. The numbered citations become static text such as `(12)` or superscripts. For each, find the entry in the old reference list, add it with `refs.py add` by DOI or PMID, and replace the number with its key. Keep a table of old number → key while doing it and report entries you could not resolve instead of guessing.
3. Rebuild tables as pipe tables inside `::: {#tbl:id}` divs and figures as `::: {#fig:id}` divs; replace "Table 2" in the text with `@tbl:id`.
4. Run `refs.py verify` and `validate.py`; fix every ERROR before the first build.

### Before upload: draft is not ready

A validator run without errors certifies a valid draft. Readiness is a separate, explicit step:

1. `validate.py --journal <j> --submission`. It refuses:
   - example content;
   - references that are unverified, incomplete, expired or flagged;
   - generic or unverified profiles;
   - any human-review item not ticked and signed in `signoff/<j>.md`.

   Tick an item only after it is done. An agent may prepare the evidence for each item, but the ticking belongs to the authors.
2. `build.py --journal <j> --submission`, then `preview.py --journal <j>`. Open the contact sheet of every file: tables, images, page breaks, marked text. The preview also catches author names left in a blinded file.

### Every revision

1. Edit the Markdown. Commit with a message saying what changed and why; separate editorial changes from scientific ones (analysis, exclusions, interpretation).
2. `python3 scripts/validate.py --journal <target>` after each substantive edit.
3. `python3 scripts/build.py --journal <target>` to produce the files for the authors.

### Changing journal

1. Create `journals/<new>.json` from the journal's current instructions (`templates/build-kit/journals/README.md`): record `source_url` and `verified_at`; never fill a limit from memory.
2. `validate.py --journal <new>`. Presentation differences are handled by the build. **Content differences are not:** a 267-word abstract for a 250-word limit, an unstructured abstract turned structured, a shorter Discussion. Propose those as a normal, reviewable edit; the exporter never cuts text.
3. Build, open the .docx, and compare it with the instructions once by eye.

### Revision round

1. Tag the submitted commit (`git tag submission-1`) if it was not tagged at submission.
2. `revision.py start --round 1 --submitted-tag submission-1 --journal <j> --returned <file.docx>`. Read `revision/round-1/journal-changes.md`: tracked changes, comments, and edits made without tracking (found by comparing with what was submitted). Present each item to the authors; apply the accepted ones to the Markdown. Never paste the returned file back.
3. `revision.py reconcile` until the only differences left are journal edits the authors rejected on purpose. Commit; `revision.py base` tags the base.
4. Make the revision. Answer each comment in `revision/round-1/responses.md` (quote it verbatim, answer, `Changed: <section ids>`). Keep scientific changes (new analyses, changed estimates) visible in the letter; never bury them.
5. `revision.py check`, then `build.py --journal <j> --revision 1`: clean file, marked file in the journal's style (J Vasc Bras: red), response letter, and a check listing unanswered comments, false "changed" claims and unexplained changes.

### File names

Every file sent to a journal is named `<short-name>_<journal>[_rev<N>]_<part>.<ext>` (e.g. `statins-ulcer_jvb_rev1_manuscript-marked.docx`): the manuscript, the journal, the revision round (absent at first submission), the part. The short name is set once in `metadata.yaml` and never contains an author's name, because blinded files carry it. When working outside the kit, name the files the same way by hand.

## What the validator does and does not decide

| Level | Examples | Who decides |
| --- | --- | --- |
| ERROR | Over a word limit (with what was counted); missing abstract part, section or declaration; citation key not in the library; duplicate, retracted, mismatched or not-found reference; figure cited but not defined; placeholder left in text; missing ORCID | Objective. The build stops unless `--force` (draft). |
| WARN | Reference unverified, incomplete (a source did not answer), expired (> 90 days) or flagged `check`; abbreviation used before definition; number in the abstract absent from the text; dash style; profile not verified or out of date | Probably wrong; confirm. |
| HUMAN | Reporting-checklist mapping; claim–evidence fit; whether each citation supports its sentence | Authors. Listed in every report so nobody forgets. |

`refs.py verify` proves that a reference **exists and matches its metadata** (title, year and first author against Crossref for a DOI and PubMed for a PMID) and flags retractions and corrections. A source that does not answer makes the result `incomplete` (exit code 3), never `ok`; a one-year gap or a missing field is `check` (look by eye); a verification older than 90 days is re-run, because retractions come after publication. Manual verifications (`add-manual`, `confirm`) record who checked what, and expire too. None of this proves that the paper supports the sentence it is attached to. That check is reading the cited abstract or full text against the claim, and it stays a HUMAN item (or an agent task whose output is a list for the authors, never a silent approval).

## Co-authors in Word

The source of truth is the Markdown. Send the generated .docx; co-authors comment or track changes; apply the accepted changes to the Markdown and rebuild. Do not convert an edited .docx back to Markdown after the initial conversion, because citations come back as static text. When co-authors must insert references themselves, have them name the reference in a comment (DOI or PMID) instead of inserting a citation.

Tag each submission in git (`submission-1-<journal>`, `revision-1`). Each build writes `outputs/<journal>/_build-info.json` with the profile and its verification date, the CSL, the pandoc version and the commit, so any submitted file can be traced to its exact source. For the marked version required with a revision, use the revision round (`build.py --revision N`): it separates the journal's edits from yours and marks yours as the journal asks (red text, highlight or tracked changes), with the same numbering as the clean file. Word's *Compare Documents* remains the tool when the manuscript lives in Word rather than in the kit, or to double-check a marked file against the submitted one; it cannot tell the journal's edits from yours.

## Limits of the kit

1. Numbers in the text are still typed. If the analysis is scripted, export its results (CSV/JSON) and have the tables built from them; Quarto with inline R or Python is the next step when the whole paper should update from the data.
2. The abbreviation and abstract-number checks are heuristics (WARN, never ERROR).
3. Journal templates with unusual layouts (two-column, custom title pages) need the journal's own `reference.docx` (`"reference_docx": {"file": ...}`), and some submission-system fields (Key Points, highlights) are prepared outside the .docx; list them in the profile's `human_checks`.
4. The ICMJE and most journals require disclosure of AI assistance and do not accept AI as an author. Keep the `{#ai-use}` declaration accurate; git history shows which changes came from which pass.
