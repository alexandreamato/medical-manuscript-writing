# Statistical Reporting Checklist (Medical Research)

This is a focused checklist to keep statistical reporting calibrated. Apply it to every Methods and Results section.

## 1. Effect Estimates and Uncertainty

1. Report a point estimate **with** its 95% confidence interval for every primary and secondary outcome. Do not report a p value alone.
2. Match the precision of the CI to the point estimate.
3. For risk-difference type outcomes, report both **absolute** (risk difference, NNT) and **relative** (risk ratio, hazard ratio, odds ratio) measures when appropriate.
4. Specify the direction: is the higher value better or worse?

Examples:

1. `The risk of the primary outcome was 8.4% (95% CI, 6.9 to 10.0) in the intervention group vs. 12.6% (95% CI, 10.8 to 14.6) in the control group, a risk difference of -4.2 percentage points (95% CI, -6.7 to -1.7) and a relative risk of 0.67 (95% CI, 0.53 to 0.84; p < 0.001).`

## 2. Hypothesis Tests and P Values

1. State the hypothesis test, the directionality (one- vs. two-sided), and the alpha level.
2. Report p values to two significant figures, except very small (`p < 0.001`) or borderline (`p = 0.054`).
3. Do not report `p = 0.000`. Use `p < 0.001`.
4. Do not interpret a non-significant p value as evidence of no effect; report the CI.
5. Adjust for multiplicity when multiple primary or secondary outcomes are tested. State the adjustment method.

## 3. Sample Size Justification

1. State the assumed effect size and its source (prior trial, mechanism, minimal clinically important difference).
2. State alpha (typically 0.05 two-sided), power (typically 0.80 or 0.90).
3. State the calculation method (formula, simulation) and any inflation for dropout, clustering, or interim analyses.
4. State the achieved sample size and explain any deviation.

## 4. Analysis Population

1. RCT: define ITT, modified ITT (mITT), per-protocol; specify the population for the primary analysis.
2. Observational: define the analysis cohort and exclusions.
3. State the consequences of choice on the interpretation.

## 5. Models — Specification

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
4. Compare results across handling methods as a sensitivity analysis.

## 8. Heterogeneity (Meta-Analysis)

1. Report `I²`, `τ²`, and the prediction interval, not only the pooled estimate.
2. Describe prespecified subgroup analyses to explore heterogeneity.
3. Distinguish clinical heterogeneity (population, intervention, outcome differences) from statistical heterogeneity.

## 9. Reporting Bias

1. Visual assessment with funnel plot (when ≥10 studies).
2. Statistical test (Egger, Peters) when appropriate.
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
4. Adjustment for multiplicity if many subgroups.
5. Mark exploratory subgroups explicitly.

## 13. Confounding (Observational)

1. Identify potential confounders a priori from a directed acyclic graph (DAG).
2. State the adjustment strategy: regression adjustment, matching, propensity score (matching, weighting, stratification), instrumental variable.
3. Provide a covariate balance metric (standardized mean difference for matching/weighting).
4. Report unadjusted and adjusted estimates.
5. Estimate residual confounding (E-value) for the primary observational result.

## 14. Sensitivity Analyses

State and report sensitivity to:

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

1. **Statistical figures** (forest plot, Kaplan-Meier, funnel plot, ROC, calibration plot — generated from data, not text): `references/diagrams.md`.
2. **Tables of effect estimates and adverse events** (formatting, precision, footnotes): `references/figures-and-tables.md`.
3. **Causal language calibrated to the design**: `references/study-types.md`.
4. **Discussion treatment of statistical vs. clinical significance**: `references/discussion.md`.

## 16. Numbers Match Across the Manuscript

Run this final check:

1. Numbers in the Abstract match the Results.
2. Numbers in tables match numbers in the body text.
3. Forest plots match tabulated effect estimates.
4. Sample sizes in the participant flow diagram match the Methods and the Results.
