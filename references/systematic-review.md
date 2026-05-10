# Systematic Review and Meta-Analysis Writing Guide (Medical Research)

This guide is for writing the manuscript and conducting the methodological steps of a systematic review (with or without meta-analysis). It complements the PRISMA 2020 checklist in `references/reporting-standards.md`. The guidance draws on Wright, Brand, Dunn, and Spindler "How to Write a Systematic Review", Cochrane Handbook practice, and current PRISMA guidance.

## When a Systematic Review Is Worth Writing

A systematic review is appropriate when one or more of the following are true:

1. The clinical question has been studied in multiple primary studies, but the conclusions appear conflicting.
2. Individual primary studies are underpowered, and pooled analysis could yield a more precise overall estimate.
3. The literature on a question has not been formally synthesized in 3 or more years.
4. Stakeholders (guideline panels, payers, regulators) need a calibrated summary of the evidence.
5. The synthesis is needed to identify gaps and inform a future definitive trial.

It is **never** wrong to do a systematic review when individual studies are heterogeneous; what is sometimes wrong is to **pool** them in a meta-analysis. If clinical or methodological heterogeneity is high, present a structured qualitative synthesis instead.

## Systematic Review vs. Narrative Review vs. Meta-Analysis

| Form | Definition | When to use |
| --- | --- | --- |
| Narrative review | Author-selected literature; no formal search; subject to selection bias | Background framing; hypothesis-generating essays |
| Systematic review | Prespecified search and synthesis; minimizes bias; can be qualitative or quantitative | Comprehensive answer to a focused clinical question |
| Meta-analysis | Statistical pooling of effect estimates within a systematic review | When studies are sufficiently similar in population, intervention, comparator, and outcome |

A systematic review without a meta-analysis is sometimes called a "narrative synthesis" or a "structured qualitative synthesis". It is a legitimate output, especially when heterogeneity is high.

## The Tradeoff — Heterogeneity, Internal Validity, External Validity

Heterogeneity is a double-edged sword:

1. **Narrow inclusion criteria** make the included studies more homogeneous and statistical pooling more defensible (higher internal validity), but the conclusions apply only to that narrow population (lower external validity).
2. **Broad inclusion criteria** improve generalizability (higher external validity), but pooling may be inappropriate (lower internal validity of the pooled estimate).

Decide where on this spectrum your review sits, and make the decision explicit in the protocol and the manuscript. Restricting to one outcome definition or one design (e.g., RCTs only) reduces clinical heterogeneity but biases the review against valuable studies that report the outcome differently.

## Step-by-Step Workflow

### Step 1 — Frame the Research Question (PICO)

A good systematic review question has four components:

| Letter | Meaning |
| --- | --- |
| P | Population (who) |
| I | Intervention (or exposure) |
| C | Comparator |
| O | Outcome |

For etiology questions, use PECO (Exposure replaces Intervention). For diagnostic accuracy questions, use PIRD (Index test, Reference standard, target Diagnosis). See `references/study-types.md`.

A good research-question test:

1. Is the question too narrow (will yield 0 to 5 studies and limited generalizability)?
2. Is the question too broad (will yield hundreds of studies and dilute conclusions)?
3. Is the primary outcome operationally defined?
4. Are the eligible study designs prespecified?

### Step 2 — Write the Protocol Before Searching

The protocol is the most important bias-control step. Write and register it (PROSPERO; OSF for non-clinical) before starting the literature search. The protocol must specify:

1. Eligibility criteria (PICO + study designs + dates + languages).
2. Information sources (databases, registries, grey literature).
3. Search strategy (terms and Boolean operators) for at least one database.
4. Selection process (number of reviewers, conflict-resolution rule, software).
5. Data extraction items (one row per study, prespecified columns).
6. Risk-of-bias tool (RoB 2 / ROBINS-I / QUADAS-2 / Newcastle-Ottawa).
7. Effect measures (RR, OR, HR, MD, SMD).
8. Synthesis plan (qualitative summary; meta-analysis model; subgroups; sensitivity analyses).
9. Certainty assessment (GRADE).

A well-formulated protocol increases efficiency and reduces wasted screening time.

### Step 3 — Construct the Search

A comprehensive search is the foundation of a credible systematic review. For PubMed-specific basics (Boolean operators, MeSH, field tags, Clinical Queries) see `references/pubmed-essentials.md`. The principles below apply across all databases:

1. **Search multiple databases.** Medline (via PubMed), Embase, Cochrane CENTRAL. Medline alone misses 20 to 70% of relevant RCTs. Medline and Embase overlap by only ~34% — both are needed.
2. **Add specialty databases when relevant.** CINAHL (nursing), PsycINFO (psychology), LILACS / SciELO (Latin American), AIM (African), IMSEAR (South-East Asian), WPRIM (Western Pacific), KoreaMed.
3. **Search trial registries.** ClinicalTrials.gov, ISRCTN, EU Clinical Trials Register, WHO ICTRP.
4. **Hand-search pertinent journals**, especially the most recent 6 months that may not yet be indexed.
5. **Search bibliographies** of included studies and of recent reviews on the topic.
6. **Search grey literature** — theses (ProQuest Dissertations), conference proceedings, regulatory documents (FDA, EMA), industry reports. Meta-analyses limited to published trials overestimate effects by ~12% relative to those including grey literature.
7. **Avoid English-only restrictions** when feasible; positive results are more likely published in English (English-language bias). If translation cost is prohibitive, state the limitation.
8. **Document the strategy.** Record exact search strings, field tags, dates of last search, and number of records retrieved per source. Provide the full strategy as a supplementary file.

Engage an information specialist or medical librarian if available; they substantially improve sensitivity.

### Step 4 — Screen and Select

1. Import all records into reference-management software (Zotero, EndNote, Mendeley) or a screening platform (Rayyan, Covidence, DistillerSR).
2. Deduplicate.
3. **Two reviewers minimum, working independently.** Title/abstract screen first; full-text screen second. Resolve disagreements by discussion or by a third reviewer.
4. Document exclusions at full-text stage with reasons; this becomes the PRISMA flow diagram.
5. Inter-rater agreement (kappa) at the title/abstract stage is informative; aim for kappa ≥ 0.6 after pilot screening of 50 to 100 records.

### Step 5 — Extract Data

1. Use a **standardized form**, paper or electronic. Pilot it on 3 to 5 studies before full extraction.
2. **Two reviewers minimum, independent extraction.** Reconcile discrepancies by discussion.
3. Capture, at minimum: study identifier, design, country, dates, population, intervention, comparator, outcome definition, effect estimate with 95% CI, sample sizes, follow-up duration, funding source, conflicts of interest.
4. Capture risk-of-bias judgments alongside data.
5. Contact authors for missing data when appropriate.

### Step 6 — Assess Risk of Bias

Choose the tool by study design:

| Design | Tool |
| --- | --- |
| Randomized trials | RoB 2 (Cochrane) |
| Non-randomized intervention studies | ROBINS-I |
| Diagnostic accuracy studies | QUADAS-2 |
| Cohort and case-control | Newcastle-Ottawa or ROBINS-E for exposures |
| Prediction model studies | PROBAST |
| Animal studies | SYRCLE |

Prefer **checklists** over numerical quality scores — a single fatal flaw can be missed if you sum item scores. Two reviewers; reconcile differences.

The four high-yield biases to assess:

1. **Selection bias.** Adequate sequence generation? Adequate allocation concealment? Inadequate concealment overestimates effects by ~30 to 40%.
2. **Performance bias.** Were participants and providers blinded?
3. **Detection bias.** Were outcome assessors blinded?
4. **Attrition bias.** How were losses to follow-up handled? Was intention-to-treat used?

Adequate vs. inadequate concealment examples:

| Adequate | Inadequate |
| --- | --- |
| Computer-generated random numbers | Date of birth |
| Centralized phone or web randomization | Date of admission |
| Sequentially numbered, opaque, sealed envelopes | Alternation |
| Tables of random numbers | Case record number |
| Drawing lots from an opaque container | Coin tossing or shuffling cards (random but not concealed) |

### Step 7 — Synthesize

#### 7a. Qualitative synthesis

Always include this step. Tabulate study characteristics: design, population, intervention, comparator, outcome, effect estimate, risk-of-bias judgment, certainty rating.

#### 7b. Decide whether to pool

Do **not** pool if any of the following hold:

1. Clinical heterogeneity is high (different populations, different intervention doses, different outcome definitions).
2. Methodological heterogeneity is high (different designs, different comparators, different analysis populations).
3. Statistical heterogeneity exceeds I² of ~75% without explanation.
4. The included studies are too few for a stable estimate (typically fewer than 3 to 5 studies).
5. Risk of bias is high in most included studies — pooling will not rescue them.

#### 7c. Meta-analysis when appropriate

1. Choose the model: **fixed-effect** (assumes one true effect) or **random-effects** (assumes a distribution of true effects). Random-effects is the default in most clinical contexts.
2. Choose the effect measure: RR, OR, HR for binary; MD, SMD for continuous.
3. Report the pooled estimate with 95% CI, heterogeneity (I², τ², 95% prediction interval), and the test for overall effect.
4. Forest plot is mandatory.
5. **Engage a statistician early** — at the protocol stage, not after extraction.

#### 7d. Heterogeneity exploration

When heterogeneity is high, do not stop at "I² = 78%". Explore it:

1. Subgroup analysis by prespecified clinical or methodological factor.
2. Meta-regression.
3. Sensitivity analyses excluding high-risk-of-bias studies.

#### 7e. Reporting bias

Assess publication bias only when ≥ 10 studies are included:

1. Funnel plot (visual).
2. Egger or Peters test (statistical).
3. Trim-and-fill or other corrections only as sensitivity analyses.

### Step 8 — Rate Certainty of Evidence (GRADE)

Rate certainty per outcome, not per study. Start at "high" for randomized trials and "low" for observational; downgrade or upgrade per:

Downgrade reasons (each step):

1. Risk of bias.
2. Inconsistency (statistical heterogeneity not explained).
3. Indirectness (population, intervention, comparator, or outcome differs from the question).
4. Imprecision (wide CIs that cross the threshold of clinical significance).
5. Publication bias.

Upgrade reasons (rare for observational):

1. Large effect.
2. Dose-response gradient.
3. All plausible confounders would bias toward the null.

Final certainty: high, moderate, low, or very low.

### Step 9 — Interpret and Conclude

The Discussion of a systematic review answers:

1. What is the strongest, most credible answer the evidence supports?
2. How certain is the answer (GRADE)?
3. Where do studies disagree, and why (clinical or methodological reasons)?
4. What are the limitations of the review itself (search dates, language, grey literature, unpublished data)?
5. What new research is needed (design, sample size, outcome, population)?

Avoid "more research is needed" without specifying which research, in which population, with which design.

## Common Failures of Systematic Reviews

1. **Insufficient search.** Missing Embase, missing trial registries, missing grey literature.
2. **Single reviewer.** Bias undetected at every stage.
3. **Inappropriate pooling.** Combining clinically heterogeneous studies into a single estimate.
4. **Combining high- and low-quality studies** without sensitivity analysis.
5. **Ignoring publication bias** when ≥ 10 studies were available.
6. **Using a numeric quality score** without checking for fatal individual flaws.
7. **Conflating clinical and statistical heterogeneity.** Low I² does not rule out clinical heterogeneity.
8. **No prespecification.** Subgroup and sensitivity analyses defined post-hoc.
9. **No registration.** PROSPERO registration is the minimum.
10. **Manuscript not built around the PRISMA flow diagram.** The flow diagram is the spine of the Results.

## Manuscript Structure

```
Title (must contain "systematic review" and/or "meta-analysis")
Structured abstract (Background, Methods, Results, Conclusions, Registration)
Introduction (clinical importance, gap, aim)
Methods (PRISMA-aligned; see references/method.md)
Results
  - PRISMA flow diagram (Figure 1)
  - Study characteristics (Table 1)
  - Risk-of-bias summary (Figure 2 or Table 2)
  - Primary outcome (forest plot or qualitative synthesis)
  - Secondary outcomes
  - Subgroup, sensitivity, and reporting bias analyses
  - GRADE summary of findings table
Discussion (key findings, comparison, limitations of the review, implications)
Conclusion
References
Supplementary materials
  - Full search strategies
  - PRISMA checklist
  - Risk-of-bias judgments per study
  - Excluded full-text studies with reasons
  - Statistical code (when feasible)
```

## Quality Checklist Before Submission

1. Protocol registered (PROSPERO); registration ID in the abstract.
2. PRISMA 2020 checklist completed and submitted as a supplement.
3. Full search strategies for each database in the supplement, with last-search dates.
4. PRISMA flow diagram present.
5. Two-reviewer screening, extraction, and risk-of-bias judgments documented.
6. Risk-of-bias tool appropriate to design.
7. GRADE certainty rating per primary and secondary outcome.
8. Heterogeneity reported with I², τ², and prediction interval.
9. Publication bias assessed if ≥ 10 studies pooled.
10. Excluded full-text studies listed with reasons (in supplement).
11. Forest plots include study weights, effect estimates with 95% CIs, heterogeneity statistics, and overall effect.
12. Causal language matched to evidence base; certainty stated.
13. References real, in citation order; tables and figures cited in text in order of appearance; body text free of em-dashes.
