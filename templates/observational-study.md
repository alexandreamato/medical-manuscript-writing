<!-- TEMPLATE: Observational study manuscript (STROBE aligned) -->
<!-- Use for cohort, case-control, or cross-sectional studies. Replace text in [BRACKETS]. -->
<!-- Inline comments like "<!-- STROBE 5 -->" point to the STROBE checklist item. -->
<!-- See references/reporting-standards.md for the full STROBE 22-item checklist. -->

# [Title: include the study design (e.g., "A prospective cohort study of ..."); name the population, exposure, and outcome]
<!-- STROBE 1a -->

**Short running title:** [≤ 40 characters]

## Authors

[First M. Last]^1^, [First M. Last]^2^

1. [Affiliation, City, Country]. ORCID: [xxxx-xxxx-xxxx-xxxx]
2. [Affiliation, City, Country]. ORCID: [xxxx-xxxx-xxxx-xxxx]

**Corresponding author:** [First M. Last], [Address], [Email]

## Manuscript metadata

- **Word counts:** Abstract [N], Body [N], References [N]
- **Tables:** [N] (Table 1 baseline characteristics; Table 2 outcomes; Table 3 sensitivity analyses)
- **Figures:** [N] (Figure 1 STROBE participant flow; Figure 2 [Kaplan-Meier or main result])
- **Funding:** [Source, role of funder]
- **Conflicts of interest:** [Per ICMJE Disclosure Form]

---

## Abstract
<!-- STROBE 1b — structured -->
<!-- See references/abstract.md -->

**Background.** [Clinical importance and the unresolved question.]

**Methods.** [Design: prospective/retrospective cohort, case-control, or cross-sectional]. [Setting and period]. [Source population, eligibility, methods of selection]. [Exposure definition and ascertainment]. [Primary outcome definition and ascertainment]. [Confounders adjusted for]. [Statistical model].

**Results.** [Of N eligible, N were included]. [Median follow-up X years]. [Main result: adjusted [HR/OR/RR] with 95% CI]. [Robustness: E-value or sensitivity analysis].

**Conclusions.** [One sentence stated as association, not causation, with scope and the next research step.]

---

## 1. Introduction
<!-- STROBE 2 (background/rationale), 3 (objectives) -->
<!-- See references/introduction.md -->

[Paragraph 1 — clinical importance and burden.]

[Paragraph 2 — what is known and the gap.]

[Paragraph 3 — present study aim and hypothesis.] We aimed to estimate the association between [exposure] and [outcome] in [population] using [design and data source]. <!-- STROBE 3 -->

---

## 2. Methods
<!-- See references/method.md -->

### 2.1 Study design
<!-- STROBE 4 -->

[Prospective cohort / retrospective cohort / case-control / cross-sectional]. [If a target trial emulation, state the target trial protocol explicitly.]

### 2.2 Setting
<!-- STROBE 5 -->

[The study used data from [registry / cohort / institution] for the period [start date] to [end date]]. [Recruitment, exposure assessment, follow-up, and outcome ascertainment dates].

### 2.3 Participants
<!-- STROBE 6a, 6b -->

**Eligibility.** [Inclusion criteria]; [exclusion criteria].

**Cohort:** [Sources of participants; methods of selection; methods of follow-up; methods of matching if applicable; numbers of exposed and unexposed at baseline].

**Case-control:** [Eligibility for cases and controls; methods of case ascertainment and control selection; rationale for choice; matching criteria; controls per case].

**Cross-sectional:** [Eligibility; methods of selection].

### 2.4 Variables
<!-- STROBE 7 -->

**Outcome.** [Operational definition; instrument or code (ICD-10/SNOMED); ascertainment method; blinding of ascertainer if any; date of definition].

**Exposure.** [Operational definition; instrument or code (ATC for drugs); duration; intensity; lag period].

**Confounders.** [Listed a priori from a directed acyclic graph (DAG): variable 1, variable 2, ...]. **Effect modifiers.** [List].

### 2.5 Data sources and measurement
<!-- STROBE 8 -->

[Source 1: e.g., electronic health record system; data extraction date]. [Source 2: e.g., national death registry; record linkage method]. [Validation of measurement instruments].

### 2.6 Bias
<!-- STROBE 9 -->

[Selection bias: how addressed (e.g., consecutive enrolment, inverse-probability weighting)]. [Information bias: blinding, validation studies, masking]. [Confounding: covariate adjustment, propensity score, instrumental variable, target-trial-emulation framework].

### 2.7 Study size
<!-- STROBE 10 -->

[Sample size determined by [available cohort / a priori calculation]. For an a priori calculation, state assumed effect size, alpha, power.]

### 2.8 Quantitative variables
<!-- STROBE 11 -->

[Continuous variables were [kept continuous in the model / categorised into groups]. Rationale for categorisation: [clinical convention / prespecified clinical thresholds].]

### 2.9 Statistical methods
<!-- STROBE 12a-12e -->
<!-- See references/statistical-reporting.md -->

The primary analysis used [Cox proportional-hazards / logistic regression / linear regression / GEE / mixed-effects model] adjusted for [confounders]. The proportional-hazards assumption was verified using Schoenfeld residuals. <!-- if Cox -->

Subgroup analyses were prespecified for [factors] with interaction p values reported. Missing data on [variables] were handled by [multiple imputation under MAR / complete-case]; the assumed mechanism was [MAR/MCAR/MNAR]. Sensitivity analyses included [E-value calculation; alternative outcome definition; alternative confounder set; matched-pair vs. unmatched analyses].

Analyses were performed in [R 4.x / SAS 9.4 / Stata 18] using [packages with versions]. A two-sided p < 0.05 was considered statistically significant.

### 2.10 Ethics
<!-- See references/ethics-and-integrity.md -->

The study was approved by [IRB / ethics committee] (protocol [number]). [Consent obtained / waiver granted because [reason: registry-based, deceased participants, deidentified data]].

---

This study is reported in accordance with the Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement. A completed STROBE checklist is provided as Supplementary File 1.

---

## 3. Results
<!-- See references/results.md -->

### 3.1 Participant flow
<!-- STROBE 13a, 13b, 13c -->

[Of [N] potentially eligible participants, [N] were excluded ([reason 1: n], [reason 2: n], [reason 3: n]), leaving [N] in the analytical cohort]. The flow is shown in Figure 1.

<!-- Build Figure 1 STROBE flow at references/diagrams.md (Mermaid template) -->

### 3.2 Baseline characteristics
<!-- STROBE 14a, 14b, 14c -->

Characteristics of the analytical cohort, by exposure status, are shown in Table 1. [For matched/weighted observational studies, report standardised mean differences rather than p values.]

### 3.3 Outcome data
<!-- STROBE 15 -->

[Cohort: number of outcome events; total person-years; incidence rates per group]. [Case-control: distribution of exposure across cases and controls]. [Cross-sectional: prevalence by exposure].

### 3.4 Main results
<!-- STROBE 16a, 16b, 16c -->

Unadjusted [effect measure] for [exposure] vs. [outcome] was [estimate] (95% CI). After adjustment for [confounders], the [effect measure] was [estimate] (95% CI; p = [value]; Table 2). [Translate relative effects into absolute terms for a meaningful time period if relevant].

### 3.5 Other analyses
<!-- STROBE 17 -->

[Subgroup analyses; sensitivity analyses; E-value]. [Mark exploratory analyses explicitly.]

---

## 4. Discussion
<!-- See references/discussion.md -->

### 4.1 Key results
<!-- STROBE 18 -->

[Open with one sentence summarising the main result. Use associative language ("X was associated with Y"), not causal, unless the design supports causal inference.]

### 4.2 Limitations
<!-- STROBE 19 -->

[Discuss limitations explicitly with both **direction and magnitude** of potential bias: residual confounding, measurement error, selection, missing data]. [E-value provides a quantitative bound on residual confounding.]

### 4.3 Interpretation
<!-- STROBE 20 -->

[Cautious interpretation considering objectives, limitations, multiplicity, prior similar studies, and other relevant evidence. Discuss possible mechanisms.]

### 4.4 Generalisability
<!-- STROBE 21 -->

[External validity. Which patients, settings, and eras do the results apply to? Single-centre vs. multi-centre. Era of treatment.]

---

## 5. Conclusions

[The exposure was associated with [direction] [outcome] in [population]. Confirmation in [specific design — RCT or quasi-experimental] is the appropriate next step before clinical recommendations.]

---

## Other information
<!-- STROBE 22 -->

**Funding:** [Source, role]. **Conflicts of interest:** [Per ICMJE]. **Data sharing:** [Statement]. **AI disclosure:** [Statement]. **CRediT contributions:** [Per author].

## References

[Vancouver-numbered, in order of first appearance.]

1. ...

## Tables and figure legends

**Table 1.** Baseline characteristics of the analytical cohort by [exposure status].

**Table 2.** Crude and adjusted association between [exposure] and [outcome].

**Figure 1.** STROBE participant flow diagram.

---

## Supplementary materials

- Supplementary File 1. Completed STROBE checklist.
- Supplementary File 2. Code list (ICD-10, ATC, SNOMED) used to define exposure, outcome, and confounders.
- Supplementary File 3. Sensitivity-analysis results.
- Supplementary File 4. Analysis code (R / SAS / Stata).

---

<!-- Pre-submission checklist (delete before submitting):
     [ ] Causal verbs avoided in body and conclusion (use "was associated with")
     [ ] STROBE flow diagram included
     [ ] STROBE checklist completed and uploaded
     [ ] DAG provided in supplementary file
     [ ] E-value or equivalent residual-confounding sensitivity reported
     [ ] No em-dashes (—) in body sentences
     [ ] Numbers in Abstract match Results exactly
     [ ] Run references/common-mistakes.md speed audit
     [ ] Run references/paper-review.md formal checklist
-->

## See Also

- `references/method.md` — Methods structure for observational studies (STROBE-aligned subsections)
- `references/results.md` — participant flow, baseline characteristics, main results
- `references/discussion.md` — limitations with direction and magnitude of bias
- `references/abstract.md` — structured abstract for observational studies
- `references/introduction.md` — three-part Introduction with aim/hypothesis
- `references/reporting-standards.md` — full STROBE 22-item checklist with cohort / case-control / cross-sectional variants
- `references/study-types.md` — design selection and causal language by design
- `references/statistical-reporting.md` — Cox / logistic / mixed models, missing data, sensitivity analyses
- `references/manuscript-conventions.md`, `references/citation-styles.md`, `references/figures-and-tables.md`
- `references/diagrams.md` — STROBE participant flow diagram (Mermaid template)
- `references/ethics-and-integrity.md` — IRB, consent, registration, AI disclosure
- `references/scientific-writing-principles.md`, `references/paragraph-flow.md`, `references/read-as-reader.md`
- `references/common-mistakes.md`, `references/paper-review.md`, `references/responding-to-reviewers.md`
