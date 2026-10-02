# D-016 decision surface — repository knowledge/work lifecycle architecture

**Status:** DECISION READY / NOT ADMITTED  
**Parent analysis:** GitHub Issue #230  
**Evidence basis:** `requirements/repository-knowledge-lifecycle-adequacy-audit-2026-10-02.md`  
**Current repository baseline:** `main@8390b268972fcbc5bdfb39aad62809927dbbe532`

This document is a D-016 owner-decision surface. It does **not** itself authorize implementation. It also does not select manuscript research scope, create a Project `NEXT ACTION`, alter #225 whole-system acceptance, or establish new scholarly truth.

## 1. Demonstrated problem

The current repository contains strong local/canonical owners and many necessary scholarly distinctions, but several cross-cutting maintainability failures remain coupled:

1. current state and valuable historical evidence are not consistently separated on the default active reading surface;
2. some programme/work Issues accumulate current state, decisions, evidence and history such that a fresh context must replay chronology;
3. consequential accepted architecture rationale can remain distributed across issue comments, analysis artifacts, admission comments, implementation and result review instead of being promoted to the durable decision owner;
4. persisted knowledge grows faster than the bounded active work context is operationally selected;
5. generated/derived views are useful but cannot safely solve ambiguous/stale source-state or lifecycle semantics by themselves;
6. repeated audit/governance accretion increases context cost and can create pressure toward overly narrow "lean/minimal" corrections before adequacy is established;
7. bounded work can be locally complete while the structural path from result → durable owner → parent reconciliation → closure → historical/inactive state remains under-operationalized.

The holistic audit dispositions these as a bounded shared structural root:

> **Repository Knowledge Lifecycle + Work/Programme Lifecycle + Operational Context Composition.**

This does not absorb the distinct scholarly Review-Premise/Evidence-Independence gap or #225's separate positive scholarly end-to-end fixture requirement.

## 2. Existing semantics that must be preserved

Any admitted solution must preserve, not rebuild or weaken:

- `GOVERNING_OBJECTIVE.md` precedence and Human-Owner boundaries;
- one durable fact/state → one canonical owner;
- Source ≠ File ≠ Project ≠ research function ≠ current work;
- Observation → Reading → Normalization → Identification → Interpretation;
- Candidate ≠ Canonical;
- Derived View ≠ canonical truth;
- Merge/CI/technical `PASS` ≠ scholarly adequacy or Human acceptance;
- resource availability ≠ task/roadmap authority;
- absence of owner-selected scholarly scope/`NEXT ACTION` is valid and non-generative;
- C1R remains read-only/rebuildable and cannot manufacture outcome authorization, requirement applicability or scholarly `NEXT ACTION`;
- #225 local-PASS containment and whole-system acceptance boundary;
- exact File/provenance and existing Project/Corpus truth;
- open scholarly semantics remain AI/specialist/Human judgement where they cannot be formalized without loss.

## 3. Adequacy requirements

An admitted design must satisfy all applicable requirements below; these are requirements of the decision surface, not yet METHOD IDs.

### AR-01 — Canonical ownership

Current durable meaning has a determinable canonical owner. New convenience surfaces may reference or derive it but do not silently become competing owners.

### AR-02 — Currentness without archaeology

A fresh maintainer can determine current programme/work/decision state without replaying long Issue or artifact chronology.

### AR-03 — Preserve history

Closure/supersession does not erase failure history, prior rationale, rejected alternatives or provenance needed for audit/recovery.

### AR-04 — Inactivate history

Historical evidence remains discoverable but does not remain mandatory default work context merely because it persists.

### AR-05 — Durable accepted decisions

Consequential accepted cross-project rationale that would otherwise need rediscovery is promoted to the existing durable decision owner (or another explicitly admitted owner if the existing one proves inadequate).

### AR-06 — Closability

Bounded audit/work/programme owners have explicit terminal semantics and can close without losing current durable meaning.

### AR-07 — Parent reconciliation

A child/local result changes a broader programme only through an explicit changed/unchanged/needs-decision (or equivalent) reconciliation; local completion is never implicit programme completion.

### AR-08 — Derived-not-owned

Human/agent operational views remain rebuildable. They must not resolve ambiguity by inventing authority.

### AR-09 — Bounded active context

The normal context for a current task is selected from applicable current owners/decisions/evidence pointers rather than being a full dump of all persistent history.

### AR-10 — On-demand provenance

A challenge can expand from the active view to decision rationale, evidence, derivation and history without requiring originating chat.

### AR-11 — Review evidence-basis visibility

For consequential scholarly review, it must be possible to distinguish direct evidence inspected by the reviewer from premises inherited from derived research artifacts. The exact implementation may be separate from the work-lifecycle mechanism.

### AR-12 — Qualification separation

Technical assurance, scholarly adequacy, specialist validation, Human/governance review and restartability remain separately stated.

### AR-13 — Exact-state assurance

A material semantic mutation after a prior check requires assurance for the new final state/head where applicable.

### AR-14 — Open semantics remain open

No lifecycle/context mechanism may deterministically invent research analysis units, scholarly interpretation, open requirement applicability, research priority or Human authority.

### AR-15 — Adequacy before simplification

Architecture/components are retained when necessary to satisfy demonstrated requirements. Size/"lean" is not a precondition that truncates the solution.

### AR-16 — Symmetric complexity burden

Unnecessary complexity must be removed after sufficiency is shown; unsupported large machinery is as invalid as under-solving via an attractive small fix.

## 4. Competing architecture classes

### Class A — local maintenance only

Potential contents:

- stale README/current pointers;
- historical status labels;
- isolated decision-log reconciliation;
- individual issue current-status pointers.

**Evidence for:** several concrete defects are routine maintenance and should be fixed regardless of larger design.

**Evidence against as full solution:** does not establish reusable closability, current/history separation, bounded active context or result→decision→parent→closure semantics.

**Disposition:** necessary subset, insufficient total architecture for the demonstrated shared root.

### Class B — lifecycle + derived operational surface over existing owners

Potential semantic components, to be refined before implementation:

1. explicit generic distinction among durable normative/canonical owners, accepted decisions, bounded programmes/revisions, bounded work packages, execution cursor, audit/analysis evidence, candidates, historical evidence and rebuildable views;
2. work/programme closure semantics that promote accepted meaning to durable owners and reconcile parent impact before the work owner becomes historical;
3. current/superseded/history semantics sufficient for fresh-reader resolution;
4. consistent use of the existing `DECISIONS.md` owner where it proves adequate;
5. bounded task/programme context compiled from current owners, decisions and pointers rather than duplicated persistent planning truth;
6. deterministic checks only for stable relationships/currentness/closure/assurance semantics;
7. separate bounded design for Review-Premise/Evidence topology if Generic-Fit shows it should not be coupled to work lifecycle.

**Evidence for:** directly matches the coupled failure families while retaining existing canonical owners and C1R/derived-view principles.

**Evidence against / open:** Generic-Fit and real fresh-maintainer qualification are still required; exact representation and physical repository changes remain unknown.

**Disposition:** **recommended architecture class for admission/refinement**, not because it is smaller, but because current evidence gives it the best problem fit while leaving unsupported semantic partitions open.

### Class C — larger repository knowledge/control restructuring

Possible examples (not pre-approved):

- new persistent transition/event model;
- stronger typed relationship store;
- physical repository reorganization;
- additional canonical lifecycle/control state;
- broader machine-readable ownership/state model.

**Evidence for:** could become necessary if Class B cannot satisfy currentness/closure/context requirements without hidden AI/human reconstruction.

**Evidence against now:** no demonstrated need yet for a new state store/event store/registry; high risk of second clocks and formalizing the wrong semantic partition.

**Disposition:** remain in solution space as a falsification fallback; do not reject because of size, do not build without demonstrated insufficiency of a less duplicative architecture.

## 5. Recommended D-016 scope if ADMITTED

A safe admission should authorize **design/implementation only to the extent needed to satisfy the adequacy requirements**, with no predetermined file count or architecture size.

Recommended bounded scope:

1. refine the generic owner/work-lifecycle semantics from the audit into explicit contracts/acceptance criteria;
2. establish result-promotion and closure semantics for programme/revision and bounded work owners;
3. establish current/history/supersession semantics sufficient for unambiguous fresh-context resolution;
4. reconcile the existing `DECISIONS.md` role with accepted programme architecture decisions;
5. design a rebuildable current programme/work context that references existing canonical owners and does not create a new parallel truth store;
6. add only deterministic checks whose semantics are stable after the design phase;
7. migrate/reconcile only the existing surfaces proven necessary by the accepted design;
8. qualify the result with an independent fresh-maintainer/restart test and exact-head assurance.

The admission should **not** fix the implementation form in advance. A larger mechanism remains allowed if the requirements prove it necessary; a smaller mechanism is acceptable only if it closes the demonstrated failure family.

## 6. Candidate affected owners/files

Exact files depend on admitted design. Likely impact surfaces:

- `methodology/maintenance.md` — work/programme lifecycle, result promotion/closure/reconciliation if promoted to generic METHOD;
- `methodology/workflow.md` — current-work/handoff/context execution hook if needed;
- `DECISIONS.md` — consistent durable decision promotion, without replacing work history;
- `README.md` and/or a generated navigation/read surface — current programme/work discoverability;
- `MILESTONES.md` — only if GitHub work-package/target lifecycle semantics materially need clarification;
- Issue/PR templates or tests — only if stable semantics warrant executable/structural checks;
- `tools/` — only for derived/current-context compilation or validators justified by the final requirements;
- `requirements/` — audit/decision evidence and migration records, not a new canonical state store.

Potentially not affected:

- Corpus Source/File schemas;
- Project schema;
- diplomatic/transcription owners;
- S1–S9 method substance;
- G1–G6 scholarly gates;
- C1R's current read-only boundary.

## 7. Migration / compatibility requirements

If material changes are admitted:

1. existing historical Issues/PRs/audits remain available; do not rewrite history into a fictitious current narrative;
2. current programme/project authority must not change merely because representation changes;
3. accepted current decisions are linked/promoted without deleting their original admission/review evidence;
4. stale/current pointers are reconciled before generated views depend on them;
5. any new derived surface is rebuildable from its source owners and declares them;
6. no migration creates automatic scholarly priority or active scope;
7. existing #225/C1R acceptance boundaries remain intact;
8. rollback must be possible without loss of canonical research truth.

## 8. Candidate work decomposition — not a roadmap

Do not create these children merely because this surface exists. Each must pass an independently reviewable-result/parent-contribution test.

Possible decomposition:

- **R1 — Owner + Work Lifecycle / Closure**
- **R2 — Decision Promotion + Supersession**
- **R3 — Current / Historical / Active-Knowledge Separation**
- **R4 — Operational Read Model + Bounded Context**
- **R5 — Review Premise / Evidence Topology**
- **R6 — Qualification / Exact-State Assurance Integration**
- **R7 — Migration / Reconciliation of Existing Surfaces**
- **R8 — Fresh-Maintainer / Closure Qualification**

Dependency hypothesis: `R1 + R2 + R3 → R4`; R5 may deserve a separate scholarly/system design track; material design results precede any broad migration. This decomposition must be revised if the actual design shows different coupling.

## 9. DoR / DoD candidate requirements

These meanings are derived from the existing #225 anti-fragmentation contract and the audit. They are not yet generic METHOD.

### Programme/revision DoR candidate

- authorized problem/outcome;
- governing/parent authority;
- demonstrated failure/need;
- scope/non-goals;
- invariants;
- dependencies;
- exit/qualification criteria;
- D-016 state where applicable.

### Programme/revision DoD candidate

- all necessary bounded results dispositioned;
- accepted cross-project decisions promoted to durable owner;
- current canonical state coherent;
- residuals/ceilings explicit;
- qualification against the original outcome;
- fresh-context restart;
- history remains discoverable but need not remain active;
- no implicit successor priority/programme.

### Bounded work DoR candidate

- parent outcome/contribution;
- input/canonical owners;
- bounded result;
- non-goals;
- dependencies;
- acceptance criteria;
- return/reconciliation condition.

### Bounded work DoD candidate

- result persisted in correct owner/artifact role;
- required assurance/review complete at actual authority level;
- assurance matches the final semantic state/head;
- parent consequence dispositioned;
- local result not promoted to global acceptance;
- candidate/superseded state handled;
- fresh restart possible;
- work can close without loss of current durable meaning.

## 10. Fresh-maintainer acceptance fixture

A final admitted implementation should be tested by a fresh capable context with no originating chat.

At minimum it must reconstruct:

- active/terminal research-system programmes and their explicit owners;
- current bounded work, if any;
- accepted durable decisions relevant to that work;
- historical/superseded audit artifacts without treating them as current state;
- #225 C1R local result versus whole-system OPEN state;
- no owner-selected manuscript scope unless explicitly present;
- exact Human/AI/specialist/deterministic boundaries for the current task;
- evidence/rationale expansion path when a claim is challenged;
- closure/history state of completed work without replaying long issue chronology.

FAIL if success depends on old chat, tacit model memory, or guessing precedence between stale status prose.

## 11. Review-Premise / Evidence boundary

The Reg. Ii 5 #171 fixture demonstrates a real open gap:

> context-independent review can still inherit the same derived scholarly premise.

A candidate review-basis representation should, if pursued, expose meanings equivalent to:

```text
CLAIM / PREMISE UNDER REVIEW
DIRECT EVIDENCE OWNER / TARGET
DERIVED OWNERS DEPENDING ON IT
PREVIOUS ADJUDICATIONS
DIRECTLY INSPECTED BY THIS REVIEWER
INHERITED BY THIS REVIEWER
JUDGEMENT / RESIDUAL UNCERTAINTY
```

This may be part of the same material revision only if Generic-Fit shows shared lifecycle/relationship semantics without forcing scholarly claims into an unsuitable control model. Otherwise split it into a separately admitted bounded design problem.

## 12. Deterministic acceptance / assurance

Where applicable after implementation:

- canonical references resolve;
- current/superseded pointers are non-contradictory;
- derived views rebuild from explicit owners;
- no Project scope or scholarly `NEXT ACTION` is generated from support/history state;
- parent/child reconciliation cannot convert local PASS into parent completion;
- accepted-decision pointers resolve;
- exact-head assurance is rerun after final material mutation;
- existing Source/Project contract tests remain green;
- historical artifacts remain discoverable;
- fresh-context acceptance passes.

Technical PASS certifies only these tested properties.

## 13. Scholarly / Human acceptance

Separate review must establish, as applicable:

- scholarly meaning and uncertainty are not lost by lifecycle/context representation;
- source/premise evidence topology does not claim scientific truth merely because relationships are typed;
- the Human Owner is not turned into repository synchronizer or specialist adjudicator;
- no new research priority is manufactured;
- the solution materially reduces reconstruction burden rather than moving it into another hidden layer.

## 14. Non-goals

Unless separately demonstrated and admitted, do not build:

- a universal workflow engine;
- autonomous scholarly planner;
- universal capability/discipline registry;
- universal manuscript ontology;
- generic maturity scalar;
- event-sourced scholarly truth store;
- second canonical Project/programme state database;
- mandatory giant status taxonomy;
- physical directory migration for aesthetic reasons alone;
- new ADR framework when existing `DECISIONS.md` suffices;
- automatic research-question generation or scholarly priority selection;
- automatic review truth from typed provenance.

## 15. Complexity justification rule

For every component proposed during design, answer:

1. Which demonstrated failure/adequacy requirement does it close?
2. What fails without it?
3. Does it remove reconstruction burden or merely relocate it?
4. What evidence/test establishes sufficiency?
5. Can any part be removed **after** sufficiency without reopening the failure?

A component is not rejected because it is large. It is rejected when its requirement is unsupported or a less complex solution closes the same demonstrated problem without loss.

## 16. Reversibility

Development should proceed on a bounded branch. Canonical scholarly state must not depend on the candidate mechanism before result review. Derived/context tooling must remain removable/rebuildable. Any migration of current/history or decision pointers must retain original repository/Git/Issue evidence.

## 17. Current decision request

The audit supports a material design/refinement step. The Human Owner should disposition the following proposal:

> **Admit a bounded repository knowledge/work-lifecycle revision design/implementation programme whose target is to satisfy AR-01…AR-16, using Class B (lifecycle + derived operational surface over existing owners) as the current best-supported architecture class, while explicitly allowing the design to grow or shrink according to demonstrated sufficiency. Class C remains available if Class B is falsified as insufficient. No manuscript scope, automatic scholarly planning, new canonical control store or broad repository migration is admitted by default.**

Human-Owner disposition:

- `ADMIT`
- `REFINE`
- `DEFER`
- `REJECT`

Until an explicit disposition is recorded, this document remains analysis/decision support only and no material lifecycle architecture implementation is authorized.
