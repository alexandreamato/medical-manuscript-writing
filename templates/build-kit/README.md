# Manuscript build kit

Write the manuscript as plain text, keep references as structured data, and **generate** the .docx for each journal. Nothing in the .docx is edited by hand.

```
manuscript/          the text: one Markdown file per section, numbered for order
  metadata.yaml      title, authors (ORCID, affiliations), keywords, study design
references.json      CSL-JSON, one complete record per reference, key = @citation
references.verified.json   result of the last Crossref/PubMed check (generated)
journals/*.json      one profile per journal: limits, structure, style, revision rule (journals/README.md)
revision/round-N/    one folder per revision round: state, journal's returned file, report, responses.md
csl/                 citation styles (Vancouver bundled, others fetched on demand)
figures/             image files referenced from the text
filters/             pandoc Lua filters: cross-references, journal presentation
scripts/             refs.py, validate.py, build.py (Python standard library only)
outputs/<journal>/   generated files to upload (named by the rule below) + _reports
```

Requirements: `pandoc` ≥ 3.1 (`brew install pandoc`) and Python ≥ 3.9. No Python packages. Network is needed only for `refs.py` and for downloading a CSL style the first time.

## Start a new manuscript

```bash
cp -R ~/.claude/skills/medical-manuscript-writing/templates/build-kit ~/path/my-article
cd ~/path/my-article && git init
```

The kit ships with a **fictional** cohort example that builds cleanly against every profile. Replace the example text, metadata and figure; keep the structure.

Profiles included: `jvb` (**Jornal Vascular Brasileiro**, the default in `metadata.yaml`; rules read in the journal's instructions on 2026-09-23, every rule annotated with its source), `generic-icmje` (drafting defaults before a journal is chosen) and `example-journal-b` (illustrative, never submit against it).

**Two languages.** Journals such as J Vasc Bras want title, abstract and keywords in Portuguese and English. Put the second title and keywords in `metadata.yaml` (`title-alt`, `keywords-alt`, `lang-alt`) and the second abstract in a section `# Resumo {#abstract-alt}` with parts `{#abstract-alt-background}`, etc. The profile names the headings in each language.

## File names

Every file for the journal follows one rule: **what · where · when · which part**.

```
<short-name>_<journal>[_rev<N>]_<part>.<ext>

statins-ulcer_jvb_manuscript.docx            first submission
statins-ulcer_jvb_title-page.docx
statins-ulcer_jvb_figure-1.png
statins-ulcer_jvb_rev1_manuscript-marked.docx   revision round 1
statins-ulcer_jvb_rev1_response-letter.docx
```

- **short-name**: set once in `metadata.yaml` (`short-name: statins-ulcer`), 1 to 5 words. Never an author's name: the blinded manuscript carries it too (the validator checks).
- **journal**: the profile id (`jvb`).
- **rev\<N\>**: only in revision rounds; absent at first submission.
- **part**: `manuscript`, `title-page`, `figure-N`, `supplementary-figure-N`, `manuscript-clean`, `manuscript-marked`, `response-letter`.
- Lowercase, no accents or spaces; hyphens inside a field, underscores between fields. Files starting with `_` (`_validation-report.txt`, `_build-info.json`) are internal and are not uploaded.

Inside the project the source files keep their own simple rule: `manuscript/NN-section.md`, where the two-digit prefix sets the order (`00-abstract.md`, `01-introduction.md`, …).

## Daily commands

```bash
python3 scripts/refs.py add 10.1016/S0140-6736(07)61602-X   # by DOI (Crossref)
python3 scripts/refs.py add PMID:18064739                   # by PMID (PubMed)
python3 scripts/refs.py verify                              # existence, metadata, retractions
python3 scripts/refs.py add-manual --key who2023x --type report --org "World Health Organization" \
    --title "..." --year 2023 --url https://... --by "Name" --evidence "official PDF imprint"
python3 -m unittest discover -s scripts/tests                # kit self-test, no network
python3 scripts/validate.py --journal generic-icmje         # checks, no output files
python3 scripts/validate.py --compare                       # fit against every journal profile
python3 scripts/build.py --journal generic-icmje            # validate, then build the .docx
python3 scripts/build.py --journal x --force                # draft build despite errors
python3 scripts/preview.py --journal jvb                    # render and inspect the files
python3 scripts/validate.py --journal jvb --submission      # the gate before upload
python3 scripts/build.py --journal jvb --submission         # final build, never forced
```

## Draft is not ready

A clean `validate.py` means **valid draft**, not ready to submit. Before upload:

1. **Submission gate** (`--submission`, for `validate.py` and `build.py`). Blocks:
   - demonstration content (`example: true` in `metadata.yaml`, which the bundled example carries);
   - references not verified, incomplete, expired or flagged `check`;
   - generic, illustrative or unverified journal profiles;
   - every human-review item not ticked in `signoff/<journal>.md`. The file is written for you with one checkbox per item, and needs "Signed off by: name, date".

   `--force` is refused in this mode.
2. **Look at the product.** `preview.py` renders every file to PDF and a contact sheet of all pages (`outputs/<journal>/_preview/`, with LibreOffice and poppler). It checks what only the finished file shows:
   - an author's name or e-mail left in the blinded manuscript (ERROR);
   - a revision "marked" file with nothing marked;
   - missing line numbers;
   - figure files that do not match the legends.

   Then open the contact sheet and look at every page.

## Revision rounds

The journal often sends back a .docx its staff or reviewers edited. Absorb their edits first; then mark only yours.

```bash
git tag submission-1                                         # at submission (or later, on that commit)
python3 scripts/revision.py start --round 1 --submitted-tag submission-1 --journal jvb \
    --returned ~/Downloads/returned.docx                    # -> revision/round-1/journal-changes.md
#   the report lists tracked changes, comments, and edits made WITHOUT tracking
#   (compared with what we sent; pass --submitted-docx to compare with the exact
#   file uploaded instead of a rebuild of the tag). Apply the accepted ones to
#   manuscript/*.md; never paste the returned file back (its citations are text).
python3 scripts/revision.py reconcile --round 1             # journal edits still missing
git commit -am "Round 1: journal edits accepted"
python3 scripts/revision.py base --round 1                  # tag revision-1-base
#   now revise manuscript/*.md and answer in revision/round-1/responses.md
python3 scripts/revision.py check --round 1                 # letter vs actual changes
python3 scripts/build.py --journal jvb --revision 1
```

`outputs/jvb/revision-1/` then holds `…_rev1_manuscript-clean.docx`, `…_rev1_manuscript-marked.docx` (inserted text in red, deleted text struck through in red, as J Vasc Bras asks), `…_rev1_response-letter.docx`, the title page and `_letter-check.txt`. The marking rule comes from the profile (`revision.marking`: `color`, `highlight`, `tracked` for real Word tracked changes, or `none`). Both manuscripts have the same reference and figure numbers: a deleted citation is shown as `[citation]` and does not take a number.

In `responses.md`, one `##` per comment, the comment quoted with `>`, the answer, and `Changed: <section ids>` (or `none`). `check` fails when a comment has no answer or claims a change in a section that did not change, and warns when a section changed without any answer mentioning it.

## Writing rules (what keeps it from breaking)

1. **Cite by key, never by number:** `[@vonelm2007strengthening]`, `[@a; @b]`. citeproc numbers references by first citation on every build, so moving a paragraph can never leave the list out of sequence, and the same file prints as Vancouver, AMA or any journal's style.
2. **References come from `refs.py add`**, never typed from memory. It pulls the full record from Crossref or PubMed, with PMID and NLM journal abbreviation. `verify` checks title, year and first author against every source the reference has, flags retractions and corrections (Crossref `updated-by` with Retraction Watch data; PubMed publication type), and re-checks anything edited or older than 90 days (`--max-age`). A source that does not answer gives `incomplete` and exit code 3, never a pass. Sources without DOI or PMID (guidelines, software documentation, books, reports) go in with `refs.py add-manual`, which records the official URL or ISBN, who checked the source and what was compared; `refs.py confirm` does the same for an existing entry.
3. **Figures and tables have ids and are cited by id:** `@fig:flow`, `@tbl:baseline`. They are numbered by first mention in the text, as ICMJE requires. Wrap them in a fenced div:

   ```markdown
   ::: {#tbl:baseline}
   Table: Baseline characteristics by statin use.

   | Characteristic | Exposed | Unexposed |
   |:--|--:|--:|
   :::

   ::: {#fig:flow}
   ![STROBE participant flow.](figures/flow.png)
   :::
   ```

   Supplementary material uses `sfig:` and `stbl:`.
4. **Sections have semantic ids**, not journal names: `# Methods {#methods}`, `## Results {#abstract-results}`. The journal profile decides whether it prints "Methods", "Patients and Methods" or "Findings".
5. **Declarations are sections with fixed ids**: `{#ethics}`, `{#funding}`, `{#conflicts}`, `{#data-availability}`, `{#author-contributions}`, `{#ai-use}`, `{#acknowledgments}`. The profile says which are required and which are dropped from the blinded file.
6. **The build never rewrites content.** If the abstract has 267 words and the journal allows 250, the validator reports it; shortening it is an editorial change for the authors (or an agent, as a reviewable diff).

## What the validator checks

- **ERROR (build stops):** word/character limits per scope, required sections and abstract parts, missing declarations, citation keys absent from `references.json`, duplicate DOIs, retracted, mismatched or not-found references, a source with neither identifier nor manual verification when the journal requires identifiers, figures/tables cited but not defined or defined but never cited, figure/table/reference caps, keyword count, ORCID presence and format, corresponding author, placeholders left in text (`[CITATION NEEDED]`, `TODO`, `[N]`, `[exposure]`).
- **WARN:** unverified, incomplete, expired (> 90 days) or to-check references, references without identifier or manual verification, references never cited, abbreviations used before definition, an estimate with its 95% CI in the abstract that does not appear with the same interval in the Results or tables, results that differ between the two abstracts, other abstract numbers that appear nowhere else (a screen: it cannot tell outcome, group or time point apart), em-dashes and en-dash ranges (unless the profile allows them), P-value style, source order of figures/tables, profile not verified or out of date.
- **HUMAN:** the reporting checklist for the study design (CONSORT 2025, STROBE, PRISMA 2020, …), the claim–evidence map, and whether each citation supports its sentence. Code cannot judge these; the report lists them so nobody forgets.

## Co-authors

The Markdown is the source; the .docx is a product.

1. Send the generated .docx. Co-authors comment or track changes in Word.
2. Apply accepted changes to the Markdown (an agent can read the .docx comments and propose the diff). Do not convert the edited .docx back to Markdown: citations become static text.
3. Rebuild. Tag each submission in git (`git tag submission-1-jvs`, `revision-1`) and keep `outputs/<journal>/_build-info.json`, which records the profile version, CSL, pandoc version and commit used.
4. For a journal revision, use the revision round above rather than Word's *Compare Documents*: it separates the journal's edits from yours and marks yours the way the journal asks.

Keep identifiable patient data out of the repository.
