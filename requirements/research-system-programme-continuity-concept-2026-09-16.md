# Research-system programme continuity — bounded P3B Concept

Status: **COMPLETE — bounded Route-A P3B Concept under #211.** This artifact records the smallest-response Concept only. It is **not METHOD, not a formal Requirement owner, not implementation admission, not implementation, not Project priority and not a Project scholarly `NEXT ACTION`.**

Programme/process navigation owner: #206. P3B Concept work owner: #211. Upstream Requirements owner/result: #200 / `requirements/research-system-programme-continuity-requirements-resolution-2026-09-16.md`.

## 1. Authorized Concept question

The Human Owner selected the Route-A P3B stage through #206 after #200 concluded `existing-owner refinement warranted`.

The bounded Concept question is:

> What is the smallest coherent, loss-preserving existing-owner refinement that operationalizes explicit programme/phase/result-transition reconciliation without creating a second state owner, new programme architecture or automatic priority?

This Concept stops before owner review / explicit implementation admission. It does not edit `methodology/maintenance.md`, `methodology/workflow.md`, `DECISIONS.md`, `requirements/domain-requirements.tsv`, Project state or software.

## 2. Requirements to preserve

The Concept must preserve the P2 property:

- only a **material programme/phase/result transition** whose result can affect whole-programme completion/maturity, selectable/current work, or materially affected restart/navigation state is in scope;
- resolve an **existing** programme/planning cursor or decision owner; do not create one merely because this rule exists;
- explicitly disposition the material consequence as `changed`, `unchanged`, or `needs decision` (or semantically equivalent existing vocabulary), with enough rationale for restart without old chat;
- local `PASS`, `STOP`, closeout or `no further local change` remains local unless the programme owner explicitly concludes otherwise;
- `unchanged` is a valid disposition; silence is not reconciliation;
- reconciliation must not manufacture research priority, Project scholarly `NEXT ACTION`, Concept/implementation admission or activation of deferred work;
- planning/navigation metadata must remain distinct from Research, Requirements, METHOD, Project truth and durable accepted decisions;
- no second state store, registry, state machine, dashboard, mandatory Milestone, universal checklist or standing Programme Review bureaucracy is warranted.

The Concept must also preserve Governing Objective technical subsidiarity and canonical/restartable-state invariants, `REQ-GWP-008`, `maintenance.md` ownership/propagation semantics and `workflow.md` execution/freshness semantics.

## 3. Alternatives compared

### C1 — `maintenance.md` only

**Shape:** Add the programme-transition reconciliation obligation only to `methodology/maintenance.md`, relying on existing workflow references to maintenance.

**Strengths:**

- one semantic owner;
- smallest file count;
- directly adjacent to propagation, bounded consistency, affected planning metadata and restartability.

**Loss / failure risk:**

- the demonstrated failure occurred specifically at execution-stage/result transitions where no canonical Project truth or `NEXT ACTION` necessarily changed;
- current `workflow.md` can complete a bounded state-transition freshness pass without explicitly returning the local result to a broader programme owner;
- a maintenance-only rule can therefore remain semantically correct yet operationally easy to miss — reproducing the exact `rule exists / activation weak` class that P2 is meant to resolve.

**Disposition:** **insufficient alone**.

### C2 — `workflow.md` only

**Shape:** Extend `State transition and canonical freshness` so workflow itself defines and executes the whole-programme reconciliation obligation.

**Strengths:**

- highly visible at the point of execution;
- directly reaches stage closeout/handoff behaviour.

**Loss / failure risk:**

- moves durable propagation/consistency semantics into the execution-mechanics owner;
- risks duplicating or partially redefining `maintenance.md` ownership semantics;
- encourages workflow to become a second policy owner rather than an execution consumer;
- makes later consistency work depend on a workflow-local formulation rather than the canonical maintenance rule.

**Disposition:** **rejected as owner misplacement**.

### C3 — coordinated thin existing-owner refinement

**Shape:** One semantic rule in `methodology/maintenance.md`, plus one narrow execution hook in `methodology/workflow.md` that invokes rather than redefines that rule.

**Primary semantic owner — `maintenance.md`:**

Introduce a narrowly scoped **programme/phase transition reconciliation** obligation adjacent to existing maintenance triggers / bounded consistency semantics. Candidate semantics:

1. Trigger only when an already-established programme/phase/result transition is material to whole-programme completion/maturity, selectable/current work, or materially affected restart/navigation state.
2. Resolve the existing programme/planning cursor or decision owner.
3. Explicitly disposition the material consequence for that owner and affected restart/navigation surfaces as `changed`, `unchanged`, or `needs decision` (or semantically equivalent vocabulary), with brief restartable rationale.
4. Preserve local scope: local `PASS`/`STOP`/closeout is not programme completion unless that owner concludes it.
5. Preserve authority: the reconciliation may expose a decision surface but does not select priority, Project scholarly `NEXT ACTION`, Concept admission or implementation.
6. Preserve owner boundaries and do not create a new current-state store.
7. If no broader programme/planning owner has been established by authority, this rule does not manufacture one.

This rule should fit the existing event-driven maintenance model rather than create a new lifecycle/schema. A material transition becomes a maintenance trigger even when no canonical research truth changed, because planning/restart consequences themselves may require explicit disposition.

**Execution consumer — `workflow.md`:**

Add only a short hook in `State transition and canonical freshness` / result-handoff semantics:

> When a consequential stage/result transition falls inside an already-established broader programme and can materially affect programme completion/current selectable work/restart-navigation state, apply the `maintenance.md` programme-transition reconciliation and return the result to the current programme/planning owner before treating the handoff as complete.

The workflow text should **reference** the maintenance rule rather than duplicate its disposition vocabulary or policy semantics. Existing current-target/dependency-authority checks continue to prevent the reconciliation from becoming automatic priority.

**Strengths:**

- keeps semantic ownership singular;
- places the trigger where execution can actually see it;
- directly addresses the demonstrated `correct rule / weak positive activation` failure class;
- preserves lean structure and does not add an object, schema, registry or service;
- allows `unchanged` with one brief disposition instead of requiring documentation churn;
- generalizes beyond #206 without making #206 itself a permanent universal mechanism.

**Loss / failure risk:**

- two methodology surfaces change, so wording must avoid semantic duplication;
- an over-broad trigger could create bureaucracy at ordinary task closeouts;
- an under-specified trigger could reproduce the present omission problem.

**Risk control:** keep the semantic rule solely in maintenance, keep the workflow hook referential, and gate the obligation on material effect within an **already-established** broader programme/planning context.

**Disposition:** **SELECTED CONCEPT — smallest coherent response.**

### C4 — new registry / state machine / dashboard / execution-state store

**Shape:** Create a persistent programme state object, registry, reconciliation packet, dashboard, mandatory Milestone or comparable central mechanism.

**Potential strength:** explicit state representation could make programme coverage mechanically visible.

**Loss / failure risk:**

- duplicates or competes with existing canonical owners and programme/planning Issues;
- creates multiple current-state clocks and freshness obligations;
- increases process/architecture beyond the evidenced need;
- risks turning support infrastructure into programme purpose;
- the `Wissensarbeit` comparator provides direct counterevidence that several individually valid state clocks can drift while remaining locally green.

**Disposition:** **rejected**.

## 4. Selected Concept

The smallest coherent response is **C3 — coordinated thin existing-owner refinement**:

```text
maintenance.md
  owns the generic semantic obligation
        ↓ referenced by
workflow.md
  executes one transition/handoff hook
        ↓ instance-specific application
existing programme/planning owner (currently #206 for this programme)
```

This is deliberately **not** a new programme layer. It is a positive activation/feedback refinement of owners that already exist.

No change to `requirements/domain-requirements.tsv` is proposed. No change to `historical-source-workflow.md`, Project lifecycle semantics, `DECISIONS.md`, `MILESTONES.md`, Source/Corpus contracts or Project `STATUS.md` is required by this Concept.

## 5. Candidate implementation scope — not admitted by this Concept

If the Human Owner later explicitly admits implementation, the smallest candidate write scope is:

1. **`methodology/maintenance.md`**
   - add one narrow material programme/phase/result-transition reconciliation rule at the maintenance-trigger / bounded-consistency boundary;
   - make explicit that planning/restart consequence can require disposition even when canonical research truth is unchanged;
   - preserve `unchanged` as valid and silence as insufficient;
   - state that an existing programme/planning owner is resolved, not created.

2. **`methodology/workflow.md`**
   - add one short reference/hook under `State transition and canonical freshness` or the immediately adjacent result-handoff transition semantics;
   - require application of the maintenance-owned rule when its material-programme trigger applies;
   - do not duplicate the maintenance rule or introduce controlled values/schema.

3. **No other canonical METHOD/data owner by default.**
   - README/#206 may require ordinary freshness propagation after an admitted write, but they do not own the generic semantics.

The exact prose is an implementation detail inside the admitted semantic scope, provided it does not widen the Concept.

## 6. Explicit non-goals

An admitted implementation must not introduce:

- a new programme or planning entity model;
- persistent `execution_state.json`, reconciliation packet, registry, state machine or dashboard;
- mandatory Milestone-per-phase or Issue-per-transition;
- standing Programme Review meetings/checklists;
- automatic activation of every deferred/open Issue;
- automatic priority, Project scholarly `NEXT ACTION`, or replacement for Human-Owner selection;
- a second canonical owner for programme state;
- duplicated Research/Requirements/METHOD/Project truth in planning metadata;
- a generalized Dev/RSE workflow engine.

## 7. Validation and scholarly-loss checks for any later admitted write

A later implementation should be accepted only if proportionate checks show all of the following.

### Positive fixtures

1. **#203–#205 local closeout fixture:** a local `observe real use / STOP` inside a broader live programme requires explicit return/disposition to that programme owner and cannot silently become programme `STOP`.
2. **post-#198 phase-transition fixture:** a completed synthesis that changes selectable downstream work requires the current planning/programme surface to receive an explicit disposition.
3. **current #200 → #206 fixture:** a bounded stage result can be returned as `changed` without activating its next stage or Route B.

### Negative / anti-bureaucracy fixtures

4. Ordinary source-reading/transcription edits with no material broader programme consequence do **not** trigger a programme review artifact.
5. A material transition whose programme consequence is genuinely `unchanged` can satisfy the rule with a brief explicit disposition; no compensating work is manufactured.
6. Absence of an already-established programme/planning owner does not cause the rule to invent a programme, Project, roadmap or `NEXT ACTION`.

### Authority / ownership loss checks

7. Planning/navigation metadata remains non-canonical for Research, Requirements, METHOD and Project truth.
8. The workflow hook does not redefine the maintenance-owned semantic rule.
9. A local technical/scholarly `PASS` remains scoped to what it tested.
10. Fresh-context restart can identify the current programme consequence without recovering the originating chat, while one fact/state still has one canonical owner.

## 8. D-016 boundary after Concept

This Concept is now sufficiently precise to present for **Human-Owner review / explicit implementation admission** under `methodology/maintenance.md`.

Possible owner dispositions include:

- **ACCEPT / ADMIT** the bounded two-file METHOD refinement above;
- **REFINE** the Concept before admission;
- **REJECT** the Concept while retaining the P2 Requirements finding;
- **DEFER** implementation while keeping the surviving need explicit.

No implementation is authorized by this artifact or by #211 completion alone.

## 9. Return boundary

```text
#206 Human Owner selected A-P3B
→ #211 bounded Concept
→ C3 coordinated thin existing-owner refinement selected
→ persist Concept
→ return to #206
→ Human-Owner review / explicit implementation-admission decision
```

Route B / #90 remains independent and inactive unless separately selected. #202 remains trigger-based/deferred. #162 remains paused/deferred. No Project scholarly scope or `NEXT ACTION` is created.
