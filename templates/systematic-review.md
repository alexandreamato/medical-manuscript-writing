<!-- TEMPLATE: Systematic review / meta-analysis manuscript (PRISMA 2020 aligned) -->
<!-- Replace text in [BRACKETS]. Inline comments like "<!-- PRISMA 7 -->" point to the PRISMA 2020 checklist item. -->
<!-- See references/systematic-review.md for full workflow and references/reporting-standards.md for the 27-item checklist. -->

# [Title: identifies the report as a systematic review and/or meta-analysis; states the population, intervention, and outcome]
<!-- PRISMA 1 -->

**Short running title:** [≤ 40 characters]

## Authors

[First M. Last]^1^, [First M. Last]^2^

1. [Affiliation, City, Country]. ORCID: [xxxx-xxxx-xxxx-xxxx]
2. [Affiliation, City, Country]. ORCID: [xxxx-xxxx-xxxx-xxxx]

**Corresponding author:** [First M. Last], [Address], [Email]

## Manuscript metadata

- **Word counts:** Abstract [N], Body [N], References [N]
- **Tables:** [N] (Table 1 study characteristics; Table 2 risk-of-bias summary; Table 3 GRADE summary of findings)
- **Figures:** [N] (Figure 1 PRISMA 2020 flow; Figure 2 forest plot of primary outcome; Figure 3 funnel plot if ≥ 10 studies)
- **Registration:** PROSPERO [CRD420260000000]
- **Funding:** [Source, role]
- **Conflicts of interest:** [Per ICMJE]

---

## Abstract
<!-- PRISMA 2 — see PRISMA for Abstracts checklist -->
<!-- See references/abstract.md (Template C: Multiple Contributions) -->

**Background.** [Clinical importance and the unresolved question this synthesis addresses.]

**Methods.** [Eligibility criteria (PICO + designs + dates + languages)]. [Information sources and last search date]. [Selection process]. [Risk-of-bias tool]. [Synthesis method (qualitative / quantitative meta-analysis with model)]. [Certainty of evidence rating (GRADE)]. [Protocol registration: PROSPERO ID].

**Results.** [Of [N] records identified, [N] studies were included]. [Pooled effect estimate (95% CI; I²) for primary outcome]. [Subgroup or sensitivity finding]. [Certainty of evidence].

**Conclusions.** [One sentence with effect direction, magnitude, scope, and certainty qualifier (high / moderate / low / very low).]

**Registration.** PROSPERO [CRD420260000000].

---

## 1. Introduction
<!-- PRISMA 3 (rationale), 4 (objectives) -->
<!-- See references/introduction.md and references/related-work.md -->

[Paragraph 1 — burden and clinical importance.]

[Paragraph 2 — what is known and the gap; existing reviews and their limitations (out-of-date, narrow scope, methodological flaws).]

[Paragraph 3 — present synthesis aim.] We conducted a systematic review and meta-analysis to estimate the effect of [intervention/exposure] on [outcome] in [population], synthesising evidence from [study designs] published through [date]. <!-- PRISMA 4 -->

---

## 2. Methods
<!-- See references/method.md and references/systematic-review.md -->

### 2.1 Protocol and registration
<!-- PRISMA 5 -->

The review protocol was registered prospectively in PROSPERO (registration number [CRD420260000000]) on [date], before screening commenced. The protocol is available at [URL].

### 2.2 Eligibility criteria
<!-- PRISMA 6 -->

**Population:** [...]
**Intervention / Exposure:** [...]
**Comparator:** [...]
**Outcomes:** Primary [...]; secondary [...].
**Study designs:** [Randomized trials / observational studies / both].
**Time frame:** Studies published between [start year] and [end year].
**Languages:** [English only / no language restriction].
**Other inclusion criteria:** [...]
**Exclusion criteria:** [...]

### 2.3 Information sources
<!-- PRISMA 7 -->

We searched MEDLINE (via PubMed), Embase (via Ovid), the Cochrane Central Register of Controlled Trials (CENTRAL), and [specialty databases: CINAHL / PsycINFO / LILACS / SciELO]. We also searched ClinicalTrials.gov and the WHO ICTRP for unpublished trials, and conducted backward and forward citation searches of all included studies. Last search date: [DD Month YYYY].

### 2.4 Search strategy
<!-- PRISMA 8 -->

The full search strategy for each database is provided in Supplementary File 1. The MEDLINE strategy combined MeSH and free-text terms for [population], [exposure/intervention], and [outcome] using Boolean operators. See `references/pubmed-essentials.md` for terminology guidance.

### 2.5 Selection process
<!-- PRISMA 9 -->

Two reviewers (initials) independently screened titles and abstracts using [Rayyan / Covidence / DistillerSR]; disagreements were resolved by discussion or by a third reviewer (initials). Full-text articles meeting eligibility were assessed by the same two reviewers; reasons for exclusion at the full-text stage are recorded.

### 2.6 Data collection process
<!-- PRISMA 10a, 10b -->

A standardised data-extraction form, piloted on [N] studies, was used by two reviewers independently. Discrepancies were resolved by discussion. Authors of included studies were contacted for [missing data].

### 2.7 Data items
<!-- PRISMA 10b -->

Variables extracted: study identifier, design, country, dates, population characteristics, intervention/exposure, comparator, outcome definitions, effect estimates with 95% CI, sample sizes, follow-up duration, funding source, conflicts of interest, and items needed for risk-of-bias assessment.

### 2.8 Risk-of-bias assessment
<!-- PRISMA 11 -->

Risk of bias in individual studies was assessed using **[RoB 2 for randomized trials / ROBINS-I for non-randomized intervention studies / QUADAS-2 for diagnostic accuracy / Newcastle-Ottawa for cohort/case-control]**. Two reviewers worked independently; differences were reconciled by discussion.

### 2.9 Effect measures
<!-- PRISMA 12 -->

For binary outcomes, effects were summarised as [risk ratio / odds ratio / hazard ratio]. For continuous outcomes, [mean difference / standardised mean difference]. For time-to-event outcomes, [hazard ratio with 95% CI].

### 2.10 Synthesis methods
<!-- PRISMA 13a-f -->
<!-- See references/statistical-reporting.md -->

When studies were sufficiently similar in population, intervention, comparator, outcome, and design, effects were pooled using **[random-effects / fixed-effect]** meta-analysis with [DerSimonian-Laird / REML / Hartung-Knapp] estimator. Heterogeneity was assessed using I², τ², and the 95% prediction interval.

Subgroup analyses were prespecified for [factors]. Sensitivity analyses included [excluding high-risk-of-bias studies; excluding small studies; alternative effect measure].

When pooling was not appropriate (high clinical heterogeneity, fewer than [3-5] studies, or methodological diversity), a structured qualitative synthesis was performed with effect estimates and CIs tabulated per study.

Analyses were performed in [R 4.x] using the `metafor` package version [x.x] [or `meta` / RevMan / Stata `meta`].

### 2.11 Reporting bias assessment
<!-- PRISMA 14 -->

When ≥ 10 studies were pooled, publication bias was assessed visually with funnel plots and statistically with Egger's test. Selective outcome reporting was assessed at the study level using protocol-versus-publication comparisons.

### 2.12 Certainty assessment
<!-- PRISMA 15 -->

Certainty of evidence for each primary and secondary outcome was rated using **GRADE** (high / moderate / low / very low), considering risk of bias, inconsistency, indirectness, imprecision, and publication bias. The summary of findings is presented in Table 3.

---

This systematic review and meta-analysis is reported in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA 2020) statement. A completed PRISMA 2020 checklist is provided as Supplementary File 2.

---

## 3. Results

### 3.1 Study selection
<!-- PRISMA 16a, 16b -->

The flow of studies through the review is shown in Figure 1. Of [N] records identified across databases and registers, [N] were screened after duplicate removal, [N] full-text reports were retrieved, and [N] studies (representing [N] reports) were included. [N] reports were excluded at the full-text stage with reasons listed in Supplementary File 3.

<!-- Build Figure 1 PRISMA 2020 flow diagram at https://enciclopedia.med.br/prisma2020 -->

### 3.2 Study characteristics
<!-- PRISMA 17 -->

Characteristics of the included studies are summarised in Table 1. Studies were conducted in [countries] between [start year] and [end year], and enrolled a total of [N] participants. [N] studies were [randomized trials / observational].

### 3.3 Risk of bias in studies
<!-- PRISMA 18 -->

The risk-of-bias assessment is shown in Figure 2 (or Table 2). [N] studies were judged at low risk of bias, [N] at some concerns, and [N] at high risk.

### 3.4 Results of individual studies
<!-- PRISMA 19 -->

Effect estimates with 95% CIs for each study are shown in the forest plot (Figure 3) and tabulated in Table 4.

### 3.5 Results of syntheses
<!-- PRISMA 20a-d -->

The pooled effect for the primary outcome was [point estimate] (95% CI, [low] to [high]; I² = [X]%; τ² = [X]; [N] studies; [N] participants).

[Subgroup analyses: in [subgroup], the effect was ... (interaction p = ...). In [subgroup], the effect was ... .]

### 3.6 Reporting biases
<!-- PRISMA 21 -->

[Funnel plot inspection; Egger test result; comments on small-study effects.]

### 3.7 Certainty of evidence
<!-- PRISMA 22 -->

Certainty of evidence was rated [high / moderate / low / very low] for the primary outcome, downgraded for [risk of bias / inconsistency / imprecision]. The full GRADE summary of findings is presented in Table 3.

---

## 4. Discussion
<!-- See references/discussion.md -->

### 4.1 Summary of evidence
<!-- PRISMA 23a -->

[Open with one sentence summarising the pooled effect with certainty: "[Intervention] [verb] [outcome] in [population], with [moderate / low] certainty."]

### 4.2 Comparison with prior reviews

[How the present synthesis differs from earlier reviews and what it adds.]

### 4.3 Limitations of the evidence
<!-- PRISMA 23b -->

[Risk of bias in the included studies; clinical heterogeneity; missing outcomes; limited geographic representation.]

### 4.4 Limitations of the review process
<!-- PRISMA 23c -->

[Search restricted to [languages]; possible missed grey literature; single-reviewer steps if any; data extraction errors.]

### 4.5 Implications
<!-- PRISMA 23d -->

[For practice: which patients does the evidence apply to, and what is the clinical recommendation?] [For policy: any implications for guidelines or coverage decisions.] [For future research: which design, population, sample size, and outcome would resolve the remaining uncertainty?]

---

## 5. Conclusions

[Concise statement of the main finding with effect direction, scope, and certainty. Match the abstract Conclusion.]

---

## Other information
<!-- PRISMA 24a-c -->

**Registration and protocol.** The review was registered in PROSPERO ([CRD420260000000]) on [date]. The protocol is available at [URL].

**Support.** [Funding source and role of funder].

**Competing interests.** [Per ICMJE Disclosure Form].

**Availability of data, code, and other materials.** [Statement; ideally GitHub / Zenodo with DOI for analysis code and a data-extraction CSV in the supplement.]

**AI disclosure.** [State any AI-tool use in writing or screening assistance.]

**Authors' contributions.** [Per CRediT.]

## References

[Vancouver-numbered, in order of first appearance.]

1. ...

## Tables and figure legends

**Table 1.** Characteristics of included studies.

**Table 2.** Risk-of-bias judgements per study and per domain.

**Table 3.** GRADE summary of findings for primary and secondary outcomes.

**Table 4.** Individual study effect estimates and pooled estimates.

**Figure 1.** PRISMA 2020 flow diagram of study selection. [Generated at https://enciclopedia.med.br/prisma2020.]

**Figure 2.** Risk-of-bias summary per study and per domain (RoB 2 / ROBINS-I).

**Figure 3.** Forest plot of [primary outcome] across included studies.

**Figure 4.** Funnel plot for [primary outcome] (only if ≥ 10 studies).

---

## Supplementary materials

- Supplementary File 1. Full search strategy for each database, with last search date.
- Supplementary File 2. Completed PRISMA 2020 checklist.
- Supplementary File 3. List of full-text reports excluded with reasons.
- Supplementary File 4. Risk-of-bias assessments per study.
- Supplementary File 5. GRADE evidence profiles per outcome.
- Supplementary File 6. Analysis code (R / Stata).

---

<!-- Pre-submission checklist (delete before submitting):
     [ ] PROSPERO registration ID in Abstract and Methods
     [ ] PRISMA 2020 flow diagram included (built at https://enciclopedia.med.br/prisma2020)
     [ ] PRISMA 2020 checklist completed and uploaded
     [ ] Full search strategies in supplementary file with last search date
     [ ] Two-reviewer screening, extraction, and risk-of-bias documented
     [ ] Risk-of-bias tool appropriate to design (RoB 2 / ROBINS-I / QUADAS-2 / Newcastle-Ottawa)
     [ ] GRADE certainty rating per primary and secondary outcome
     [ ] Heterogeneity reported with I², τ², and 95% prediction interval
     [ ] Publication bias assessed if ≥ 10 studies pooled
     [ ] Excluded full-text studies listed with reasons in supplement
     [ ] No em-dashes (—) in body sentences
     [ ] References real, in citation order
     [ ] Run references/common-mistakes.md speed audit
     [ ] Run references/paper-review.md formal checklist
-->

## See Also

- `references/systematic-review.md` — End-to-end workflow (protocol, searching, screening, extraction, RoB, synthesis, GRADE)
- `references/reporting-standards.md` — Full PRISMA 2020 27-item checklist with subitem detail
- `references/diagrams.md` — PRISMA 2020 flow diagram tool at https://enciclopedia.med.br/prisma2020 (preferred) plus PRISMA2020 R package fallback
- `references/pubmed-essentials.md` — MEDLINE search strategies, MeSH vs. free-text, Boolean operators, hedges
- `references/research-apis.md` — Crossref, OpenAlex, Europe PMC, NCBI E-utilities, OpenCitations for citation searches and grey literature
- `references/statistical-reporting.md` — Random- vs. fixed-effect meta-analysis, heterogeneity (I², τ², prediction interval), subgroup and sensitivity analyses
- `references/abstract.md` — Structured abstract for systematic reviews (Template C: Multiple Contributions)
- `references/introduction.md` — Three-paragraph Introduction that motivates the synthesis
- `references/related-work.md` — Positioning the review against prior syntheses
- `references/method.md` — Methods structure for systematic reviews (PRISMA-aligned subsections)
- `references/results.md` — Reporting selection, characteristics, RoB, syntheses, certainty
- `references/discussion.md` — Summary of evidence, evidence limitations vs. process limitations, implications
- `references/figures-and-tables.md` — Forest plot, funnel plot, RoB summary, GRADE summary of findings
- `references/ethics-and-integrity.md` — PROSPERO registration, AI disclosure, data and code availability
- `references/manuscript-conventions.md`, `references/citation-styles.md`
- `references/narrative-review.md` — When a narrative review or scoping review is more appropriate
- `references/study-types.md` — Choosing between SR, meta-analysis, scoping review, umbrella review
- `references/scientific-writing-principles.md`, `references/paragraph-flow.md`, `references/read-as-reader.md`
- `references/common-mistakes.md`, `references/paper-review.md`, `references/responding-to-reviewers.md`
