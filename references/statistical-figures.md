# Statistical Figures for Medical Manuscripts

Statistical figures are generated from the data by code, never drawn by hand. This file lists, for each common type, the reporting standard that expects it, the tools that produce it, and what the figure must show. Flow diagrams, timelines, trial schemas and DAGs are in `references/diagrams.md`; general figure design (captions, resolution, accessibility, image ethics) is in `references/figures-and-tables.md`.

## Quick Selector

| Figure | Expected by | Tools | Section |
| --- | --- | --- | --- |
| Forest plot (meta-analysis) | PRISMA 2020 (recommended display for each meta-analysis) | R: `metafor`, `meta`, `forestplot`; or RevMan | [Forest plot](#forest-plot-meta-analysis) |
| Kaplan-Meier survival | None (standard for time-to-event) | R: `survival` + `survminer` | [Kaplan-Meier](#kaplan-meier-survival-curve) |
| Funnel plot | Meta-analyses with 10 or more studies (Cochrane Handbook 13.3.4.4) | R: `metafor`, `meta` | [Funnel plot](#funnel-plot) |
| ROC curve | STARD (recommended) | R: `pROC`; Python: `scikit-learn` | [ROC curve](#roc-curve) |
| Calibration plot | TRIPOD+AI (recommended) | R: `rms`, `CalibrationCurves` | [Calibration plot](#calibration-plot) |

## Export

1. Line art (plots) as vector files (SVG, EPS or PDF); if a raster file is unavoidable, 1000 to 1200 dpi for plots and 300 dpi for photographs, as the journal requires (`references/figures-and-tables.md`, Resolution).
2. Keep the script that produced each figure in version control and regenerate the figure from it after every change to the data or analysis; do not edit exported files by hand.
3. Report in the caption what the figure shows (estimate, interval, model), so it stands alone.

## Forest Plot (Meta-Analysis)

Cannot be generated from text: requires data. Generated in:

1. **R `metafor` package** (gold standard for academic meta-analysis). https://www.metafor-project.org. Functions: `forest()`, `forest.rma()`. Highly customizable.
2. **R `meta` package**. Also widely used; produces clean forest plots.
3. **R `forestplot` package**. Specialized; handles complex multi-row formats and subgroups.
4. **RevMan** (Cochrane). Standard tool for Cochrane Reviews.
5. **Stata** `meta forestplot` command (Stata 16+).

A forest plot must show: study labels, sample sizes per arm, point estimate per study with 95% CI, the pooled estimate (diamond), the heterogeneity statistic (I², τ²), the test for overall effect, and the model used (fixed or random effects).

## Kaplan-Meier Survival Curve

Cannot be generated from text. Generated in:

1. **R: `survival` + `survminer` packages**. `survfit()` to fit; `ggsurvplot()` to draw. Add the at-risk table beneath the plot (expected by many journals and reviewers): `ggsurvplot(..., risk.table = TRUE)`.
2. **Stata**: `sts graph` command.
3. **Python**: `lifelines` package, `KaplanMeierFitter().plot()`.

A KM curve must show: survival probability over time per group, the at-risk table at each timepoint, censoring marks, the hazard ratio with 95% CI, and the log-rank p value.

## Funnel Plot

For small-study effects (of which publication bias is one cause) when a meta-analysis has 10 or more studies (Cochrane Handbook version 6.5, section 13.3.4.4). With fewer studies, assess missing evidence in other ways (registries, protocol-publication comparison, ROB-ME): `references/systematic-review.md` (7e).

1. **R `metafor`**: `funnel(meta_analysis_object)`.
2. **R `meta`**: `funnel(...)`.
3. **Stata**: `meta funnelplot`.

## ROC Curve

Common in diagnostic accuracy studies (STARD).

1. **R**: `pROC` package; `roc()` to fit, `plot()` or `ggroc()` to draw.
2. **R alternative**: `ROCR`, `precrec`.
3. **Python**: `sklearn.metrics.roc_curve` + `matplotlib`.
4. **Stata**: `roctab`, `roccomp`.

Report the AUC with 95% CI in the caption and on the plot.

## Calibration Plot

Standard for prediction-model studies (TRIPOD+AI).

1. **R**: `rms` package (`val.prob`); `CalibrationCurves` package (`val.prob.ci.2`); `riskRegression` package.
2. **Python**: `sklearn.calibration.CalibrationDisplay`.

Report the calibration intercept and slope, and ideally the integrated calibration index (ICI).

## Cross-References Within This Skill

1. Statistical reporting rules behind each figure (effect sizes, intervals, models): `references/statistical-reporting.md`.
2. Figure design, captions and file formats: `references/figures-and-tables.md`.
3. Flow diagrams, timelines and DAGs: `references/diagrams.md`.
