# Abstract Template C — Multiple Contributions (Systematic Review / Meta-Analysis)

Use for systematic reviews and meta-analyses reported under PRISMA. The "multiple contributions" pattern fits this design because most reviews report (a) the pooled effect, (b) a heterogeneity / subgroup contribution, and (c) the certainty assessment.

## Structured-abstract skeleton

```
Background
% [Clinical importance and the question this review answers.]

Methods
% [Eligibility (PICO + designs + dates) + databases and search dates + selection process + risk-of-bias tool + synthesis method + GRADE.]

Results
% [Pooled estimate + heterogeneity. Then key subgroup / sensitivity finding. Then certainty rating.]

Conclusions
% [One-sentence finding with scope and the certainty qualifier.]

Registration
% [PROSPERO ID.]
```

## Reusable sentence skeleton

1. `[Condition / question] is [importance].`
2. `Existing systematic reviews are [out of date / limited to one design / missing recent trials], and an up-to-date synthesis is needed to inform [practice / guideline].`
3. `We searched [databases] from [start date] to [latest date] for [study designs] of [intervention/exposure] vs. [comparator] in [population], reporting [outcomes].`
4. `Two reviewers independently selected studies, extracted data, and assessed risk of bias using [RoB 2 / ROBINS-I / QUADAS-2 / Newcastle-Ottawa]. We pooled estimates with a random-effects model and rated certainty of evidence with GRADE.`
5. `[Number] studies (N = [total participants]) met eligibility. The pooled effect was [point estimate] (95% CI, [lower] to [upper]; I² = [X]%; [N] studies).`
6. `[Subgroup / sensitivity contribution]: in [subgroup], the effect was [point estimate] (95% CI, [lower] to [upper]; interaction p = [value]).`
7. `Certainty of evidence for the primary outcome was [high / moderate / low / very low], rated down for [reasons].`
8. `[Intervention / exposure] [verb appropriate to evidence base] [outcome] in [population], with [moderate / low] certainty.`

## Worked example (illustrative — fictional numbers)

```
Background
Anti-amyloid monoclonal antibodies have shown benefit in early Alzheimer's disease in pivotal trials, but the magnitude of cognitive benefit relative to risk of amyloid-related imaging abnormalities (ARIA) across patient subgroups remains debated.

Methods
We searched MEDLINE, Embase, the Cochrane CENTRAL register, and ClinicalTrials.gov from inception to 31 January 2026 for randomized trials of anti-amyloid monoclonal antibodies vs. placebo in adults with mild cognitive impairment or mild dementia due to Alzheimer's disease. Two reviewers independently extracted data and assessed risk of bias with RoB 2. We pooled effects on the Clinical Dementia Rating Sum of Boxes (CDR-SB) using random-effects meta-analysis and assessed certainty with GRADE. The protocol was registered in PROSPERO (CRD420260000000).

Results
Eight trials (N = 12,480) were included. Anti-amyloid antibodies reduced 18-month CDR-SB worsening compared with placebo by 0.42 points (95% CI, 0.30 to 0.54; I^2 = 32%; 8 trials). The benefit was larger in ApoE4 non-carriers (0.55 points; 95% CI, 0.40 to 0.70) than in ApoE4 homozygotes (0.18 points; 95% CI, -0.05 to 0.41; interaction p = 0.01). Symptomatic ARIA occurred in 14.2% of treated vs. 1.6% of placebo participants (risk ratio 8.6; 95% CI, 6.0 to 12.4). Certainty was moderate for cognitive benefit and high for ARIA risk.

Conclusions
Anti-amyloid monoclonal antibodies produce a small but consistent reduction in cognitive decline in early Alzheimer's disease at the cost of substantially increased ARIA risk, with larger benefit in ApoE4 non-carriers (moderate certainty).

Registration
PROSPERO CRD420260000000.
```

## Notes

1. Each sentence in Results pairs one contribution with its quantitative result.
2. Heterogeneity is reported alongside the pooled estimate.
3. The subgroup result includes the interaction p value, not just the within-subgroup point estimate.
4. The Conclusion communicates effect direction, magnitude, and certainty in one sentence.
5. PROSPERO registration is named per PRISMA.
