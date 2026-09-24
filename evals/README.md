# Behaviour evals

**Status: prepared, not yet run.** These are evaluation cases, not a completed validation. No result is claimed until a run is recorded under `runs/` as described below.

The build kit's unit tests show that the code works. These cases test whether an agent using the skill **follows its rules**:

- the scope of a point edit;
- a reference that exists but does not support the claim;
- a non-significant result with a wide interval;
- a meta-analysis of three studies;
- missing ethics information;
- a translation that keeps the numbers and flags an ambiguous measure;
- numbers derived from raw data;
- references formatted when no journal is chosen.

`evals.json` follows the skill-creator schema (`skill_name`, `evals[]` with `prompt`, `expected_output`, `expectations`). All manuscript text in the prompts is fictional.

## Procedure (reproducible, any agent tool)

1. Record the setup in `runs/<YYYY-MM-DD>-<model>/setup.md`:
   - the agent tool and its version (e.g. Claude Code 2.x);
   - the model id;
   - the skill version (`metadata.version` in `SKILL.md`, or the git commit);
   - the date.
2. For each case, run the prompt twice in fresh sessions:
   - **with the skill** installed: `runs/.../<id>-with.md`;
   - **without it** (skill removed or disabled): `runs/.../<id>-without.md`.

   Save the complete response, unedited.
3. Grade every expectation of every case as `pass` or `fail`, with a short quote from the response as evidence, in `runs/.../grades.json`: `[{"id": 1, "run": "with", "expectation": "...", "result": "pass", "evidence": "..."}]`. Grade blind to the condition if possible (a second person, or a separate grader session that sees only the response and the expectations).
4. Summarize in `runs/.../summary.md`:
   - the pass rate with and without the skill, per case and overall;
   - every failed expectation with the skill, and the rule in `SKILL.md` or the guide that it points to.

With Claude Code and the Anthropic skill-creator skill installed, its evaluation workflow automates steps 2 to 4 (paired with-skill and baseline subagents, grading, and a benchmark viewer). Record the skill-creator version in `setup.md` as well.

Re-run after any change to `SKILL.md` or to the guides the cases touch (`statistical-reporting.md`, `systematic-review.md`, `non-native-authors.md`, `citation-styles.md`, `ethics-and-integrity.md`).

## Adding a case

Add a case when a real session shows the agent getting something wrong: write the smallest prompt that reproduces it and expectations a grader can check without judgement ("keeps 0.72, 0.55 and 0.94", not "writes well").
