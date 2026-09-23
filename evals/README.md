# Behaviour evals

The build kit's tests show that the code works. These evals show whether an agent using the skill **follows its rules**: scope of a point edit, references that exist but do not support a claim, non-significant results, meta-analysis of few studies, missing ethics information, translation, numbers derived from raw data, and an unknown target journal.

`evals.json` follows the skill-creator schema: each case has a prompt, a description of success and a list of observable expectations. All manuscript text in the prompts is fictional.

## Running them

With the skill-creator skill, ask for an evaluation of this skill: it runs each prompt with and without the skill and grades every expectation. Compare the pass rates, and read the failures: a failed expectation points to the rule (in `SKILL.md` or a guide) that the agent did not apply.

Re-run after any change to `SKILL.md` or to the guides the cases touch (`statistical-reporting.md`, `systematic-review.md`, `non-native-authors.md`, `citation-styles.md`, `ethics-and-integrity.md`).

## Adding a case

Add a case when a real session shows the agent getting something wrong: write the smallest prompt that reproduces it and expectations a grader can check without judgement ("keeps 0.72, 0.55 and 0.94", not "writes well").
