# Pre-Submission Adversarial Review (Medical Research)

## Goal

Use a reviewer-style checklist to detect rejection risks early and revise the manuscript before submission. Read the paper twice as a methodologist and once as a busy clinician.

This file is the skill's **single full pre-submission checklist**. Section guides keep only the checks specific to their section and point here for everything that cuts across sections; `references/common-mistakes.md` is the five-minute version of the same ground.

## Core Principle

Pursue calibrated honesty: assume reviewers will probe every claim, every number, every citation, and every choice. Reviewers reward visible self-criticism; they punish overstated claims and missing reporting items.

## Critical Rules (Do Not Violate)

1. **Every claim is technically correct and supported by the evidence its type requires** (`SKILL.md`, Integrity Rule 2). Classify before judging:
   - *Prior knowledge* (background, burden, earlier findings) is supported by a citation to a source that says it. The Results are irrelevant to it; do not remove a well-sourced background statement because this study did not test it.
   - *This study's findings* are supported by the Results, tables, and figures, with the same numbers, from the prespecified analysis or labelled exploratory.
   - *Interpretation* (meaning, comparison with other studies, implications) is supported by both, in language proportional to the design.

   If a claim lacks its kind of evidence, source it, weaken it, or remove it.
2. **Every reference is a real publication.** Verify each citation against PubMed / DOI / journal record before submission. Fabricated references are grounds for rejection and retraction.
3. **The manuscript agrees with itself.** See Cross-Section Consistency Checks below.
4. **Causal language matches the design.** RCTs may use causal verbs; observational studies use associative verbs.
5. **Reporting checklist is satisfied** for the design (`references/reporting-standards.md`) and submitted with the manuscript.
6. **Ethics, registration, and conflicts of interest are disclosed** as the design and the journal require (`references/ethics-and-integrity.md`).

## Cross-Section Consistency Checks

The canonical list; other files link here instead of repeating it.

1. **Numbers are identical everywhere they appear**: Abstract (both abstracts, when the journal wants two languages), Results, tables, figures, and the participant flow diagram. Point estimates, 95% CIs, P values, percentages, denominators.
2. **Every analysis in the Results is described in the Methods**, and every claim in the Discussion has the evidence its type requires (`SKILL.md`, Integrity Rule 2).
3. **Terminology and variable names do not change** between sections (intervention name, exposure and outcome definitions, analysis population).
4. **Citation and figure order**: references numbered by first appearance in numeric styles; tables and figures cited in numerical order. The rules: `references/manuscript-conventions.md` §1.2 and §2.1.
5. **Punctuation and number style are consistent**: dash and range style (`references/manuscript-conventions.md` §3.1), P-value and decimal format (`references/statistical-reporting.md`).
6. **Every reference is verified** and classified if it is not (Reference problems: four categories, below).

## What Usually Gets a Medical Paper Accepted

1. A clinically meaningful question, clearly stated.
2. A study design appropriate to the question and adequately powered.
3. Prespecification (registered protocol, prespecified analysis plan).
4. Honest, complete reporting against the relevant checklist.
5. Calibrated interpretation that does not outrun the evidence.

## What Reviewers Actually Look For (Bordage Survey)

Survey research on the criteria reviewers use to **accept** manuscripts converges on five top factors:

1. The **importance, timeliness, relevance, and prevalence** of the problem addressed.
2. The **quality of writing**: well-written, clear, straightforward, easy to follow, logical.
3. The **study design**: appropriate, rigorous, comprehensive.
4. The **literature review**: thoughtful, focused, up-to-date.
5. The **sample size**: sufficiently large for the question.

Build each of these into the manuscript explicitly: a clear problem statement in the Introduction, clean prose, a rigorous Methods, a focused literature framing, and an honest sample-size justification.

## Common Rejection Dimensions

| Rejection Dimension | Typical Failure Signals |
| --- | --- |
| 1. Insufficient clinical relevance | 1.1 Question is incremental or already settled. 1.2 Population or outcome is too narrow to inform practice. 1.3 Effect size is not clinically meaningful even if statistically significant. |
| 2. Unclear writing / not reproducible | 2.1 Methods cannot be replicated from the manuscript. 2.2 Statistical model is described in vague terms. 2.3 Outcome definition or ascertainment is missing. 2.4 Inconsistent terminology between sections. |
| 3. Methodological weakness | 3.1 Inappropriate design for the question. 3.2 Confounding not addressed in observational study. 3.3 Inadequate blinding or allocation concealment in trial. 3.4 Surrogate outcome without justification. 3.5 Underpowered study. 3.6 Multiplicity not handled. 3.7 Missing-data assumption unjustified. |
| 4. Incomplete reporting | 4.1 Missing flow diagram. 4.2 Missing baseline characteristics. 4.3 Sensitivity analyses missing. 4.4 Adverse events incompletely reported. 4.5 Reporting checklist not satisfied. |
| 5. Safety / ethics / integrity issue | 5.1 No IRB approval reported. 5.2 No registration of trial. 5.3 Conflicts of interest not declared. 5.4 Data sharing statement missing. 5.5 Authorship does not meet ICMJE criteria. 5.6 Fabricated or duplicated references, or unverified ones left unresolved (four categories, below). 5.7 Image or data manipulation suspected. |

## End-of-Paper Self-Review Question List

Answer each item before submission in a separate audit document (never appended to the text meant for the journal; `SKILL.md`, Stopping Rule).

### 1. Clinical relevance and contribution

1. What new knowledge does this paper add?
2. Does the question address a real unmet need (clinical, mechanistic, methodological)?
3. Is the effect size clinically meaningful, not only statistically significant?
4. Is there at least one clear contribution type (new evidence on an unresolved question / improved precision / new population / new outcome / new analytic approach)?
5. Does the contribution survive the 30-second clinician test ("would this change anything I do tomorrow")?

### 2. Writing clarity and reproducibility

1. Could a competent investigator replicate the study from the Methods?
2. Is each statistical model described with covariates, link function, and software version?
3. Is each outcome operationalized (instrument, units, timepoint, ascertainer, blinding)?
4. Are terms and units consistent across Abstract, Methods, Results, Discussion, and tables?
5. Does each paragraph deliver one clear message with smooth transitions?
6. Is causal language calibrated to the design?

### 3. Methodological rigor

1. Is the design appropriate for the question?
2. Is the sample size justified with explicit assumptions?
3. Is bias addressed: selection (recruitment, loss to follow-up), information (measurement, ascertainment), confounding (covariate adjustment, instrumental variables, target trial emulation)?
4. Is the analysis prespecified (registered protocol, statistical analysis plan)?
5. Are subgroup and sensitivity analyses prespecified or labeled exploratory?
6. Is missing data handled with a stated assumption?
7. Is multiplicity addressed: adjusted for confirmatory claims, or secondary and exploratory outcomes labelled as such? (An unadjusted exploratory outcome is acceptable when labelled; see `references/statistical-reporting.md` §2.)

### 4. Reporting completeness

1. Is the relevant reporting checklist (CONSORT/STROBE/PRISMA/STARD/CARE/TRIPOD+AI/ARRIVE) satisfied?
2. Is there a participant flow diagram?
3. Are baseline characteristics presented with appropriate balance metric (no p values for randomized trials)?
4. Are primary, secondary, subgroup, sensitivity, and adverse-event analyses all reported?
5. Do the Cross-Section Consistency Checks pass?
7. Is there a data and code availability statement?

### 5. Safety, ethics, and integrity

1. Is IRB / ethics committee approval reported with the protocol number?
2. Was informed consent obtained and described?
3. Is the trial / review registered (NCT, ISRCTN, ReBEC, EU CT number from CTIS or EudraCT for a legacy EU trial, PROSPERO)?
4. Are conflicts of interest fully disclosed?
5. Is the role of the funder stated?
6. Does the authorship list meet ICMJE criteria? Are contributions stated?
7. Is AI use disclosed (for analysis, writing assistance, image generation) per current journal policies?
8. Does the manuscript respect copyright and patient privacy (no identifiable images without consent)?

## See Also

1. **Critical self-reading from three reader perspectives** (the qualitative simulation that runs before this formal checklist): `references/read-as-reader.md`.
2. **Three-pass self-review and pre-peer-review workflow**: `references/writing-process.md`.
3. **Reporting-standard checklists** (CONSORT, STROBE, PRISMA, STARD) that reviewers will compare against: `references/reporting-standards.md`.
4. **Sentence- and word-level common pitfalls** that frequently trigger "writing clarity" rejection: `references/scientific-writing-principles.md`.
5. **Section-specific quality checklists** integrated at the end of each section guide: `references/abstract.md`, `references/introduction.md`, `references/method.md`, `references/results.md`, `references/discussion.md`.

## Adversarial Writing Workflow

1. Read the paper as a skeptical methodologist; mark every methodological gap.
2. Read it again as a skeptical clinician; mark every overstated implication.
3. Answer every question above with explicit evidence (paragraph, table, figure, page).
4. Mark each item as `pass`, `needs revision` (fixable in the text), or one of the four statuses for what writing cannot fix (the same four as the `SKILL.md` Stopping Rule): `needs new data`, `needs new analysis`, `needs author decision`, `needs author information` (a fact only the authors have, such as a protocol date or a committee number).
5. Fix every `needs revision` item in the text.
6. Stop there (`SKILL.md`, Stopping Rule). List the other items for the authors in a separate document, grouped under those four statuses; do not keep rewriting to argue around a design limitation or a missing analysis, and do not append the audit to the manuscript meant for the journal.
7. Finalize the reporting checklist and verify references.

## Common Specific Reasons Manuscripts Are Rejected

Top biomedical journals accept fewer than 25% of submitted manuscripts. Rejection does not necessarily mean the manuscript is poor; it often means the reviewers did not give it a high enough priority for the journal. The most common specific failures are:

1. **Inappropriate or incomplete statistics.** Wrong test for the design; missing 95% CIs; missing handling of missing data; multiplicity neither controlled for confirmatory claims nor acknowledged by labelling outcomes as exploratory.
2. **Over-interpretation of results.** Conclusions that outrun the design.
3. **Inappropriate or sub-optimal instrumentation.** Unvalidated measurement; obsolete assay; inappropriate outcome scale for the population.
4. **Sample too small or biased.** Underpowered, single-center, or convenience sample with unstated selection mechanism.
5. **Difficult-to-follow writing.** Long sentences, inconsistent terminology, missing logical connectors.
6. **Insufficient problem statement.** Reader cannot tell what specific question the study answers.
7. **Inaccuracy or inconsistency of data.** Numbers in the abstract do not match the Results; tables disagree with the body text.
8. **Incomplete, inaccurate, or outdated literature review.** Missing recent landmark trials; missing competing prior evidence.
9. **Insufficient data presented.** Headline result without supporting subgroup, sensitivity, or safety data.
10. **Defective tables or figures.** Missing units, missing 95% CIs, illegible labels, missing flow diagram.
11. **Inappropriate journal choice.** Manuscript scope mismatched to the journal's audience or remit.
12. **Confirmatory findings without added value.** Pure replications without new population, design strength, or analytic contribution face a higher bar.
13. **Ethics or registration gaps.** No IRB, no trial registration, no data-sharing statement.
14. **Reference problems.** Treat them in proportion to the evidence (see "Reference problems: four categories" below). Only apparent fabrication is a potential misconduct issue.

### Reference problems: four categories

A reference that could not be checked is not a fabricated reference. Classify before acting; the categories match the statuses of the build kit's `refs.py verify`.

| Category | What it means | Action |
| --- | --- | --- |
| **Not verified** | The record could not be checked: source unreachable, no DOI or PMID, a book or report not indexed (`incomplete`, `unverifiable`, `stale`) | Check it against the source itself (publisher page, library catalogue, the document) and record how. Resolve before submission. Not a sign of wrongdoing. |
| **Inconsistent** | The work exists, but the reference differs from its record: year, author, title, volume, pages (`mismatch`, `check`) | Correct the reference from the source record. Usually a transcription or reference-manager error. |
| **Retracted** (or corrected, or under an expression of concern) | The work exists and has an update notice (`retracted`, `corrected`) | Remove it, or keep it only if the retraction itself is relevant, cite the retraction notice, and say so in the text. For a correction, check that the cited result survived it. |
| **Apparent fabrication** | No record anywhere after a thorough search (PubMed, Crossref, the journal's own archive, Google Scholar), or details that match no real publication (a real journal with a nonexistent volume, a DOI belonging to another paper, an author list that never published together) | Remove it and tell the authors which statement it supported. This is the only category that raises a possible misconduct concern; it typically comes from a reference generated by an AI tool or copied from an unreliable source, and the statement it supported needs a real source or must be weakened. |

When the manuscript is rejected, read the reviewers' comments carefully: they are advice, not enemies. Most papers reach the same fate at some point. Reviewers' criticism makes you a better scientific writer and a more critical scientist over the long run.
