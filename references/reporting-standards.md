# Reporting Standards (Medical Research)

Match the manuscript to the right reporting checklist before drafting Methods and again before submission. Most journals require the completed checklist as a supplementary file.

The EQUATOR Network maintains the canonical list at https://www.equator-network.org/. The most commonly used standards in medical research are below.

## Quick Selector

| Study type | Reporting standard | What it covers |
| --- | --- | --- |
| Randomized controlled trial (parallel) | CONSORT 2010 | Trial design, randomization, blinding, outcomes, analysis. |
| Randomized trial (crossover, cluster, factorial, pragmatic, noninferiority) | CONSORT extensions | Design-specific items added to the core checklist. |
| Pilot or feasibility trial | CONSORT extension for pilot and feasibility trials | Feasibility outcomes, sample size justification. |
| Trial protocol | SPIRIT 2013 | Protocol items required before trial starts. |
| Cohort, case-control, or cross-sectional observational | STROBE | Bias control, confounding, generalizability. |
| Routinely collected data / registries | RECORD (STROBE extension) | Database provenance, codes used, data linkage. |
| Pharmacoepidemiology | RECORD-PE | Treatment definition, exposure misclassification. |
| Systematic review and meta-analysis | PRISMA 2020 | Search, selection, risk of bias, synthesis, certainty. |
| Systematic review protocol | PRISMA-P | Protocol items prior to the review. |
| Network meta-analysis | PRISMA-NMA | Comparison structure, ranking, assumptions. |
| Diagnostic accuracy study | STARD 2015 | Index test, reference standard, flow, accuracy estimates. |
| Diagnostic prediction model (development / validation) | TRIPOD 2015 / TRIPOD+AI 2024 | Predictors, model specification, calibration, discrimination, validation. |
| Prognostic model | TRIPOD | As above. |
| Animal preclinical study | ARRIVE 2.0 | Sample size, randomization, blinding, animal welfare. |
| Case report | CARE | Patient perspective, timeline, intervention, outcome. |
| Qualitative research | SRQR / COREQ | Sampling, data collection, analysis, reflexivity. |
| Mixed methods | MMR Reporting Standards | Integration of quantitative and qualitative components. |
| Quality improvement study | SQUIRE 2.0 | Local context, intervention iterations, mechanism. |
| Economic evaluation | CHEERS 2022 | Perspective, time horizon, costs, outcomes, sensitivity. |
| Surveys | CHERRIES (online surveys) | Recruitment, response rates, randomization of items. |
| Genetic association study | STREGA | Genotyping methods, population stratification. |
| Mendelian randomization | STROBE-MR | Assumptions, instruments, sensitivity. |
| AI / machine learning model in medicine | TRIPOD+AI / CONSORT-AI / SPIRIT-AI | Data, model, validation, performance, fairness. |

## CONSORT 2010 — RCT (key items, abridged)

1. Title and abstract identified as randomized.
2. Background and objectives.
3. Trial design (parallel / crossover / etc.) including allocation ratio.
4. Participants — eligibility and settings.
5. Interventions — sufficient detail to replicate.
6. Outcomes — primary and secondary, prespecified.
7. Sample size determination.
8. Randomization — sequence generation, allocation concealment, implementation.
9. Blinding of participants, clinicians, assessors, analysts.
10. Statistical methods.
11. Participant flow (CONSORT diagram).
12. Recruitment and follow-up dates.
13. Baseline characteristics by group.
14. Numbers analyzed for each outcome.
15. Outcomes and estimation (effect size, CI).
16. Ancillary analyses (subgroup, sensitivity).
17. Adverse events.
18. Limitations, generalizability, interpretation.
19. Registration, protocol availability, funding.

### CONSORT 25-item checklist organized by manuscript section (Falci & Marques 2015)

Most authors find it easier to navigate the CONSORT 25 items grouped into the six manuscript sections they correspond to:

| Section | Key CONSORT items |
| --- | --- |
| **1. Title and abstract** | Title contains the word "randomized"; structured abstract reports trial design, methods, main results, conclusions. |
| **2. Introduction** | Brief literature review; rationale for the trial; objective or hypothesis stated clearly. |
| **3. Methods** | Trial design; eligibility criteria with rationale; how and where data were collected; intervention described in enough detail to replicate; sample size calculation; **changes during the course of the trial** with reasons; allocation method; participant and assessor blinding; statistical analysis. |
| **4. Results** | Primary outcome per group; participant numbers, losses, and exclusions per group with reasons; post-intervention assessment and follow-up periods; statistical results for primary and secondary outcomes (e.g., 95% CI). |
| **5. Discussion** | Trial limitations including sources of bias, imprecision, and methodological weaknesses; external validity; applicability and interpretation consistent with the results, balancing benefits and harms in the context of other published evidence. |
| **6. Other information** | RCT registration number; full trial protocol availability; sources of funding and other support; role of the funders. |

The CONSORT 2010 statement also requires the **participant flow diagram** (enrollment → allocation → follow-up → analysis) — see `references/diagrams.md` for a ready-to-use Mermaid template.

### Not every CONSORT item applies to every trial

CONSORT items are an upper bound, not a floor. Some items only apply when something specific happened during the trial. Common items that may legitimately not apply (state explicitly when they do not):

1. **Item 3b — Changes to methods after trial commencement.** Skip if no changes were made.
2. **Item 6b — Changes to outcomes after trial commencement.** Skip if no changes.
3. **Item 7b — Interim analyses.** Skip if no interim analysis was prespecified.
4. **Item 14b — Trial stopping.** Skip if the trial was not stopped early.

When an item does not apply, write `Not applicable` in the checklist with a one-line reason rather than leaving it blank. Reviewers prefer an explicit "not applicable" over an unanswered field.

## STROBE — Observational (Full 22-Item Checklist)

Single 22-item checklist with design-specific instructions for cohort, case-control, and cross-sectional studies. Items marked `*` should be reported separately for cases and controls (case-control studies) or for exposed and unexposed groups (cohort and cross-sectional studies).

| Section | Item | Recommendation |
| --- | --- | --- |
| **Title and abstract** | 1 | (a) Indicate the study's design with a commonly used term in the title or abstract. (b) Provide an informative and balanced abstract summary of what was done and what was found. |
| **Introduction** — Background / rationale | 2 | Explain the scientific background and rationale for the investigation. |
| **Introduction** — Objectives | 3 | State specific objectives, including any prespecified hypotheses. |
| **Methods** — Study design | 4 | Present key elements of study design early in the paper. |
| **Methods** — Setting | 5 | Describe the setting, locations, and relevant dates, including periods of recruitment, exposure, follow-up, and data collection. |
| **Methods** — Participants | 6 | (a) Cohort: eligibility, sources, methods of selection, methods of follow-up. Case-control: eligibility, sources, methods of case ascertainment and control selection; rationale for choice of cases and controls. Cross-sectional: eligibility, sources, methods of selection. (b) Matched studies: matching criteria; numbers of exposed and unexposed (cohort) or controls per case (case-control). |
| **Methods** — Variables | 7 | Clearly define all outcomes, exposures, predictors, potential confounders, and effect modifiers. Give diagnostic criteria, if applicable. |
| **Methods** — Data sources / measurement | 8\* | For each variable of interest, give sources of data and details of measurement methods. Describe comparability of assessment methods if more than one group. |
| **Methods** — Bias | 9 | Describe any efforts to address potential sources of bias (selection, information, confounding). |
| **Methods** — Study size | 10 | Explain how the study size was arrived at. |
| **Methods** — Quantitative variables | 11 | Explain how quantitative variables were handled. If applicable, describe which groupings were chosen and why. |
| **Methods** — Statistical methods | 12 | (a) All statistical methods, including those used to control for confounding. (b) Methods to examine subgroups and interactions. (c) How missing data were addressed. (d) Cohort: handling of loss to follow-up. Case-control: how matching was addressed. Cross-sectional: methods accounting for sampling strategy. (e) Any sensitivity analyses. |
| **Results** — Participants | 13\* | (a) Numbers at each stage — potentially eligible, examined, confirmed eligible, included, completing follow-up, analysed. (b) Reasons for non-participation at each stage. (c) Consider a flow diagram. |
| **Results** — Descriptive data | 14\* | (a) Characteristics of participants (demographic, clinical, social) and information on exposures and confounders. (b) Number of participants with missing data per variable. (c) Cohort: summarise follow-up time (average and total). |
| **Results** — Outcome data | 15\* | Cohort: numbers of outcome events or summary measures over time. Case-control: numbers in each exposure category, or summary measures of exposure. Cross-sectional: numbers of outcome events or summary measures. |
| **Results** — Main results | 16 | (a) Unadjusted **and**, if applicable, confounder-adjusted estimates with precision (e.g., 95% CI). State which confounders were adjusted for and why. (b) Category boundaries when continuous variables were categorized. (c) If relevant, translate relative risk into absolute risk for a meaningful time period. |
| **Results** — Other analyses | 17 | Other analyses — subgroups, interactions, sensitivity analyses. |
| **Discussion** — Key results | 18 | Summarise key results with reference to study objectives. |
| **Discussion** — Limitations | 19 | Discuss limitations, including sources of potential bias or imprecision. **Discuss both direction and magnitude of any potential bias.** |
| **Discussion** — Interpretation | 20 | Cautious overall interpretation considering objectives, limitations, multiplicity of analyses, results from similar studies, and other relevant evidence. |
| **Discussion** — Generalisability | 21 | Discuss the generalisability (external validity). |
| **Other information** — Funding | 22 | Source of funding and role of funders for the present study and, if applicable, for the original study on which the present article is based. |

`*` Report separately for cases and controls (case-control) or for exposed and unexposed (cohort, cross-sectional).

The STROBE flow diagram (Item 13) is recommended; a Mermaid template is in `references/diagrams.md`.

## PRISMA 2020 — Systematic Reviews

The 27-item checklist plus the abstract checklist. Highest-value items:

1. Protocol and registration (PROSPERO ID).
2. Eligibility criteria — PICO/PECO + designs + dates.
3. Information sources — databases with last-search dates.
4. Search strategy — full strategy in supplement.
5. Selection process — number of reviewers, blinding, software (e.g., Rayyan, Covidence).
6. Data collection — items collected.
7. Risk-of-bias assessment — tool (RoB 2 / ROBINS-I / QUADAS-2 / Newcastle-Ottawa).
8. Effect measures.
9. Synthesis methods — pooled estimates, model, heterogeneity (`I²`, `τ²`), subgroups, sensitivity.
10. Reporting bias assessment — funnel plots, statistical tests for asymmetry.
11. Certainty of evidence — GRADE for each outcome.
12. PRISMA flow diagram.

## STARD 2015 — Diagnostic Accuracy (Full 30-Item Checklist)

| Section | Item | Recommendation |
| --- | --- | --- |
| **Title or abstract** | 1 | Identification as a study of diagnostic accuracy using at least one measure of accuracy (sensitivity, specificity, predictive values, AUC). |
| **Abstract** | 2 | Structured summary of study design, methods, results, and conclusions (see STARD for Abstracts). |
| **Introduction** | 3 | Scientific and clinical background, including the **intended use** and **clinical role** of the index test. |
| | 4 | Study objectives and hypotheses. |
| **Methods — Study design** | 5 | Whether data collection was planned **before** the index test and reference standard were performed (prospective) or **after** (retrospective). |
| **Methods — Participants** | 6 | Eligibility criteria. |
| | 7 | On what basis potentially eligible participants were identified (symptoms, results from previous tests, registry inclusion). |
| | 8 | Where and when potentially eligible participants were identified (setting, location, dates). |
| | 9 | Whether participants formed a **consecutive, random, or convenience series**. |
| **Methods — Test methods** | 10a | Index test, in sufficient detail to allow replication. |
| | 10b | Reference standard, in sufficient detail to allow replication. |
| | 11 | Rationale for choosing the reference standard (if alternatives exist). |
| | 12a | Definition of and rationale for test positivity cut-offs or result categories of the **index test**, distinguishing prespecified from exploratory. |
| | 12b | Definition of and rationale for test positivity cut-offs or result categories of the **reference standard**, distinguishing prespecified from exploratory. |
| | 13a | Whether clinical information and reference standard results were available to performers / readers of the **index test**. |
| | 13b | Whether clinical information and index test results were available to assessors of the **reference standard**. |
| **Methods — Analysis** | 14 | Methods for estimating or comparing measures of diagnostic accuracy. |
| | 15 | How **indeterminate** index test or reference standard results were handled. |
| | 16 | How **missing data** on the index test and reference standard were handled. |
| | 17 | Any analyses of variability in diagnostic accuracy, distinguishing prespecified from exploratory. |
| | 18 | Intended sample size and how it was determined. |
| **Results — Participants** | 19 | Flow of participants, **using a diagram**. |
| | 20 | Baseline demographic and clinical characteristics of participants. |
| | 21a | Distribution of severity of disease in those **with** the target condition. |
| | 21b | Distribution of alternative diagnoses in those **without** the target condition. |
| | 22 | Time interval and any clinical interventions between index test and reference standard. |
| **Results — Test results** | 23 | **Cross-tabulation** of the index test results (or their distribution) by the results of the reference standard. |
| | 24 | Estimates of diagnostic accuracy and their precision (e.g., 95% CIs). |
| | 25 | Any adverse events from performing the index test or the reference standard. |
| **Discussion** | 26 | Study limitations, including sources of potential bias, statistical uncertainty, and generalisability. |
| | 27 | Implications for practice, including the intended use and clinical role of the index test. |
| **Other information** | 28 | Registration number and name of registry. |
| | 29 | Where the full study protocol can be accessed. |
| | 30 | Sources of funding and other support; role of funders. |

The STARD participant flow diagram (Item 19) is mandatory; a Mermaid template is in `references/diagrams.md`.

### STARD 2015 — Concepts the Items Assume (from the Cohen et al. 2016 E&E paper)

These distinctions sit behind multiple items and are commonly missed:

1. **Intended use** of the test (Item 3) — diagnosis, screening, staging, monitoring, surveillance, prognosis, treatment selection.
2. **Clinical role** of the test (Item 3) — `triage` (used before an existing test; lower cost or burden; often less accurate; needs high sensitivity if rule-out), `add-on` (used after existing tests to improve total strategy accuracy by catching false positives or false negatives), or `replacement` of an existing test. The clinical role determines the *relative* importance of false positives vs. false negatives and therefore the targeted sensitivity and specificity.
3. **Single-gate vs. multiple-gate design** (Item 6).
   - **Single-gate (cohort) studies** apply one set of eligibility criteria to all participants (e.g., consecutive adults with suspected pulmonary embolism). Yields realistic estimates.
   - **Multiple-gate (case-control) studies** apply different eligibility criteria to those with vs. without the target condition (e.g., confirmed C. difficile cases vs. healthy controls). **Extreme contrasts between severe cases and healthy controls inflate accuracy estimates** — flag this limitation explicitly.
4. **Test description in three phases** (Item 10) — describe the **pre-analytical** phase (patient preparation, sample handling, anatomic site), the **analytical** phase (materials, instruments, procedures), and the **post-analytical** phase (calculations, risk-score formulas). Include the **number, training, and expertise** of test readers (especially for imaging and cytology, where inter-reader variability is large).
5. **Prespecified vs. exploratory positivity thresholds** (Item 12). Prespecified thresholds may be based on (a) previous studies, (b) clinical practice, (c) clinical guidelines, or (d) the manufacturer's recommendation. **A threshold selected after the data have been examined to maximize accuracy will produce optimistic estimates that subsequent studies often cannot replicate.** Always declare whether thresholds were prespecified.
6. **Blinding (Item 13)** — STARD does not say blinding is desirable in every study; it requires that authors **report whether** clinical information was available to test readers and reference-standard assessors, so readers can interpret accuracy estimates accordingly.
7. **Indeterminate results** (Item 15) — every diagnostic study has them. Report how they were handled (excluded, treated as positive, treated as negative, treated as missing, sensitivity-analysed in alternative ways).
8. **Spectrum bias** (Item 21) — accuracy depends on the severity of disease in cases and the prevalence of alternative diagnoses in non-cases. Report distributions explicitly so readers can judge transportability.
9. **Adverse events** (Item 25) — both the index test and the reference standard can cause harm (e.g., contrast reactions, biopsy bleeding). Report them.

### What to Report About Diagnostic Accuracy Estimates

For each accuracy measure (sensitivity, specificity, PPV, NPV, LR+, LR−, AUC, diagnostic OR), report the **point estimate with 95% CI** and the underlying **2 × 2 cross-tabulation** (Item 23). Predictive values depend on prevalence; report the prevalence in the studied population so readers can recompute predictive values for their own setting.

Comparing two index tests requires a prespecified comparison metric (relative sensitivity, absolute gain in sensitivity, relative diagnostic OR) matched to the clinical role. Report a paired-data analysis (e.g., McNemar's test for sensitivity and specificity differences) when both tests are applied to the same participants.

## TRIPOD 2015 / TRIPOD+AI 2024 — Prediction Models

Key items beyond standard:

1. Source of data and dates.
2. Participants — eligibility, treatment, sample size.
3. Outcome definition and assessment, blinded to predictors.
4. Predictors — type, measurement.
5. Missing data — extent and handling.
6. Model development — selection, complexity, internal validation method.
7. Model performance — discrimination (C-statistic), calibration (intercept, slope, plot), reclassification (NRI/IDI).
8. Internal and external validation.
9. Algorithm fairness (TRIPOD+AI) — performance across subgroups.
10. Availability of the model (formula, code, web tool).

## How to Use a Reporting Checklist

1. Open the checklist before drafting Methods. Use it to structure the section.
2. After drafting, fill in the page or paragraph number for each item.
3. If an item is not applicable, state why; do not leave it blank.
4. Submit the completed checklist as a supplementary file.
5. During revision, re-verify each item; reviewers will spot omissions and demand them.

### Adherence statement in Methods

Most major medical journals expect or require a statement of adherence inside the Methods section. Add one short sentence naming the guideline and pointing to the supplementary checklist file.

Examples (copy and adapt):

```
This study is reported in accordance with the Consolidated Standards of Reporting
Trials (CONSORT) statement. A completed CONSORT checklist is provided as
Supplementary File 1.
```

```
This observational study is reported in accordance with the Strengthening the
Reporting of Observational Studies in Epidemiology (STROBE) statement. A completed
STROBE checklist is provided as Supplementary File 1.
```

```
This systematic review and meta-analysis is reported in accordance with the
Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA 2020)
statement. The protocol was registered in PROSPERO (CRD420260000000). A completed
PRISMA 2020 checklist is provided as Supplementary File 1.
```

```
This case report is reported in accordance with the CARE (CAse REport) guideline.
A completed CARE checklist is provided as Supplementary File 1.
```

### Checklist completion template (with page or line numbers)

Most journals expect the supplementary checklist to point to where each item is addressed in the manuscript. Use page numbers if the journal uses page numbering; line numbers if continuous line numbering is required (most do).

Example checklist entry:

```
Item 7. Eligibility criteria for participants and the settings and locations
where the data were collected.
Page 6, lines 112-125: "Participants were community-dwelling adults aged 60 to 85
years with mild cognitive impairment as defined by Petersen criteria. Exclusion
criteria included a dementia diagnosis, major psychiatric disorders, or unstable
medical conditions. Recruitment occurred at three memory clinics in Boston, MA,
between January 2024 and December 2025."
```

If an item is not applicable, state why explicitly:

```
Item 14. Blinding.
Not applicable: this was an open-label trial because the comparator (no treatment)
made blinding impossible. Outcome assessors were blinded to allocation; see
Methods, page 8, lines 156-160.
```

### Cover letter mention

Most editors notice and appreciate a one-line mention in the cover letter:

```
The manuscript adheres to the [CONSORT 2010 / STROBE / PRISMA 2020 / STARD 2015 /
CARE 2013] reporting guideline. The completed checklist accompanies the
submission as Supplementary File 1.
```

## Cross-Standard Common Items

Every checklist agrees on these. They are non-negotiable:

1. The clinical question and study design are stated explicitly.
2. The participants, intervention/exposure, comparator, and outcome are defined.
3. The participant flow is shown in a diagram. **Ready-to-use Mermaid templates and the PRISMA2020 R package workflow are in `references/diagrams.md`.**
4. The primary outcome is prespecified.
5. The statistical analysis plan is described.
6. Limitations and generalizability are discussed.
7. Funding, conflicts of interest, registration, and ethics approval are reported.
