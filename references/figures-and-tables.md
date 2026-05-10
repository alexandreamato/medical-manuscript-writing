# Figures and Tables — Best Practices for Medical Manuscripts

This file covers general design and submission principles for figures and tables in medical manuscripts. For the specific reporting-standard flow diagrams (CONSORT, STROBE, PRISMA, STARD), CARE timelines, trial schemas, and statistical figures (forest, Kaplan-Meier, funnel, ROC), see `references/diagrams.md`. For Results-section narrative around tables and figures, see `references/results.md`.

## Contents

1. [Tables vs. Figures — When to Use Each](#tables-vs-figures--when-to-use-each)
2. [Optimal Quantity](#optimal-quantity)
3. [Six Core Design Principles](#six-core-design-principles)
4. [Figure-Type Reference](#figure-type-reference) — bar, line, scatter, box, heatmap, images
5. [Table Design](#table-design) — anatomy, formatting, common mistakes
6. [Statistical Presentation Inside Display Items](#statistical-presentation-inside-display-items)
7. [Numbering and In-Text References](#numbering-and-in-text-references)
8. [Captions](#captions) — figure and table caption structure
9. [Technical Requirements](#technical-requirements) — file formats, resolution, dimensions
10. [Image Manipulation Ethics](#image-manipulation-ethics)
11. [Accessibility — Practical Tools](#accessibility--practical-tools)
12. [Software for Creating Figures](#software-for-creating-figures)
13. [Pre-Submission Checklist](#pre-submission-checklist)
14. [Cross-References](#cross-references)

## Tables vs. Figures — When to Use Each

### Use a **table** when

1. Precise numerical values are needed.
2. Multiple variables are compared across multiple categories (e.g., baseline characteristics).
3. Statistical model output is being reported (coefficients, 95% CIs, p values).
4. Dose-response, gene expression, or compound concentrations require exact values.
5. Readers will need to look up specific data points.

Common medical-manuscript tables:

1. Baseline characteristics by group (Table 1).
2. Primary and secondary outcomes (Table 2).
3. Adverse events by group (Table 3).
4. Subgroup analyses with interaction p values.
5. Sensitivity-analysis results.
6. Diagnostic-accuracy 2×2 with sensitivity, specificity, predictive values.

### Use a **figure** when

1. Trends over time or across continuous variables are central.
2. Group comparisons are visual (forest plots, KM curves).
3. Distributions, correlations, or relationships are central.
4. The information is an image (histology, radiology, photograph).
5. The information is a workflow or schema (CONSORT/STROBE/PRISMA/STARD flow, trial schema).

Common medical-manuscript figures:

1. Participant flow diagram (mandatory in CONSORT, STROBE, PRISMA, STARD).
2. Forest plot of primary outcome and subgroups.
3. Kaplan-Meier survival curves.
4. ROC curves for diagnostic studies.
5. Calibration plots for prediction-model studies.
6. Box / violin plots of distributions across groups.

### General decision rule

Can the information be conveyed in 1–2 sentences of text?

- **Yes** → text only.
- **No, and precise values are needed** → table.
- **No, and patterns or trends are most important** → figure.

## Optimal Quantity

A widely cited rule of thumb is **one display item per ~1,000 words of body text**. Typical medical manuscripts:

| Manuscript type | Body words | Display items |
| --- | --- | --- |
| Original article | 2,500–4,000 | 4–7 (commonly Tables 1–3 and Figures 1–3) |
| Brief report / research letter | 800–1,500 | 1–3 |
| Case report | 1,000–1,500 | 1–3 (timeline + 1–2 images) |
| Systematic review | 4,000–6,000 | 3–6 plus PRISMA flow diagram |
| Clinical update | 3,000–5,000 | 2–4 plus a key-take-home-points table |

Quality over quantity. A few well-designed displays beat many redundant ones.

## Six Core Design Principles

### 1. Self-Explanatory Display Items

Every figure and every table must stand alone without requiring the body text. The reader who jumps to Figure 2 must be able to interpret it.

Required elements:

1. Complete, descriptive caption.
2. All abbreviations defined in the caption or a footnote.
3. Units of measurement clearly indicated.
4. Sample sizes (n) reported per arm or per group.
5. Statistical significance annotations explained.
6. Legend for figures with multiple data series.

Example self-explanatory caption:

```
Figure 2. Mean systolic blood pressure (SBP) over 12 weeks in the dapagliflozin
and placebo groups. Error bars represent 95% confidence intervals. Asterisks
indicate significant between-group differences at each time point (* p < 0.05,
** p < 0.01, *** p < 0.001; mixed-effects model with treatment-by-time
interaction). n = 48 dapagliflozin, n = 50 placebo. SBP, systolic blood
pressure.
```

### 2. Avoid Redundancy

Do not duplicate information among text, tables, and figures.

Bad:

```
"Mean age was 45.2 years in the intervention group and 47.8 years in
the control group. Mean BMI was 26.3 in the intervention group and 28.1
in the control group..." [Same numbers also shown in Table 1]
```

Better:

```
"Baseline characteristics were similar between groups (Table 1), with no
clinically important differences in age, BMI, or comorbidity burden."
[Detail in Table 1]
```

The body text **highlights** the key findings; tables and figures **carry** the numbers.

### 3. Consistency

Maintain uniform formatting across all display items in a manuscript:

1. Font types and sizes.
2. Color schemes (use the same palette across figures).
3. **Variable-to-color mapping is locked across the whole manuscript.** If group A is green in Figure 1, group A must remain green in Figures 2, 3, 4 and any supplementary figures. Same rule applies to study arms (intervention vs. control), exposure categories (low / medium / high), or any categorical variable that recurs across multiple displays. Switching colors across figures forces the reader to re-learn the legend; consistent encoding lets them read the second figure in seconds.
4. Terminology and abbreviations.
5. Axis labels and units.
6. Statistical-annotation methods (always 95% CI, always SE, or always SD; do not switch).
7. Decimal precision per metric column.

Example of inconsistency to avoid:

- Figure 1 says "standard error" while Figure 2 says "SE".
- Table 1 shows `p = 0.023` while Table 2 shows `p-value = .023`.
- Figures 1, 3 use blue/red while Figure 2 uses green/yellow.
- **Group A is green in Figure 1 but red in Figure 2** (most common version of this error).
- Intervention arm appears as a solid line in Figure 1 but as a dashed line in Figure 2.

### Variable-to-encoding mapping — practical workflow

Before drafting any figure, write down a small mapping table and apply it everywhere:

| Variable / group | Color | Symbol | Line style |
| --- | --- | --- | --- |
| Intervention arm (dapagliflozin) | `#1f77b4` blue | filled circle | solid |
| Control arm (placebo) | `#d62728` red | open circle | dashed |
| Subgroup: ApoE4 carrier | `#2ca02c` green | triangle | solid |
| Subgroup: non-carrier | `#ff7f0e` orange | square | solid |

Then: forest plot, KM curve, line graph, box plot, bar graph — **all** use the same color, symbol, and line style for each entity. The reader learns the encoding once and re-uses it across the manuscript.

This applies equally to:

1. **Forest plots** with subgroups: each subgroup keeps the same color across the primary forest plot, sensitivity-analysis forest plot, and any subgroup forest plots.
2. **KM curves** across multiple endpoints: if intervention is blue in the primary-outcome KM, keep it blue in the secondary-outcome KM and the subgroup KMs.
3. **Box / violin plots** across timepoints: each group's color stays fixed across baseline, week 4, week 12.
4. **Heatmaps** with annotation rows: a study-group annotation row uses the same colors as everywhere else.

If you regenerate figures in R or Python, set the palette **once** in a config block and reuse:

```r
group_colors <- c(
  "Dapagliflozin" = "#1f77b4",
  "Placebo"       = "#d62728"
)
# Reuse in every plot:
ggplot(df) + geom_line(aes(color = group)) +
  scale_color_manual(values = group_colors)
```

```python
GROUP_COLORS = {
    "Dapagliflozin": "#1f77b4",
    "Placebo":       "#d62728",
}
ax.plot(x, y, color=GROUP_COLORS[group_name])
```

This makes consistency mechanical rather than manual.

### 4. Clarity and Simplicity

Avoid cluttered displays:

1. Do not include too many variables in one figure.
2. Use readable fonts (≥ 8 pt at final print size, often 10–12 pt).
3. Provide adequate spacing between elements.
4. Use high contrast.
5. Remove unnecessary grid lines, borders, and decoration.
6. Maximize the data-ink ratio (Tufte's principle: minimize non-data ink).

### 5. Accessibility

1. **Color-blind safe palettes.** Avoid red-green encodings. Recommended palettes: ColorBrewer (`colorbrewer2.org`), Viridis / Plasma / Inferno (for heatmaps and continuous scales), Okabe-Ito 8-color qualitative palette.
2. **Do not rely on color alone.** Add patterns, shapes, or labels that distinguish groups.
3. **Test in grayscale.** Print every figure in black and white before submission; if groups become indistinguishable, redesign.
4. **High contrast.** Dark text on light background; thick lines (≥ 0.5 pt); ≥ 8 pt text at final size.

### 6. Truthful Visualization

1. **Bar chart y-axes start at zero**, unless showing tiny absolute differences in a small range — and even then, mark the broken axis explicitly.
2. **No 3-D bar or pie charts.** They distort perception.
3. **No truncated y-axes** that exaggerate effect size.
4. **No cherry-picked images.** Show representative examples and quantify across the cohort separately.
5. **No image manipulation** beyond linear brightness/contrast adjustment applied to the entire image (see "Image Manipulation Ethics" below).

## Figure-Type Reference

For statistical-figure types specific to medical manuscripts (forest plot, Kaplan-Meier, funnel plot, ROC, calibration plot), see `references/diagrams.md`. The general types below cover most other situations.

### Bar graphs

Best for: comparing discrete categories or groups; showing means with error bars.

Rules:

1. Y-axis starts at zero.
2. Order bars logically (by size, alphabetically, by time).
3. Error bars: SD, SEM, or 95% CI — pick one and stick to it; **state which** in every caption.
4. Include n per bar.
5. No 3-D effects.

### Line graphs

Best for: trends over time or another continuous x-variable; multi-group comparisons.

Rules:

1. Different line styles or colors per group; legible in grayscale.
2. Data-point markers for sparse data.
3. Shaded confidence bands or vertical error bars.
4. Consistent x-axis intervals.

### Scatter plots

Best for: relationships between two continuous variables.

Rules:

1. Show every data point (use semi-transparent points if dense overlap).
2. Include a trend line with 95% CI band when meaningful; report the correlation coefficient and p value in the caption.
3. Consider log scales for wide ranges.
4. For method-comparison studies (e.g., Bland-Altman), show the mean line and the 95% limits of agreement.

### Box plots and violin plots

Best for: distributions across groups.

Rules:

1. Define box elements in the caption (median, IQR, whiskers).
2. Mark outliers explicitly.
3. For small samples (n < 20 per group), overlay individual data points or use violin/strip plots.

### Heatmaps

Best for: matrices of data; patterns across many conditions.

Rules:

1. Perceptually uniform color scales (Viridis, Cividis); avoid rainbow.
2. Always include a color-scale bar with units.
3. Consider hierarchical clustering of rows and columns.
4. Choose diverging vs. sequential color scales based on whether the midpoint is meaningful.

### Images (microscopy, histology, radiology, gels)

Rules:

1. Include a **scale bar** on the image (do not put magnification in the caption).
2. Show representative images alongside quantification.
3. Label important features with arrows or letters.
4. Resolution ≥ 300 dpi for raster.
5. Show full, unmanipulated images; report all cropping.
6. Include all relevant controls.

## Table Design

### Anatomy

1. Table number and title (above the table).
2. Column headers with units.
3. Row labels.
4. Data cells with appropriate precision.
5. Footnotes (below) for abbreviations, statistical methods, and notes.

### Formatting

1. Align decimal points within numeric columns.
2. Consistent decimal precision per column (e.g., 1 decimal for percentages, 2 for hazard ratios, 0 for counts).
3. Use an en-dash `–` or `NA` for "not applicable"; do not leave cells blank without explanation.
4. Use superscript symbols (`a`, `b`, `c`, or `*`, `†`, `‡`) for footnote pointers.
5. Define every abbreviation in the footnote, even if also in the caption.
6. Footnotes explain the statistical test used and the significance threshold.

### Example baseline-characteristics table

```
Table 1. Baseline characteristics of study participants

Characteristic              Intervention (n=625)   Control (n=625)
─────────────────────────────────────────────────────────────────
Age, years                  72.1 ± 8.3             71.8 ± 8.5
Female sex, n (%)           351 (56.2)             348 (55.7)
BMI, kg/m^2                 28.4 ± 4.6             28.6 ± 4.7
NYHA class III/IV, n (%)    218 (34.9)             221 (35.4)
LVEF, %                     58.2 ± 6.1             57.9 ± 6.3
Diabetes, n (%)             271 (43.4)             268 (42.9)
Atrial fibrillation, n (%)  189 (30.2)             192 (30.7)
─────────────────────────────────────────────────────────────────

Data are mean ± SD or n (%). BMI, body mass index; LVEF, left
ventricular ejection fraction; NYHA, New York Heart Association.
For randomized trials, baseline p values are not reported per
CONSORT.
```

Notes:

1. **No p values for baseline differences in randomized trials** (CONSORT discourages this; standardized mean differences are preferred for matched/weighted observational studies).
2. **Precision matched** within column.
3. **Footnote** defines abbreviations and explains design-specific conventions.

### Common table mistakes

1. Excessive complexity (too many rows or columns).
2. Missing units, unclear abbreviations.
3. Over-precision (5 decimal places for p values).
4. Missing sample sizes.
5. Inconsistent formatting across multiple tables.
6. Image-of-table instead of editable table (most journals require editable tables in Word).

## Statistical Presentation Inside Display Items

For each comparison, report:

1. Point estimate (mean, median, proportion, hazard ratio).
2. Variability (SD, SEM, 95% CI).
3. Sample size (n).
4. Test statistic (t, F, χ², HR, OR, RR) when applicable.
5. p value (exact when p > 0.001; `< 0.001` when smaller).
6. Effect size when relevant.

### Choosing the error-bar measure

| Measure | Meaning | When to use |
| --- | --- | --- |
| SD | Variability of the data | Showing data spread |
| SEM | Precision of the mean estimate | Showing measurement precision (small n) |
| 95% CI | Range likely to contain the true value | Default; lets readers infer significance |

The default in medical manuscripts is the **95% confidence interval**: non-overlapping CIs roughly imply a significant difference, and CIs are interpretable by clinicians. Always state which measure the error bars represent.

### Significance indicators

1. Stars: `* p < 0.05`, `** p < 0.01`, `*** p < 0.001`.
2. Or report exact p values (`p = 0.024`).
3. Define the threshold in every caption.
4. `n.s.` or `NS` for not significant; or report the exact p.
5. Avoid `p = 0.000`; write `p < 0.001`.

## Numbering and In-Text References

1. Number figures and tables separately, in Arabic numerals: Figure 1, Figure 2, ... and Table 1, Table 2, ...
2. Supplementary: Figure S1, Table S1.
3. Number by **order of first mention in the text**. Renumber after every revision pass.
4. In-text reference: `(Figure 1)` or `Figure 1 shows ...`. Avoid "the figure below" or "above" — pagination changes.
5. Cite each table and each figure at least once in the body text.

## Captions

### Figure caption structure

```
Figure N. [One-sentence title]. [Description sentences: panels, what is plotted, units,
sample sizes, statistical tests, definition of error bars and significance indicators,
abbreviations.]
```

Example:

```
Figure 3. Cognitive performance over 12 weeks. (A) Mean Mini-Mental State Examination
(MMSE) score at baseline, 6 weeks, and 12 weeks for treatment (blue) and placebo
(grey) groups. (B) Individual participant trajectories in the treatment group. Error
bars are 95% confidence intervals. * p < 0.05, ** p < 0.01, *** p < 0.001 by
mixed-effects model with treatment-by-time interaction and Bonferroni correction.
n = 42 treatment, n = 40 placebo. MMSE scores range from 0 to 30; higher scores
indicate better cognitive function.
```

### Table caption structure

Above the table:

```
Table N. [Descriptive title.]
```

Below the table (footnote):

```
Data are [mean ± SD / median (IQR) / n (%)]. [Statistical method.] [Abbreviations.]
```

## Technical Requirements

### File formats

Vector (preferred for line art and graphs):

1. **PDF** — universal; preserves quality.
2. **EPS** — Encapsulated PostScript; publishing standard at many journals.
3. **SVG** — Scalable Vector Graphics; web-friendly; default Mermaid output.
4. **AI** — Adobe Illustrator native; some journals accept.

Raster (for photographs and halftone images):

1. **TIFF** — uncompressed, high quality, large files.
2. **PNG** — lossless compression; good for screen.
3. **JPEG** — lossy; acceptable for photographs but not for figures with sharp lines.

Avoid:

1. Low-resolution screenshots.
2. Figures copied from PowerPoint (usually too low resolution).
3. Heavily compressed JPEGs (artifacts).

### Resolution

Minimum standards:

1. **Line art (graphs, diagrams):** 300–600 dpi (vector preferred).
2. **Halftones (photos, grayscale images):** 300 dpi.
3. **Combination (image with text/labels):** 600 dpi.

Create figures at the **final size and resolution**; do not enlarge low-resolution images.

### Dimensions

Verify the journal's Instructions to Authors. Common targets:

1. **Single column:** 8–9 cm (3–3.5 inches) wide.
2. **Double column:** 17–18 cm (6.5–7 inches) wide.
3. **Full page:** journal-specific.

Designing for single-column is the safest default and avoids forced down-scaling.

### Color space

1. **RGB** for online-only or web supplements.
2. **CMYK** for print (some journals require). Some figures look different in CMYK; verify after conversion.
3. **Grayscale** for journals that print in B&W.

### File submission

1. One figure per file. Name clearly: `Figure1.tif`, `Figure2.eps`.
2. Tables: most journals accept editable Word tables embedded at the end of the manuscript or as a separate file. Do not submit tables as images.
3. Multi-panel figures: assemble in Illustrator/Inkscape; submit as a single panel-labeled file (A, B, C in upper-left of each panel).

## Image Manipulation Ethics

Allowed:

1. Brightness and contrast adjustment applied to the **entire** image.
2. Color balance applied uniformly.
3. Cropping (with notation in caption or methods).
4. Rotation.

**Not allowed**:

1. Selective editing (e.g., enhancing specific bands in a gel; healing-brushing artifacts in microscopy).
2. Removing background features that change interpretation.
3. Splicing images from different sources without a clearly visible black line and explicit notation in the caption.
4. Any manipulation that obscures, eliminates, or misrepresents data.

Disclose all image processing in the Methods section. Editorial offices increasingly screen images with forensic tools (e.g., the "ImageTwin" or "Proofig" services); manipulation is detected and grounds for rejection or retraction.

## Accessibility — Practical Tools

1. **ColorBrewer 2** (`colorbrewer2.org`) — pre-tested categorical and sequential palettes.
2. **Viridis family** (`viridis`, `magma`, `plasma`, `cividis`) — perceptually uniform; works in grayscale.
3. **Okabe-Ito 8-color palette** — recommended for qualitative encoding with up to 8 groups; color-blind safe.
4. **Coblis** (`color-blindness.com/coblis-color-blindness-simulator`) — simulate how figures appear to readers with different color-vision deficiencies.

## Software for Creating Figures

For statistical figures specific to medical manuscripts (forest plots, Kaplan-Meier, funnel plots, ROC, calibration), see `references/diagrams.md`.

General-purpose graphing:

| Tool | Strengths | Notes |
| --- | --- | --- |
| **R + ggplot2** | Highly customizable; reproducible; excellent statistical packages | Recommended default for medical research |
| **Python + matplotlib / seaborn / plotnine** | Flexible; programmable; integrates with pandas | Good for ML and large-data work |
| **GraphPad Prism** | User-friendly; statistics integrated | Common in life sciences and bench labs |
| **Stata** | Built-in graphing tied to stats | Standard in epidemiology |
| **Origin** | Advanced graphing | Engineering and physics |
| **Excel** | Widely available; basic | Limited customization; avoid for publication-grade figures |

For figure assembly and label addition:

1. **Adobe Illustrator** — professional standard.
2. **Inkscape** — free vector editor.
3. **Affinity Designer** — paid alternative to Illustrator.

For image processing (microscopy, gels):

1. **ImageJ / Fiji** — free, powerful, widely used.
2. **Adobe Photoshop** — professional standard.
3. **GIMP** — free alternative.

Best practice: script your figure generation (R, Python) for reproducibility; save the script alongside the manuscript.

## Pre-Submission Checklist

For every figure:

1. High enough resolution (≥ 300 dpi for raster; vector preferred for line art).
2. Correct file format per the journal's Instructions.
3. Correct dimensions for the journal (single or double column).
4. Correct color space (RGB or CMYK).
5. Self-explanatory caption with all abbreviations defined.
6. Caption length within journal limit.
7. All symbols, lines, and colors explained in the legend or caption.
8. Error bars defined (SD vs. SEM vs. 95% CI).
9. Sample sizes reported.
10. Statistical tests described.
11. Axes labeled with units.
12. Readable text at final print size (≥ 8 pt).
13. Works in grayscale; color-blind safe palette.
14. Cited in the body text in order of first appearance.
15. Style matches the target journal's published figures.
16. No undisclosed image manipulation.

For every table:

1. Clear, descriptive title.
2. Column headers include units.
3. Appropriate numerical precision (consistent within column).
4. Abbreviations defined in the footnote.
5. Statistical methods explained.
6. Sample sizes included.
7. Consistent formatting across all tables in the manuscript.
8. Editable format (not image).
9. Cited in the body text in order of first appearance.

Overall manuscript:

1. Number of display items within journal limits.
2. ~ 1 display item per 1,000 words of body text.
3. No duplication between text, figures, and tables.
4. Consistent formatting across all display items.
5. Each display item necessary (each tells an important part of the story).
6. Visual style matches the target journal.
7. Quality comparable to published examples in the journal.

## Cross-References

1. **Reporting-standard flow diagrams (CONSORT, STROBE, PRISMA, STARD), CARE timelines, trial schemas, statistical figures (forest, KM, funnel, ROC, calibration):** `references/diagrams.md`.
2. **Results-section narrative around figures and tables (participant flow, Table 1, primary outcome figure, etc.):** `references/results.md`.
3. **Manuscript-level conventions (citation order of figures and tables, file format defaults):** `references/manuscript-conventions.md`.
4. **Statistical reporting standards (effect sizes, CIs, p values):** `references/statistical-reporting.md`.
