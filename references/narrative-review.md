# Narrative Literature Review and Evidence-Based Clinical Review (Medical Research)

This guide is for narrative review papers and evidence-based clinical updates — review articles whose central contribution is the synthesis itself, not a primary study. For PRISMA-aligned systematic reviews and meta-analyses, see `references/systematic-review.md`. For background framing inside an original research article, see `references/related-work.md`.

The guidance synthesizes Van Wee & Banister (Transp Rev 2016) "How to Write a Literature Review Paper", Siwek et al. (Am Fam Physician 2002) "How to Write an Evidence-Based Clinical Review Article", and Gülpınar & Güçlü (Turk J Urol 2013) "How to Write a Review Article".

## Three Kinds of Review Article (Choose Deliberately)

| Type | What it does | When to write it |
| --- | --- | --- |
| Narrative review / "clinical update" | Selectively reviews the literature on a broad topic; integrates current knowledge for clinical practice; allows author judgement and emphasis. | Topic of broad relevance; need to teach or refresh practice; new evidence prompts a change in practice. |
| Non-quantitative systematic review | Comprehensive, prespecified search and selection; synthesizes all relevant evidence on a focused question. | Focused clinical question; prior reviews are out of date or contradictory. |
| Meta-analysis (quantitative systematic review) | Pools effect estimates from multiple studies. | Multiple studies with comparable population/intervention/outcome and quantifiable effect estimates. |

Narrative reviews and clinical updates are **not** systematic reviews. Each has a place; mixing the labels misleads the reader.

## The Cardinal Rule — Add Value

The single biggest distinction between a publishable review article and a manuscript that gets desk-rejected is **added value**. An overview restates what is known; a review **adds** something. Decide upfront which kind of value the paper delivers:

| Option for added value | What you contribute |
| --- | --- |
| Empirical insights | A synthesis of the state of knowledge, gaps, and methodological weaknesses across studies. |
| Methodologies | Overview of dominant methods used, their pros and cons, opportunities for new methods. |
| Theories or mechanisms | Comparison of competing biological or clinical explanations; impact of the chosen theory on results. |
| Gaps and a research agenda | Map of unresolved questions; concrete future-research directions. |
| Real-world relevance | Translation of evidence into clinical, policy, or implementation guidance, sometimes via case studies. |
| Conceptual model | A new framework that organizes the evidence and exposes which parts are well or poorly supported. |

The added value should permeate the whole paper, not just the conclusions.

## Reasons Not to Write a Review

Before drafting, check that none of these apply:

1. A recent review of the same scope already exists.
2. The literature is too thin to support a review (consider broadening the scope, or wait).
3. The literature is so vast that the review will lose focus (narrow the scope).
4. You have nothing distinctive to add — no new angle, no new methodological focus, no new population, no new framework.

Writing a review takes substantial time. The reading is one part; the synthesis and writing are usually longer than for a primary research paper. Plan accordingly.

## Topic Selection (Evidence-Based Clinical Review)

For an evidence-based clinical update, the best topics meet **all** of:

1. **Common in practice** for the target audience (avoid rarities and curiosities).
2. **Recent new evidence** — diagnostics, therapeutics, prevention, deimplementation.
3. **Practice-changing potential** — new evidence prompts a change, or new evidence that an established treatment is no longer beneficial (or is harmful).

State the continuing-medical-education or practice-relevance objectives in a separate table at the start.

## Patient-Oriented Evidence That Matters (POEM) vs. Disease-Oriented Evidence (DOE)

A central distinction for clinical review writing:

| Type | What it measures | Example |
| --- | --- | --- |
| POEM | Outcomes that matter to patients (mortality, morbidity, quality of life, function, symptoms). | "Does this drug reduce mortality after MI?" |
| DOE | Surrogate or laboratory endpoints that may or may not translate into POEM. | "Does this drug reduce LDL cholesterol?" |

Where possible, base recommendations on POEM. When only DOE is available, say so explicitly: `Although [DOE finding], it has not yet been shown that [intervention] improves [POEM outcome].` Antiarrhythmic therapy after MI is the classic cautionary example: drug X reduces premature ventricular contractions on ECG (DOE) but increases mortality (POEM).

## Search Strategy — Be Explicit

The methodological section is the weakest part of most narrative review papers. For PubMed-specific basics (Boolean operators, MeSH, field tags, Clinical Queries), see `references/pubmed-essentials.md`. Even when the review is non-systematic, report:

1. **Databases searched.** Medline (via PubMed), Embase, Cochrane CENTRAL, plus specialty databases when relevant (CINAHL for nursing, PsycINFO for psychology, LILACS / SciELO for Latin American sources). For evidence-based clinical reviews, add: Cochrane Library, BMJ Clinical Evidence, AHRQ guidelines, USPSTF, National Guideline Clearinghouse, TRIP database.
2. **Search terms.** Including MeSH headings, free-text terms, Boolean operators (AND, OR, NOT) and wildcards (`transport*`).
3. **Languages covered** and the rationale for any restriction.
4. **Time frame** with rationale (e.g., post-1998 because earlier reviews exist; or last 5 years because the methodology emerged then).
5. **Geographic or contextual restrictions**, with rationale (e.g., only US studies because of healthcare-system context).
6. **Snowballing.** Distinguish **forward snowballing** (citations TO a paper, found in tools like Web of Science) from **backward snowballing** (citations IN a paper). Both should be made explicit.
7. **Selection criteria.** If the search returns more papers than the review will cover, describe the selection rule (citation count, recency, geographical balance, methodological fit, seminal status).

Most narrative reviews in medicine cite between 30 and 100 papers; ranges outside that should be justified.

## Levels of Evidence

For evidence-based clinical reviews, rate the evidence supporting each key clinical recommendation. Two practical schemes:

### Simple ABC scheme (Siwek 2002; AFP)

| Level | Evidence type |
| --- | --- |
| A | High-quality RCT considering all important outcomes, or high-quality meta-analysis with comprehensive search. |
| B | Other evidence: well-designed non-randomized clinical trial; non-quantitative systematic review with appropriate search; lower-quality RCT; clinical cohort or case-control study with non-biased selection and consistent findings; high-quality historical uncontrolled study or epidemiologic study with compelling findings. |
| C | Consensus or expert opinion. |

In-text format: `[Evidence level A, RCT]`, `[Evidence level B, non-randomized clinical trial]`, `[Evidence level C, expert opinion]`.

### Question-type-specific hierarchy (Gülpınar & Güçlü 2013)

The level of evidence depends on the type of clinical question:

| Level | Intervention | Diagnosis | Prognosis | Etiology |
| --- | --- | --- | --- | --- |
| I | Systematic review of Level II studies | Systematic review of Level II studies | Systematic review of Level II studies | Systematic review of Level II studies |
| II | RCT | Cross-sectional study in consecutive patients | Inception cohort study | Prospective cohort study |
| III | Non-randomized experimental study; comparative observational studies (cohort, case-control) | Cross-sectional study in non-consecutive cases; diagnostic case-control | Untreated control arm of an RCT; retrospective cohort | Retrospective cohort, case-control |
| IV | Case series | Case series | Case series | Cross-sectional |

Always cite primary research, not secondary review articles, when rating evidence. Systematic reviews that pool RCTs are the best basis for ratings.

### Modern alternative — GRADE

For a more granular per-outcome rating, use GRADE (high / moderate / low / very low certainty). See `references/statistical-reporting.md` and `references/systematic-review.md`.

## Methodological Cautions in Narrative Reviews

These are the failures most often flagged by reviewers:

1. **Unfair criticism of original authors.** Do not criticize a primary study for not addressing something outside its scope. State it as an observation, not a flaw.
2. **Naïve averaging of heterogeneous results.** A 5-patient case series and a 5,000-patient RCT cannot be averaged with equal weight. Present individual results with their sample sizes; if averaging, weight by precision.
3. **Reporting only averages.** The range of effects is at least as informative as the mean.
4. **Hidden attribution of conclusions.** State explicitly whether a conclusion is from the original authors or your interpretation: `Smith and Jones reported that ...` vs. `In our reading, the studies collectively suggest ...`.
5. **Speculation without flagging.** Speculation about mechanism is permissible if marked: `We speculate that ...`, `In the authors' opinion ...`. Unflagged speculation reads as overreach.
6. **Selective referencing.** Avoid citing only the studies that support your conclusion. If there is a controversy, present the full scope.
7. **Citing reviews when primary sources exist.** Cite the original trial, not a review of it.
8. **Anecdotes as evidence.** Conventional wisdom (`prolonged bed rest for low back pain`) often does not survive scientific scrutiny.
9. **Subspecialty-population evidence presented as primary-care guidance** (or vice versa). Note the population context of the original studies.

## Manuscript Structure

A typical narrative review structure:

```
Title
Authors and affiliations

1) Abstract (often structured: background, methods, conclusions; include the main conclusions and the added-value claim, not just a description)
2) Introduction
   - Topic and clinical relevance
   - Existing reviews on the topic and how this one differs
   - Aim, scope, and target audience
   - CME / practice-relevance objectives (in a table)
3) Methods (yes, even for narrative reviews)
   - Databases searched, dates, languages
   - Search terms and Boolean operators
   - Selection criteria and rationale
   - Snowballing strategy
4) Body of the review (sections by theme, not by study)
   - Etiology / pathophysiology
   - Clinical presentation
   - Diagnostic evaluation
   - Differential diagnosis
   - Treatment (medical, surgical, supportive, follow-up)
   - Prognosis
   - Prevention
   - Future directions
   With ratings of evidence inline for each key clinical recommendation
5) Discussion / Synthesis
   - Strengths and gaps in the evidence base
   - Controversies, unresolved questions, recent developments
   - Limitations of the review (search, selection, language)
6) Conclusion / Take-home points (often a separate summary table)
References
```

## Structuring the Body — Tables Are Powerful

Synthesize evidence in tables, not in prose lists. Common table designs:

1. **Author × characteristics** (one row per study; columns: author, year, design, country, sample, key result). Long tables can move to an appendix.
2. **Theme × evidence** (one row per theme; columns: definition, key references, level of evidence, recommendation). Easier for clinical updates.
3. **Method × pros and cons** for methodological reviews.
4. **Intervention × outcomes** for therapeutic comparisons.

A summary "key take-home points" table near the end is particularly valuable for clinical updates.

## Common Reasons Narrative Reviews Are Rejected

1. **The paper is an overview, not a review.** No added value.
2. **Aims not met.** Stated objectives in the introduction are not addressed in the conclusion.
3. **Premature submission.** Weak structure, partial evidence, no real synthesis.
4. **No methodology section.** Reader cannot judge how comprehensive the review is.
5. **Unweighted or hidden citation choices.** Selective referencing toward a preferred conclusion.
6. **Ratings of evidence missing or inconsistent.**
7. **Topic too broad or too narrow.** "Hypertension" is too broad; "blood pressure response in left-handed adults aged 47" is too narrow.
8. **Heavy reliance on review articles** instead of primary sources for rated recommendations.
9. **Inappropriate journal choice.** Some general medical journals do not accept narrative reviews; check the journal's policy.

## Quality Checklist Before Submission

1. Is the topic common, relevant, and accompanied by recent practice-changing evidence?
2. Is the type of review (narrative update vs. systematic vs. meta-analysis) clearly identified in the title and abstract?
3. Is the added-value claim explicit in the abstract and conclusion?
4. Are the methods (databases, terms, languages, dates, selection rule, snowballing) reported?
5. Are key clinical recommendations rated (A / B / C, GRADE, or per-question hierarchy)?
6. Is POEM emphasized over DOE, with DOE flagged when no POEM is available?
7. Are recommendations supported by **primary** research, not by secondary reviews?
8. Are conclusions and interpretations explicitly attributed (original authors vs. review authors)?
9. Are tables used to synthesize, with a key-take-home-points summary table?
10. Are references real, in citation order, and balanced between classic and recent?
11. Is the body free of em-dashes (see `references/manuscript-conventions.md`)?
12. Does the abstract include the main conclusions and added value, not just a description?

## Source

Synthesized from:

- Van Wee B, Banister D. How to write a literature review paper? Transp Rev 2016;36(2):278-288.
- Siwek J, Gourlay ML, Slawson DC, Shaughnessy AF. How to write an evidence-based clinical review article. Am Fam Physician 2002;65(2):251-258.
- Gülpınar Ö, Güçlü AG. How to write a review article? Turk J Urol 2013;39(Suppl 1):44-48.
- Hoogenboom BJ, Manske RC. How to write a scientific article. Int J Sports Phys Ther 2012;7(5):512-517.
