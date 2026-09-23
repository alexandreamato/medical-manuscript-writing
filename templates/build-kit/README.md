# Manuscript build kit

Write the manuscript as plain text, keep references as structured data, and **generate** the .docx for each journal. Nothing in the .docx is edited by hand.

```
manuscript/          the text: one Markdown file per section, numbered for order
  metadata.yaml      title, authors (ORCID, affiliations), keywords, study design
references.json      CSL-JSON, one complete record per reference, key = @citation
references.verified.json   result of the last Crossref/PubMed check (generated)
journals/*.json      one profile per journal: limits, structure, style (journals/README.md)
csl/                 citation styles (Vancouver bundled, others fetched on demand)
figures/             image files referenced from the text
filters/             pandoc Lua filters: cross-references, journal presentation
scripts/             refs.py, validate.py, build.py (Python standard library only)
outputs/<journal>/   generated: manuscript.docx, title-page.docx, figures/, reports
```

Requirements: `pandoc` ≥ 3.1 (`brew install pandoc`) and Python ≥ 3.9. No Python packages. Network is needed only for `refs.py` and for downloading a CSL style the first time.

## Start a new manuscript

```bash
cp -R ~/.claude/skills/medical-manuscript-writing/templates/build-kit ~/path/my-article
cd ~/path/my-article && git init
```

The kit ships with a **fictional** cohort example that builds cleanly. Replace the example text, metadata and figure; keep the structure.

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
```

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
- **WARN:** unverified, incomplete, expired (> 90 days) or to-check references, references without identifier or manual verification, references never cited, abbreviations used before definition, numbers in the abstract that appear nowhere else, em-dashes and en-dash ranges (unless the profile allows them), P-value style, source order of figures/tables, profile not verified or out of date.
- **HUMAN:** the reporting checklist for the study design (CONSORT 2025, STROBE, PRISMA 2020, …), the claim–evidence map, and whether each citation supports its sentence. Code cannot judge these; the report lists them so nobody forgets.

## Co-authors and revisions

The Markdown is the source; the .docx is a product.

1. Send the generated .docx. Co-authors comment or track changes in Word.
2. Apply accepted changes to the Markdown (an agent can read the .docx comments and propose the diff). Do not convert the edited .docx back to Markdown: citations become static text.
3. Rebuild. Tag each submission in git (`git tag submission-1-jvs`, `revision-1`) and keep `outputs/<journal>/build-info.json`, which records the profile version, CSL, pandoc version and commit used.
4. For the response to reviewers, produce the marked-up version with Word's *Compare Documents* between the two tagged builds.

Keep identifiable patient data out of the repository.
