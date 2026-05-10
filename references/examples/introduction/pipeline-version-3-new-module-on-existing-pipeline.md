# Design Version 3 — New Analytic Step on an Established Design

`Use when you take a familiar design (a cohort, a meta-analysis) and add one new analytic component (target trial emulation, individual participant data, network meta-analysis, sensitivity analysis with E-values, Bayesian re-analysis).`

## Skeleton

```
% Start from the established design
We extended the established design of [DESIGN] in [POPULATION].

% Introduce the new analytic component
Our innovation is [NEW COMPONENT].

% Provide the observation or methodological insight that motivates it
We observe that [OBSERVATION / METHODOLOGICAL INSIGHT].

% Explain how the component changes the inference
Considering this, we [IMPLEMENTATION] to [INFERENTIAL GAIN].

% Compare against the conventional analysis
In contrast to the conventional [DESIGN], this approach [BENEFIT FOR INFERENCE].
```

## Worked example (illustrative; fictional)

```
We extended the established cohort design of the UK Biobank to estimate the effect of
statin initiation on incident dementia.

Our innovation is to emulate a target trial within the cohort.

We observe that conventional cohort analyses of statins and dementia are vulnerable to
immortal time bias because exposure assessment and outcome ascertainment overlap, and
to indication bias because cardiovascular risk drives both prescription and outcome.

Considering this, we explicitly specified the target trial protocol (eligibility,
treatment strategies, time zero, outcome, analysis plan) and emulated it using
sequential trial emulation with cloning and inverse-probability-of-treatment weighting,
which removes immortal time bias and provides per-protocol and intention-to-treat
estimates analogous to those of a randomized trial.

In contrast to the conventional Cox model with time-fixed exposure, this approach
yields effect estimates that are interpretable as the consequence of a sustained
treatment strategy and that can be benchmarked directly against existing trials.
```

## Notes

1. The contribution is the analytic step (target trial emulation), not the dataset.
2. Cite the methodological foundation (Hernan and Robins, target trial emulation literature) as a real reference.
3. The closing comparison must be specific about which inferential bias is removed.
