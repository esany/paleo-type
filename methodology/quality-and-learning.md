# Quality and learning

## Continuous research integrity check

This is the central lightweight quality routine for substantive research work. It is a **research gate**, not a reporting ritual. Run the relevant checks when research truth changes and at the end of a substantive work block. Do not run a full checklist for every token.

### Five integrity questions

1. **Evidence** — Does each consequential new claim rest on material actually inspected at the level claimed (image, passage, full text, metadata only)?
2. **Layer separation** — Are `OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION` still distinct, with no silent promotion between them?
3. **Independence** — Is additional support genuinely additional evidence, or merely repetition of an earlier AI/model reading, context-derived plausibility, or a dependent derivative?
4. **Persistence** — Did every changed research truth reach its canonical record (transcription, decision log, source audit/register, palaeographic evidence, learnings, `STATUS.md` as applicable)?
5. **Goal alignment** — Did this work reduce consequential uncertainty or produce a usable research result, rather than drift into generic research, tooling, methodological ceremony or fluent interpretation unsupported by evidence?

### Fail rule

If a consequential point fails one of the relevant questions, the work block is **not complete for that point**. Do not repair the failure by making the prose more confident. Instead choose the shortest discriminating action: reinspect the image, compare a genuine same-hand anchor, inspect the actual external passage, preserve a variant/unresolved state, correct the canonical record, or escalate when independent specialist validation is warranted.

An unresolved result can pass the integrity check. An unsupported resolved result cannot.

### Event-triggered use

Use only the relevant branch of the check:

- **reading changed** → evidence, layer separation, independence, transcription/decision persistence;
- **comparison anchor added/changed** → inspected-image basis, independence, palaeographic persistence;
- **external source used** → access/status, exact passage inspected, claim/source fit, source-audit persistence;
- **historical identification/interpretation added** → separation from reading, explicit evidential basis, source/inference distinction;
- **work block ended or next action changed** → goal alignment, `STATUS.md` restartability, missing durable state;
- **new tool/model/workflow proposed** → identify the current research bottleneck it solves and prefer the simpler direct test when that is faster;
- **AI/HTR automation begins shaping corpus-level findings** → trigger the formal evaluation requirements in `ai-governance.md`.

## Adversarial evidence spot-check

Formal consistency is not evidence of correctness. At useful checkpoints, perform a small adversarial sample of consequential `working` readings or claims and actively try to falsify them.

For each sampled item:

1. return to the underlying primary evidence without treating the current reading as ground truth;
2. generate graphically/evidentially viable alternatives where possible;
3. test the current reading against same-hand forms or a genuinely independent primary control;
4. check whether historical context or previous AI output contaminated the apparent certainty;
5. downgrade to `variant` or `unresolved` if the evidence does not discriminate.

Keep this lean: sample a few **consequential** items, not random easy words and not every row. Increase the sample or validation strength only when the observed failure rate, novelty of the hand/notation, or consequence of error warrants it.

The spot-check is successful when it can expose and correct error; it is not intended to confirm that the repository is internally consistent.

## Quality gates

Before a reading is used as a comparison anchor:

- it must be visible in an inspected primary image;
- its status and alternatives must be recorded;
- it must not depend solely on historical plausibility;
- if it is important, seek at least one independent same-hand comparison or external primary parallel.

Before research literature affects interpretation:

- the relevant passage must actually have been read;
- source status and page/passage must be logged;
- distinguish the author's claim from our inference.

## Error taxonomy

When useful, classify failures as:

- `silhouette_guess` — whole-word shape guessed without grapheme control;
- `semantic_completion` — syntax/context filled missing signs;
- `context_leakage` — historical knowledge altered blind reading;
- `source_laundering` — metadata/snippet treated as read content;
- `false_consensus` — repeated model outputs treated as independent evidence;
- `normalization_leakage` — modern form substituted for manuscript form;
- `segmentation_error` — wrong line/region boundaries distorted reading;
- `notation_error` — numeral/currency/measure sign read as ordinary text.

## Learning loop

1. Log concrete project failure/correction in `LEARNINGS.md`.
2. State the observed failure mode and corrective practice.
3. Apply it to the current project.
4. Promote it to general methodology only if it is methodologically general, not a source-specific fact.
5. Remove or simplify rules that create overhead without preventing real errors.

A failed integrity check or adversarial spot-check is learning input: record the concrete project failure when it changes how future work should proceed. Promote only the generalizable corrective rule.

The system should become more reliable, not merely larger.
