# Gap: Existing Scores, Tests, or Models Perform Poorly in This Population

`Use for prediction-model and diagnostic-accuracy studies when tools exist but are miscalibrated, unvalidated, or impractical in the target population.`

## Skeleton

```
% State the clinical decision the tool supports
Decisions about [DECISION] in [POPULATION] depend on estimating [RISK / DIAGNOSIS].

% Name the available tools and the specific way they fail
Available [scores / tests] ([NAMES]) were [derived / validated] in [OTHER POPULATION] and
[SPECIFIC FAILURE: underestimate risk in the highest band / have low sensitivity / require
unavailable inputs].

% Name the obstacle to a better tool
[OBSTACLE: heterogeneous measurement of a key predictor / lack of external validation]
has limited attempts to improve them.

% State the consequence
As a result, [CONSEQUENCE for patients or decisions].
```

## Worked example (illustrative; fictional)

```
Decisions about proceeding with emergency laparotomy in patients aged 75 years or
older depend on estimating 30-day mortality. Available risk scores (P-POSSUM, NELA,
ACS-NSQIP) were derived in mixed-age populations and underestimate the effect of
frailty, so they are miscalibrated in the highest-risk band. Frailty itself is measured
inconsistently across centres (Clinical Frailty Scale, Edmonton Frail Scale, modified
Frailty Index), which has hindered adding it to existing models. External validation in
this age group is rare and usually limited to a single national audit. As a result,
surgeons and families often weigh operative risk without a reliable estimate.
```

## Notes and pitfalls

1. State the failure in measurable terms (calibration, discrimination, sensitivity, missing inputs). "Existing scores are inadequate" is not a gap.
2. The closing paragraph should say whether the study develops, updates, or externally validates a model, and name TRIPOD+AI (or STARD for diagnostic accuracy) as the reporting guideline.
3. Keep this to 4 to 6 sentences; reviewers do not reward length here.
