# Reading Your Own Draft as a Reader

This file is a structured technique to read your own draft from three reader perspectives, before running the formal pre-submission checklist. The framework adapts Trisha Greenhalgh's "How to Read a Paper" critical-appraisal questions (BMJ 1997 series; *How to Read a Paper: The Basics of Evidence-Based Medicine*, BMJ Publishing Group) to **self-review** of your own manuscript.

The premise: reviewers and readers approach your paper with three very different mindsets. By simulating each, you find the weaknesses they would find — before they find them.

## Where this fits

| Stage | File | Purpose |
| --- | --- | --- |
| Drafting | `references/writing-process.md` | Drafting order, daily-writing strategy |
| Sentence-level revision | `references/scientific-writing-principles.md` | Wordy → concise, hedging, voice, tense |
| Paragraph flow | `references/paragraph-flow.md` | Reverse outlining, transitions |
| **Critical self-reading (this file)** | `references/read-as-reader.md` | **Simulated reading by 3 reader personas** |
| Formal pre-submission checklist | `references/paper-review.md` | 5-dimension rejection-risk audit |
| Post-submission | `references/responding-to-reviewers.md` | Point-by-point response |

This file is the layer **between** sentence-level revision and the formal pre-submission checklist. It catches problems that the checklist alone does not surface — the kind that emerge only when someone reads the draft cold.

## The Three Reader Personas

Different readers approach the same paper with different goals. Each is a real audience your paper must serve.

### Persona 1 — The Skeptical Methodologist

Reads Methods and Statistical Analysis **first**, before Results. Greenhalgh: "If you are deciding whether a paper is worth reading, you should do so on the design of the methods section and not on the interest of the hypothesis or the speculation in the discussion." If Methods does not stand up, this persona stops reading and rejects.

Diagnostic questions to ask of your own draft:

1. **What clinical question is being addressed?** Read only the first paragraph of the Introduction. Can you state the question in one sentence? If not, the gap statement is unclear.
2. **Is the study design appropriate for the question?** Therapy questions need RCTs; prognosis needs longitudinal cohorts; etiology needs cohort or case-control; diagnostic accuracy needs cross-sectional with reference standard. See `references/study-types.md` for the design-by-question matrix.
3. **Are the variables adequately measured?** Each outcome and exposure has an instrument, units, timing, and ascertainer specified. Check by trying to operationalize a replication.
4. **Is the sample size justified?** Read the sample-size paragraph and verify the assumed effect size, alpha, power, and dropout inflation are stated.
5. **Are selection, information, and confounding bias addressed?** Selection: how were participants identified, with what risk of selective enrollment? Information: how were exposures and outcomes measured, with what blinding? Confounding: what was adjusted for, and on what basis?
6. **Do the conclusions match the design?** RCT may say "reduced"; observational must say "was associated with". A claim like "X causes Y" from a cross-sectional study is a red flag.
7. **Is multiplicity addressed?** Multiple primary outcomes? Many subgroups? Were exploratory analyses labelled as such?
8. **What is the most likely fatal flaw a methodologist reviewer would find?** Force yourself to name one, even if the paper looks solid.

Action when this persona finds something: edit Methods or Discussion to address the concern explicitly. If the design genuinely cannot answer the question, the manuscript may need redirection (e.g., reframe as hypothesis-generating; downgrade causal language; add a sensitivity analysis).

### Persona 2 — The Busy Clinician

Reads only the **Title → Abstract → Conclusion of Discussion → Table 1 → primary outcome figure**. Total time: 3 to 5 minutes. After that, decides whether to read the full paper, file it for later, or ignore.

Diagnostic questions:

1. **In 30 seconds reading the abstract, do I know the question, design, primary outcome, headline numerical result, and conclusion?** If not, the abstract is failing.
2. **Is the effect size clinically meaningful, not just statistically significant?** A relative risk reduction of 5% may be statistically significant but clinically trivial. The Discussion should distinguish.
3. **Does the studied population resemble my patients?** Eligibility, age range, comorbidity burden, country, era of treatment, and care setting must be visible quickly. Read Table 1.
4. **What would I do differently tomorrow because of this paper?** Force the answer. If you cannot complete the sentence "Because of this paper, I will ...", the take-home message is missing.
5. **Are the limitations that affect my decision clear?** Single-centre? Open-label? Surrogate outcome? Short follow-up? These belong in the abstract conclusion, not buried in paragraph 5 of the Discussion.
6. **If I act on this conclusion and turn out wrong, how big is the harm?** A high-stakes claim with weak design should trigger more cautious wording.
7. **Does the title accurately set expectations?** A title saying "X reduces Y" should not be followed by an abstract saying "X was associated with Y".

Action when this persona finds something: edit Title, Abstract, and Conclusion paragraph of the Discussion to surface the answer explicitly. Most editing here is **promotion**: bringing a fact that exists deeper in the paper to a more prominent position.

### Persona 3 — The Non-Specialist Reader

Greenhalgh: many published papers are technically correct but "so badly written that they are incomprehensible". This persona is a colleague from a different specialty, a graduate student outside your field, or — for journals with broad readership — a clinician who has not worked on your topic. They catch language failures and structural confusion.

Diagnostic questions:

1. **Is each abbreviation defined at first occurrence in the body text?** Abbreviations defined in the abstract do not carry over.
2. **Does the Introduction set up the problem without assuming I already know the field?** A non-specialist should reach the gap statement smoothly. Open with burden, then current management, then the unresolved question.
3. **Does each paragraph have a single message stated in the first sentence?** Run the reverse-outlining test from `references/paragraph-flow.md`.
4. **Are critical technical terms accompanied by a one-clause explanation or context?** "We used inverse probability of treatment weighting (IPTW), which weights each participant by the inverse of their predicted probability of being in their assigned group, to adjust for measured confounding." beats "We used IPTW".
5. **Can I follow Methods → Results without flipping back?** The order of analyses in Results should mirror the order in Methods.
6. **Do the tables and figures stand alone?** Read each caption without reading the body text. Are units, sample sizes, error-bar definitions, and abbreviations all in the caption?
7. **Is causal language calibrated to the design** in a way a non-specialist would notice if it were wrong? Phrases like "X cures Y" should be replaced with carefully calibrated verbs.
8. **Read aloud once.** Sentences that catch your tongue catch the reader's eye too.

Action when this persona finds something: most edits are local — define abbreviations, add a clarifying clause, split a long sentence, move a forward reference. See `references/scientific-writing-principles.md` for the sentence-level rules.

## The Read-As-Reader Workflow

Run the three passes in order, with cooling time between them when possible.

### Pass A — Methodologist (60–90 minutes)

1. Print or fullscreen the manuscript.
2. Read **Methods** and **Statistical Analysis only** first. Skip Introduction, Results, Discussion.
3. Answer the eight Persona 1 questions in writing.
4. List concerns in an Action Items table (see template below).

### Pass B — Busy Clinician (10 minutes)

1. Reset (ideally next day, or after a coffee break).
2. Read **only** Title → Abstract → Conclusion paragraph of the Discussion → Table 1 → primary outcome figure caption. Do not read the body.
3. Answer the seven Persona 2 questions.
4. List concerns. Most will be about visibility (information exists but is not surfaced).

### Pass C — Non-Specialist (60 minutes)

1. Reset (ideally 1 to 2 weeks later — see "cooled-manuscript pass" in `references/writing-process.md`). Or hand the draft to a real non-specialist colleague.
2. Read the manuscript front-to-back, slowly.
3. Mark every place you stumble: undefined abbreviations, unclear sentences, forward references, missing transitions, confusing figures.
4. Answer the eight Persona 3 questions.

After all three passes, consolidate the action items, prioritize, and edit.

## Action Items Template

Track findings in a single document:

```
| Pass | Issue                                      | Location           | Severity | Edit proposed                                    |
| ---- | ------------------------------------------ | ------------------ | -------- | ------------------------------------------------ |
| A    | Sample-size assumption source not cited    | Methods, p7 l140   | High     | Add reference to pilot study; state effect size  |
| A    | Causal verb in Discussion for cohort study | Discuss, p21 l455  | High     | Change "reduced" to "was associated with lower"  |
| B    | Effect size present but not in abstract    | Abstract           | High     | Add HR + 95% CI to abstract Results              |
| B    | Single-centre limitation not in abstract   | Abstract           | Medium   | Add to abstract Conclusion                       |
| B    | Title overpromises                         | Title              | Medium   | Change "prevents" to "was associated with lower" |
| C    | "ATM" used without definition              | Results, p15 l312  | Low      | Define on first use in body text                 |
| C    | Figure 2 caption missing n                 | Figure 2           | Low      | Add n=625 per arm to caption                     |
| C    | Forward reference to Table 4 in Methods    | Methods, p9 l188   | Low      | Reorder so Table 4 is mentioned in Results first |
```

Severity scale:

- **High** — would likely trigger a major-revision request or rejection if a reviewer found it.
- **Medium** — would prompt a reviewer comment but probably not block acceptance.
- **Low** — copy-editing level; fix in passing.

Address all High items first. Medium items often resolve as side-effects of High edits. Low items are fixed in the final polish pass.

## Common Patterns Each Persona Finds

After running this technique on dozens of manuscripts, certain patterns recur. Knowing them lets you pre-empt the corresponding fix.

### Patterns Persona 1 (Methodologist) finds

1. **Mismatched design and conclusion.** Cross-sectional study with causal language in Discussion. Cohort study claiming an "intervention effect".
2. **Underspecified primary outcome.** "Quality of life" without naming the instrument; "improved cognition" without the score and timepoint.
3. **Unjustified sample size.** Effect-size assumption appears from nowhere. Common in retrospective studies that "use what was available".
4. **Unhandled confounding.** Adjusted analyses listed but the rationale for variable selection is not stated; no DAG; no E-value sensitivity.
5. **Multiplicity ignored.** Multiple "primary" outcomes, or many subgroup analyses, with no adjustment or labelling.

### Patterns Persona 2 (Busy Clinician) finds

1. **Effect size hidden.** The headline number is in the body but not in the abstract.
2. **Population mismatch surfacing late.** Eligibility criteria so narrow that the result does not transport to general practice — this should be in the abstract conclusion, not paragraph 6 of the Discussion.
3. **Take-home message vague.** Conclusion ends with "more research is needed" without saying what kind.
4. **Title-Abstract-Conclusion mismatch.** Title says one thing; abstract says another; Discussion says a third. Fix by writing Conclusion → Title → Abstract in that order to align.
5. **Over-promising Title.** Verbs like "prevents", "cures", "treats" when the design supports only "was associated with lower risk of".

### Patterns Persona 3 (Non-Specialist) finds

1. **Abbreviation explosion.** First mention in body text uses the abbreviation as if defined in abstract.
2. **Methods bouncing.** Statistical analysis described before outcome ascertainment, even though Outcomes section depends on it.
3. **Captions that don't stand alone.** Figure shows error bars but caption does not say SD vs. SEM vs. CI; Table 1 footnote missing abbreviations.
4. **Pronouns without antecedents.** "This was unexpected" — what is "this"? Always pair "this" with a noun.
5. **Sentence length variance gone.** Multiple 30+ word sentences in a row, or every sentence chopped to 10 words. Mix lengths.

## Working with a Real Non-Specialist Reader

If a real colleague is available, this is more powerful than self-simulation. Brief them carefully:

1. **Pick the right reader.** Same training level (medical or research) but **different specialty**.
2. **Set the framing.** "I want you to tell me where you stumbled, not whether you agreed with the science."
3. **Give them the eight Persona 3 questions** and ask them to mark up the draft as they read.
4. **Do not defend in real time.** Write down their feedback; debate it later.
5. **Give them a deadline** (typically 1 week) — open-ended requests rarely return.

This is the "general internal reviewer" pattern from `references/writing-process.md`.

## Combining the Three Passes — A Sequencing Guide

Recommended sequence relative to the rest of the workflow:

```
1. First draft complete                           (writing-process.md drafting order)
2. Reverse outlining and paragraph flow           (paragraph-flow.md)
3. Sentence-level revision                        (scientific-writing-principles.md)
4. Pass A — Methodologist self-read              (this file)
5. Address High items from Pass A                 (re-edit Methods, Discussion)
6. Pass B — Busy Clinician self-read             (this file)
7. Address High items from Pass B                 (re-edit Title, Abstract, Conclusion)
8. Cool the manuscript for 1 to 2 weeks           (writing-process.md)
9. Pass C — Non-Specialist read or hand to colleague (this file)
10. Address all items from Pass C                 (final polish)
11. Formal pre-submission checklist                (paper-review.md)
12. Reporting checklist + adherence statement      (reporting-standards.md)
13. Submit
```

The three personas are designed to be **complementary**, not redundant. Skip none.

## See Also

1. **Reverse outlining and paragraph flow** (the level below this one): `references/paragraph-flow.md`.
2. **Sentence-level revision** that Persona 3 will reveal: `references/scientific-writing-principles.md`.
3. **Formal 5-dimension rejection-risk audit** (the level above this one): `references/paper-review.md`.
4. **Writing process and three-pass cooling**: `references/writing-process.md`.
5. **Causal language calibrated to design** (Persona 1 + 2): `references/study-types.md`.
6. **Reporting checklist that catches structural omissions** Persona 1 will flag: `references/reporting-standards.md`.

## Source

The framework adapts Trisha Greenhalgh's "How to Read a Paper" series:

- Greenhalgh T. How to read a paper: getting your bearings (deciding what the paper is about). BMJ 1997;315:243-246.
- Greenhalgh T. *How to Read a Paper: The Basics of Evidence-Based Medicine*. BMJ Publishing Group; 2001 (subsequent editions through 2019).

Greenhalgh's questions were designed to appraise other authors' papers; this file inverts them onto the author's own draft.
