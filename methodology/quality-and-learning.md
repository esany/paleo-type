# Quality and learning

## Purpose

This file owns the lightweight **quality, falsification, certification-boundary and learning** routines for consequential work.

It does not redefine Project authority, Source/File semantics, evidence states, workflow mechanics or Dev authority. Those remain in their primary owners and are checked here only for the quality consequence relevant to the review.

## Continuous research integrity check

Run the relevant questions when consequential research truth changes and at the end of a substantive work block. This is a research-quality gate, not a reporting ritual; do not run a full checklist for every token.

### Five integrity questions

1. **Evidence** — Does each consequential claim rest on material actually inspected at the level claimed?
2. **Layer separation** — Are `OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION` still distinct?
3. **Independence** — Is additional support genuinely independent evidence rather than repeated model output, contextual plausibility or a dependent derivative?
4. **Persistence** — Did changed durable truth reach its canonical owner?
5. **Goal alignment** — Did the work advance the authorized Project/research purpose rather than drift into convenient evidence, generic research, tooling or ceremony?

Internal repository consistency is not by itself evidence of scholarly correctness or owner authority.

### Fail rule

If a consequential point fails a relevant question, that point is not complete. Use the shortest discriminating response: reinspect evidence, test a genuine comparison, inspect the actual external passage, preserve `variant`/`unresolved`, repair canonical state, return an authority gap, or escalate to qualified specialist review when consequence warrants it.

Do not repair a failed check by making prose more confident.

An unresolved but adequately evidenced/tested result may pass. An unsupported resolved result may not.

If Project/priority authority is missing, follow `project-lifecycle.md`: preserve valid completed work and do not invent a replacement Project or `NEXT ACTION`.

## Event-triggered quality use

Apply only the relevant branch:

- **reading changed** → evidence, layer separation, independence, decision/persistence trace;
- **comparison anchor changed** → exact inspected evidence, independence, recoverable anchor;
- **external source used** → actual access level, passage/claim fit, source audit;
- **identification/interpretation added** → separation from reading and traceable evidential basis;
- **Project/priority state changed** → authority/restartability quality using `project-lifecycle.md`;
- **work block / transition ended** → persistence, target alignment and restartability using `workflow.md`;
- **tool/model/workflow proposed** → demonstrated need, smallest adequate mechanism, no speculative infrastructure;
- **systematic AI/HTR begins shaping corpus findings** → formal evaluation trigger in `ai-governance.md`;
- **material research-system change** → D-016/result-review boundary in `maintenance.md`.

## Cross-role assurance reviews

No single model/chat/CI result certifies every dimension of a consequential change. Keep review dimensions distinct and state only what the review can establish.

Reviews are **semantic, not lexical/template-based**. Missing a preferred heading is not a defect when the required meaning is reconstructable; a complete-looking template does not rescue contradictory state.

### Role / authority review

Quality question:

> Is the actor executing the correct bounded role/stage/target with the authority required by the primary owner?

Check the relevant authority facts through `project-lifecycle.md`, `maintenance.md` and `workflow.md`; do not redefine them here.

This review may detect Project/priority inference, support-task drift, premature downstream execution or missing D-016 admission. It does not create Project authority or certify scholarly truth.

### Evidence / provenance / availability review

Quality question:

> Is the exact evidence/provenance/access state sufficient for the claim/action actually being performed?

Use `source-and-provenance.md`, `evidence-policy.md` and the target-context execution gate in `workflow.md`.

This review distinguishes formal identity/access checks from scholarly interpretation. Evidence availability does not establish Project authority or current priority.

### Technical assurance review

Quality question:

> Does the implementation solve the demonstrated problem inside admitted scope while preserving deterministic invariants, provenance, restartability and declared non-goals?

As applicable inspect:

- traceability to requirements/failure fixture;
- smallest adequate mechanism;
- referential/canonical ownership integrity;
- deterministic acceptance/regression tests;
- migration/semantic-loss/rebuildability/provenance evidence;
- no parallel truth store;
- security/rights/platform boundary;
- scope/non-goals preservation.

A technical `PASS` certifies only the properties actually tested. It is not scholarly adequacy, Project authority or Human Owner acceptance.

### Scholarly adequacy review

Quality question:

> Does the returned representation/implementation preserve required scholarly meaning, uncertainty, source phenomena, provenance and research usability?

This is Domain Review and, where triggered, qualified specialist territory. `CI PASS` or Dev self-review cannot satisfy independent scholarly/specialist validation.

### Human / restartability / challengeability review

Quality question:

> Can a fresh capable human/AI context understand and challenge the consequential state/action without the originating chat or hidden implementation assumptions?

Check that canonical owners are reachable, volatile state is not copied as authority, prior consequential work remains recoverable, the user is not forced to act as repository operator/substitute specialist, and the authorized continuation state is reconstructable.

### Governance / purpose review

Human Owner review is required only where governance reserves the decision, such as research purpose/material priority, whether/what Project exists where not already established, unresolved rights/authority facts, consequential publication/use, material research-system admission or Governing Objective amendment.

Do not turn this into routine approval for ordinary scholarship or bounded implementation inside an admitted scope.

## Review-status separation

Where several dimensions apply, keep them separate rather than collapsing them into one generic QA flag:

```text
TECHNICAL ASSURANCE      pass | fail | pending | not-triggered
SCHOLARLY ADEQUACY       pass | fail | pending | not-triggered
SPECIALIST VALIDATION    pass | fail | pending | not-triggered
HUMAN/GOVERNANCE REVIEW  pass | fail | pending | not-triggered
RESTARTABILITY           pass | fail | pending | not-triggered
```

A `pass` in one dimension must never be represented as a `pass` in another.

Fresh/restartable state may faithfully reproduce bad authority or bad scholarship; restartability alone is not validation of the reproduced truth.

## Cross-role handoff quality

Use the execution semantics in `workflow.md`; assess whether the receiver can reconstruct the consequential meaning without replaying the sender's chat.

### Domain → Dev

Quality is sufficient when Dev can reconstruct the demonstrated problem, evidence/reproduction fixture, research consequence, established domain meaning, unresolved/non-investigated state, required system property, scope/non-goals and return question **without** being handed an implementation design.

### Dev → Domain

Quality is sufficient when Domain Review can inspect what changed, which deterministic checks passed, which limits/migration/loss/provenance risks remain, and the exact scholarly adequacy question **without** replaying the Dev chat.

Presence/absence of literal field labels is not the criterion; reconstructable, non-contradictory meaning is.

## Adversarial evidence spot-check

Formal consistency is not evidence of correctness. At useful checkpoints, sample a small number of consequential `working` readings/claims and actively try to falsify them.

For each sampled item:

1. return to the underlying evidence without treating the current reading as ground truth;
2. generate evidentially viable alternatives where possible;
3. test against appropriate internal/independent evidence;
4. check for context leakage or previous-AI contamination;
5. downgrade to `variant`/`unresolved` when the evidence does not discriminate.

Keep the sample consequence-driven. Expand it only when failure rate, novelty or consequence warrants stronger validation.

The spot-check succeeds when it can expose/correct error; it is not a ritual for confirming internal consistency.

## Two specific scholarly quality gates

### Comparison anchors

Before using a reading as a comparison anchor:

- the relevant primary evidence was actually inspected;
- status/alternatives are visible;
- the anchor does not depend solely on historical plausibility;
- important use has appropriate internal or independent control proportional to consequence.

### Research literature

Before literature materially affects interpretation:

- the relevant passage was actually read;
- exact source/access/passages are traceable as appropriate;
- the author's claim is distinguished from our inference.

## Error taxonomy

Use these labels only when they help diagnose/prevent a real failure:

- `silhouette_guess` — whole-word shape guessed without grapheme control;
- `semantic_completion` — syntax/context filled missing signs;
- `context_leakage` — external/historical context altered source reading prematurely;
- `source_laundering` — metadata/snippet treated as read content;
- `false_consensus` — repeated model output treated as independent evidence;
- `normalization_leakage` — normalized form replaced manuscript form;
- `segmentation_error` — wrong line/region boundaries distorted reading;
- `notation_error` — numeral/currency/measure sign read as ordinary text;
- `project_scope_inference` — Project identity/boundary inferred without owner authority;
- `priority_drift` — support/available evidence silently became the current target;
- `role_priority_conflation` — structural/research function was treated as priority;
- `work_state_loss` — migration/cleanup preserved objects but lost consequential restart/checkpoint state.

Do not create a new generic taxonomy entry merely because one isolated incident occurred; apply Generic-Fit first.

## Learning loop

1. Record the concrete Project failure/correction where its evidence lives.
2. State the observed failure mode and corrective practice.
3. Apply it to the current case.
4. Promote only the genuinely general safeguard after Generic-Fit.
5. If the generic safeguard is deterministic, prefer the executable owner + regression fixture over another prose copy.
6. Remove/simplify rules that add overhead without preventing demonstrated error.

A failed integrity/adversarial check is useful evidence about the method. Preserve the concrete case; do not generalize its incidental details.

The system should become more reliable, not merely larger.
