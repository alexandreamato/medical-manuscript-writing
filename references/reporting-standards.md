# Reporting Standards (Medical Research)

Match the manuscript to the right reporting checklist before drafting Methods and again before submission. Most journals require the completed checklist as a supplementary file.

The EQUATOR Network maintains the canonical list at https://www.equator-network.org/. The most commonly used standards in medical research are below.

## Quick Selector

| Study type | Reporting standard | What it covers |
| --- | --- | --- |
| Randomized controlled trial (parallel) | CONSORT 2025 (supersedes 2010) | Trial design, randomization, blinding, outcomes, analysis. |
| Randomized trial (crossover, cluster, factorial, pragmatic) | CONSORT extensions (use with the CONSORT 2025 core checklist until each extension is updated) | Design-specific items added to the core checklist. |
| Noninferiority or equivalence trial | CONSORT extension for noninferiority and equivalence trials (2012), with the CONSORT 2025 core checklist | Margin and its justification, analysis populations, interpretation against the margin. |
| Pilot or feasibility trial | CONSORT extension for pilot and feasibility trials | Feasibility outcomes, sample size justification. |
| Trial protocol | SPIRIT 2025 (supersedes 2013) | Protocol items required before trial starts. |
| Cohort, case-control, or cross-sectional observational | STROBE | Bias control, confounding, generalizability. |
| Routinely collected data / registries | RECORD (STROBE extension) | Database provenance, codes used, data linkage. |
| Pharmacoepidemiology | RECORD-PE | Treatment definition, exposure misclassification. |
| Systematic review and meta-analysis | PRISMA 2020 | Search, selection, risk of bias, synthesis, certainty. |
| Search strategy of any systematic review | PRISMA-S (with PRISMA 2020) | Every database, platform, date, limit and full search string, so the search can be rerun. |
| Systematic review of diagnostic test accuracy | PRISMA-DTA | Index test, reference standard, 2 × 2 data, accuracy synthesis, QUADAS-2 risk of bias. |
| Systematic review synthesised without meta-analysis | SWiM (with PRISMA 2020) | How studies were grouped, the standardised metric, the synthesis method, and its limits. |
| Scoping review | PRISMA-ScR (PRISMA extension, 2018) | Rationale for a scoping rather than a systematic review, protocol, sources and search, selection, charting of data, synthesis; appraisal of included studies is optional. |
| Systematic review protocol | PRISMA-P | Protocol items prior to the review. |
| Network meta-analysis | PRISMA-NMA | Comparison structure, ranking, assumptions. |
| Diagnostic accuracy study | STARD 2015 | Index test, reference standard, flow, accuracy estimates. |
| Prediction model, diagnostic or prognostic (development, validation, updating), regression or machine learning | TRIPOD+AI 2024 (supersedes TRIPOD 2015) | Data, predictors, model specification, calibration, discrimination, validation, fairness, availability. |
| Study using a large language model | TRIPOD-LLM 2025 | LLM version, prompts, task, evaluation, and the TRIPOD+AI items that apply. |
| Reliability or agreement study (inter-rater, test-retest) | GRRAS | Raters, subjects, sampling, the agreement or reliability statistic and its CI. |
| Animal preclinical study | ARRIVE 2.0 | Sample size, randomization, blinding, animal welfare. |
| Case report | CARE | Patient perspective, timeline, intervention, outcome. |
| Surgical case series | PROCESS 2025 (supersedes PROCESS 2020 and 2023) | Consecutive or not, setting, operator experience, intervention details, follow-up, outcomes, AI disclosure. |
| Case series (any specialty; no dedicated EQUATOR reporting guideline) | JBI checklist for case series (critical appraisal tool, used as a reporting reminder), with CARE for the per-patient detail | Inclusion criteria, standard measurement, consecutive and complete inclusion, demographics, clinical information, outcomes, site, statistics. |
| Narrative review | SANRA (a quality scale, not a reporting guideline) | Importance for readers, concrete aims, literature search, referencing, scientific reasoning, presentation of data. |
| Qualitative research | SRQR / COREQ | Sampling, data collection, analysis, reflexivity. |
| Mixed methods | MMR Reporting Standards | Integration of quantitative and qualitative components. |
| Quality improvement study | SQUIRE 2.0 | Local context, intervention iterations, mechanism. |
| Economic evaluation | CHEERS 2022 | Perspective, time horizon, costs, outcomes, sensitivity. |
| Surveys | CHERRIES (online surveys) | Recruitment, response rates, randomization of items. |
| Genetic association study | STREGA | Genotyping methods, population stratification. |
| Mendelian randomization | STROBE-MR | Assumptions, instruments, sensitivity. |
| AI / machine learning model in medicine | TRIPOD+AI (model development and validation) / CONSORT-AI (trials of an AI intervention) / SPIRIT-AI (their protocols) | Data, model, validation, performance, fairness. |
| Any design: statistical methods and results | SAMPL (alongside the design guideline) | How each analysis, estimate, CI and P value is described. |
| Any design with human participants or animals | SAGER (alongside the design guideline) | Sex and gender: how they were defined, collected, analysed, and reported. |

## CONSORT 2025: RCT (Full 30-Item Checklist)

CONSORT 2025 (published April 2025) **supersedes CONSORT 2010**, which its authors state should no longer be used. It keeps the two-group parallel trial as its reference design and consists of a 30-item checklist, a flow diagram, and an expanded checklist (appendix 2 of the statement) that lists the critical elements of each item. Use it together with the CONSORT 2025 Explanation and Elaboration paper.

**Transition.** Some journals' Instructions to Authors still link the 2010 checklist. Default to CONSORT 2025. Use the 2010 checklist only if the target journal explicitly asks for it; check the journal's current instructions before choosing.

**Extensions.** Until each extension is realigned with CONSORT 2025, keep using the current version of the relevant extension (cluster, crossover, non-inferiority/equivalence, pragmatic, multi-arm, pilot and feasibility, n-of-1, within-person, non-pharmacological treatments, outcomes, patient-reported outcomes, harms, abstracts, health equity, CONSORT-AI), alongside the CONSORT 2025 core checklist.

| Section / topic | Item | What to report |
| --- | --- | --- |
| **Title and abstract** | 1a | Identification as a randomised trial in the title. |
| | 1b | Structured summary of trial design, methods, results, and conclusions (see CONSORT for Abstracts). |
| **Open science**: Trial registration | 2 | Registry name, identifying number (with URL), and **date of registration**. |
| Protocol and SAP | 3 | Where the trial protocol **and statistical analysis plan** can be accessed. |
| Data sharing | 4 | Where and how de-identified individual participant data (with data dictionary), statistical code, and other materials can be accessed. *New.* |
| Funding and conflicts | 5a | Sources of funding and other support (e.g., drug supply); role of funders in design, conduct, analysis, and reporting. |
| | 5b | Financial and other conflicts of interest of the manuscript authors. *New.* |
| **Introduction**: Background | 6 | Scientific background and rationale. |
| Objectives | 7 | Specific objectives related to **benefits and harms**. |
| **Methods**: Patient and public involvement | 8 | Details of patient or public involvement in design, conduct, and reporting. *New.* |
| Trial design | 9 | Type of trial (parallel, crossover…), allocation ratio, and framework (superiority, equivalence, non-inferiority, exploratory). |
| Changes to protocol | 10 | Important changes after the trial commenced, including outcomes or analyses that were not prespecified, with reasons. |
| Trial setting | 11 | Settings (community, hospital) and locations (countries, sites). |
| Eligibility criteria | 12a | Eligibility criteria for participants. |
| | 12b | If applicable, eligibility criteria for sites and for individuals delivering the interventions (e.g., surgeons, physiotherapists). *New.* |
| Intervention and comparator | 13 | Intervention and comparator in enough detail to allow replication; where additional materials (e.g., intervention manual) can be accessed. |
| Outcomes | 14 | Prespecified primary and secondary outcomes, each with measurement variable, analysis metric (change from baseline, final value, time to event), method of aggregation (median, proportion), and time point. |
| Harms | 15 | How harms were defined and assessed (systematically, non-systematically). *New.* |
| Sample size | 16a | How sample size was determined, with all assumptions behind the calculation. |
| | 16b | Interim analyses and stopping guidelines. |
| Randomisation: Sequence generation | 17a | Who generated the random allocation sequence and the method used. |
| | 17b | Type of randomisation and any restriction (stratification, blocking, block size). |
| Allocation concealment | 18 | Mechanism used to implement the sequence (central computer/telephone; sequentially numbered, opaque, sealed containers) and steps to conceal it until assignment. |
| Implementation | 19 | Whether the personnel who enrolled and those who assigned participants had access to the allocation sequence. |
| Blinding | 20a | Who was blinded after assignment (participants, care providers, outcome assessors, data analysts). |
| | 20b | If blinded, how blinding was achieved and how similar the interventions were. |
| Statistical methods | 21a | Methods used to compare groups for primary and secondary outcomes, **including harms**. |
| | 21b | Who is included in each analysis (e.g., all randomised participants) and in which group. *New.* |
| | 21c | How missing data were handled. *New.* |
| | 21d | Methods for additional analyses (subgroup, sensitivity), distinguishing prespecified from post hoc. |
| **Results**: Participant flow (with diagram) | 22a | For each group, numbers randomly assigned, receiving the intended intervention, and analysed for the primary outcome. |
| | 22b | For each group, losses and exclusions after randomisation, with reasons. |
| Recruitment | 23a | Dates defining the periods of recruitment and of follow-up for benefits and harms. |
| | 23b | If relevant, why the trial ended or was stopped. |
| Intervention and comparator delivery | 24a | Intervention and comparator as actually administered (who delivered them, adherence, fidelity). *New.* |
| | 24b | Concomitant care received during the trial in each group. *New.* |
| Baseline data | 25 | Table of baseline demographic and clinical characteristics for each group. |
| Numbers analysed, outcomes, estimation | 26 | For each primary and secondary outcome, by group: number included in the analysis; number with available data at the outcome time point; result per group with effect size and precision (95% CI); for binary outcomes, both absolute and relative effect sizes. |
| Harms | 27 | All harms or unintended events in each group. |
| Ancillary analyses | 28 | Other analyses (subgroup, sensitivity), distinguishing prespecified from post hoc. |
| **Discussion**: Interpretation | 29 | Interpretation consistent with the results, balancing benefits and harms, considering other relevant evidence. |
| Limitations | 30 | Limitations: sources of potential bias, imprecision, **generalisability**, and, if relevant, multiplicity of analyses. |

Item wording above is abridged; submit the official checklist from https://www.consort-spirit.org with page or line numbers filled in.

### What changed from CONSORT 2010

1. **Seven new items:** data sharing (4), authors' conflicts of interest (5b), patient and public involvement (8), eligibility of sites and intervention deliverers (12b), harms assessment (15), analysis population and missing data (21b, 21c), and intervention delivery and concomitant care (24a, 24b).
2. **Three revised items:** protocol **and statistical analysis plan** access (3); changes after commencement now include non-prespecified outcomes and analyses (10); per-outcome numbers analysed and with available data at each time point (26).
3. **One deleted item:** generalisability no longer stands alone; it is folded into limitations (30).
4. **Integrated extensions:** CONSORT Harms (items 7, 15, 21a, 23a, 27), CONSORT Outcomes (14, 26), and Non-pharmacological Treatment/TIDieR (24).
5. **New "Open science" section** placed right after the abstract: registration, protocol/SAP, data sharing, funding and conflicts (items 2 to 5). In 2010 these sat at the end as "Other information" (items 23 to 25).
6. **Renumbering.** Every item from 2 onwards has a new number. Do not reuse 2010 item numbers in a 2025 checklist or in reviewer responses (e.g., the flow diagram moved from 2010 item 13 to 2025 item 22; baseline data from 15 to 25; limitations from 20 to 30).

The CONSORT 2025 flow diagram keeps the same four stages (enrolment, allocation, follow-up, analysis); see `references/diagrams.md` for the wording changes.

### Not every CONSORT item applies to every trial

CONSORT is a **minimum** set of items to report for a randomised trial (the statement's own wording): every applicable item must be reported, and nothing stops authors from reporting more. A few items only apply when something specific happened during the trial. An item that does not apply is still answered: say that it does not apply and why, in one line. Common items that may legitimately not apply:

1. **Item 10, changes to the trial after commencement.** If there were none, say so ("There were no changes to outcomes or analyses after the trial commenced").
2. **Item 12b, eligibility of sites and intervention deliverers.** Not applicable when the intervention is not delivered by selected personnel (e.g., a drug dispensed by pharmacy); say so.
3. **Item 16b, interim analyses.** Not applicable when no interim analysis was prespecified; say so.
4. **Item 23b, trial stopping.** Not applicable when the trial was not stopped early; say so.

Item 8 (patient and public involvement) is not optional: if there was none, say so.

When an item does not apply, write `Not applicable` in the checklist with a one-line reason rather than leaving it blank. Reviewers prefer an explicit "not applicable" over an unanswered field.

## SPIRIT 2025: Trial Protocols

SPIRIT 2025 (published April 2025) supersedes SPIRIT 2013. It has **34 minimum items**, a schedule-of-enrolment-interventions-and-assessments diagram (item 18, participant timeline), and an expanded checklist, and it was developed jointly with CONSORT 2025 so that protocol and report items use aligned wording.

Main changes from SPIRIT 2013:

1. **New items:** patient and public involvement (11); trial monitoring (29), replacing the former auditing item.
2. **New "Open science" section:** registration with date (4), access to protocol and statistical analysis plan (5), data-sharing plans (6), funding and conflicts of interest, now including steering-committee members (7a, 7b), and dissemination policy (8).
3. **Split items:** eligibility for participants vs. sites and personnel (14a, 14b); who is blinded vs. how (24a, 24b); analysis population vs. missing-data handling (27b, 27c).
4. **Harms and intervention detail** strengthened (items 10, 15a, 17, 27a), drawing on CONSORT Harms 2022 and TIDieR.
5. **Removed or merged:** the appendix items on informed-consent materials and biological specimens were deleted; access to data for investigators merged into data management (26); authorship and professional-writer policy merged into dissemination (8).

A protocol written to SPIRIT 2025 maps almost one-to-one onto the CONSORT 2025 report, so write the protocol's open-science, outcomes, harms, and analysis-population sections with the final report in mind.

## STROBE: Observational (Full 22-Item Checklist)

Single 22-item checklist with design-specific instructions for cohort, case-control, and cross-sectional studies. Items marked `*` should be reported separately for cases and controls (case-control studies) or for exposed and unexposed groups (cohort and cross-sectional studies).

| Section | Item | Recommendation |
| --- | --- | --- |
| **Title and abstract** | 1 | (a) Indicate the study's design with a commonly used term in the title or abstract. (b) Provide an informative and balanced abstract summary of what was done and what was found. |
| **Introduction**: Background / rationale | 2 | Explain the scientific background and rationale for the investigation. |
| **Introduction**: Objectives | 3 | State specific objectives, including any prespecified hypotheses. |
| **Methods**: Study design | 4 | Present key elements of study design early in the paper. |
| **Methods**: Setting | 5 | Describe the setting, locations, and relevant dates, including periods of recruitment, exposure, follow-up, and data collection. |
| **Methods**: Participants | 6 | (a) Cohort: eligibility, sources, methods of selection, methods of follow-up. Case-control: eligibility, sources, methods of case ascertainment and control selection; rationale for choice of cases and controls. Cross-sectional: eligibility, sources, methods of selection. (b) Matched studies: matching criteria; numbers of exposed and unexposed (cohort) or controls per case (case-control). |
| **Methods**: Variables | 7 | Clearly define all outcomes, exposures, predictors, potential confounders, and effect modifiers. Give diagnostic criteria, if applicable. |
| **Methods**: Data sources / measurement | 8\* | For each variable of interest, give sources of data and details of measurement methods. Describe comparability of assessment methods if more than one group. |
| **Methods**: Bias | 9 | Describe any efforts to address potential sources of bias (selection, information, confounding). |
| **Methods**: Study size | 10 | Explain how the study size was arrived at. |
| **Methods**: Quantitative variables | 11 | Explain how quantitative variables were handled. If applicable, describe which groupings were chosen and why. |
| **Methods**: Statistical methods | 12 | (a) All statistical methods, including those used to control for confounding. (b) Methods to examine subgroups and interactions. (c) How missing data were addressed. (d) Cohort: handling of loss to follow-up. Case-control: how matching was addressed. Cross-sectional: methods accounting for sampling strategy. (e) Any sensitivity analyses. |
| **Results**, Participants | 13\* | (a) Numbers at each stage, potentially eligible, examined, confirmed eligible, included, completing follow-up, analysed. (b) Reasons for non-participation at each stage. (c) Consider a flow diagram. |
| **Results**: Descriptive data | 14\* | (a) Characteristics of participants (demographic, clinical, social) and information on exposures and confounders. (b) Number of participants with missing data per variable. (c) Cohort: summarise follow-up time (average and total). |
| **Results**: Outcome data | 15\* | Cohort: numbers of outcome events or summary measures over time. Case-control: numbers in each exposure category, or summary measures of exposure. Cross-sectional: numbers of outcome events or summary measures. |
| **Results**: Main results | 16 | (a) Unadjusted **and**, if applicable, confounder-adjusted estimates with precision (e.g., 95% CI). State which confounders were adjusted for and why. (b) Category boundaries when continuous variables were categorized. (c) If relevant, translate relative risk into absolute risk for a meaningful time period. |
| **Results**, Other analyses | 17 | Other analyses, subgroups, interactions, sensitivity analyses. |
| **Discussion**: Key results | 18 | Summarise key results with reference to study objectives. |
| **Discussion**: Limitations | 19 | Discuss limitations, including sources of potential bias or imprecision. **Discuss both direction and magnitude of any potential bias.** |
| **Discussion**: Interpretation | 20 | Cautious overall interpretation considering objectives, limitations, multiplicity of analyses, results from similar studies, and other relevant evidence. |
| **Discussion**: Generalisability | 21 | Discuss the generalisability (external validity). |
| **Other information**: Funding | 22 | Source of funding and role of funders for the present study and, if applicable, for the original study on which the present article is based. |

`*` Report separately for cases and controls (case-control) or for exposed and unexposed (cohort, cross-sectional).

The STROBE flow diagram (Item 13) is recommended. Build it at https://enciclopedia.med.br/strobe (preferred: cohort, case-control, and cross-sectional templates with an arithmetic consistency check); a Mermaid fallback and the JSON format are in `references/diagrams.md`.

## PRISMA 2020: Systematic Reviews

The 27-item checklist plus the abstract checklist. Highest-value items:

1. Protocol and registration (PROSPERO ID).
2. Eligibility criteria: PICO/PECO + designs + dates.
3. Information sources: databases with last-search dates.
4. Search strategy: full strategy in supplement.
5. Selection process: number of reviewers, blinding, software (e.g., Rayyan, Covidence).
6. Data collection: items collected.
7. Risk-of-bias assessment: tool (RoB 2 / ROBINS-I / QUADAS-2 / Newcastle-Ottawa).
8. Effect measures.
9. Synthesis methods: pooled estimates, model, heterogeneity (`I²`, `τ²`), subgroups, sensitivity.
10. Reporting bias assessment: funnel plots, statistical tests for asymmetry.
11. Certainty of evidence: GRADE for each outcome.
12. PRISMA flow diagram.

## STARD 2015: Diagnostic Accuracy (Full 30-Item Checklist)

| Section | Item | Recommendation |
| --- | --- | --- |
| **Title or abstract** | 1 | Identification as a study of diagnostic accuracy using at least one measure of accuracy (sensitivity, specificity, predictive values, AUC). |
| **Abstract** | 2 | Structured summary of study design, methods, results, and conclusions (see STARD for Abstracts). |
| **Introduction** | 3 | Scientific and clinical background, including the **intended use** and **clinical role** of the index test. |
| | 4 | Study objectives and hypotheses. |
| **Methods: Study design** | 5 | Whether data collection was planned **before** the index test and reference standard were performed (prospective) or **after** (retrospective). |
| **Methods: Participants** | 6 | Eligibility criteria. |
| | 7 | On what basis potentially eligible participants were identified (symptoms, results from previous tests, registry inclusion). |
| | 8 | Where and when potentially eligible participants were identified (setting, location, dates). |
| | 9 | Whether participants formed a **consecutive, random, or convenience series**. |
| **Methods: Test methods** | 10a | Index test, in sufficient detail to allow replication. |
| | 10b | Reference standard, in sufficient detail to allow replication. |
| | 11 | Rationale for choosing the reference standard (if alternatives exist). |
| | 12a | Definition of and rationale for test positivity cut-offs or result categories of the **index test**, distinguishing prespecified from exploratory. |
| | 12b | Definition of and rationale for test positivity cut-offs or result categories of the **reference standard**, distinguishing prespecified from exploratory. |
| | 13a | Whether clinical information and reference standard results were available to performers / readers of the **index test**. |
| | 13b | Whether clinical information and index test results were available to assessors of the **reference standard**. |
| **Methods: Analysis** | 14 | Methods for estimating or comparing measures of diagnostic accuracy. |
| | 15 | How **indeterminate** index test or reference standard results were handled. |
| | 16 | How **missing data** on the index test and reference standard were handled. |
| | 17 | Any analyses of variability in diagnostic accuracy, distinguishing prespecified from exploratory. |
| | 18 | Intended sample size and how it was determined. |
| **Results: Participants** | 19 | Flow of participants, **using a diagram**. |
| | 20 | Baseline demographic and clinical characteristics of participants. |
| | 21a | Distribution of severity of disease in those **with** the target condition. |
| | 21b | Distribution of alternative diagnoses in those **without** the target condition. |
| | 22 | Time interval and any clinical interventions between index test and reference standard. |
| **Results: Test results** | 23 | **Cross-tabulation** of the index test results (or their distribution) by the results of the reference standard. |
| | 24 | Estimates of diagnostic accuracy and their precision (e.g., 95% CIs). |
| | 25 | Any adverse events from performing the index test or the reference standard. |
| **Discussion** | 26 | Study limitations, including sources of potential bias, statistical uncertainty, and generalisability. |
| | 27 | Implications for practice, including the intended use and clinical role of the index test. |
| **Other information** | 28 | Registration number and name of registry. |
| | 29 | Where the full study protocol can be accessed. |
| | 30 | Sources of funding and other support; role of funders. |

The STARD participant flow diagram (Item 19) is mandatory; a Mermaid template is in `references/diagrams.md`.

### STARD 2015: Concepts the Items Assume (from the Cohen et al. 2016 E&E paper)

These distinctions sit behind multiple items and are commonly missed:

1. **Intended use** of the test (Item 3): diagnosis, screening, staging, monitoring, surveillance, prognosis, treatment selection.
2. **Clinical role** of the test (Item 3): `triage` (used before an existing test; lower cost or burden; often less accurate; needs high sensitivity if rule-out), `add-on` (used after existing tests to improve total strategy accuracy by catching false positives or false negatives), or `replacement` of an existing test. The clinical role determines the *relative* importance of false positives vs. false negatives and therefore the targeted sensitivity and specificity.
3. **Single-gate vs. multiple-gate design** (Item 6).
   - **Single-gate (cohort) studies** apply one set of eligibility criteria to all participants (e.g., consecutive adults with suspected pulmonary embolism). Yields realistic estimates.
   - **Multiple-gate (case-control) studies** apply different eligibility criteria to those with vs. without the target condition (e.g., confirmed C. difficile cases vs. healthy controls). **Extreme contrasts between severe cases and healthy controls inflate accuracy estimates**: flag this limitation explicitly.
4. **Test description in three phases** (Item 10): describe the **pre-analytical** phase (patient preparation, sample handling, anatomic site), the **analytical** phase (materials, instruments, procedures), and the **post-analytical** phase (calculations, risk-score formulas). Include the **number, training, and expertise** of test readers (especially for imaging and cytology, where inter-reader variability is large).
5. **Prespecified vs. exploratory positivity thresholds** (Item 12). Prespecified thresholds may be based on (a) previous studies, (b) clinical practice, (c) clinical guidelines, or (d) the manufacturer's recommendation. **A threshold selected after the data have been examined to maximize accuracy will produce optimistic estimates that subsequent studies often cannot replicate.** Always declare whether thresholds were prespecified.
6. **Blinding (Item 13)**: STARD does not say blinding is desirable in every study; it requires that authors **report whether** clinical information was available to test readers and reference-standard assessors, so readers can interpret accuracy estimates accordingly.
7. **Indeterminate results** (Item 15): every diagnostic study has them. Report how they were handled (excluded, treated as positive, treated as negative, treated as missing, sensitivity-analysed in alternative ways).
8. **Spectrum bias** (Item 21): accuracy depends on the severity of disease in cases and the prevalence of alternative diagnoses in non-cases. Report distributions explicitly so readers can judge transportability.
9. **Adverse events** (Item 25): both the index test and the reference standard can cause harm (e.g., contrast reactions, biopsy bleeding). Report them.

### What to Report About Diagnostic Accuracy Estimates

For each accuracy measure (sensitivity, specificity, PPV, NPV, LR+, LR−, AUC, diagnostic OR), report the **point estimate with 95% CI** and the underlying **2 × 2 cross-tabulation** (Item 23). Predictive values depend on prevalence; report the prevalence in the studied population so readers can recompute predictive values for their own setting.

Comparing two index tests requires a prespecified comparison metric (relative sensitivity, absolute gain in sensitivity, relative diagnostic OR) matched to the clinical role. Report a paired-data analysis (e.g., McNemar's test for sensitivity and specificity differences) when both tests are applied to the same participants.

## TRIPOD+AI 2024: Prediction Models

TRIPOD+AI (published 2024) is the reporting guideline for studies that develop, validate or update a clinical prediction model, diagnostic or prognostic, whether the model uses regression or machine learning. It **supersedes TRIPOD 2015**, whose checklist its authors state should no longer be used; cite TRIPOD 2015 only as history. It has a 27-item checklist and a separate TRIPOD+AI for Abstracts checklist.

Key items beyond a standard observational report:

1. Source of data and dates; how the data were collected and prepared.
2. Participants: eligibility, setting, treatments received, and how the sample size was decided.
3. Outcome: definition, timing, and assessment blinded to predictors.
4. Predictors: definition, measurement, timing, and blinding to the outcome.
5. Missing data: extent and handling.
6. Model development: type of model, predictor selection, hyperparameter tuning, and internal validation (bootstrap or cross-validation).
7. Model performance: discrimination (C-statistic or AUC) and calibration (calibration plot, intercept, slope), with CIs; clinical utility (e.g., decision curve) when claimed.
8. Validation: internal and external, and how the validation data differ from the development data.
9. Fairness: performance in relevant subgroups (sex, age, ethnicity, setting).
10. Availability: the full model (formula, code, or tool) so others can apply and validate it; data and code sharing.

Reclassification statistics (NRI, IDI) are not substitutes for discrimination and calibration.

**Studies of large language models** (as a tool for prediction, text generation or summarisation) use **TRIPOD-LLM** (2025), which adds items on the LLM version, prompts and the evaluation task.

**Citations**

> Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378

> Gallifant J, Afshar M, Ameen S, Aphinyanaphongs Y, Chen S, Cacciamani G, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-9. doi:10.1038/s41591-024-03425-5

Historical: Collins GS, Reitsma JB, Altman DG, Moons KGM. Transparent reporting of a multivariable prediction model for individual prognosis or diagnosis (TRIPOD): the TRIPOD statement. BMJ. 2015;350:g7594. doi:10.1136/bmj.g7594

## Guidelines That Complement the Design Checklist

These are used together with the design guideline above, not instead of it.

### PRISMA-S: reporting the literature search

Use with PRISMA 2020 in every systematic review. Its 16 items make the search reproducible: each database and the platform used to search it, registries and other sources, the full search strategy for every database exactly as run, limits and filters, date of each search, peer review of the strategy, and deduplication. Put the complete strategies in a supplementary file.

> Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP, Moher D, Page MJ, et al. PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. Syst Rev. 2021;10(1):39. doi:10.1186/s13643-020-01542-z

### PRISMA-DTA: systematic reviews of diagnostic test accuracy

A stand-alone PRISMA extension for reviews whose question is how accurate a test is (the review-level counterpart of STARD). It adds items on the target condition, index test and reference standard, the 2 × 2 data extracted from each study, risk of bias and applicability (typically QUADAS-2), and the accuracy synthesis (e.g., bivariate or hierarchical models, summary sensitivity and specificity or summary ROC).

> McInnes MDF, Moher D, Thombs BD, McGrath TA, Bossuyt PM; the PRISMA-DTA Group. Preferred Reporting Items for a Systematic Review and Meta-analysis of Diagnostic Test Accuracy Studies: the PRISMA-DTA statement. JAMA. 2018;319(4):388-96. doi:10.1001/jama.2017.19163

### SWiM: synthesis without meta-analysis

When studies cannot be pooled (different outcomes or metrics, missing variance, too much clinical diversity), the synthesis still has to be reported as a method. SWiM's nine items cover how studies were grouped for synthesis, the standardised metric used, the synthesis method (e.g., vote counting based on direction of effect, combining P values, summarising effect estimates), criteria for prioritising results, investigation of heterogeneity, certainty of evidence, data presentation, and the limitations of the chosen method.

> Campbell M, McKenzie JE, Sowden A, Katikireddi SV, Brennan SE, Ellis S, et al. Synthesis without meta-analysis (SWiM) in systematic reviews: reporting guideline. BMJ. 2020;368:l6890. doi:10.1136/bmj.l6890

### GRRAS: reliability and agreement studies

For studies whose question is how consistently a measurement is made: inter-rater and intra-rater agreement, test-retest reliability (e.g., a new ultrasound measurement read by two vascular sonographers). It asks for the number and characteristics of raters and subjects and how they were sampled, the rating process and blinding, the statistic chosen (intraclass correlation with its model and type, kappa and its weighting, limits of agreement) with a CI, and why that statistic fits the question.

> Kottner J, Audigé L, Brorson S, Donner A, Gajewski BJ, Hróbjartsson A, et al. Guidelines for Reporting Reliability and Agreement Studies (GRRAS) were proposed. J Clin Epidemiol. 2011;64(1):96-106. doi:10.1016/j.jclinepi.2010.03.002

### SAMPL: basic statistical reporting

Statistical reporting guidance for any design: describe each analysis and the question it answers, report effect sizes with CIs rather than P values alone, give exact P values, state the assumptions checked, name the software. `references/statistical-reporting.md` follows it.

> Lang TA, Altman DG. Basic statistical reporting for articles published in biomedical journals: the "Statistical Analyses and Methods in the Published Literature" or the SAMPL Guidelines. Int J Nurs Stud. 2015;52(1):5-9. doi:10.1016/j.ijnurstu.2014.09.006

### SAGER: sex and gender

For any research with humans or animals: use "sex" and "gender" correctly, report how each was determined, report data disaggregated by sex (and gender where relevant), analyse sex or gender differences when appropriate, and discuss the implications of not doing so. Many journals now ask for a sex and gender statement.

> Heidari S, Babor TF, De Castro P, Tort S, Curno M. Sex and Gender Equity in Research: rationale for the SAGER guidelines and recommended use. Res Integr Peer Rev. 2016;1:2. doi:10.1186/s41073-016-0007-6

### PRISMA-ScR: scoping reviews

A scoping review maps the extent and nature of the evidence on a question (concepts, types of studies, gaps) rather than estimating an effect. PRISMA-ScR has 20 essential items and 2 optional ones; it differs from PRISMA 2020 chiefly in making critical appraisal optional and in asking how data were charted. Say in the title and Methods that the review is a scoping review, and why that design fits the question.

> Tricco AC, Lillie E, Zarin W, O'Brien KK, Colquhoun H, Levac D, et al. PRISMA Extension for Scoping Reviews (PRISMA-ScR): checklist and explanation. Ann Intern Med. 2018;169(7):467-73. doi:10.7326/M18-0850

### Case series: PROCESS and the JBI checklist

CARE is written for a single case. A series of patients needs more: how patients were selected (consecutive or not, and whether all eligible patients were included), how the condition and outcomes were measured, and follow-up.

1. **Surgical and interventional case series: PROCESS.** The current version is PROCESS 2025, which keeps the earlier checklist and adds items on the use of artificial intelligence. Check https://www.processguideline.com/ for the version current at submission. Unlike the 2020 and 2023 versions (International Journal of Surgery), the 2025 update was published in the Premier Journal of Science, a newer journal; cite the version the target journal names if it names one.

> Agha RA, Mathew G, Rashid R, Kerwan A, Al-Jabir A, Sohrabi C, et al. Revised Preferred Reporting of Case Series in Surgery (PROCESS) guideline: an update for the age of artificial intelligence. Premier J Sci. 2025;10:100080. doi:10.70389/PJS.100080

2. **Other case series: the JBI critical appraisal checklist for case series.** It is an appraisal tool, not a reporting guideline, but its ten questions (clear inclusion criteria; standard and reliable measurement of the condition; valid identification methods; consecutive inclusion; complete inclusion; demographics; clinical information; outcomes or follow-up; site or clinic demographics; appropriate statistics) are what a reviewer or a later systematic review will check, so report each of them.

> Munn Z, Barker TH, Moola S, Tufanaru C, Stern C, McArthur A, et al. Methodological quality of case series studies: an introduction to the JBI critical appraisal tool. JBI Evid Synth. 2020;18(10):2127-33. doi:10.11124/JBISRIR-D-19-00099

### SANRA: narrative reviews

Narrative reviews have no EQUATOR reporting guideline. SANRA is a six-item scale (each item scored 0 to 2) that editors and reviewers use to judge a narrative review, and authors can use it as a checklist while writing: justification of the article's importance for the readership, concrete aims or questions, description of the literature search, referencing, scientific reasoning, and appropriate presentation of data. See `references/narrative-review.md`.

> Baethge C, Goldbeck-Wood S, Mertens S. SANRA: a scale for the quality assessment of narrative review articles. Res Integr Peer Rev. 2019;4:5. doi:10.1186/s41073-019-0064-8

### Noninferiority and equivalence trials

Use the CONSORT extension together with the CONSORT 2025 core checklist; the analysis and interpretation rules are in `references/statistical-reporting.md` (Noninferiority and Equivalence Trials).

> Piaggio G, Elbourne DR, Pocock SJ, Evans SJW, Altman DG; CONSORT Group. Reporting of noninferiority and equivalence randomized trials: extension of the CONSORT 2010 statement. JAMA. 2012;308(24):2594-604. doi:10.1001/jama.2012.87802

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
This trial is reported in accordance with the Consolidated Standards of Reporting
Trials (CONSORT 2025) statement. A completed CONSORT 2025 checklist is provided as
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
Item 12a. Eligibility criteria for participants (CONSORT 2025).
Page 6, lines 112-125: "Participants were community-dwelling adults aged 60 to 85
years with mild cognitive impairment as defined by Petersen criteria. Exclusion
criteria included a dementia diagnosis, major psychiatric disorders, or unstable
medical conditions. Recruitment occurred at three memory clinics in Boston, MA,
between January 2024 and December 2025."
```

If an item is only partly applicable, say which part applies:

```
Item 20a. Blinding (CONSORT 2025).
Page 8, lines 156-160: open-label trial; participants and care providers were not
blinded because the comparator (no treatment) made blinding impossible. Outcome
assessors and data analysts were blinded to allocation.
```

If an item is not applicable, state why explicitly:

```
Item 23b. Why the trial ended or was stopped (CONSORT 2025).
Not applicable: the trial was completed as planned, with no early stopping.
```

### Cover letter mention

Most editors notice and appreciate a one-line mention in the cover letter:

```
The manuscript adheres to the [CONSORT 2025 / STROBE / PRISMA 2020 / STARD 2015 /
CARE 2013] reporting guideline. The completed checklist accompanies the
submission as Supplementary File 1.
```

## Cross-Standard Common Items

The design checklists for original research (CONSORT, STROBE, STARD, TRIPOD+AI, PRISMA) share these items; apply each one that fits the design (a case report, for example, has no participant flow or prespecified primary outcome, and CARE asks for a timeline instead):

1. The clinical question and study design are stated explicitly.
2. The participants, intervention/exposure, comparator, and outcome are defined.
3. The participant flow is shown in a diagram (required by CONSORT, PRISMA and STARD; recommended by STROBE). **Ready-to-use Mermaid templates and the PRISMA2020 R package workflow are in `references/diagrams.md`.**
4. The primary outcome is prespecified.
5. The statistical analysis plan is described.
6. Limitations and generalizability are discussed.
7. Funding and conflicts of interest are reported; ethics approval and registration are reported where the design requires them (`references/ethics-and-integrity.md`).
