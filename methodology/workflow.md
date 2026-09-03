# Workflow — operational execution map

## Authority

This file owns **execution mechanics**: how a bounded task starts, advances, hands off, detects no-progress loops and returns to canonical state.

It does not own the underlying scholarly or data semantics. Use:

- `historical-source-workflow.md` — authoritative scholarly end-to-end method;
- `research-gates.md` — generic G1–G6 maturity requirements;
- `project-lifecycle.md` — Project authority, documentary anchor, Project→Source use and priority boundaries;
- `source-and-provenance.md` — Source/File/provenance/preservation/access semantics;
- `transcription-guidelines.md` — diplomatic/source-phenomenon semantics;
- `evidence-policy.md` — evidence/source-status semantics;
- `ai-governance.md` — AI provenance/evaluation obligations;
- `maintenance.md` — ownership, D-016 admission and propagation.

If an operational shortcut conflicts with one of those owners, repair the shortcut rather than redefining the owner here.

## Goal

Execute the authorized scholarly/technical task with the least process necessary to preserve evidence, authority, restartability and reviewability.

The operational sequence is the same S1–S9 scholarly sequence defined in `historical-source-workflow.md`; this file adds only the execution safeguards needed across sessions/roles.

## Cross-role work-context contract

Role/chat contexts are execution environments, not durable owners of Project knowledge or generic method.

For consequential work, a fresh capable context must be able to determine, preferably by derivation rather than copied prose:

```text
ROLE / RESPONSIBILITY
TASK / ISSUE OWNER
CURRENT EXECUTABLE STAGE
FIRST / NEXT BOUNDED ACTION
PREREQUISITES: unknown | pass | fail
INVALIDATION EVENT for any sticky PASS
EVIDENCE REQUIRED
EVIDENCE / ACCESS STATE
EXECUTION CURSOR
COMPLETION CONDITION
OUT OF SCOPE / NOT AUTHORIZED
HANDOFF TARGET
RETURN / REVIEW CONDITION
```

These are required meanings, not a mandatory serialization/template. Assurance is semantic: do not reject a usable handoff merely because a preferred field label is absent.

Stable Project/Source/File facts should be resolved/derived from their canonical owners rather than recopied into handoffs.

## Current-work-target authority

At task start and whenever `NEXT ACTION` changes, verify that the current executable target is traceable to the canonical Project purpose/scope or another explicit authority source.

Do not infer current priority from Source/File identity, `project_source_id`, structural status, research-function labels, upload order, File availability, staged evidence, a migration fixture, GitHub scheduling or whichever prerequisite required the most recent work.

The underlying Project/priority semantics are owned by `project-lifecycle.md`. This workflow enforces only the execution consequence:

> If target authority is missing, preserve valid completed evidence/support work and block only the unsupported target mutation. Do not invent a replacement priority.

A support task may be necessary and complete without becoming the scholarly objective it supports.

## Sticky prerequisites

A prerequisite deterministically established as `PASS` remains `PASS` for the current execution context until an explicit invalidation event occurs.

Valid invalidation events include, as applicable:

- actual retrieval/access failure;
- checksum/identity contradiction;
- rights/authority change;
- relevant canonical state change making the earlier check stale.

New model uncertainty is not an invalidation event.

Re-entering an already-passed prerequisite without invalidation is an execution fault, not progress.

## Evidence staging for visual work

Source/File identity and preservation semantics are owned by `source-and-provenance.md`. For execution, keep these target-context states distinct:

```text
RETRIEVABLE        an authorized path can recover the bytes
STAGED              the required evidence object is present in the target work context
VISION-INSPECTABLE  the scholarly context can actually inspect the required pixels
```

Derived gate:

```text
VISUAL EVIDENCE READY = PASS
iff STAGED = PASS
and VISION-INSPECTABLE = PASS
for the same evidence object in the same target context
```

Historical success in another session does not establish current `STAGED` or `VISION-INSPECTABLE` state.

If the object is staged but inspectability has not yet been demonstrated, the target scholarly context may perform one local preflight:

```text
STAGED = PASS
→ local pixel-inspectability check
→ VISION-INSPECTABLE = PASS
→ execute source inspection
```

If the check fails:

```text
VISION-INSPECTABLE = FAIL
→ EVIDENCE NOT READY
→ return to the evidence-availability/staging owner
→ do not simulate scholarship from metadata/transcription alone
```

Do not use `EVIDENCE STAGED = PASS` as an ambiguous composite token.

If the decisive staging capability lies outside repository/tool control, record the platform boundary instead of building repo machinery that cannot cross it.

## Progress / delta and loop control

A repeated action, delegation or return is justified only when at least one material state changes, for example:

- new evidence was inspected;
- uncertainty/decision state changed;
- the bounded question became narrower;
- canonical state advanced;
- a prerequisite was invalidated;
- escalation/review level changed for a stated reason.

Repeated delegation with no evidence/state/question delta is a `no-progress / delegation-loop candidate`.

On first detection, redirect to the valid cursor. If the same no-delta re-entry repeats, stop the loop, preserve current state and route the execution/process defect to its owner. Resume scholarship only from a valid executable state.

This rule does not forbid legitimate scholarly iteration where new inspection/comparison/judgement changes evidential state.

## Senior Domain → Senior Dev interface

A demonstrated research-system/process problem crosses into Dev/RSE only after the scholarly/domain side has established enough meaning to avoid technical guesswork.

The domain side supplies:

```text
DEMONSTRATED PROBLEM
EVIDENCE / REPRODUCTION POINTER
RESEARCH CONSEQUENCE
ESTABLISHED DOMAIN SEMANTICS / REQUIRED MEANING
UNRESOLVED / NOT INVESTIGATED
REQUIRED SYSTEM PROPERTY
SCOPE / NON-GOALS
DOMAIN ACCEPTANCE / RETURN QUESTION
```

The domain side does not prescribe connector architecture, retry logic, state-machine design, storage/platform selection or other implementation mechanics unless already governed by the admitted requirement.

The Dev/RSE side then owns:

```text
REHYDRATE canonical state
→ VERIFY scope / authority / requirements
→ CAPABILITY / FEASIBILITY TEST
→ BOUND repository vs platform responsibility
→ DESIGN smallest adequate mechanism
→ EXECUTE admitted deterministic mechanics
→ VERIFY invariants / regression / provenance / restartability
→ PERSIST consequential result
→ RETURN to the correct scholarly/domain owner
```

Dev does not re-adjudicate manuscript readings, scholarly classification, research purpose or other owner-reserved semantics. Technical `PASS` is not scholarly acceptance.

## Consequential technical Issue contract

A consequential technical/process Issue is ready for Dev when these meanings are reconstructable:

```text
DEMONSTRATED PROBLEM / FAILURE
EVIDENCE / REPRODUCTION FIXTURE
CANONICAL OWNER / AUTHORITY
DEPENDENCIES / PREREQUISITES
BOUNDED SCOPE
EXPLICIT NON-GOALS
DETERMINISTIC ACCEPTANCE CRITERIA
SCHOLARLY / DOMAIN / HUMAN ACCEPTANCE CRITERIA where applicable
PERSISTENCE / RESTARTABILITY OBLIGATION
RETURN / CLOSE CONDITION
```

Derive stable facts from canonical state where possible. Do not turn this into a mandatory template family.

For material research-system changes, this contract does not replace D-016 admission in `maintenance.md`.

A domain observation must not automatically become a Dev requirement. First determine whether it is incomplete research, Project-local, already covered, genuinely reusable/systemic, specialist-dependent, or no action.

## State transition and canonical freshness

A completed stage/handoff is not restartable if the canonical restart surface still points to the prior stage.

Whenever a consequential stage or authorized `NEXT ACTION` changes, run the smallest freshness pass:

```text
result persisted in canonical owner
→ Project STATUS/restart state synchronized where applicable
→ current target authority still valid
→ handoff points to current canonical state
→ stale prior prose is not treated as authority
```

Freshness is not authority. A synchronized repository can still reproduce an unauthorized priority, so target authority must be checked separately.

## Review points in the flow

Use consequence-scaled review at real transitions:

```text
TASK START
→ role/authority + prerequisite/evidence check

WORK / ITERATION
→ progress/delta check when triggered

RESULT HANDOFF
→ persistence + unresolved/non-result + return question

PRE-DEV
→ requirement/scope/authority/D-016 state

DEV / PRE-MERGE
→ technical assurance + regression/provenance/loss/rebuild checks

DEV RETURN
→ scholarly/domain adequacy where scholarly meaning is affected

STATE TRANSITION
→ canonical freshness + target authority + restartability
```

The review may use a fresh/independent context when consequence or self-review risk warrants it. Do not create permanent roles merely to name review lenses.

Detailed review/certification questions live in `quality-and-learning.md`.

## Persistence and canonical owners

When durable truth changes, update the owning canonical record during the same work block when practical. Use `maintenance.md` for propagation and `README.md`/generated context for navigation.

Do not maintain a second routing table here.

Do not make a future context recover durable research state from chat.

## Gate and priority boundary

`research-gates.md` owns G1–G6 maturity semantics. Project `STATUS.md` owns actual Project gate/restart state.

A gate requirement or support task may justify work only when it is also compatible with the authorized current target. Gate readiness, technical readiness or Milestone scheduling does not independently select research priority.

## Deferred technology

If a useful technical option is not required by an authorized current need, preserve it as a trigger-based Issue rather than implementing it speculatively.

## Operational acceptance test

A fresh capable context passes the workflow/restart test when it can answer without old chat:

- what role/stage may execute now;
- what bounded action is authorized;
- which prerequisites are PASS/FAIL/unknown and what invalidates PASS;
- which exact evidence is required and whether it is actually ready in this context;
- where the execution cursor/completion boundary lies;
- what is explicitly out of scope;
- what changed since the prior state;
- who receives the result and under what return condition.

If the answer requires replaying a prior chat, re-running an already-valid prerequisite without cause, or inferring priority from structural/support state, the execution surface is not restartable.
