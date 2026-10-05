# Bugwave design closure — Architecture Decision Record surface — 2026-10-04

**Status:** NON-NORMATIVE DETAILED DESIGN / **#248 DESIGN COMPLETE / PROPOSED ADRS NOT ACCEPTED**  
**Baseline:** `main@b633ac81f65952775d2d203b7b9986903d48365b`  
**Work owner:** #248; parent #244  
**Inventory:** `system-development-bugwave-adr-inventory-2026-10-04.md`  
**This file is not:** an accepted architecture decision, Current Configuration, D-016 admission, or permission to implement the proposed ADR set.

## 1. Why an ADR surface is justified

`DECISIONS.md` is intentionally a lean accepted cross-project decision record. The bugwave contains architecture-significant choices whose context, alternatives, costs, reversibility and supersession are too rich to remain recoverable only through dated audit/design prose.

A separate ADR surface is justified if and only if it preserves this ownership split:

```text
Requirements       → what must hold
DECISIONS.md       → lean accepted cross-project decision authority
ADR                → architecture choice/rationale/lifecycle
Configuration      → which accepted baselines/architecture are current
Issue/change       → bounded work and execution state
Evidence/history   → source support and prior reasoning
```

An ADR does not become current architecture merely because the file exists.

## 2. ADR identity and lifecycle

Each material architecture decision gets a stable ADR identity, candidate format:

```text
ADR-0001
ADR-0002
...
```

The exact numbering scheme is implementation detail; identity is immutable.

Supported lifecycle states:

```text
PROPOSED
ACCEPTED
REJECTED
DEFERRED
SUPERSEDED
DEPRECATED
```

`DEPRECATED` is reserved for an accepted decision that remains historical but is no longer recommended/operative without necessarily having one direct replacement. `SUPERSEDED` names the replacing ADR/accepted decision.

No `latest wins` behavior is allowed.

## 3. Contemporary vs retrospective records

Every ADR states a record type:

```text
contemporary
retrospective
```

### Contemporary

Created while the decision is being considered. `PROPOSED` until the applicable authority accepts/rejects/defers it.

### Retrospective

Records an already-established architecture decision from an existing accepted owner such as `D-013`, `D-016`, `D-019` or `D-021`.

A retrospective ADR must say explicitly:

> This ADR records an existing decision; this file did not cause or re-authorize it.

It must link the actual accepted authority and may not broaden that authority.

## 4. ADR content contract

A material ADR must make reconstructable, proportionally:

```text
ID / Title
Status
Record type
Decision authority / accepted-by (when accepted)
Context / demonstrated problem
Decision
Decision drivers / Requirements
Serious alternatives considered
Why alternatives were not selected
Consequences / costs
Risks / failure modes
Reversibility / revisit trigger
Related material Findings
Related Requirements
Related Issues/change/implementation
Supersedes / superseded by
Evidence / provenance pointers
```

Not every trivial implementation choice earns an ADR. Use an ADR when changing the choice later would materially affect architecture, ownership, lifecycle, compatibility/migration, context/authority, or cross-cutting quality attributes.

## 5. Relationship to `DECISIONS.md`

### Accepted architecture decision already owned by a `D-*`

- `DECISIONS.md` remains accepted authority.
- ADR may be retrospective explanatory detail.
- ADR status `ACCEPTED`, with `accepted-by: decision:D-...`.
- ADR cannot silently expand the `D-*` semantics.

### New material architecture proposal

- ADR status starts `PROPOSED`.
- D-016 decision brief may group/select proposed ADRs for Human admission/acceptance as appropriate.
- Human `ADMIT` to a bounded implementation scope does not automatically mean every unrelated proposed ADR in the repository is accepted; the decision brief must enumerate the included decisions.
- Once accepted, `DECISIONS.md` receives only the cross-project rationale that genuinely belongs in its lean record; the ADR retains detailed architecture rationale.

### Rejected/deferred proposal

Keep the ADR. Do not delete/rewrite history merely because the proposal lost.

## 6. Relationship to Current Configuration

Configuration identifies which accepted architecture baseline/ADRs are current/applicable.

ADR status alone does not resolve all currentness:

- an `ACCEPTED` ADR may apply only to one bounded scope/version;
- a superseded ADR remains accepted historical decision evidence;
- configuration/baseline selects the currently applicable accepted set.

Therefore no generated ADR index may claim `all ACCEPTED = all current everywhere`.

## 7. Proposed initial ADR set from the bugwave

The current inventory already contains enough evidence to seed the eventual ADR layer without making the proposed records accepted.

### Retrospective accepted candidates

These map to existing accepted authority and can be represented retrospectively after the ADR layer is admitted:

- A-001 scholarly objective precedes system architecture;
- A-002 repository-first durable state / chat transient;
- A-003 material research-system change requires D-016;
- A-004 consequential meaning is context-owned / semantic-boundary preservation;
- A-005 outcome/control context is derived and cannot manufacture priority;
- A-006 demonstrated need for automation/infrastructure, interpreted under sufficiency;
- A-007 assurance dimensions remain separate.

Their accepted status already comes from current governing/`D-*` owners, not from this design.

### Contemporary proposed candidates

The future D-016 decision surface should present the following as a coherent proposed architecture package, not as dozens of Finding votes:

- P-001 separate Engineering Information Management from Configuration Management;
- P-002 explicit material-finding source coverage and forward disposition;
- P-003 authority/evidence-controlled configuration transitions;
- P-004 stable engineering identity survives path movement/supersession;
- P-005 Human overview and Agent execution context are distinct derived views;
- P-006 current-first progressive context with applicability provenance;
- P-007 readiness names next admissible activity;
- P-008 material bounded work carries proportional contract and whole return;
- P-009 ADR surface distinct from DECISIONS/Requirements/Issues/Configuration;
- P-010 semantic contracts precede physical brownfield migration;
- P-011 executable engineering fitness follows stable semantics;
- P-012 `.prompt` is a thin prompt-construction capability, not planner/authority.

#245/#246/#247/#249/#250/#251/#252/#253 now provide the detailed design/evidence behind that package. The package remains **PROPOSED** until an explicit material decision.

## 8. Negative/deferred decisions

The eventual ADR index should also preserve architecture options rejected/deferred for the current demonstrated need:

- workflow engine / autonomous planner;
- graph database / Wirknetz runtime / dedicated Bridge;
- package/`src` split/distributable framework;
- developer portal/Backstage-class platform;
- physical `requirements/` bulk move as first implementation.

These are not universal prohibitions. Each retains its revisit trigger/evidence boundary.

## 9. Target physical surface after admission

Selected under #251:

```text
engineering/decisions/
  README.md       # index/lifecycle/explanation
  ADR-0001-....md
  ADR-0002-....md
  ...
```

The index should show at most the information needed to navigate:

```text
ADR
short title
status
scope
accepted authority if any
supersedes / superseded-by
```

Do not duplicate full rationale or Current Configuration in the index.

## 10. Fresh developer journey

A developer asking `why is architecture X this way?` should be able to:

```text
current architecture/configuration
→ accepted ADR(s)
→ decision context/alternatives/consequences
→ Findings/Requirements/evidence on demand
```

A developer should not need to discover that the newest dated design superseded an older one by comparing prose manually.

## 11. Change rule

Material change to an accepted ADR normally creates a new ADR that supersedes the old one. Do not edit history so that the old decision appears to have always meant the new thing.

Corrective edits that do not change meaning are allowed under normal repository maintenance and Git history.

## 12. Assurance

Future validation should check structurally:

- unique ADR IDs;
- valid status;
- accepted ADR has resolvable accepted authority where required;
- retrospective ADR marks its nature;
- supersession targets resolve and are non-circular;
- proposed ADR is not referenced by configuration as accepted/current unless an explicit valid transition accepts it;
- ADR links/related artifacts resolve.

CI cannot decide whether an architecture decision is good or whether Human acceptance was substantively informed.

## 13. Readiness disposition

**#248 design is complete.**

The ADR inventory, lifecycle, relationship to `DECISIONS.md`/Configuration/Issues/Requirements/evidence, retrospective semantics, proposed initial ADR package, negative dispositions, target physical location and validation rules are sufficiently defined. Creating the operative ADR directory/files and accepting P-001–P-012 remain part of a future explicit material admission.