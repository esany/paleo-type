# D-016 lifecycle decision-surface refinement — autonomous authorized work and context efficiency — 2026-10-03

**Status:** DECISION-SURFACE REFINEMENT / NOT ADMITTED  
**Repository baseline:** `main@cab6b8d14359519c35d4e3fcbf12b87347949b41`  
**Refines:** `requirements/repository-knowledge-lifecycle-d016-decision-surface-2026-10-02.md` and `requirements/repository-target-state-implementation-readiness-2026-10-03.md`  
**Evidence refinements:** `requirements/product-co-development-boundary-deep-check-2026-10-03.md` and `requirements/human-proxy-work-lifecycle-context-efficiency-audit-2026-10-03.md`  
**This artifact is not:** D-016 admission, METHOD, a new Project/programme owner, manuscript scope, a scholarly `NEXT ACTION`, implementation permission, a workflow engine, an autonomous planner, a package/refactor decision, or evidence that #225 whole-system acceptance was achieved.

## A. Disposition

The post-target-state audits do **not** justify a new architecture class. They require a bounded refinement of the existing Class-B decision surface before the Human Owner can make a clean D-016 disposition.

The architecture class remains:

> **existing canonical research owners + explicit closable work/programme lifecycle + durable decision promotion + current/history/supersession semantics + rebuildable operational views + qualification against a persisted target state.**

The refinement adds four properties that were previously present only incompletely or implicitly:

1. **work begins before implementation** — analysis, requirements, research, concept, design, planning, implementation, verification, validation, reconciliation and learning can all be bounded authorized work;
2. **autonomous continuation inside existing authority** — when no material Human/specialist/evidence decision is unresolved, the system must continue without using the Human Owner as relay, router or confirmation proxy;
3. **context/token efficiency as an architectural property** — compile applicable current context and expand provenance/history on demand; reduce reconstruction, not evidence;
4. **Human-relay elimination as a qualification requirement** — a fresh capable context must demonstrate multi-step autonomous continuation and must stop exactly at genuine authority, specialist or evidence boundaries.

The Class-B core remains unchanged. D-016 remains **NOT ADMITTED**.

---

## B. Why the existing decision surface needs this refinement

The current repository already has the constitutional authority boundary. `GOVERNING_OBJECTIVE.md` and `AGENTS.md` reserve Human decisions for non-derivable purpose, materially changed priority/scope, unresolved rights/authority, D-016 admission and consequential use, while assigning routine bounded work to AI/implementation agents. `methodology/maintenance.md` already says admitted bounded implementation proceeds without owner micromanagement.

The remaining defect is operational composition:

```text
correct purpose / authority
+ current bounded work
+ applicable requirements
+ evidence / provenance
+ allowed action
+ completion condition
+ return / reconciliation target

but

no generic continuation semantics
        ↓
Human says "weiter" / "ausführen" / chooses route / carries result
        ↓
work continues
```

That final Human relay is not a new authority decision. It is reconstruction/continuation burden.

`tools/outcome_context.py` is useful negative evidence: it can compile a read-only derived outcome context, expose responsibility/authority boundaries and refuse to invent scholarly priority, but deliberately leaves `generated_next_action = None` and `NO_DETERMINISTIC_WORK_GENERATION`. Therefore the repository increasingly knows **what may not be invented**, but still lacks a generic contract for **what already-authorized work may continue without another Human prompt**.

The refinement must close that gap without manufacturing priority or creating a second manually maintained planning clock.

---

## C. Refined work model

### C1. Work is phase-neutral

For research-system work, the system must support bounded work across a coverage model equivalent to:

```text
Problem / Human Need
→ Problem Understanding / Analysis
→ Requirements / Acceptance Conditions
→ Research / SOTA / Best Practice / Domain Evidence
→ Competing Concepts
→ Concept Decision
→ Detailed Design
→ Implementation Planning / Work Decomposition
→ Implementation / Execution
→ Verification
→ Validation / Human or Specialist Acceptance
→ Integration / Reconciliation
→ Closure
→ Learning / Maintenance
```

This is **not** a mandatory waterfall or a new universal lifecycle enum.

Real work may:

- skip inapplicable phases;
- combine phases;
- loop to an earlier phase;
- branch into independently bounded work packages;
- terminate at a legitimate evidence/authority/specialist ceiling;
- return from a local repair to the same higher-level objective.

The required generic property is that every material bounded work package, regardless of phase, can expose enough semantics to be authorized, resumed, checked, reconciled and closed.

### C2. D-016 still gates material implementation, not the beginning of work

The accepted D-016 rule remains intact:

`analysis → requirements → concept → owner review / explicit implementation admission → development → tests/loss checks → result review`

This refinement does **not** remove the admission gate for material research-system implementation.

It clarifies that analysis, requirements, research, concept formation and detailed design are themselves substantive bounded work and therefore require the same restartability, parent-contribution, context and Human-relay protections as development.

`implementation admission` must not be interpreted as `permission to begin thinking/working`.

---

## D. Authorized-work continuation contract — target semantics

The admitted architecture should be able to reconstruct meanings equivalent to the following for a bounded work package:

```text
PARENT OBJECTIVE / PROGRAMME
BOUNDED CONTRIBUTION / TARGET
WORK TYPE / PHASE (descriptive, not authority)
AUTHORITY / ADMISSION BASIS
INPUT / CANONICAL OWNERS
APPLICABLE REQUIREMENTS / CONSTRAINTS
EVIDENCE / PREREQUISITES
ALLOWED WORK BOUNDARY
ACCEPTANCE / COMPLETION CONDITION
DECISION-NEEDED CONDITIONS
RETURN / PARENT RECONCILIATION TARGET
PROVENANCE / HISTORY POINTERS
```

Literal field names or one persistent schema are not required. The information may be derived from existing owners where reliable.

### D1. Execution-only continuation

A continuation is `EXECUTION ONLY` when all applicable conditions hold:

1. the parent objective/work remains authorized;
2. the next bounded action is inside the established work contract/scope;
3. the action is derivable from accepted/current state rather than a new material preference;
4. no Human-reserved or specialist-reserved decision is required;
5. required evidence/prerequisites are sufficient for that action;
6. the completion/return boundary is known;
7. continuation does not create new Project priority, scope or material architecture authority.

When these conditions hold, the system should continue without asking the Human to say `continue`, choose a routine tool/mode, re-supply known state or relay an already-persisted child result.

### D2. Genuine stop/return categories

When continuation is not `EXECUTION ONLY`, the system should distinguish the reason rather than collapse everything into `ask Human`:

- `needs-human-decision` — genuinely non-derivable Human authority/value/acceptance choice;
- `needs-specialist` — independent specialist judgement/validation is required;
- `needs-evidence` — required evidence is unavailable/insufficient and cannot be replaced legitimately;
- `needs-replanning` — current bounded work is no longer the right contribution but no Human-reserved choice is necessarily involved;
- `scope/authority-invalidated` — governing scope/authority has changed or no longer supports the work;
- `complete` — bounded contribution and required return/reconciliation are complete;
- `legitimate-ceiling` — no further valid progress is possible at the current evidence/authority level.

These are target meanings, not a mandated universal status vocabulary.

### D3. Artificial Human relay is a failure

The following are qualification failures when no material Human-owned decision is actually unresolved:

- asking the Human to say `weiter`, `ausführen`, `ja` solely to advance an already-authorized sequence;
- asking the Human which execution route/tool to use when that is derivable from available capability and task needs;
- asking the Human to transport a result between work contexts;
- asking the Human to restate current repository facts;
- asking the Human to choose technical sequencing already entailed by accepted requirements/design;
- asking the Human to repair routine current/history/status synchronization;
- losing the parent return target after a local support/repair action.

---

## E. Context and token efficiency — target semantics

### E1. Principle

> **Reduce reconstruction, not evidence.**

Context efficiency is not permission to omit uncertainty, authority, source evidence, provenance or system-coherence context required for correct work.

The target is to stop repeatedly paying for irrelevant persistent history and duplicated orientation material.

### E2. Normal bounded context

A normal fresh work context should be compilable approximately as:

```text
purpose / authority
→ current parent objective/programme
→ current bounded work
→ applicable accepted requirements / decisions
→ evidence/prerequisite pointers
→ required specialist/method interfaces
→ allowed action boundary
→ acceptance / completion
→ decision-needed conditions
→ return / reconciliation target
```

Historical audits, rejected alternatives, superseded work, full Issue chronology and deep rationale should load only when:

- the current work directly depends on them;
- a claim/decision is challenged;
- supersession/currentness is ambiguous;
- qualification/review requires the deeper evidence chain.

### E3. Reference before replay

Where a stable canonical owner or durable decision exists, context should reference that owner rather than replaying its entire history.

A reference is insufficient only when the executor genuinely needs the underlying content to perform or review the bounded work.

### E4. Externalize before compaction / environment change

Material findings, decisions needed, changed assumptions, unresolved risks and restart-relevant work state must be persisted or otherwise recoverably externalized before a continuity boundary such as:

- handoff;
- environment/tool switch;
- context compaction;
- session end;
- programme/work closure.

Persistence of a candidate/finding does not itself promote it to canonical truth.

### E5. Result/return envelope

A completed bounded worker should be able to return a compact, reviewable delta equivalent to:

```text
WORK / TARGET
RESULT
EVIDENCE / CHECKS
CHANGED CANONICAL OR CANDIDATE STATE
UNCHANGED / NON-CONCLUSIONS
RESIDUAL / CEILING
PARENT CONSEQUENCE
DECISION NEEDED? if any
RETURN / CLOSURE STATE
DEEPER PROVENANCE POINTERS
```

The return should not require replaying all reasoning that is already represented in durable evidence or canonical owners.

---

## F. Additional adequacy requirements for the current D-016 surface

These refine the existing AR-01…AR-16 requirements. They are **decision-surface requirements**, not yet METHOD IDs.

### AR-17 — Phase-neutral bounded work

Analysis, requirements, research, concept, design, planning, implementation, verification, validation, reconciliation and learning can all be represented/reconstructed as bounded work without requiring one fixed linear pipeline.

### AR-18 — Autonomous continuation inside authority

When the current objective/work remains authorized and the next action requires no new material authority/judgement/evidence decision, the system can continue without a Human confirmation proxy.

### AR-19 — Decision-needed discrimination

The system can distinguish routine continuation from genuine Human, specialist, evidence, replanning, invalidation, completion and ceiling conditions without laundering one class into another.

### AR-20 — Applicability-bounded context

Normal execution context is selected by current work/applicability and does not scale proportionally with accumulated repository history.

### AR-21 — No context starvation

Context reduction must preserve every authority, uncertainty, evidence, requirement and system-coherence element whose absence could change the action, conclusion, review or return condition.

### AR-22 — Result/return continuity

A bounded result can return to its parent objective through a compact durable result/reconciliation envelope without Human transport or replay of originating chat.

### AR-23 — Cursor/state burden proof

Any new persisted execution cursor or work-state owner is justified only if derivation from existing canonical/work owners cannot meet restartability/continuation requirements. No second manual roadmap/state clock is allowed by convenience.

### AR-24 — Human-relay qualification

Whole-revision qualification must include cases proving both:

1. autonomous multi-step continuation across `EXECUTION ONLY` boundaries; and
2. correct fail-closed stopping at genuine Human/specialist/evidence boundaries.

A system that reconstructs state correctly but still needs the Human as relay does not close the demonstrated failure.

---

## G. Candidate-register refinement

The prior candidate register remains in force except for the bounded refinements below.

| Candidate | Refined disposition | Refinement |
|---|---|---|
| IC-01 — Generic work/programme lifecycle + closure | **READY FOR D-016 ADMISSION after this decision-surface refinement** | Treat work lifecycle as phase-neutral; include authority basis, decision-needed semantics, autonomous continuation, result/return and Human-relay prohibition. |
| IC-02 — Current/history/supersession + durable decision promotion | **READY FOR D-016 ADMISSION; likely integrated with IC-01** | No architecture-class change. Its role is additionally required for context economy: persistent history remains recoverable while inactive by default. |
| IC-03 — Rebuildable operational status / bounded context | **NEEDS DESIGN AFTER IC-01/02 SEMANTICS** | Add applicability-bounded context, reference-before-replay, decision-needed exposure and result/return envelope. |
| IC-06 — Fresh-maintainer + closure qualification | **KNOWN NECESSARY WORK; EXPANDED** | Must prove autonomous continuation without Human relay, correct genuine-gate stopping, local-repair return and materially different fixture behavior. |
| IC-10 — package / `src` boundary | **NOT WARRANTED NOW; TRIGGER REFINED** | External distribution is not required for a package boundary. Reconsider if several generic entry points/tests/views need a stable internal module API or current `tools/` imports become fragile/coupled. |

No `Wirknetz Runtime`, `Wirknetz Skill`, autonomous planner, workflow engine or separate Bridge component is added.

Wirknetz-derived properties remain a design/qualification lens: provenance, source-role distinction, relation correctness, supersession, `latest wins` prohibition, uncertainty/non-conclusions and verification ≠ validation.

---

## H. Execution-state design hypothesis — B0 before B1

The implementation form remains intentionally open.

### B0 — derive from existing owners

Try first to reconstruct authorized work continuation from:

- explicit programme/work owner (GitHub Issue/PR where applicable);
- durable repository authority/decisions/requirements;
- current Project/canonical research owners;
- rebuildable derived context;
- persisted result/reconciliation evidence.

B0 passes only if a fresh context can reliably determine:

- current bounded work or explicit absence;
- allowed continuation;
- prerequisites/dependencies;
- decision-needed state;
- completion/return target;
- current vs historical state;
- parent reconciliation;

without Issue archaeology or tacit chat knowledge.

### B1 — minimal persisted execution cursor

A small persisted cursor is justified only if B0 fails in a demonstrated way.

If introduced, it must:

- reference rather than duplicate planning/research authority;
- contain only state that cannot be safely/reliably derived at execution time;
- be rebuildable/auditable against its owning sources;
- fail closed on ambiguous continuation;
- never create priority, Project scope, scholarly truth or D-016 authority;
- have explicit supersession/closure semantics;
- not become a permanent second roadmap.

The Wissensarbeit cursor is comparator evidence for feasibility, not a representation to copy automatically.

### B2 — larger lifecycle/control machinery

A larger state/event/control model remains a valid falsification fallback only if B0/B1 cannot satisfy the requirements without hidden reconstruction burden. It is not rejected because it is larger and not selected because it is comprehensive.

---

## I. Qualification additions

The admitted revision, if any, must include an independent fresh-context fixture that can test at least the following scenarios.

### Q1 — analysis continuation without relay

An authorized system analysis has clear scope, evidence and next discriminating work. A fresh agent continues analysis/research without requiring a Human `continue` acknowledgement.

### Q2 — requirements/design continuation without relay

Accepted analysis establishes a bounded requirements/design contribution and no material alternative choice is pending. The system continues within that bounded authority and stops before any unadmitted material implementation.

### Q3 — routine implementation inside admitted scope

A precise D-016-admitted scope exists. Implementation/test repair proceeds autonomously inside that scope without repeated owner approval.

### Q4 — local repair and return

A valid parent work cursor is interrupted by a local evidence/tool/context failure. The system performs only the authorized repair, rechecks the affected prerequisite and returns to the same parent work instead of stopping at local PASS.

### Q5 — genuine Human gate

A material architecture/scope/value choice emerges that is not covered by existing authority. The system stops, prepares the smallest decision surface and does not proceed by inference.

### Q6 — specialist gate

The next consequential conclusion requires independent palaeographic/philological/archival/other specialist judgement. The Human Owner is not used as substitute specialist.

### Q7 — evidence ceiling

Required evidence is unavailable or genuinely non-discriminating. The system reports a legitimate ceiling rather than fabricating continuation or asking the Human to choose a scholarly answer.

### Q8 — context/history economy

A fresh worker receives current/applicable context plus provenance pointers, not the full historical audit/Issue corpus. It can expand the evidence chain on challenge. Omission of non-applicable history must not change the result or authority boundary.

### Q9 — materially different fixture

The same lifecycle/context semantics are exercised on a materially different future research case so that Reg.-Ii.-5-shaped assumptions can be falsified.

FAIL if success depends on old chat, newest-note-wins, manual Human transport, hidden Issue chronology, duplicated planning truth or pilot-specific special casing.

---

## J. Product/co-development boundary retained

The lifecycle revision must remain subordinate to paleo-type's actual product model:

> **the scholarly result/source understanding is the product; METHOD, executable support and repository architecture are supporting means.**

Therefore:

- current research Projects are real scholarship, first real-use evidence and falsification fixtures;
- they are not the limit of intended application;
- genericity is required to prevent pilot overfitting;
- genericity does not imply clone/template/software distribution;
- system changes should return into real scholarly use/falsification rather than becoming a self-sustaining framework programme;
- package/release/productization decisions remain trigger-based.

A lifecycle implementation that optimizes for framework distribution at the expense of scholarly product flow fails the target state.

---

## K. Updated recommended D-016 scope if the Human Owner later ADMITs

A future `ADMIT` should authorize a bounded lifecycle revision sufficient to satisfy AR-01…AR-24, without fixing implementation form in advance.

The scope should include only what is demonstrated necessary to:

1. define phase-neutral programme/bounded-work/closure/result-return semantics;
2. define autonomous continuation versus genuine decision-needed/ceiling semantics;
3. define current/history/supersession and durable-decision promotion sufficient for fresh resolution;
4. define a rebuildable applicability-bounded operational context over existing owners;
5. test B0 derivation from existing owners before adding persisted cursor state;
6. add stable deterministic checks only after semantics are sufficiently mature;
7. reconcile/migrate only existing surfaces actually affected by the accepted design;
8. qualify fresh-context restart, Human-relay elimination, repair-return, history inactivation, context efficiency and materially different fixtures;
9. run exact-head assurance after final material mutation;
10. close the revision programme without creating an automatic successor.

A future `ADMIT` would **not** by itself authorize:

- manuscript Project scope or scholarly `NEXT ACTION`;
- autonomous research-priority selection;
- a universal workflow engine/planner/agent framework;
- a new canonical Project/programme database;
- a mandatory global lifecycle enum;
- a Wirknetz runtime/Skill/graph store;
- Python packaging/`src` migration absent its independent trigger;
- release/SemVer/template productization;
- reactivation of #90;
- treating #225 GitHub closure as proof of whole-system scholarly acceptance.

---

## L. Human decision surface

This refinement is now suitable to accompany the original D-016 decision surface for a later explicit Human disposition.

The available material dispositions remain:

### `ADMIT`

Authorize a new closable lifecycle-revision owner to design/implement/qualify the Class-B architecture under AR-01…AR-24 and the scope/non-goals above.

### `REFINE`

Require a specific additional decision-surface change before material implementation admission. The requested refinement must identify what remains materially unresolved; generic requests for “more detail” should not create another open-ended audit cycle.

### `DEFER`

Retain the decision surface and evidence without active implementation. No new programme/priority is inferred.

### `REJECT`

Reject the Class-B lifecycle revision direction. Preserve the analysis/history and state what architecture/problem interpretation replaces it or which demonstrated failure is intentionally accepted.

**No disposition is selected by this artifact.** The current state remains:

> **DECISION READY / REFINED / NOT ADMITTED.**

If admitted, use a new bounded, closable revision/programme owner. Do not reopen #230 as a permanent planning store and do not reactivate #225 merely because its evidence remains relevant.
