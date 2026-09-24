# Glossary

Short definitions of statistical, methodological, and reporting terms used throughout this skill. For deeper coverage, follow the cross-reference at the end of each entry.

## A

**Absolute risk reduction (ARR).** The arithmetic difference in event rates between two groups (control rate − intervention rate). Complement of relative risk reduction. Source for `references/statistical-reporting.md`.

**Adjudication.** Independent verification of an outcome event by a committee blinded to treatment assignment. Standard in RCTs and event-driven cohorts. See `references/method.md`.

**Adverse event (AE).** Any untoward medical occurrence in a participant during a study; not necessarily caused by the intervention. **Serious adverse event (SAE):** results in death, hospitalization, persistent disability, or congenital anomaly.

**AIC / BIC.** Akaike / Bayesian Information Criterion: model-selection metrics that balance fit against complexity. Lower is better.

**Allocation concealment.** Mechanism (central or web-based randomization service; sequentially numbered, opaque, sealed envelopes) preventing those enrolling participants from foreseeing the upcoming assignment. Distinct from **sequence generation** (how the random list was made) and from blinding (who knows the assignment after it is made). Open lists, unsealed or translucent envelopes and deterministic rules such as alternation cannot conceal. In one meta-epidemiological study, odds ratios were exaggerated by 41% with inadequate and 30% with unclear concealment (Schulz KF, et al. JAMA. 1995;273(5):408-12). See `references/systematic-review.md` (Step 6).

**AMSTAR 2.** A MeaSurement Tool to Assess systematic Reviews, version 2 (2017): critical appraisal tool for systematic reviews of randomized and non-randomized studies (Shea BJ, et al. BMJ. 2017;358:j4008; https://amstar.ca/Amstar-2.php; checked 2026-09-23).

**Analysis population.** The set of participants included in an analysis: ITT (intention-to-treat), mITT (modified ITT), per-protocol (PP), as-treated. See `references/statistical-reporting.md`.

**ARRIVE.** Animal Research: Reporting of In Vivo Experiments: reporting standard for animal studies. Current version: ARRIVE 2.0.

**AUC.** Area Under the receiver-operating-characteristic Curve. Summary measure of diagnostic discrimination; 0.5 = chance, 1.0 = perfect.

## B

**Bias.** Systematic error producing results that differ from the truth. Major types in clinical research: selection, information / measurement, confounding, attrition, reporting.

**Bland-Altman plot.** Method-comparison plot showing the difference between two measurements against their mean. Reports mean bias and 95% limits of agreement.

**Blinding (masking).** Withholding allocation information from one or more parties: participants, clinicians, outcome assessors, analysts.

## C

**CARE.** CAse REport: reporting standard for case reports (CARE 2013, 13 items).

**CHEERS.** Consolidated Health Economic Evaluation Reporting Standards (CHEERS 2022).

**Cluster randomized trial.** Trial that randomizes groups (clusters: clinics, schools, wards) rather than individuals. Sample size must inflate for the intracluster correlation coefficient (ICC).

**Confidence interval (CI).** Range of values that, under repeated sampling, would contain the true parameter at a stated frequency (commonly 95%). Use 95% CI as the default for medical reporting.

**Confounding.** A third variable causally related to both the exposure and the outcome that distorts their observed association. Adjustment, matching, weighting, or instrumental variables can reduce, not eliminate, measured confounding.

**CONSORT.** Consolidated Standards of Reporting Trials: reporting standard for randomized trials (CONSORT 2025, 30 items + flow diagram; supersedes CONSORT 2010, 25 items).

**Cox proportional-hazards model.** Regression for time-to-event data assuming a proportional hazards relationship. Yields hazard ratios with 95% CI. Verify the assumption with Schoenfeld residuals.

**CRediT.** Contributor Roles Taxonomy: 14 standardized author-contribution categories (Conceptualization, Methodology, Software, Validation, etc.).

## D

**DAG.** Directed Acyclic Graph: visual representation of causal assumptions used to identify which variables to adjust for. Tool: DAGitty (https://www.dagitty.net).

**DOI.** Digital Object Identifier: permanent string uniquely identifying a digital publication. Format: `doi:10.xxxx/xxxxx`.

## E

**E-value.** Sensitivity-analysis metric quantifying the minimum strength of association an unmeasured confounder would need with both exposure and outcome to fully explain away an observed effect (VanderWeele & Ding 2017). Higher values indicate more robust observational findings.

**Effect size.** Magnitude of a difference or association: hazard ratio (HR), odds ratio (OR), relative risk (RR), risk difference (RD), mean difference (MD), standardized mean difference (SMD), Cohen's d.

**Eligibility criteria.** Inclusion and exclusion criteria defining who can join the study.

**eLocator (article number).** Identifier replacing page numbers in some online-only journals (e.g., `e0225770` in *PLoS ONE*).

**EQUATOR Network.** Enhancing the QUAlity And Transparency Of health Research: central library of reporting guidelines (https://www.equator-network.org).

## F

**Fixed-effect / random-effects model.** Two meta-analysis approaches: fixed-effect assumes one true underlying effect; random-effects assumes a distribution of effects. Random-effects is the default in clinical meta-analysis.

**Forest plot.** Standard meta-analysis figure showing each study's effect estimate with 95% CI, the pooled estimate, and heterogeneity statistics (I², τ²).

**Funnel plot.** Plot of effect size versus precision (or standard error). Asymmetry indicates small-study effects, of which publication bias is one possible cause. Asymmetry tests need at least 10 studies (Cochrane Handbook version 6.5, section 13.3.4.4), and with fewer the plot is descriptive only; other checks for missing evidence (registry searches, protocol-publication comparison, ROB-ME) apply with any number of studies.

## G

**GRADE.** Grading of Recommendations Assessment, Development and Evaluation: system for rating certainty of evidence per outcome (high / moderate / low / very low) and strength of recommendations. Guidance: the GRADE Handbook (https://book.gradepro.org) and the GRADE Working Group (https://www.gradeworkinggroup.org/; checked 2026-09-23).

**Grey literature.** Conference abstracts, theses, government reports, industry data not appearing in peer-reviewed journals. Including grey literature is recommended in systematic reviews to mitigate publication bias.

## H

**Hazard ratio (HR).** Ratio of instantaneous event rates between two groups in time-to-event analysis.

**Heterogeneity.** Variation in effect estimates across studies in a meta-analysis. Statistical: I², τ², prediction interval. Clinical: differences in population, intervention, outcome.

## I

**ICC.** Intracluster Correlation Coefficient: measure of similarity within clusters in cluster RCTs; used in sample-size calculations.

**ICMJE.** International Committee of Medical Journal Editors. Sets the Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals (https://www.icmje.org).

**Imputation.** Methods to handle missing data: complete-case analysis, mean substitution, single imputation, **multiple imputation** (preferred when MAR is assumed).

**IMRaD.** Introduction, Methods, Results, and Discussion: the standard structure of original research articles. Variants: IMRAD with separate Conclusion, IaMRDC (with explicit aim and conclusion), Combined Results-Discussion.

**Index test.** The diagnostic test under evaluation in a STARD-style accuracy study, contrasted with the **reference standard**.

**Indeterminate result.** A test result that cannot be classified as positive or negative. STARD requires reporting how indeterminate results were handled.

**IPD meta-analysis.** Individual Participant Data meta-analysis: pooled re-analysis of the raw data from each included study, allowing harmonized variable definitions and more flexible analyses.

**ITT (Intention-to-treat).** Analysis principle: every randomized participant is analysed according to the assigned group, regardless of adherence or treatment received. Default primary analysis in RCTs.

## K

**Kaplan-Meier curve.** Non-parametric estimate of survival probability over time. Show with at-risk numbers under the plot, censoring marks, hazard ratio with 95% CI, and log-rank p value.

**Kappa (κ).** Cohen's kappa: measure of inter-rater agreement adjusted for chance. Values: < 0.40 poor, 0.40 to 0.59 fair, 0.60 to 0.79 good, ≥ 0.80 excellent.

## L

**Likelihood ratio (LR+, LR−).** Ratios summarizing how a test result changes the pre-test to post-test probability of disease. LR+ > 10 and LR− < 0.1 are clinically useful.

**Loss to follow-up.** Participants who do not complete the study. Differential loss between arms biases results.

## M

**MAR / MCAR / MNAR.** Missing-data mechanisms: Missing At Random (depends on observed variables only), Missing Completely At Random (independent of observed and unobserved), Missing Not At Random (depends on unobserved values).

**Mendelian randomization.** Use of genetic variants as instrumental variables for an exposure to estimate causal effects under stated assumptions.

**MeSH.** Medical Subject Headings: NLM-controlled vocabulary for indexing biomedical literature in PubMed.

**MID / MCID.** Minimal (Clinically) Important Difference: smallest change in an outcome that patients perceive as meaningful. Used to interpret whether a statistically significant effect is clinically meaningful.

**Multiple imputation.** Statistical technique generating several plausible imputed datasets, analysed separately and combined using Rubin's rules. Default for MAR missingness.

**Multiplicity.** The problem of inflated false-positive rate when multiple hypotheses are tested. Control via prespecified primary outcome, gatekeeping procedures, Bonferroni / Holm / Hochberg adjustments.

## N

**NLM Catalog.** US National Library of Medicine catalogue of journals indexed in PubMed, with the **NLM Title Abbreviation** required by Vancouver and AMA citation styles (https://www.ncbi.nlm.nih.gov/nlmcatalog/journals).

**NMA.** Network meta-analysis: meta-analytic technique combining direct and indirect comparisons across multiple interventions.

**NNT.** Number Needed to Treat: number of patients who must be treated for one additional good outcome. NNT = 1 / ARR. Companion: **NNH** (Number Needed to Harm).

**Non-inferiority margin.** Prespecified threshold below which a new intervention is considered not unacceptably worse than the comparator. Must be clinically justified.

## O

**Odds ratio (OR).** Ratio of odds of an event between two groups. Approximates RR when the outcome is rare; otherwise diverges.

**ORCID.** Open Researcher and Contributor ID: persistent unique identifier for researchers (https://orcid.org).

## P

**PECO.** Population, Exposure, Comparator, Outcome: question framework for etiology questions in observational studies.

**Per-protocol (PP) analysis.** Analysis restricted to participants who adhered to the assigned intervention. Reported as a sensitivity analysis alongside ITT.

**PICO.** Population, Intervention, Comparator, Outcome: question framework for therapy and prevention questions.

**PIRD.** Population, Index test, Reference standard, Diagnosis: question framework for diagnostic accuracy questions.

**PMID.** PubMed Identifier: unique number for a record in PubMed.

**POEM / DOE.** Patient-Oriented Evidence that Matters (mortality, morbidity, function, quality of life) vs. Disease-Oriented Evidence (lab values, surrogate markers). Prefer POEM-based recommendations.

**Power.** Probability of detecting an effect of a given size if it truly exists. Conventional target: 80% or 90% at α = 0.05 (two-sided).

**PPV / NPV.** Positive / Negative Predictive Value: probability that a positive (negative) test result reflects true disease (no disease). Depend on prevalence in the studied population.

**Prediction interval.** Range expected to contain the true effect in a future similar study; complementary to the confidence interval in random-effects meta-analysis.

**Preregistration.** Public registration of the study protocol before data collection (ClinicalTrials.gov, ISRCTN, PROSPERO) reduces reporting bias.

**PRISMA.** Preferred Reporting Items for Systematic Reviews and Meta-Analyses: current version PRISMA 2020 (27 items + flow diagram).

**PROBAST.** Prediction model Risk Of Bias ASsessment Tool (2019; Wolff RF, et al. Ann Intern Med. 2019;170(1):51-58). Updated and extended as **PROBAST+AI** (2025), for prediction models built with regression or artificial intelligence methods, which assesses quality, risk of bias and applicability (Moons KGM, et al. BMJ. 2025;388:e082505. doi:10.1136/bmj-2024-082505; https://www.probast.org/; checked 2026-09-23).

**Propensity score.** Predicted probability of receiving an exposure given measured covariates. Used for matching, weighting (IPTW), or stratification to control confounding in observational studies.

**PROSPERO.** International Prospective Register of Systematic Reviews (https://www.crd.york.ac.uk/prospero/).

**P value.** Probability of obtaining the observed result, or one more extreme, if the null hypothesis were true. Not the probability that the null is true. Should not be the only summary; report effect estimate with 95% CI.

## Q

**QUADAS-2.** Quality Assessment of Diagnostic Accuracy Studies, version 2 (2011): risk-of-bias and applicability tool for diagnostic accuracy primary studies (Whiting PF, et al. Ann Intern Med. 2011;155(8):529-536). Still used in reviews whose protocol named it.

**QUADAS-3.** Revision of QUADAS-2, published February 2026: assessment at the level of each accuracy estimate against an "ideal" test accuracy trial, with domains Participants, Index Test, Target Condition and Analysis (Whiting PF, et al. Ann Intern Med. 2026;179:548-555. doi:10.7326/ANNALS-25-02104; https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-3/; checked 2026-09-23).

## R

**RCT.** Randomized Controlled Trial.

**Reference standard.** The "gold standard" against which an index test is compared in a diagnostic accuracy study. Reported per STARD Item 10b.

**Relative risk (RR), risk ratio.** Ratio of event rates between two groups. RR = 1 means no effect.

**RECORD.** Reporting of studies Conducted using Observational Routinely-collected health Data: STROBE extension.

**ROB-ME.** Risk Of Bias due to Missing Evidence: tool for judging, per meta-analysis, the risk of bias from unpublished studies or unreported results (Page MJ, et al. BMJ. 2023;383:e076754. doi:10.1136/bmj-2023-076754; https://www.riskofbias.info/welcome/rob-me-tool; checked 2026-09-23).

**ROBINS-E.** Risk Of Bias In Non-randomized Studies of Exposures: tool for non-randomized follow-up studies of exposure effects; version of 24 March 2024 (Higgins JPT, et al. Environ Int. 2024;186:108602. doi:10.1016/j.envint.2024.108602; https://www.riskofbias.info/welcome/robins-e-tool; checked 2026-09-23).

**ROBINS-I.** Risk Of Bias In Non-randomised Studies of Interventions: risk-of-bias tool for non-randomized studies of interventions (2016; Sterne JAC, et al. BMJ. 2016;355:i4919). **ROBINS-I V2**, revised release of 20 November 2025, is labelled a draft by its developers and covers follow-up (cohort) studies; no journal publication found (https://www.riskofbias.info/welcome/robins-i-v2; checked 2026-09-23).

**RoB 2.** Revised Cochrane tool for assessing Risk of Bias in randomized trials; current version 22 August 2019, with variants for cluster-randomized and crossover trials (Sterne JAC, et al. BMJ. 2019;366:l4898; https://www.riskofbias.info/welcome/rob-2-0-tool; checked 2026-09-23). Domain 1 (randomization process) covers sequence generation and allocation concealment together; the original tool (RoB 1, 2011) judged them as separate domains.

**ROC curve.** Receiver Operating Characteristic curve: plot of sensitivity vs. 1 − specificity across thresholds. Summarized by AUC.

## S

**Sensitivity.** Probability that a diseased subject is correctly identified by the test. `True Positives / (True Positives + False Negatives)`.

**Sensitivity analysis.** Re-running the primary analysis under alternative assumptions (different missing-data handling, alternative model, different analysis population) to test robustness.

**Sequence generation.** How the allocation list of a trial was produced. Adequate when it includes an element of chance (computer-generated random numbers, random number table, drawing lots, coin tossing); inadequate when it follows a rule (alternation, date of birth, record number). A random sequence still needs allocation concealment to protect it. See **Allocation concealment**.

**Snowballing.** Reference-finding technique. **Forward snowballing:** finding citations *to* a paper. **Backward snowballing:** finding citations *in* a paper.

**Specificity.** Probability that a non-diseased subject is correctly identified as negative. `True Negatives / (True Negatives + False Positives)`.

**SPIRIT.** Standard Protocol Items: Recommendations for Interventional Trials: reporting standard for trial protocols (SPIRIT 2025, 34 items; supersedes SPIRIT 2013, 33 items).

**SRQR.** Standards for Reporting Qualitative Research.

**STARD.** Standards for Reporting of Diagnostic Accuracy Studies (STARD 2015, 30 items + flow diagram).

**STROBE.** Strengthening the Reporting of Observational Studies in Epidemiology (22 items, with cohort / case-control / cross-sectional variants).

**Surrogate outcome.** Lab or imaging marker used in place of a clinical outcome (e.g., HbA1c instead of microvascular events). Justify the surrogate or downgrade conclusions.

## T

**Target trial emulation.** Methodological framework explicitly specifying the (hypothetical) randomized trial that an observational analysis emulates, then applying analytic techniques (sequential trial emulation, IPTW) that mimic randomization.

**TRIPOD+AI.** Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis, 2024 update (27 items), for regression and machine-learning models, diagnostic and prognostic. Supersedes TRIPOD 2015 (22 items), which should no longer be used. TRIPOD-LLM (2025) covers studies of large language models.

## V

**Vancouver style.** Numbered citation style maintained by ICMJE; the default style of this skill. References numbered in order of first appearance; superscript or bracketed numerals in-text. See `references/citation-styles.md`.

## See Also

For full discussion of any term, follow these section guides:

1. **Statistical reporting** (CIs, effect sizes, missing data, software): `references/statistical-reporting.md`.
2. **Study designs and PICO framing**: `references/study-types.md`.
3. **Reporting standards**: `references/reporting-standards.md`.
4. **Methods-section detail**: `references/method.md`.
5. **Citation styles**: `references/citation-styles.md`.
