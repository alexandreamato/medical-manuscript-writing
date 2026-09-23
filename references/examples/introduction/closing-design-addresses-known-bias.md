# Closing: The Design Is Chosen to Remove a Known Bias

`Use for observational studies whose main strength is a design or analysis that removes a bias affecting prior studies (target trial emulation, active-comparator new-user design, self-controlled designs, instrumental variables, Mendelian randomization, individual participant data).`

## Skeleton

```
% Name the bias in prior analyses (already described in the gap paragraph)
Previous [cohort] analyses of [EXPOSURE] and [OUTCOME] were vulnerable to [BIAS].

% State the design and how it removes the bias
To avoid this, we [DESIGN / ANALYSIS], which [MECHANISM: aligns time zero with treatment
start / compares new users of two active drugs / uses each patient as their own control].

% State the aim in PECO form and the causal estimand
We aimed to estimate [ESTIMAND: the effect of initiating X versus Y] on [OUTCOME] at
[TIMEPOINT] in [POPULATION].
```

## Worked example (illustrative; fictional)

```
Previous cohort analyses of statins and dementia were vulnerable to immortal time bias,
because exposure was assessed during follow-up, and to confounding by indication,
because cardiovascular risk influences both prescription and cognitive outcomes. To
avoid these biases, we emulated a target trial in a population-based cohort, specifying
eligibility, treatment strategies, time zero, outcome, and analysis in advance, and
aligning time zero with statin initiation. We aimed to estimate the effect of
initiating a statin, compared with not initiating one, on the 10-year risk of incident
dementia in adults aged 60 to 75 years without prior cardiovascular disease.
```

## Notes and pitfalls

1. Name the bias precisely (immortal time, prevalent-user, confounding by indication, reverse causation). "Previous studies had limitations" does not justify a design.
2. Cite the methodological foundation of the design with a verified reference.
3. Even with a bias-removing design, keep the aim and later conclusions in the language of an observational estimate; residual confounding remains.
