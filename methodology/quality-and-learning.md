# Quality and learning

## Continuous research integrity check

This is the central lightweight quality routine for substantive research work. It is a **research gate**, not a reporting ritual. Run the relevant checks when research truth changes and at the end of a substantive work block. Do not run a full checklist for every token.

### Five integrity questions

1. **Evidence** — Does each consequential new claim rest on material actually inspected at the level claimed (image, passage, full text, metadata only)?
2. **Layer separation** — Are `OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION` still distinct, with no silent promotion between them?
3. **Independence** — Is additional support genuinely additional evidence, or merely repetition of an earlier AI/model reading, context-derived plausibility, or a dependent derivative?
4. **Persistence** — Did every changed research truth reach its canonical record (transcription, decision log, source audit/register, palaeographic evidence, learnings, `STATUS.md` as applicable)?
5. **Goal alignment** — Did this work reduce consequential uncertainty or produce a usable research result **for the owner-grounded Project/purpose/current scope**, rather than drift into generic research, tooling, methodological ceremony, a convenient available Source, or fluent interpretation unsupported by evidence? Internal consistency among project files is not evidence that the Project definition or a materially changed priority was owner-authorized.

### Fail rule

If a consequential point fails one of the relevant questions, the work block is **not complete for that point**. Do not repair the failure by making the prose more confident. Instead choose the shortest discriminating action: reinspect the image, compare a genuine same-hand anchor, inspect the actual external passage, preserve a variant/unresolved state, correct the canonical record, or escalate when independent specialist validation is warranted.

If the failure is missing owner authority for Project creation/boundary or current priority, preserve the valid evidence/work already completed, record the missing authority state, and **do not invent a replacement Project or NEXT ACTION**. Restore a prior target only when that target itself has an owner-grounded authority basis.

An unresolved result can pass the integrity check. An unsupported resolved result cannot.

### Event-triggered use

Use only the relevant branch of the check:

- **reading changed** → evidence, layer separation, independence, transcription/decision persistence;
- **comparison anchor added/changed** → inspected-image basis, independence, palaeographic persistence;
- **external source used** → access/status, exact passage inspected, claim/source fit, source-audit persistence;
- **historical identification/interpretation added** → separation from reading, explicit evidential basis, source/inference distinction;
- **Project created/redefined** → explicit human-owner Project decision, source-root anchoring only after that decision, prior-state/restartability preservation;
- **work block ended or next action changed** → owner-grounded goal alignment, `STATUS.md` restartability, work-target authority, missing durable state;
- **new tool/model/workflow proposed** → identify the current research bottleneck it solves and prefer the simpler direct test when that is faster;
- **AI/HTR automation begins shaping corpus-level findings** → trigger the formal evaluation requirements in `ai-governance.md`.

## Cross-role assurance reviews

Quality assurance is split by competence and authority. No single model/chat/CI result may certify all dimensions of a consequential change.

Use the following review lenses only when triggered by the work. Each review must state what it can certify and what remains outside its authority. Review semantic completeness and actual state, not compliance with preferred wording or a template. A review that invents mandatory field syntax where the required meaning is already reconstructable is itself process overhead, not added assurance.

### Role / authority review

Checks:

- the Project itself, when materialized or re-bounded, is traceable to a human-owner decision rather than inferred from Source structure, an archival act, a PDF, a place focus or an AI-created working bundle;
- current executable role/stage is correct;
- canonical owner and handoff target are correct;
- the current work target is traceable to owner-grounded purpose/priority/scope rather than inferred from Project root, `principal`, internal/external status, upload order, evidence availability, metadata verification or a technical/architecture fixture;
- a support prerequisite has not silently become the research objective merely because it was necessary or recently completed;
- downstream work is not being executed early;
- material-change admission is present when required;
- owner-reserved purpose/Project/scope/rights/publication decisions have not been inferred by AI.

Machine-checkable owner/stage/admission facts may be verified deterministically where canonical state is explicit. This review does not certify scholarly truth, create Projects, or infer research priority from structural facts.

### Evidence / provenance / availability review

Checks:

- exact evidence identity and provenance;
- the evidence level actually inspected matches the claim;
- required visual evidence is `STAGED = PASS` and `VISION-INSPECTABLE = PASS` for the same object in the same target context when the task requires it; only then is `VISUAL EVIDENCE READY = PASS`;
- transformation/rebuild provenance is sufficient;
- rights/storage boundaries are respected;
- identifiers or metadata are not substituted for source inspection.

Technical identity/access checks may be deterministic. Scholarly adequacy of what the evidence means remains a domain judgement. Evidence availability does not establish that the available Source is a Project or the authorized current work target.

### Technical assurance review

Checks, as applicable:

- traceability to demonstrated problem and applicable requirements;
- smallest adequate mechanism rather than speculative infrastructure;
- referential integrity and canonical ownership;
- deterministic acceptance tests for deterministic properties;
- migration/semantic-loss/rebuildability/provenance fixtures;
- no parallel truth store;
- security/rights leakage controls;
- preservation of declared scope and non-goals;
- honest platform/tool boundary where repo code cannot solve the decisive problem.

A technical `PASS` certifies only the technical properties actually tested. Correct bytes, checksums, routing and reproducibility do not certify Project creation, Project boundary or a research-priority decision.

### Scholarly adequacy review

Owned by Domain Review and, where triggered, qualified specialist review. It checks whether a returned implementation or transformed representation preserves required scholarly meaning, evidence layers, uncertainty, source phenomena, provenance and research usability.

`CI PASS` or Dev self-review cannot satisfy this review.

### Human / restartability / challengeability review

Checks:

- consequential result and `NEXT ACTION` are understandable without the originating chat;
- current state is persisted in canonical owners;
- owner-defined Project identity/boundary is distinguishable from Source structure and AI-created historical scopes;
- the current work target remains explainable from owner-grounded research purpose/priority/scope, not merely because several canonical files agree with each other;
- consequential prior work/checkpoint state remains recoverable after Project-model or path migrations;
- the human owner is not forced to act as repository operator or substitute specialist;
- a fresh capable context can resume from canonical state plus authorized evidence;
- consequential actions remain explainable as `problem → requirement/evidence → owner → change → deterministic vs judgement → consequences/open points`.

### Governance / purpose review

Human Owner review is required only where existing governance reserves the decision: research purpose/priorities, **whether/what Project exists and its boundary**, unresolved rights/authority facts, genuinely new scope, consequential publication/use, material research-system change admission, or Governing Objective amendment.

Do not convert this into routine approval for ordinary source work or bounded implementation already covered by an admitted scope. Conversely, do not let Source independence, a technically necessary prerequisite or an internally consistent repository rewrite stand in for an owner-reserved Project/priority/scope decision.

### Review status separation

Where multiple reviews apply, keep their status distinct rather than collapsing them into one generic QA flag:

```text
TECHNICAL ASSURANCE      pass | fail | pending | not-triggered
SCHOLARLY ADEQUACY       pass | fail | pending | not-triggered
SPECIALIST VALIDATION    pass | fail | pending | not-triggered
HUMAN/GOVERNANCE REVIEW  pass | fail | pending | not-triggered
RESTARTABILITY           pass | fail | pending | not-triggered
```

A `pass` in one dimension must never be represented as a `pass` in another. In particular, restartability/freshness may faithfully reproduce an unauthorized or incorrectly inferred Project/scope/priority; fresh state is not authority-valid state.

### Cross-role handoff quality

At a Senior Domain → Senior Dev/RSE handoff, quality is sufficient when Dev can reconstruct the demonstrated problem, evidence/reproduction fixture, research consequence, established domain semantics, unresolved/non-investigated state, required system property, scope/non-goals and domain return question **without** being given an implementation design.

At the Dev → Domain return, quality is sufficient when Domain Review can inspect what changed, which deterministic tests passed, which limits remain, whether any migration/loss/provenance risk remains, and the exact scholarly adequacy question **without** re-running the Dev chat.

For any role-to-role handoff, assess the **meaning**, not literal headings: if the receiver can reconstruct the current role/stage, executable action, prerequisite/evidence state, cursor, completion, non-goals, persistence obligation and return target unambiguously, absence of a preferred label is not a defect. Conversely, presence of all labels does not rescue contradictory or semantically incomplete state.

If either side must replay the other chat to understand consequential state, the handoff fails restartability.

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
- `notation_error` — numeral/currency/measure sign read as ordinary text;
- `project_scope_inference` — a Source, archival structure or AI-created working bundle was materialized/reused as Project identity without human-owner authority;
- `priority_drift` — correct or newly available Source/File/support evidence was silently promoted into a different current research target without owner-grounded purpose/priority/scope authority;
- `role_priority_conflation` — structural status or a research-function label such as `principal` was treated as if it selected what must be worked on next;
- `work_state_loss` — a structural migration preserved data objects but removed consequential checkpoint/evidence-limit/restart state from ordinary auditability.

## Learning loop

1. Log concrete project failure/correction in `LEARNINGS.md`.
2. State the observed failure mode and corrective practice.
3. Apply it to the current project.
4. Promote it to general methodology only if it is methodologically general, not a source-specific fact.
5. Remove or simplify rules that create overhead without preventing real errors.

A failed integrity check or adversarial spot-check is learning input: record the concrete project failure when it changes how future work should proceed. Promote only the generalizable corrective rule.

The system should become more reliable, not merely larger.