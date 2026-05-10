# Rationale-Writing Patterns for Methods Subsections

`Each Methods subsection should open with a rationale sentence that ties the choice to the study aim or to a known bias.`

## Typical opening sentences

1. `We selected [DESIGN / MEASUREMENT / ANALYSIS] because [unresolved question or known bias].`
2. `To address [SPECIFIC BIAS: confounding / immortal time / measurement error], we [CHOICE].`
3. `Because [OUTCOME] is rare in this population, we [STRATEGY: case-control sampling / longer follow-up / pooled cohort].`
4. `Because [INSTRUMENT] is operator-dependent, we [STRATEGY: blinded adjudication / standardized training / inter-rater agreement metric].`

## Usage

1. State the specific failure or bias before naming the strategy.
2. Keep the rationale paragraph independent from the procedure paragraph; reviewers should be able to read the rationale alone and understand why the choice was made.
3. Do not collapse rationale into procedure ("We used X because we used X."). State the bias-driven reason.

## Worked rationale openings

```
% Why a Cox model rather than logistic regression
We selected Cox proportional hazards regression because the time to event was variable
across participants and informative censoring (death from competing causes) was expected
in older adults.

% Why central blinded adjudication
Because outcome ascertainment of recurrent stroke can be biased by knowledge of treatment
in an open-label trial, we used central blinded adjudication of all suspected events.

% Why multiple imputation
Because the primary outcome had 8% missingness with a plausible missing-at-random
mechanism conditional on baseline covariates, we performed multiple imputation by
chained equations rather than complete-case analysis.

% Why a target trial emulation
Because conventional cohort analyses of statins and dementia are vulnerable to immortal
time bias and indication bias, we explicitly specified a target trial protocol and
emulated it with sequential trial emulation.
```
