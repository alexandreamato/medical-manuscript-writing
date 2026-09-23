# Statistical Reporting Checklist (Medical Research)

This is a focused checklist to keep statistical reporting calibrated. Apply it to the Methods and Results of any quantitative study. It follows the SAMPL guidelines for basic statistical reporting (`references/reporting-standards.md`, Guidelines That Complement the Design Checklist), which apply alongside the design checklist (CONSORT, STROBE, and so on).

## 0. Report What Was Done; Propose, Do Not Prescribe

This checklist is about **reporting** the analyses the authors actually ran, not about adding analyses to the manuscript.

1. **Report the method actually used**, as prespecified in the protocol or statistical analysis plan, or labelled as not prespecified.
2. **When a limitation exists, state it.** If there was no sensitivity analysis for unmeasured confounding, or no multiplicity adjustment, say so in the Methods or Limitations, and propose to the authors that they consider an analysis. The proposal goes to the authors, separately from the manuscript, under the Stopping Rule status `needs new analysis` (SKILL.md, Stopping Rule; the same statuses are in `paper-review.md`).
3. **Never turn an optional analysis into a universal requirement**, and never add an analysis, a number or a result to the manuscript without the authors. That would break SKILL.md Integrity Rule 3 (stay faithful to the data and the protocol).

Items that could be read as asking for an analysis carry one of three labels; unlabelled items describe how to report what was done (SAMPL):

- **REQUIRED**: asked for by the reporting guideline that applies (the item is cited). "Required" means the manuscript must *report* it; where the guideline item is conditional ("if done", "if applicable"), reporting that it was not done satisfies it.
- **RECOMMENDED**: a common expectation of methodologists, editors or regulators, with its source; its absence is a limitation to state, not an error to fix silently.
- **OPTIONAL**: context-dependent; one of several acceptable approaches.

Item numbers are CONSORT 2025, STROBE and PRISMA 2020 as listed in `references/reporting-standards.md`.

## 1. Effect Estimates and Uncertainty

1. REQUIRED (CONSORT 2025 item 26; STROBE item 16a): report a point estimate **with** its precision (usually the 95% confidence interval) for every primary and secondary outcome. Do not report a p value alone.
2. Match the precision of the CI to the point estimate.
3. For binary outcomes, report both **absolute** (risk difference, NNT) and **relative** (risk ratio, hazard ratio, odds ratio) measures: REQUIRED in trials (CONSORT 2025 item 26); RECOMMENDED in observational studies (STROBE item 16c, translating relative risk into absolute risk "if relevant").
4. Specify the direction: is the higher value better or worse?

Examples:

1. `The risk of the primary outcome was 8.4% (95% CI, 6.9 to 10.0) in the intervention group vs. 12.6% (95% CI, 10.8 to 14.6) in the control group, a risk difference of -4.2 percentage points (95% CI, -6.7 to -1.7) and a relative risk of 0.67 (95% CI, 0.53 to 0.84; p < 0.001).`

## 2. Hypothesis Tests and P Values

1. State the hypothesis test, the directionality (one- vs. two-sided), and the alpha level.
2. Report p values to two significant figures, except very small (`p < 0.001`) or borderline (`p = 0.054`).
3. Do not report `p = 0.000`. Use `p < 0.001`.
4. Do not interpret a non-significant p value as evidence of no effect; report the CI.
5. **Multiplicity.** Report what was done, and label it:
   - REQUIRED only when the protocol makes several **confirmatory** claims (several primary outcomes, each able to establish efficacy on its own, or secondary outcomes intended to support claims): report the prespecified method that controls the type I error (for example a hierarchical or gatekeeping procedure, Holm, Hochberg) as part of the statistical methods (CONSORT 2025 item 21a). Controlling the type I error for such claims is the regulatory expectation (FDA. Multiple Endpoints in Clinical Trials: Guidance for Industry. October 2022, section III.A; https://www.fda.gov/media/162416/download).
   - Accepted alternative for secondary and exploratory outcomes: report them as exploratory, without adjustment, and interpret them as hypothesis-generating. The same FDA guidance states that exploratory endpoints do not need multiplicity adjustment because they are generally not used to support conclusions (section III.A.2).
   - If several outcomes were tested with no adjustment and no exploratory label, state this among the limitations (CONSORT 2025 item 30: limitations, including multiplicity of analyses, if relevant) and propose a correction or relabelling to the authors; do not apply an adjustment yourself.

## 3. Sample Size Justification

1. State the assumed effect size and its source (prior trial, mechanism, minimal clinically important difference).
2. State alpha (typically 0.05 two-sided), power (typically 0.80 or 0.90).
3. State the calculation method (formula, simulation) and any inflation for dropout, clustering, or interim analyses.
4. State the achieved sample size and explain any deviation.

## 4. Analysis Population

1. RCT: define ITT, modified ITT (mITT), per-protocol; specify the population for the primary analysis.
2. Observational: define the analysis cohort and exclusions.
3. State the consequences of choice on the interpretation.

## 5. Models: Specification

State for each model:

1. Type (logistic regression, Cox proportional hazards, linear mixed model, generalized estimating equations, etc.).
2. Outcome and link function.
3. Covariates: confounders, prespecified vs. data-driven; interaction terms.
4. Random effects (for mixed models): unit and structure.
5. Stratification or matching variables.
6. Software with version and key packages.

## 6. Assumption Checks

1. **Cox proportional hazards:** test or visually assess proportional hazards (Schoenfeld residuals); report.
2. **Logistic regression:** check linearity of continuous predictors on the logit scale; check separation.
3. **Linear regression and mixed models:** check residual normality and homoscedasticity.
4. **Generalized estimating equations:** specify the working correlation structure.
5. State whether assumptions held and what was done if not.

## 7. Missing Data

1. Report the amount of missing data per variable.
2. State the assumed missingness mechanism (MCAR, MAR, MNAR) with justification.
3. State the handling: complete-case analysis, multiple imputation (number of imputations, predictors, software), inverse probability weighting.
4. RECOMMENDED: a sensitivity analysis under different plausible missing-data assumptions (in trials, ICH E9(R1) addendum on estimands and sensitivity analysis, 2019, section A.5.2.2: "the need for sensitivity analysis in respect of missing data is established"; https://database.ich.org/sites/default/files/E9-R1_Step4_Guideline_2019_1203.pdf). If not done, state it as a limitation.

Items 1 and 3 are REQUIRED in trials (CONSORT 2025 item 21c, how missing data were handled) and in observational studies (STROBE item 12c).

## 8. Heterogeneity (Meta-Analysis)

1. Report `I²`, `τ²`, and the prediction interval, not only the pooled estimate.
2. Describe prespecified subgroup analyses to explore heterogeneity.
3. Distinguish clinical heterogeneity (population, intervention, outcome differences) from statistical heterogeneity.

## 9. Reporting Bias

1. REQUIRED (PRISMA 2020 item 14): describe the methods used to assess risk of bias due to missing results. With any number of studies this includes registry searches, comparison of protocols and registry entries with publications, and a structured judgment such as ROB-ME (Page MJ, et al. BMJ. 2023;383:e076754. doi:10.1136/bmj-2023-076754).
2. Funnel plot (visual) and asymmetry tests (Egger, Peters, Harbord): only when a meta-analysis has at least 10 studies (Cochrane Handbook version 6.5, section 13.3.4.4). With fewer studies, say why they were not done.
3. Discuss small-study effects and selective outcome reporting in the discussion.

## 10. Diagnostic Accuracy

For STARD-compliant reporting:

1. Sensitivity, specificity, with 95% CIs.
2. Positive and negative predictive values, conditional on prevalence in the studied population.
3. Positive and negative likelihood ratios.
4. AUC with 95% CI.
5. Cross-tabulation of index test against reference standard.
6. Threshold rationale; if optimized post-hoc, clearly mark exploratory.

## 11. Survival Analysis

1. Median follow-up via reverse Kaplan-Meier.
2. Number at risk at each timepoint shown under the survival plot.
3. Hazard ratio with 95% CI for each comparison.
4. Test of proportional hazards.
5. Censoring assumption stated.

## 12. Subgroup Analyses

1. Prespecified subgroups listed in protocol.
2. Test of interaction (interaction p value), not just within-subgroup p values.
3. Forest plot showing effects across subgroups.
4. Multiplicity: most subgroup analyses are exploratory. Label them as such (REQUIRED: CONSORT 2025 item 21d and item 28, distinguishing prespecified from post hoc), and interpret them with caution; formal adjustment is needed only when a subgroup claim is confirmatory and prespecified (see §2, item 5).
5. Mark exploratory subgroups explicitly.

## 13. Confounding (Observational)

1. State how confounders were chosen (REQUIRED to report the methods used to control confounding: STROBE item 12a). Choosing them a priori from a directed acyclic graph (DAG) is RECOMMENDED practice; if selection was data-driven, say so.
2. State the adjustment strategy: regression adjustment, matching, propensity score (matching, weighting, stratification), instrumental variable.
3. When matching or weighting was used, report covariate balance (standardized mean differences) after matching or weighting (RECOMMENDED).
4. REQUIRED (STROBE item 16a): report unadjusted and, if applicable, confounder-adjusted estimates with their precision, and which confounders were adjusted for and why.
5. RECOMMENDED: address unmeasured (residual) confounding, at least in the Discussion; a quantitative sensitivity analysis is OPTIONAL and context-dependent. The E-value (VanderWeele TJ, Ding P. Ann Intern Med. 2017;167(4):268-274. doi:10.7326/M16-2607) is one option among several: negative-control outcomes or exposures, quantitative bias analysis with plausible confounder parameters, active-comparator or instrumental-variable designs. If none was done, state the limitation and propose one to the authors; STROBE item 12e asks only that sensitivity analyses be described if they were done.

## 14. Sensitivity Analyses

REQUIRED to describe the sensitivity analyses that were done (CONSORT 2025 item 21d; STROBE item 12e; PRISMA 2020 item 13f). Which ones to run is RECOMMENDED or OPTIONAL by context; common targets:

1. Missing-data assumption.
2. Analysis population (ITT vs. PP).
3. Model specification.
4. Outcome definition.
5. Inclusion criteria.

A sensitivity analysis that materially changes the conclusion must be discussed in the Discussion.

## 15. Software and Reproducibility

1. State software name and version (e.g., `R 4.3.1`, `SAS 9.4`, `Stata 18`).
2. List key packages with versions (e.g., `survival 3.5-7`, `lme4 1.1-35`).
3. Provide analysis code with the manuscript or in a public repository (Zenodo, GitHub).
4. Provide the prespecified statistical analysis plan as a supplement.

## See Also

1. **Statistical figures** (forest plot, Kaplan-Meier, funnel plot, ROC, calibration plot, generated from data, not text): `references/statistical-figures.md`.
2. **Tables of effect estimates and adverse events** (formatting, precision, footnotes): `references/figures-and-tables.md`.
3. **Causal language calibrated to the design**: `references/study-types.md`.
4. **Discussion treatment of statistical vs. clinical significance**: `references/discussion.md`.

## 16. Numbers Match Across the Manuscript

The general check is in `references/paper-review.md` (Cross-Section Consistency Checks). Statistical specifics:

1. Estimates and intervals in the text are the same as in the tables, with the same decimals.
2. The model that produced each estimate is the one described in the Methods.
3. Forest plots match tabulated effect estimates.
4. Sample sizes in the participant flow diagram match the Methods and the Results.

## 17. Noninferiority and Equivalence Trials

A noninferiority trial asks whether a new intervention is not worse than an active comparator by more than a prespecified margin; an equivalence trial asks whether the difference lies within a margin in both directions. Report with the CONSORT extension for noninferiority and equivalence trials together with the CONSORT 2025 core checklist.

1. **Margin.** State the margin, the scale it is on (risk difference, risk ratio, hazard ratio), and how it was chosen, before the trial started. Justify it both ways:
   - *statistically*, from the effect of the active comparator against placebo in earlier trials (conservatively estimated, for example from the bound of its CI nearer to no effect), so that "not worse by the margin" still means better than placebo;
   - *clinically*, as the largest loss of efficacy that the advantages of the new intervention (safety, cost, convenience) would justify.

   A margin chosen after seeing the data, or without justification, makes the conclusion uninterpretable.
2. **Sample size** is calculated from the margin, the expected true difference, the one-sided alpha, and the power.
3. **Interpretation against the margin.** Conclude noninferiority when the whole CI for the difference lies on the acceptable side of the margin. Say which interval was used: a two-sided 95% CI corresponds to a one-sided alpha of 0.025 (the usual standard); a one-sided 95% interval (alpha 0.05) is a weaker test and must be named as such. For equivalence, both ends of the interval must lie within the margins (two one-sided tests); state the confidence level used.
4. **Assay sensitivity and constancy.** A noninferiority result is meaningful only if the trial could have detected a difference: the comparator must be used at its proven dose, in a population, setting and outcome definition similar to the trials that established its effect (the constancy assumption). Discuss both.
5. **Analysis populations.** Report both the intention-to-treat and the per-protocol analyses, and say which is primary. In a superiority trial the intention-to-treat analysis is conservative; in a noninferiority trial it is not, because nonadherence and crossover make the groups look alike and favour a noninferiority conclusion. Noninferiority is convincing when both analyses agree.
6. **Wording of conclusions.**
   - CI entirely within the margin: "X was noninferior to Y (margin M)".
   - CI crosses the margin: "noninferiority was not shown", not "X was inferior", and not "X was as effective as Y".
   - CI excludes the margin on the harmful side: inferiority.
   - Testing superiority after noninferiority is shown is acceptable when prespecified; claiming noninferiority after a failed superiority trial is not, unless the margin was prespecified.
7. **Figure.** A plot of the point estimate and CI against the margin (and against zero) lets readers see the conclusion at once.

