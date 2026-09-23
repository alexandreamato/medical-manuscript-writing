# Abstract Writing Guide (Medical Research)

## Goal

Write a strong abstract by doing three things repeatedly:

1. Think through the abstract logic first (clinical question → design → main result).
2. Follow the template below that matches the study design (A: randomized trial; B: observational; C: systematic review).
3. Revise the abstract many times.

## Format Reminder

Most biomedical journals require a **structured abstract** with explicit headings. Match the format to the study type and the journal:

- Randomized controlled trial: Background, Methods, Results, Conclusions, Trial Registration (CONSORT for Abstracts).
- Observational study: Background, Methods, Results, Conclusions (STROBE).
- Diagnostic accuracy study: Background, Methods, Results, Conclusions (STARD for Abstracts).
- Systematic review / meta-analysis: Background, Methods, Results, Conclusions, Registration / PROSPERO ID (PRISMA for Abstracts).
- Case report: Background, Case presentation, Conclusions (CARE).

Word count is usually 250 to 350 words. The abstract is what most readers, and many reviewers on the first pass, will actually read; treat it as the highest-stakes paragraph in the paper.

## Pre-Writing Questions

Answer these before writing:

1. What is the clinical question (PICO/PECO/PIRD/PIRT) and why is it currently unresolved? (important)
2. What is the study design and the prespecified primary outcome?
3. What is the headline numerical result for the primary outcome (point estimate, 95% CI, and, for hypothesis tests, the p value)?
4. What is the single most important conclusion the reader should walk away with, and what is its scope of generalizability? (important)

## Five-Element Checklist (Adapted from Koopman 1997)

A good abstract is a self-contained capsule of the paper. Before submission, verify it answers all five elements. Each element is typically one sentence; some can be merged.

1. **Motivation.** Why does the question matter? Disease burden, current management gap, or stakes for patients or policy.
2. **Problem statement.** What unresolved question does this study answer? State the scope precisely (population, setting, intervention or exposure, outcome).
3. **Approach.** How was the study done? Design, sample size, analytic strategy in plain clinical terms.
4. **Results.** What was found? Concrete numbers: point estimate, 95% CI, and where appropriate the p value. Avoid vague terms ("very", "small", "significant" without numbers, "promising", "novel").
5. **Conclusions.** What are the implications? State the take-home message and its scope of generalizability. Match causal language to the design.

## Self-Containment Rules

The abstract is the only part of the paper that most readers, and many editors and reviewers on the first pass, will read. It must stand alone:

1. Every clinical, epidemiological, and statistical term is readable on first occurrence.
2. Spell out every abbreviation at first use (limit to 6 to 8 abbreviations across the abstract).
3. Numbers in the abstract appear identically in the Results, tables, and figures (`references/paper-review.md` (Cross-Section Consistency Checks)). Re-check after every revision.
4. No reference to "see below", "in this paper", or "(data not shown)".
5. No citations inside the abstract unless explicitly required by the journal.

## Search-Retrievability Rules

The abstract is the entry point for PubMed, Embase, Scopus, and Google Scholar searches. Reviewers and clinicians find your paper through its abstract; structure it so retrieval works:

1. Identify 6 to 8 search terms a reader would use to find your work; include them verbatim in the abstract.
2. Use MeSH-aligned terminology where possible (`myocardial infarction`, not `heart attack`; `randomized controlled trial`, not `randomised study`).
3. State the design in the abstract title or in the first sentence (e.g., "A multicenter randomized trial of ...").
4. State the population precisely: age range, condition, setting.

## Word-Count Discipline

Most journals limit abstracts to 250 to 350 words.

1. Cut yourself before the editor or copy-editor cuts you. They cut for length, not for fidelity to your message.
2. Write the abstract last, after the body of the paper is final.
3. Verb economy: "We randomized 4,250 adults" beats "A total of 4,250 adults were enrolled and subsequently randomized".
4. One number, one place: do not repeat the headline number in two sentences.

## Tense

1. Background: present tense for established knowledge, past for prior studies cited.
2. Methods: past tense ("We randomized ...", "We searched ...").
3. Results: past tense ("The primary outcome occurred in ...").
4. Conclusions: present or simple-future-style ("[Intervention] reduced ...", "These findings support ..."). Do not write "results will be discussed".

## The Logic Every Structured Abstract Follows

Whatever the headings a journal requires, the abstract answers four questions in order, and each part must connect to the next:

1. **Background: what is unknown, and why does it matter?** One or two sentences: the clinical problem and the specific gap. End on the gap, not on general importance.
2. **Methods: what design answers that gap?** Design, setting, population, intervention or exposure, comparator, primary outcome and timepoint, and the analysis that handles the main threat to validity (randomization and blinding; confounding adjustment; risk of bias and synthesis).
3. **Results: what was found, and how precisely?** Participants analysed, then the primary outcome with an effect size and 95% CI (absolute and relative where relevant), then harms or the key prespecified secondary result.
4. **Conclusions: what does it mean, within what the design allows?** One or two sentences, with the population and follow-up as scope. Causal verbs only for randomized evidence; "was associated with" for observational designs; the GRADE certainty qualifier for evidence syntheses.

The three templates below apply this logic to the three most common designs. Choose by design, not by how the paper "feels".

## Template A: Randomized Controlled Trial

Reported under CONSORT and CONSORT for Abstracts.

### Structure

1. Clinical question and the specific gap in current evidence (the limitation of design, sample size, population, or follow-up).
2. Design, population, intervention, comparator, and prespecified primary outcome with timepoint.
3. Number randomized and analysed.
4. Primary result: counts in each group, absolute and relative effect, 95% CI.
5. Harms (serious adverse events) or the key secondary outcome.
6. Conclusion in causal language, limited to the trial population and duration.
7. Trial registration identifier (NCT, ISRCTN, EudraCT) per ICMJE.

### Expert Notes

1. Discuss prior evidence around the exact gap this trial fills; the first Methods sentence should read as the answer to it.
2. State design, population, and primary outcome; do not preview every secondary analysis.
3. The condition, intervention, and outcome must be readable to a non-specialist; spell them out before any abbreviation.
4. If the primary outcome was not significant, say so; do not lead the Results or Conclusion with a secondary outcome.

Local cite: `references/examples/abstract/template-a.md`.

## Template B: Observational Study

For cohort, case-control, and cross-sectional studies, target trial emulations, and Mendelian randomization, reported under STROBE or STROBE-MR.

### Structure

1. Clinical question and the specific limitation of prior evidence (for example, confounding by indication, immortal time bias, small cohorts, crude exposure measurement).
2. Design, data source, setting, population, exposure and comparator, outcome, and follow-up.
3. The strategy that addresses the main bias: confounders adjusted for and how, the target trial specification, or the genetic instruments.
4. Adjusted association with 95% CI, and at least one sensitivity analysis for residual confounding (for example, an E-value or a negative-control outcome).
5. Conclusion stated as an association, with scope and the appropriate next step.

### Expert Notes

1. A prespecified hypothesis can be stated in one sentence; do not frame it as a discovery.
2. Name the analytic strategy in plain terms so a reviewer can map it to STROBE items 7 to 12.
3. A design that reduces bias does not license causal verbs; keep "was associated with" in the Conclusion.
4. Avoid previewing the Discussion; reserve interpretation for the Conclusion line.

Local cite: `references/examples/abstract/template-b.md`.

## Template C: Systematic Review and Meta-Analysis

Reported under PRISMA 2020 and PRISMA for Abstracts.

### Structure

1. Why a synthesis is needed now (conflicting trials, new trials since the last review, an unresolved subgroup or harm).
2. Eligibility (PICO and designs), databases and search dates, risk-of-bias tool, synthesis method, and certainty assessment (GRADE).
3. Number of studies and participants included.
4. Pooled effect with 95% CI and heterogeneity (I², prediction interval where possible).
5. Prespecified subgroup, sensitivity, or harms result, with the interaction test for subgroups.
6. Certainty of evidence for the main outcomes and the main reasons for rating down.
7. Conclusion whose verb and strength match the certainty; PROSPERO registration.

### Expert Notes

1. One finding per sentence, each with its quantitative result.
2. Report only prespecified subgroups in the abstract; label any post-hoc subgroup as exploratory.
3. Low or very low certainty calls for "may" or "is uncertain", not "reduces".

Local cite: `references/examples/abstract/template-c.md`.

## Example Bank

1. `references/examples/abstract-examples.md`
2. `references/examples/abstract/template-a.md`: randomized controlled trial
3. `references/examples/abstract/template-b.md`: observational study, target trial emulation, Mendelian randomization
4. `references/examples/abstract/template-c.md`: systematic review and meta-analysis

## See Also

1. **Drafting order** (write the abstract last): `references/writing-process.md`.
2. **Reporting-checklist abstract items** (CONSORT for Abstracts, PRISMA for Abstracts, STARD for Abstracts): `references/reporting-standards.md`.
3. **Sentence- and word-level revision** (conciseness, hedging, calibration): `references/scientific-writing-principles.md`.
4. **Pre-submission audit of the abstract** (numbers must match Results; abstract is the first thing reviewers read): `references/paper-review.md`.

## Abstract Quality Checklist

1. Can a busy clinician identify question, design, primary outcome, headline result, and conclusion in one read-through?
2. Are all numerical claims supported by the Results section, with matching point estimates and CIs?
3. Are clinical terms self-contained and readable on first occurrence?
4. Is exactly one prespecified primary outcome named (or is the abstract honest that the headline finding is exploratory)?
5. Is causal language calibrated to the design (RCT → "reduced"; observational → "was associated with")?
6. Is the scope of generalizability stated (population, setting, time horizon)?
7. For trials and reviews: is the registration number present?
