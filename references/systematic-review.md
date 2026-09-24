# Systematic Review and Meta-Analysis Writing Guide (Medical Research)

This guide is for writing the manuscript and conducting the methodological steps of a systematic review (with or without meta-analysis). It complements the PRISMA 2020 checklist in `references/reporting-standards.md`. The guidance draws on Wright, Brand, Dunn, and Spindler "How to Write a Systematic Review", Cochrane Handbook practice, and current PRISMA guidance.

## When a Systematic Review Is Worth Writing

A systematic review is appropriate when one or more of the following are true:

1. The clinical question has been studied in multiple primary studies, but the conclusions appear conflicting.
2. Individual primary studies are underpowered, and pooled analysis could yield a more precise overall estimate.
3. The literature on a question has not been formally synthesized in 3 or more years.
4. Stakeholders (guideline panels, payers, regulators) need a calibrated summary of the evidence.
5. The synthesis is needed to identify gaps and inform a future definitive trial.

It is **never** wrong to do a systematic review when individual studies are heterogeneous; what is sometimes wrong is to **pool** them in a meta-analysis. If clinical or methodological diversity makes an average effect meaningless for the question, present a structured synthesis without meta-analysis instead (see 7b).

## Systematic Review vs. Narrative Review vs. Meta-Analysis

| Form | Definition | When to use |
| --- | --- | --- |
| Narrative review | Author-selected literature; no formal search; subject to selection bias | Background framing; hypothesis-generating essays |
| Systematic review | Prespecified search and synthesis; minimizes bias; can be qualitative or quantitative | Comprehensive answer to a focused clinical question |
| Meta-analysis | Statistical pooling of effect estimates within a systematic review | When studies are sufficiently similar in population, intervention, comparator, and outcome |

A systematic review without a meta-analysis is sometimes called a "narrative synthesis" or a "structured qualitative synthesis". It is a legitimate output, especially when heterogeneity is high, but "narrative" does not mean informal: report how studies were grouped, the standardised metric, the synthesis method (for example vote counting based on the direction of effect, or summarising the range of effect estimates), and its limitations, following the SWiM reporting guideline (Campbell M, et al. BMJ. 2020;368:l6890. doi:10.1136/bmj.l6890; see `references/reporting-standards.md`).

Two companions to PRISMA 2020 are often needed: **PRISMA-S** for reporting the search itself, and **PRISMA-DTA** instead of PRISMA 2020 when the review question is diagnostic accuracy (`references/reporting-standards.md`).

## The Tradeoff: Heterogeneity, Internal Validity, External Validity

Heterogeneity is a double-edged sword:

1. **Narrow inclusion criteria** make the included studies more homogeneous and statistical pooling more defensible (higher internal validity), but the conclusions apply only to that narrow population (lower external validity).
2. **Broad inclusion criteria** improve generalizability (higher external validity), but pooling may be inappropriate (lower internal validity of the pooled estimate).

Decide where on this spectrum your review sits, and make the decision explicit in the protocol and the manuscript. Restricting to one outcome definition or one design (e.g., RCTs only) reduces clinical heterogeneity but biases the review against valuable studies that report the outcome differently.

## Step-by-Step Workflow

### Step 1: Frame the Research Question (PICO)

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

### Step 2: Write the Protocol Before Searching

The protocol is the most important bias-control step. Write and register it (PROSPERO; OSF for non-clinical) before starting the literature search. The protocol must specify:

1. Eligibility criteria (PICO + study designs + dates + languages).
2. Information sources (databases, registries, grey literature).
3. Search strategy (terms and Boolean operators) for at least one database.
4. Selection process (number of reviewers, conflict-resolution rule, software).
5. Data extraction items (one row per study, prespecified columns).
6. Risk-of-bias tool, with its version (for example RoB 2, ROBINS-I or ROBINS-I V2, QUADAS-2 or QUADAS-3, PROBAST+AI; see Step 6).
7. Effect measures (RR, OR, HR, MD, SMD).
8. Synthesis plan (qualitative summary; meta-analysis model; subgroups; sensitivity analyses).
9. Certainty assessment (GRADE).

A well-formulated protocol increases efficiency and reduces wasted screening time.

### Step 3: Construct the Search

A comprehensive search is the foundation of a credible systematic review. For PubMed-specific basics (Boolean operators, MeSH, field tags, Clinical Queries) see `references/pubmed-essentials.md`. The principles below apply across all databases:

1. **Search multiple databases.** Medline (via PubMed), Embase, Cochrane CENTRAL at minimum. No single database indexes all relevant trials, and Medline and Embase cover different journals, so searching one of them alone misses eligible studies (see the Cochrane Handbook chapter on searching for the evidence).
2. **Add specialty databases when relevant.** CINAHL (nursing), PsycINFO (psychology), LILACS / SciELO (Latin American), AIM (African), IMSEAR (South-East Asian), WPRIM (Western Pacific), KoreaMed.
3. **Search trial registries.** ClinicalTrials.gov, WHO ICTRP (which aggregates primary registries such as ReBEC and ISRCTN), and for the EU the CTIS public portal (euclinicaltrials.eu) plus the legacy EU Clinical Trials Register.
4. **Hand-search pertinent journals**, especially the most recent 6 months that may not yet be indexed.
5. **Search bibliographies** of included studies and of recent reviews on the topic.
6. **Search grey literature**: theses (ProQuest Dissertations), conference proceedings, regulatory documents (FDA, EMA), industry reports. In one methodological study, published trials yielded intervention effects on average 15% larger than grey literature (ratio of odds ratios 1.15, 95% CI 1.04 to 1.28; McAuley L, Pham B, Tugwell P, Moher D. Lancet 2000;356(9237):1228-31, doi:10.1016/S0140-6736(00)02786-0).
7. **Avoid English-only restrictions** when feasible; positive results are more likely published in English (English-language bias). If translation cost is prohibitive, state the limitation.
8. **Document the strategy.** Record exact search strings, field tags, dates of last search, and number of records retrieved per source. Provide the full strategy as a supplementary file.

Engage an information specialist or medical librarian if available; they substantially improve sensitivity.

### Step 4: Screen and Select

1. Import all records into reference-management software (Zotero, EndNote, Mendeley) or a screening platform (Rayyan, Covidence, DistillerSR).
2. Deduplicate.
3. **Two reviewers minimum, working independently.** Title/abstract screen first; full-text screen second. Resolve disagreements by discussion or by a third reviewer.
4. Document exclusions at full-text stage with reasons; this becomes the PRISMA flow diagram.
5. Inter-rater agreement (kappa) at the title/abstract stage is informative; aim for kappa ≥ 0.6 after pilot screening of 50 to 100 records.

### Step 5: Extract Data

1. Use a **standardized form**, paper or electronic. Pilot it on 3 to 5 studies before full extraction.
2. **Two reviewers minimum, independent extraction.** Reconcile discrepancies by discussion.
3. Capture, at minimum: study identifier, design, country, dates, population, intervention, comparator, outcome definition, effect estimate with 95% CI, sample sizes, follow-up duration, funding source, conflicts of interest.
4. Capture risk-of-bias judgments alongside data.
5. Contact authors for missing data when appropriate.

### Step 6: Assess Risk of Bias

Choose the tool by study design, and name the version in the protocol and the Methods (versions and sources checked 2026-09-23):

| Design | Tool and version | Reference | Official source |
| --- | --- | --- | --- |
| Randomized trials | RoB 2, current version 22 August 2019 (variants for cluster-randomized and crossover trials) | Sterne JAC, et al. BMJ. 2019;366:l4898. doi:10.1136/bmj.l4898 | https://www.riskofbias.info/welcome/rob-2-0-tool |
| Non-randomized studies of interventions | ROBINS-I (2016); ROBINS-I V2, revised release 20 November 2025, still labelled a draft by its developers and scoped to follow-up (cohort) studies | ROBINS-I: Sterne JAC, et al. BMJ. 2016;355:i4919. doi:10.1136/bmj.i4919. V2: no journal publication found; cite the website and release date | https://www.riskofbias.info/welcome/robins-i-v2 |
| Non-randomized follow-up studies of exposures | ROBINS-E, version of 24 March 2024 | Higgins JPT, et al. Environ Int. 2024;186:108602. doi:10.1016/j.envint.2024.108602 | https://www.riskofbias.info/welcome/robins-e-tool |
| Diagnostic accuracy studies | QUADAS-3 (published February 2026); QUADAS-2 (2011) remains in use in reviews whose protocol named it | QUADAS-3: Whiting PF, et al. Ann Intern Med. 2026;179:548-555. doi:10.7326/ANNALS-25-02104. QUADAS-2: Whiting PF, et al. Ann Intern Med. 2011;155(8):529-536. doi:10.7326/0003-4819-155-8-201110180-00009 | https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-3/ |
| Prediction model studies (regression or AI) | PROBAST+AI (2025), an update and extension of PROBAST (2019) | Moons KGM, et al. BMJ. 2025;388:e082505. doi:10.1136/bmj-2024-082505. PROBAST: Wolff RF, et al. Ann Intern Med. 2019;170(1):51-58. doi:10.7326/M18-1376 | https://www.probast.org/ |
| Cohort and case-control (quality appraisal) | Newcastle-Ottawa Scale (no versioned release) | See the official page | https://www.ohri.ca/programs/clinical_epidemiology/oxford.asp |
| Animal studies | SYRCLE risk-of-bias tool (2014) | Hooijmans CR, et al. BMC Med Res Methodol. 2014;14:43. doi:10.1186/1471-2288-14-43 | https://www.syrcle.network/ |
| Missing evidence in a meta-analysis (review level) | ROB-ME (2023) | Page MJ, et al. BMJ. 2023;383:e076754. doi:10.1136/bmj-2023-076754 | https://www.riskofbias.info/welcome/rob-me-tool |
| Appraising a systematic review (overviews, critical reading) | AMSTAR 2 (2017) | Shea BJ, et al. BMJ. 2017;358:j4008. doi:10.1136/bmj.j4008 | https://amstar.ca/Amstar-2.php |
| Certainty of a body of evidence | GRADE (GRADE Handbook) | See Step 8 | https://book.gradepro.org and https://www.gradeworkinggroup.org/ |

**Tool changes during a review.** In a review already under way, keep the tool (and version) named in the registered protocol (for example in PROSPERO), even when a newer version has appeared since; if you change it, report the change as a protocol deviation, with the reason, in the Methods (PRISMA 2020 item 24c, amendments to the protocol).

Prefer **domain-based judgments** over numerical quality scores: a single fatal flaw can be missed if you sum item scores. Two reviewers; reconcile differences.

The four high-yield biases to assess:

1. **Selection bias** (in trials: the randomization process). Was the allocation sequence random, and was it concealed until assignment? These are two different questions (see below). In trials from Cochrane pregnancy and childbirth meta-analyses, odds ratios were exaggerated by 41% when concealment was inadequate and by 30% when it was unclear (Schulz KF, Chalmers I, Hayes RJ, Altman DG. JAMA 1995;273(5):408-12, doi:10.1001/jama.273.5.408).
2. **Performance bias.** Were participants and providers blinded?
3. **Detection bias.** Were outcome assessors blinded?
4. **Attrition bias.** How were losses to follow-up handled? Was intention-to-treat used?

#### Sequence generation and allocation concealment are different questions

**Sequence generation** asks whether the list of assignments was produced by a process that includes an element of chance. **Allocation concealment** asks whether the people enrolling participants could foresee the next assignment before a participant was irreversibly enrolled. A random sequence can be left unconcealed (for example, a computer-generated list pinned to the ward noticeboard), and a non-random sequence cannot be concealed at all, because anyone who knows the rule can predict the next assignment.

1. **Sequence generation.**
   - *Adequate (random):* computer-generated random numbers; a random number table; coin tossing; shuffling cards or envelopes; throwing dice; drawing lots; minimization (generally implemented with a random element).
   - *Inadequate (non-random or predictable):* alternation or rotation; date of birth or date of admission; patient or case record number; allocation decided by clinicians or participants; allocation by availability of the intervention.
2. **Allocation concealment.**
   - *Adequate:* central or remote allocation controlled by a unit independent of the enrolling staff (telephone or web-based randomization service, independent central pharmacy); sequentially numbered, opaque, sealed envelopes opened only after the envelope is irreversibly assigned to the participant; sequentially numbered drug containers of identical appearance.
   - *Inadequate:* an open list or table of assignments; unsealed or non-opaque (translucent) envelopes, or envelopes not sequentially numbered; any deterministic rule (alternation, dates, record numbers), which enrolling staff can predict; fixed-size blocks in a single-centre trial where assignments are revealed after each enrolment, which can make the last assignments of a block predictable.

**How the tools handle them.** RoB 2 assesses both together in domain 1, "bias arising from the randomization process" (signalling questions 1.1, random sequence; 1.2, concealment; 1.3, baseline imbalance suggesting a problem), and gives one judgment for the domain. The original Cochrane tool (RoB 1; Higgins JPT, et al. BMJ. 2011;343:d5928, doi:10.1136/bmj.d5928) judged random sequence generation and allocation concealment as two separate domains. Examples above follow the RoB 2 guidance document (22 August 2019, riskofbias.info) and Cochrane Handbook version 6.5, chapter 8 (section 8.3).

### Step 7: Synthesize

#### 7a. Qualitative synthesis

Always include this step. Tabulate study characteristics: design, population, intervention, comparator, outcome, effect estimate, risk-of-bias judgment, certainty rating.

#### 7b. Decide whether to pool

There is no universal rule. Whether to pool depends on the review question, on whether participants, interventions, comparisons and outcomes are similar enough for an average to be clinically meaningful, and on the synthesis method planned (Cochrane Handbook version 6.5, chapter 10; the MECIR box in section 10.10 asks authors to undertake a meta-analysis only if participants, interventions, comparisons and outcomes are judged sufficiently similar to ensure a clinically meaningful answer). A systematic review need not contain a meta-analysis. The conditions below call for caution and an explicit justification in the protocol and the Methods, not an automatic ban:

1. **Clinical diversity** (different populations, intervention doses, comparators or outcome definitions). Ask whether an average effect would answer the question; if not, pool within clinically coherent groups or synthesise without meta-analysis (SWiM).
2. **Methodological diversity** (different designs, analysis populations, risk-of-bias profiles). Consider separate syntheses by design, or prespecified subgroups.
3. **Statistical heterogeneity.** The Handbook bands for I² are rough guides and overlap on purpose: 0% to 40% might not be important; 30% to 60% may represent moderate, 50% to 90% substantial, and 75% to 100% considerable heterogeneity (section 10.10.2). How much a given I² matters depends on the magnitude and direction of the effects and on the strength of the evidence for heterogeneity (the P value of the chi-squared test, or a CI for I²), and I² is very uncertain when studies are few. Wide variation, and especially inconsistency in the direction of effect, may make an average misleading; explore it (7d) and report the prediction interval rather than stopping at a threshold.
4. **Few studies.** A meta-analysis of two or three studies is possible, but the between-study variance (τ²) is poorly estimated, so a random-effects result can be unstable. Options, stated in the protocol where possible: the Hartung-Knapp-Sidik-Jonkman (HKSJ) adjustment for the CI of a random-effects estimate (which can give very wide intervals with two or three studies); a fixed-effect (common-effect) model, which is more stable with few studies but ignores heterogeneity and must be presented with that caveat; and a sensitivity analysis comparing methods (Handbook sections 10.10.4.2 and 10.10.4.5). Present the result cautiously, with the number of studies stated beside it.
5. **High risk of bias.** Pooling cannot remove bias from the studies being pooled: a precise estimate from biased studies is still biased. Handle it with a sensitivity analysis restricted to studies at low risk of bias (or stratified by risk of bias), and let it feed the GRADE risk-of-bias domain, rather than by silently pooling everything or silently excluding studies.

#### 7c. Meta-analysis when appropriate

1. Choose the model: **fixed-effect** (assumes one true effect) or **random-effects** (assumes a distribution of true effects). Random-effects is the default in most clinical contexts.
2. Choose the effect measure: RR, OR, HR for binary; MD, SMD for continuous.
3. Report the pooled estimate with 95% CI, heterogeneity (I², τ², 95% prediction interval), and the test for overall effect.
4. Forest plot is mandatory.
5. **Engage a statistician early**: at the protocol stage, not after extraction.

#### 7d. Heterogeneity exploration

When heterogeneity is high, do not stop at "I² = 78%". Explore it:

1. Subgroup analysis by prespecified clinical or methodological factor.
2. Meta-regression.
3. Sensitivity analyses excluding high-risk-of-bias studies.

#### 7e. Reporting bias

Assess the risk of bias due to missing evidence in every review, whatever the number of studies. Only the funnel-plot methods depend on having enough studies.

With any number of studies:

1. Search trial registries (ClinicalTrials.gov, WHO ICTRP) and grey literature for unpublished studies (Step 3).
2. Compare each study's protocol, registry entry or statistical analysis plan with its publication, to detect results that were measured but not reported, or reported selectively (selective outcome reporting).
3. Judge the risk of bias due to missing evidence for each meta-analysis with ROB-ME (Page MJ, et al. BMJ. 2023;383:e076754. doi:10.1136/bmj-2023-076754; https://www.riskofbias.info/welcome/rob-me-tool), and carry the judgment into the GRADE publication-bias domain.

Funnel-plot methods. As a rule of thumb, asymmetry tests only when the meta-analysis has at least 10 studies (Cochrane Handbook version 6.5, section 13.3.4.4: with fewer studies, the tests have too little power to distinguish chance from real asymmetry; Sterne JAC, et al. BMJ. 2011;343:d4002. doi:10.1136/bmj.d4002). The plot itself may be shown with fewer studies, but it cannot support a conclusion:

1. Funnel plot (visual), read as a display of small-study effects, of which publication bias is only one possible cause; with fewer than 10 studies, descriptive only.
2. Egger test (continuous outcomes), or Peters or Harbord tests (binary outcomes) for funnel-plot asymmetry, with at least 10 studies.
3. Trim-and-fill or other corrections only as sensitivity analyses.

### Step 8: Rate Certainty of Evidence (GRADE)

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

### Step 9: Interpret and Conclude

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
5. **Ignoring missing evidence.** No registry search, no comparison of protocols with publications, no ROB-ME judgment; or, with 10 or more studies in a meta-analysis, no funnel plot or asymmetry test. With fewer than 10 studies, running an asymmetry test anyway is the opposite failure.
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
3. Full search strategies for each database in the supplement, with last-search dates (PRISMA-S).
4. PRISMA flow diagram present.
5. Two-reviewer screening, extraction, and risk-of-bias judgments documented.
6. Risk-of-bias tool appropriate to design, with version stated, and the same as in the protocol (or the change reported and justified).
7. GRADE certainty rating per primary and secondary outcome.
8. Heterogeneity reported with I², τ², and prediction interval.
9. Risk of bias due to missing evidence assessed for every synthesis (registries, protocol-publication comparison, ROB-ME); funnel plot and asymmetry tests only for meta-analyses with 10 or more studies.
10. Excluded full-text studies listed with reasons (in supplement).
11. Forest plots include study weights, effect estimates with 95% CIs, heterogeneity statistics, and overall effect.
12. Causal language matched to evidence base; certainty stated.
13. Cross-section consistency checks pass: `references/paper-review.md` (Cross-Section Consistency Checks).
