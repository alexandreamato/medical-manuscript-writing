# Study Types and Question Framing (Medical Research)

Match the question to the design, then the design to the reporting standard. The Methods section structure is largely determined by these choices.

## Question Frameworks

### PICO — Therapy / prevention questions

| Letter | Meaning |
| --- | --- |
| P | Population (who) |
| I | Intervention (what is given) |
| C | Comparator (vs. what) |
| O | Outcome (measured how) |

Example: In adults with type 2 diabetes (P), does once-weekly semaglutide (I) compared with placebo (C) reduce major adverse cardiovascular events at 2 years (O)?

### PECO — Etiology / harm questions

P-E-C-O replaces Intervention with Exposure. Used for cohort and case-control studies.

Example: In pregnant women (P), does exposure to fine particulate matter above 25 µg/m³ (E) compared with below 10 µg/m³ (C) increase the risk of preterm birth (O)?

### PIRD — Diagnostic accuracy questions

| Letter | Meaning |
| --- | --- |
| P | Population (suspected disease) |
| I | Index test |
| R | Reference standard |
| D | Diagnosis (target condition) |

Example: In adults presenting to the emergency department with chest pain (P), what is the diagnostic accuracy of high-sensitivity troponin T at presentation (I) compared with serial 6-hour troponin (R) for acute myocardial infarction (D)?

### PIRT — Prognostic questions (validation of a prognostic model)

| Letter | Meaning |
| --- | --- |
| P | Population at decision point |
| I | Index prognostic model or factor |
| R | Reference (existing model or no model) |
| T | Time horizon and outcome |

## Hierarchy of Evidence (Therapy Questions)

From highest to lowest internal validity for causal inference:

1. Systematic review of randomized controlled trials with low risk of bias.
2. Individual randomized controlled trial.
3. Pragmatic / cluster randomized trial.
4. Quasi-experimental designs (regression discontinuity, interrupted time series).
5. Prospective cohort with target trial emulation.
6. Cohort studies (prospective > retrospective).
7. Case-control studies.
8. Cross-sectional studies.
9. Case series and case reports.
10. Mechanistic and bench studies.
11. Expert opinion.

For etiology or rare-outcome questions, large prospective cohorts and case-control studies often outrank single trials. For diagnostic questions, prospective cross-sectional or cohort studies in representative populations are the gold standard.

## Design Choice — Common Types

### 1. Randomized controlled trial (parallel)

- Random allocation to intervention or comparator at the individual level.
- Allows causal inference if conducted with allocation concealment, blinding, ITT analysis, and adequate power.
- Reporting: CONSORT 2010.

### 2. Cluster randomized trial

- Randomization at the unit (clinic, ward, school).
- Required when the intervention is delivered at the cluster level or to avoid contamination.
- Sample-size calculation must inflate for the intracluster correlation coefficient (ICC).
- Reporting: CONSORT extension for cluster trials.

### 3. Crossover trial

- Each participant receives all interventions in randomized sequence with washout.
- Suited to chronic, stable conditions.
- Analysis must address period and carryover effects.

### 4. Noninferiority / equivalence trial

- Specific aim is to show a new intervention is not unacceptably worse than (or is similar to) an active comparator.
- Requires a prespecified noninferiority margin justified clinically.
- Both ITT and per-protocol analyses are typically reported.

### 5. Pragmatic trial

- Designed to inform real-world practice.
- Broad eligibility, usual-care comparator, routinely collected outcomes.
- Reporting: PRECIS-2 to characterize pragmatism plus CONSORT.

### 6. Adaptive trial

- Prespecified rules to modify the trial during conduct (sample size re-estimation, dropping arms, response-adaptive randomization).
- Reporting: ACE checklist (extension of CONSORT).

### 7. Prospective cohort

- Follow exposed and unexposed participants forward to ascertain outcomes.
- Strong for incidence and temporal sequence; vulnerable to confounding.
- Reporting: STROBE.

### 8. Retrospective cohort

- Cohorts assembled from existing records; outcomes ascertained from records.
- Faster and cheaper but vulnerable to information bias and missing covariates.
- Reporting: STROBE / RECORD.

### 9. Case-control

- Cases (with outcome) compared to matched or unmatched controls (without outcome) on prior exposure.
- Efficient for rare outcomes; vulnerable to recall and selection bias.
- Reporting: STROBE.

### 10. Cross-sectional

- Snapshot at one timepoint; estimates prevalence and associations.
- Cannot establish temporality.
- Reporting: STROBE.

### 11. Diagnostic accuracy

- Cross-sectional or cohort design comparing index test to reference standard.
- Reports sensitivity, specificity, predictive values, likelihood ratios, AUC.
- Reporting: STARD 2015.

### 12. Systematic review and meta-analysis

- Comprehensive synthesis of all studies meeting prespecified eligibility.
- Reporting: PRISMA 2020.

### 13. Individual participant data (IPD) meta-analysis

- Pooled re-analysis of raw data from each included study.
- Allows uniform definitions and subgroup analyses.
- Reporting: PRISMA-IPD.

### 14. Network meta-analysis

- Combines direct and indirect comparisons across multiple interventions.
- Requires assessment of transitivity and consistency.
- Reporting: PRISMA-NMA.

### 15. Mendelian randomization

- Uses genetic variants as instrumental variables for an exposure.
- Reporting: STROBE-MR.

### 16. Target trial emulation

- Frames an observational analysis as the trial that would have been run.
- Reduces immortal time bias and selection bias.
- Reporting: STROBE plus the target trial protocol.

### 17. Real-world evidence / registry studies

- Routinely collected health data with explicit attention to data provenance.
- Reporting: RECORD / RECORD-PE.

### 18. Case report and case series

- Single patient or small group with a notable clinical course.
- Reporting: CARE.

## Causal Language by Design

| Design | Permitted verbs |
| --- | --- |
| RCT (well-conducted) | "reduced", "increased", "did not change", "caused" (cautious) |
| Pragmatic / quasi-experimental | "reduced", "increased" with stated assumptions |
| Cohort / case-control / cross-sectional | "was associated with", "was not associated with" |
| Mendelian randomization (under assumptions) | "supports a causal effect of" / "does not support a causal effect of" |
| Diagnostic accuracy | "had a sensitivity of X% and a specificity of Y%" — do not say "diagnosed" |
| Prognostic model | "predicted", "discriminated"; not "caused" |

## See Also

1. **Reporting checklists matched to each design** (CONSORT, STROBE, PRISMA, STARD, CARE, TRIPOD): `references/reporting-standards.md`.
2. **Methods-section structure per design**: `references/method.md`.
3. **Statistical reporting per design** (e.g., proportional-hazards check for Cox; calibration plot for prediction models): `references/statistical-reporting.md`.

## Common Misalignments to Catch in Pre-Submission Review

1. Cohort study with causal claim in the Discussion; downgrade to associative.
2. RCT with subgroup conclusion not prespecified; mark as exploratory.
3. Cross-sectional study claiming temporality; remove or rephrase.
4. Diagnostic accuracy study reporting only sensitivity and specificity for a clinical-decision context that needs predictive values.
5. Single-center trial with a generalizability claim to "all patients" — rephrase to scope.
6. Systematic review with one missing reporting item (search dates, registration, risk-of-bias) — fix before submission.
