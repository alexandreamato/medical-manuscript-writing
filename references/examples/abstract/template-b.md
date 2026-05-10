# Abstract Template B — Challenge → Insight → Contribution (Observational)

Use for observational cohort studies, case-control studies, target trial emulations, and Mendelian randomization studies reported under STROBE / STROBE-MR.

## Structured-abstract skeleton

```
Background
% [Clinical importance and the specific unresolved question.]

Methods
% [Design + setting + population + exposure + comparator + outcome + analytic strategy + analysis population.]

Results
% [Primary association with effect estimate and 95% CI. State analysis population. State residual confounding sensitivity (e.g., E-value).]

Conclusions
% [One-sentence finding stated as association, not causation, with scope and the next step.]
```

## Reusable sentence skeleton

1. `[Condition / question] is [importance].`
2. `Whether [exposure] is associated with [outcome] in [population / setting] is uncertain because [prior evidence limitation].`
3. `We hypothesized that [insight].`
4. `In this [prospective cohort / case-control / target trial emulation], we [followed / assembled / matched] [N] participants with [eligibility criterion] using [data source]. The primary outcome was [outcome] over [time horizon]. We adjusted for [key confounders] using [analytic method] and assessed residual confounding with [sensitivity analysis].`
5. `Over a median follow-up of [duration], [n] events occurred. After adjustment, [exposure] was associated with [outcome]: [hazard / odds / risk ratio] [point estimate] (95% CI, [lower] to [upper]). Results were robust to [sensitivity analysis] (E-value [X]).`
6. `[Exposure] was associated with [direction] [outcome] in [population]. Confirmatory randomized evidence is needed before clinical recommendations.`

## Worked example (illustrative — fictional numbers)

```
Background
Long-term ambient fine particulate matter (PM2.5) exposure has been linked to incident cardiovascular disease, but evidence on incident dementia from large prospective cohorts with individual-level exposure assessment is limited.

Methods
We conducted a prospective cohort study within the UK Biobank, including 412,000 adults aged 40 to 69 years at baseline who were free of dementia. Annual residential PM2.5 was estimated from validated land-use regression models. The primary outcome was incident dementia ascertained from linked hospital and primary care records and death registries through 2022. We used Cox proportional hazards models adjusted for age, sex, education, smoking, alcohol use, body-mass index, hypertension, diabetes, ApoE4 carrier status, and area-level deprivation. We tested residual confounding using E-values.

Results
Over a median follow-up of 11.4 years, 4,820 incident dementia cases were identified. Each 5 µg/m^3 higher PM2.5 was associated with a higher risk of dementia (adjusted hazard ratio 1.16; 95% CI, 1.09 to 1.24). The association was robust to adjustment for ApoE4 carrier status and to a sensitivity analysis using a 5-year exposure lag (E-value 1.62).

Conclusions
Higher long-term PM2.5 exposure was associated with a higher risk of incident dementia in this population-based cohort. These observational findings support a public health rationale for reducing ambient air pollution but require confirmation through quasi-experimental and Mendelian randomization studies.
```

## Notes

1. The associative verb ("was associated with") matches the observational design.
2. The insight sentence — that long-term exposure with individual assessment may resolve prior limitations — sits between the gap and the contribution.
3. The Methods sentence reports analytic strategy (Cox model + adjustment + E-value) so a reviewer can map to STROBE.
4. The Conclusion is calibrated: it acknowledges the design's inferential limit and states the appropriate next step.
