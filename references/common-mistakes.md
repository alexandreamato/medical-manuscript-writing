# Common Mistakes — Pre-Submission Speed Audit

A consolidated cheatsheet of the desk-rejection patterns and reviewer-comment triggers scattered across the rest of the skill. Use this as a 5-minute audit immediately before running the formal `references/paper-review.md` checklist.

For each mistake: the **pattern**, **why it fails**, the **fix**, and the **deeper file** with full guidance.

## Manuscript-level

| Pattern | Why it fails | Fix | See |
| --- | --- | --- | --- |
| Numbers in Abstract do not match Results | Reviewers spot inconsistencies on minute one; signals carelessness | Verify every CI, point estimate, p value, n; reconcile | `paper-review.md`, `abstract.md` |
| Causal verb in observational study | Overreach; reviewer comment guaranteed | "X reduced Y" → "X was associated with lower Y" | `study-types.md`, `discussion.md` |
| Title overpromises ("X prevents Y" from a single trial) | Triggers desk reviewer skepticism; first thing the editor reads | Match Title strength to evidence; use the same verb as the Conclusion | `read-as-reader.md` (Persona 2) |
| Conclusion goes beyond what the design supports (e.g., cost claims with no economic analysis) | Reviewers reject for overinterpretation | Restrict Conclusion to outcomes actually measured; add explicit limitation | `discussion.md`, `paper-review.md` |
| Sample size "justified" by what was available | Reviewers ask "what was the prespecified power calculation?" | Either provide a real prespecified calculation or label as exploratory | `method.md`, `statistical-reporting.md` |
| Multiple "primary" outcomes | Multiplicity inflates false-positive risk | Pick one primary; demote others to secondary; or apply gatekeeping with prespecified rule | `statistical-reporting.md` |
| Subgroup analyses presented as confirmatory | Major rejection trigger | Mark explicitly as "prespecified" or "exploratory"; report interaction p value | `experiments.md` (results), `paper-review.md` |
| Conclusion changes the population studied (e.g., results from elderly extrapolated to "all patients") | Reviewer flags external validity | Restrict the Conclusion to the population studied | `discussion.md`, `study-types.md` |

## Reporting-standard-level

| Pattern | Why it fails | Fix | See |
| --- | --- | --- | --- |
| No participant flow diagram in an RCT | CONSORT mandatory; immediate desk-rejection trigger | Build CONSORT flow at https://enciclopedia.med.br/consort2010 | `diagrams.md`, `reporting-standards.md` |
| No PRISMA flow diagram in a systematic review | PRISMA 2020 mandatory | Build PRISMA flow at https://enciclopedia.med.br/prisma2020 | `diagrams.md`, `systematic-review.md` |
| No CARE timeline in a case report | CARE Item 7 mandatory | Add a section-based or date-based timeline | `case-report.md`, `diagrams.md` |
| No reporting-checklist file in the supplement | Most journals require it | Complete the relevant checklist with page/line numbers | `reporting-standards.md` |
| Trial not registered (or registration not cited in Abstract/Methods) | ICMJE non-publication trigger | Register prospectively; cite the NCT/ISRCTN/EudraCT in Abstract | `ethics-and-integrity.md` |
| Systematic review not registered in PROSPERO | Most journals now require | Register before data extraction; cite PROSPERO ID | `systematic-review.md` |
| Adherence statement missing in Methods | Editors check | Add "This study is reported in accordance with [standard]. The completed [name] checklist is provided as Supplementary File X." | `reporting-standards.md` |

## Citation-level

| Pattern | Why it fails | Fix | See |
| --- | --- | --- | --- |
| Fabricated reference (the paper does not actually exist or DOI does not resolve) | Research misconduct; immediate retraction risk | Verify every citation against PubMed / DOI / publisher record | SKILL.md Hard Rule #1, `citation-styles.md` |
| Citation [12] appears in the text before [8] | Vancouver/AMA require ascending order | Renumber after every revision; scan top-to-bottom | `manuscript-conventions.md` |
| In-text citation has no matching reference list entry (or vice versa) | Editorial check fails | Run a final cross-check or use a reference manager that tracks both | `citation-styles.md` |
| Citing a review when a primary source exists | Reviewers prefer primary | Trace the original trial or cohort and cite that | `narrative-review.md`, `pubmed-essentials.md` |
| Journal name spelled out in some refs and abbreviated in others | Inconsistency triggers copy-editor pushback | Use NLM-approved abbreviations consistently (verify at https://www.ncbi.nlm.nih.gov/nlmcatalog/journals) | `citation-styles.md`, `pubmed-essentials.md` |
| URL in place of DOI when both exist | DOIs are permanent; URLs break | Replace URLs with `doi:10.xxxx/xxxxx` | `citation-styles.md` |
| Cited the preprint when the peer-reviewed version is now available | Reviewers spot it | Update to the published version | `citation-styles.md` |
| Reference to a retracted paper without acknowledging the retraction | Editorial integrity issue | Either cite as "retracted" with explanation or replace | `ethics-and-integrity.md` |

## Tables and figures

| Pattern | Why it fails | Fix | See |
| --- | --- | --- | --- |
| Tables/figures not cited in order of appearance | Editorial copy-editing flag | Renumber by first text mention; scan top-to-bottom | `manuscript-conventions.md` |
| Figure not cited at all in the body | Editorial integrity flag | Add the in-text citation or remove the figure | `figures-and-tables.md` |
| Bar chart y-axis not starting at zero | Distorts perception | Start at zero unless absolutely necessary; mark broken axis | `figures-and-tables.md` |
| Error bars present but caption does not say SD vs. SEM vs. CI | Reviewer asks; ambiguous interpretation | State which in every caption | `figures-and-tables.md`, `statistical-reporting.md` |
| Caption depends on body text (not self-contained) | Reviewer skim test fails | Define abbreviations, units, n, statistical test in caption | `figures-and-tables.md` |
| Image manipulation undisclosed (selective enhancement, lane splicing) | Research misconduct screen flags | Apply only linear adjustments; disclose all in Methods | `figures-and-tables.md`, `ethics-and-integrity.md` |
| 3-D bar chart or pie chart | Distorts perception | Use 2-D bar or table | `figures-and-tables.md` |
| No scale bar on histology / radiology images | Reviewer comment guaranteed | Add a scale bar; do not put magnification only in caption | `figures-and-tables.md` |
| Color encoding only (no shape / pattern) | Inaccessible for color-blind readers | Add shape or texture; test in grayscale | `figures-and-tables.md` |
| Same group plotted in different colors across figures (intervention green in Fig 1, red in Fig 2) | Forces the reader to re-learn the legend on every figure | Lock variable-to-color mapping once; reuse in every figure | `figures-and-tables.md` |
| Inconsistent line style / symbol per group across figures | Same as above — visual disorientation | Lock symbol and line style alongside color | `figures-and-tables.md` |

## Sentence-level

| Pattern | Why it fails | Fix | See |
| --- | --- | --- | --- |
| Em-dash (`—`) inside body sentences | Most medical journals discourage; copy-editor will flag | Replace with comma, semicolon, parenthesis, or full stop. For ranges: `12 to 18` not `12—18` | `manuscript-conventions.md`, `scientific-writing-principles.md` |
| `p = 0.000` | Mathematically impossible | Write `p < 0.001` | `statistical-reporting.md`, `scientific-writing-principles.md` |
| Anthropomorphism: "the study wanted to ...", "the data tell us ..." | Reviewers find it unscientific | "We aimed to ...", "The data indicate that ..." | `scientific-writing-principles.md` |
| `This was unexpected` (pronoun without antecedent) | Reader stops to figure out "this" | Pair `this` with a noun: `this finding`, `this association` | `scientific-writing-principles.md` |
| Excessive hedging: "It could perhaps be possible that ... might possibly ..." | Reads as evasive | Calibrate to evidence: "X reduced Y" (RCT) or "X was associated with Y" (observational) | `scientific-writing-principles.md` |
| Insufficient hedging: "X cures Y" from one trial | Overreach | Use "reduced" / "was associated with lower" with confidence interval | `scientific-writing-principles.md`, `study-types.md` |
| Abbreviation used without definition at first mention in the body | Non-specialist readers stumble | Define at first use in the body, even if defined in the Abstract | `scientific-writing-principles.md` |
| Abbreviation defined and never used again | Cognitive load with no payoff | Spell out and remove the abbreviation if used fewer than 3 times | `scientific-writing-principles.md` |
| `due to the fact that` / `in order to` / `at the present time` | Wordy; signals lack of revision | `because` / `to` / `now` | `scientific-writing-principles.md` (full table) |
| Sentence > 30 words consistently | Reader fatigue | Split or vary length; aim ≤ 25–30 words | `scientific-writing-principles.md` |
| Numerals < 10 used with non-unit context | Style inconsistency | Spell out small numbers without units; numerals for measurements (`5 mg`) | `scientific-writing-principles.md` |
| Number at start of sentence | Style violation | Spell out (`Five participants ...`) or restructure | `scientific-writing-principles.md` |

## Methods-section

| Pattern | Why it fails | Fix | See |
| --- | --- | --- | --- |
| "We measured outcomes" with no instrument, units, or timing | Not reproducible | Specify instrument (model, manufacturer), units, timing, ascertainer, blinding | `method.md` |
| Statistical model named without covariates or software | Reviewer cannot replicate | Name model + covariates + software with version (`R 4.3.1`, `lme4 1.1-35`) | `method.md`, `statistical-reporting.md` |
| Missing-data handling not stated | Reviewer red flag | Name the mechanism assumed (MAR / MCAR / MNAR) and the method (multiple imputation, complete-case) | `statistical-reporting.md` |
| Confounding adjustment without rationale | Looks data-driven | State variable selection a priori, ideally from a DAG | `method.md`, `study-types.md` |
| Recruitment-data leakage in Methods (e.g., "from 1,215 patients admitted ...") | Methods describes design, not Results | "Patients were recruited consecutively from those admitted to ..." | `method.md` (Alexandrov 2004) |
| Surrogate outcome treated as primary without justification | Editorial weakness | Justify the surrogate (mechanism + empirical link to clinical outcome) or downgrade | `method.md`, `discussion.md` |
| Ethics approval missing or vague | Desk-rejection trigger | Name the IRB, the protocol number, the date | `ethics-and-integrity.md` |

## Discussion-section

| Pattern | Why it fails | Fix | See |
| --- | --- | --- | --- |
| Discussion repeats the Results | Wastes the reader's time | Reference the numbers; do not retabulate | `discussion.md` |
| Introducing new data in the Discussion | Editorial structural flag | Move data to Results; the Discussion only interprets | `discussion.md` |
| Limitations buried in paragraph 5 | Busy clinician misses them | Surface in the Abstract Conclusion if they affect the take-home | `discussion.md`, `read-as-reader.md` (Persona 2) |
| Inflated importance: "novel", "first study", "groundbreaking" | Reads as self-congratulatory | Let the data speak; remove unnecessary intensifiers | `discussion.md` |
| Bully pulpit: criticizing other studies disrespectfully | Antagonizes reviewers, who often know those authors | Discuss differences methodologically; never insult | `discussion.md` |
| Generic "more research is needed" | Vague closing fails | Specify which design, population, sample size, outcome | `discussion.md`, `narrative-review.md` |

## Submission and post-submission

| Pattern | Why it fails | Fix | See |
| --- | --- | --- | --- |
| Wrong journal scope | Mismatched audience triggers rejection | Read 3–5 recent papers from the target journal; verify scope | `writing-process.md` |
| Manuscript not in `.docx` when journal requires it | Editorial submission error | Default to .docx with line numbering, double-spaced | `manuscript-conventions.md` |
| Cover letter empty or boilerplate | Lost opportunity | Summarize 3–5 key changes; mention reporting checklist; declare originality | `responding-to-reviewers.md` |
| Missing data-sharing statement | ICMJE compliance flag for trials | Add a statement: what, when, how, with whom | `ethics-and-integrity.md` |
| Conflicts of interest not declared | Integrity flag | Use the ICMJE Disclosure Form; declare everything | `ethics-and-integrity.md` |
| AI-tool use undisclosed | Most major journals now require disclosure | State tool, version, and how it was used in Methods or Acknowledgments | `ethics-and-integrity.md`, `citation-styles.md` |

## Responding to reviewers

| Pattern | Why it fails | Fix | See |
| --- | --- | --- | --- |
| Defending the existing text instead of editing | Reviewer feels ignored | Apply the **70% rule**: positively address ≥ 70% of comments | `responding-to-reviewers.md` |
| Vague response: "the text was amended for clarity" | Reviewer must hunt for the change | Quote the new text + page/line | `responding-to-reviewers.md` |
| Cross-referencing instead of duplicating | Reviewer reads only their own comments | Repeat the response in full under each instance | `responding-to-reviewers.md` |
| Defensive vocabulary: "obviously", "the reviewer misunderstood", "as we already wrote" | Antagonizes editor and reviewer | "We may not have explained this clearly. We have ..." | `responding-to-reviewers.md` |
| Skipping editorial author-instructions | Desk-rejection at resubmission | Address every editorial request under a separate heading | `responding-to-reviewers.md` |
| Tracked changes not submitted | Reviewer cannot find changes | Submit both tracked and clean versions | `responding-to-reviewers.md` |

## Five-minute speed audit (use this list)

Run through these in order. Each takes < 30 seconds.

1. Open Abstract; copy each numerical value; verify it appears identically in the Results and tables.
2. Read the Title; ask whether the verb matches the design strength (RCT can say "reduced"; observational says "was associated with").
3. Scan the body top-to-bottom looking for `—` (em-dash); replace each occurrence.
4. Scan numerical citations top-to-bottom; verify ascending order.
5. Open the reference list; spot-check 5 random references against PubMed.
6. Verify the participant flow diagram exists and uses the correct reporting-standard format.
7. Verify the registration number appears in the Abstract (trials, systematic reviews).
8. Verify ethics approval, conflicts of interest, data-sharing, and AI-disclosure statements are all present.
9. Read each table/figure caption alone; verify each stands without the body.
10. Read the Discussion's first paragraph; confirm causal language matches the design.

If any of these fail, fix before formal `paper-review.md` audit.

## See Also

1. **Formal pre-submission audit**: `references/paper-review.md`.
2. **Sentence-level revision**: `references/scientific-writing-principles.md`.
3. **Reporting-standard adherence**: `references/reporting-standards.md`.
4. **Three-pass self-review and pre-peer-review**: `references/writing-process.md`.
5. **Reading the manuscript as a reader**: `references/read-as-reader.md`.
