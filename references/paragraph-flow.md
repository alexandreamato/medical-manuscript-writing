# Paragraph flow

Flow is the quality readers point to when prose feels clear, coherent, and inevitable. It is not a stylistic decoration. It is the manuscript-level effect of well-built paragraphs, ordered points, and intentional transitions. This file gives you concrete tools to diagnose and fix flow at three scales: paragraph, section, and manuscript.

For a structured self-reading from three reader perspectives that operationalizes the "pretend you are the reader" technique at the manuscript level, see `references/read-as-reader.md`. For sentence-level clarity rules (active voice, present tense for established results, hedging), see `references/scientific-writing-principles.md`.

## What flow really means

When a reader says "this paper flows," they mean three concrete things working together:

1. **Each paragraph has one job.** A topic sentence sets the job; every other sentence in the paragraph serves it.
2. **Paragraphs are sequenced in a logical chain.** Each paragraph builds on what came before and prepares what comes next.
3. **The reader is signposted.** Transitions, headings, and forward references tell the reader where they are and where they are going.

Flow breaks when one of these three fails. Most flow problems traced to the paragraph level: a paragraph trying to do two jobs, an out-of-order chain of paragraphs, or a missing transition between paragraphs.

## Paragraph-level rules

### The one-job rule

One paragraph, one job. State the job in the first sentence (topic sentence). Defend or develop it in the next three to six sentences. Close with a sentence that either resolves the point or hands off to the next paragraph.

A medical Methods paragraph that tries to define both the exposure and the outcome in the same six sentences is doing two jobs. Split it.

### Topic sentences carry the paper

Read just the first sentence of every paragraph in your Discussion. If those sentences alone tell a coherent story that maps onto the Discussion's purpose (key results, comparison with literature, limitations, implications), the paragraph flow is sound. If they read as a disconnected list, the paragraphs are out of order or are doing the wrong jobs.

### Paragraph length

Medical-manuscript paragraphs typically run 80 to 180 words (roughly 4 to 8 sentences). Paragraphs under 40 words are usually under-developed or are headings in disguise; paragraphs over 250 words usually contain two jobs that should be split. The Abstract is the exception: structured-abstract paragraphs are intentionally short.

## Section-level rules

### Order within a section

Each IMRaD section has a conventional internal order. Following it is not stylistic, it is reader-respect: reviewers and clinicians scan in that order.

| Section | Internal order |
| --- | --- |
| Introduction | Burden → what is known → gap → aim and hypothesis |
| Methods | Design → setting → participants → variables → bias → size → analysis → ethics |
| Results | Participant flow → baseline → primary outcome → secondary → sensitivity / subgroup |
| Discussion | Key result → comparison with literature → limitations → interpretation → generalizability |

If a paragraph appears in the wrong slot, even good prose will feel rough. The fix is to move it, not to rewrite it.

### Section transitions

End the final paragraph of a section with a sentence that bridges to the next. The Introduction's last sentence states the aim and hands off to Methods. The Methods' last paragraph (often Ethics) hands off to Results by completing the protocol description. The Results' last paragraph (often sensitivity analyses) hands off to Discussion by signalling the robustness of the main result. The Discussion's last paragraph (often generalizability) hands off to Conclusions.

## Manuscript-level rules

### Reverse-outline before final submission

A reverse outline is the single most efficient flow check for a finished draft.

How to reverse outline a manuscript:

1. Extract the title, the four-sentence aim statement, and every first sentence of every paragraph.
2. Read the extract as if it were the manuscript.
3. Mark each topic sentence with a one-word job label (definition, mechanism, prior evidence, gap, aim, design, eligibility, exposure, outcome, analysis, sensitivity, ethics, flow, baseline, primary, secondary, sensitivity, subgroup, summary, comparison, limitation, interpretation, generalizability, conclusion).
4. Check that the sequence of labels matches the conventional internal order for each section.
5. Flag any paragraph whose label repeats a label from a different section (e.g., a limitation discussed in Results), is missing (e.g., no generalizability paragraph), or sits in the wrong order.

The reverse outline is a one-page artefact. Edit it before editing the full manuscript.

### Cross-section consistency

Numbers in the Abstract must match the Results exactly. Variable names introduced in Methods must be used unchanged in Results and Discussion. Group labels and colour assignments on figures must stay constant across all figures (see `references/figures-and-tables.md` for the variable-to-colour mapping rule). Inconsistencies break flow because the reader pauses to verify whether two terms mean the same thing.

### Forward and backward references

Use forward references sparingly and only where useful: "as we show in Section 3.4" is acceptable in Methods if it prevents repeating a long analytic specification. Use backward references generously: "as shown in Table 1" is a flow aid because it tells the reader which evidence the current sentence is built on.

Every table and figure must be cited in the text in order of first appearance. Out-of-order citation forces the reader to flip back and forth and is a frequent reviewer complaint. See `references/figures-and-tables.md`.

## Transitions

Transitions are guideposts. They state the relationship between two adjacent thoughts. Use them at three scales: within a paragraph (between sentences), between paragraphs (first or last sentence), and between sections (last sentence of one, first of the next).

Functional categories of transitions and example words for each:

- Cause and effect: accordingly, as a result, because, consequently, hence, so, therefore, thus
- Comparison: also, likewise, similarly, in the same way
- Contrast or exception: although, but, by contrast, however, in contrast, instead, nevertheless, on the contrary, yet
- Example: for example, for instance, in particular, indeed, in fact, such as
- Sequence in space or argument: above, below, adjacent to, beyond, first, second, third, furthermore, moreover, finally
- Sequence in time: after, as soon as, at first, before, eventually, immediately, later, meanwhile, next, simultaneously, so far, soon, then, thereafter
- Summary or conclusion: as we have seen, in brief, in conclusion, in short, on the whole, taken together, therefore, to summarize

Avoid overusing the same transition. "However" three times in one paragraph signals an unresolved argument and irritates readers. Vary by function, not by ornament.

Avoid empty transitions ("It is interesting to note that ..."). They consume words without signalling a relationship.

## Read as your reader

Authorial blindness is real: the manuscript makes sense to you because you wrote it. Three concrete moves help break it:

1. Read the manuscript aloud. Sentences that need re-reading aloud are the same sentences readers will need to re-read silently.
2. Read after at least 24 hours away from the draft. The freshness gap restores reader perspective.
3. Read with the three personas in `references/read-as-reader.md`: a sceptical methodologist, a busy clinician, and an interested non-specialist. Each catches a different class of flow failure.

## Common flow problems and fixes

| Symptom | Root cause | Fix |
| --- | --- | --- |
| Paragraph reads as a list of disconnected facts | No topic sentence; paragraph has no single job | Write a topic sentence first; cut anything that does not serve it |
| Reader gets lost mid-paragraph | Paragraph is doing two jobs | Split into two paragraphs |
| Same fact appears in three sections | No reverse outline; jobs not separated | Pick one section that owns the fact; replace duplicates with a cross-reference |
| Methods feels longer than the journal allows | Procedural detail in body that belongs in supplement | Move detail to supplement; keep the principle in body |
| Discussion reads like a second Results section | Discussion is restating numbers instead of interpreting | Each Discussion paragraph must do interpretation, comparison, or implication; if it only restates numbers, cut or rework |
| Figures cited out of order | Order of figures not aligned to order of argument | Renumber figures to match the order of first textual citation |
| Numbers in Abstract differ from Results | Late edits not propagated | Lock Results numbers first; copy into Abstract last |
| Reader cannot find the main result | Buried in the middle of a long paragraph | Move the main result to the first sentence of Section 3.4 (or its equivalent) |

## See also

- `references/read-as-reader.md` — Structured manuscript-level self-reading from three reader personas
- `references/scientific-writing-principles.md` — Sentence-level clarity, voice, tense, hedging
- `references/figures-and-tables.md` — Citation-in-order rule, variable-to-colour mapping rule, table and figure construction
- `references/abstract.md`, `references/introduction.md`, `references/method.md`, `references/results.md`, `references/discussion.md` — Section-by-section structure
- `references/common-mistakes.md` — Speed audit including flow-related defects
- `references/paper-review.md` — Formal pre-submission checklist
- `references/writing-process.md` — When in the writing process to run a reverse outline (after draft, before submission)
