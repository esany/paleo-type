# System-development bugwave — D-016 implementation decision brief — 2026-10-04

**Status:** NON-NORMATIVE HUMAN DECISION BRIEF / **ADMITTED FOR IMPLEMENTATION / WP1 ACTIVE**
**Baseline:** `main@b633ac81f65952775d2d203b7b9986903d48365b`  
**Human-visible programme owner:** #244  
**Candidate implementation programme:** **SD-KA-01 — Engineering Knowledge & Configuration Plane + Development Readiness operationalization**  
**This file is not:** the Human decision itself, implementation permission, Current Configuration, manuscript scope, scholarly `NEXT ACTION`, or proof of #225 scholarly acceptance.

## 1. Why this decision exists

Across multiple real failures and audits, paleo-type accumulated a connected system-development bugwave:

```text
rich failure/audit evidence
→ only part of the consequence remains active
→ current engineering meaning spreads across dated files / README / Issues / history
→ Human, developer and AI reconstruct current state repeatedly
→ pressure grows for a small local fix
→ local technical PASS can look like closure
→ parent gap survives
→ another audit reconstructs the whole
```

The technical core of the repository is comparatively disciplined. The weak surface is the **engineering information/configuration architecture and development work experience** around that core.

The bugwave has now been re-audited for material finding coverage, decomposed into visible Issues #244–#253, compared against Portfolio/Wissensarbeit, and taken through detailed design for finding promotion, configuration/reference semantics, context/DevEx, ADRs, readiness/Human decisions, assurance, brownfield migration, `.prompt`, and Review Premise Inheritance.

The remaining choice is no longer `what problem are we solving?` or `what architecture class might work?`. It is whether to **admit the bounded implementation described below**.

## 2. What is true now

Today:

- scholarly Project/Corpus owners and their restart/evidence semantics remain authoritative and are not being redesigned by this change;
- repository-first persistence, canonical-vs-derived discipline, D-016, semantic-boundary protection and assurance separation already exist;
- Source/File/Project-use deterministic checks and Project context tooling are real strengths;
- the current engineering-development surface still lacks a first-class current configuration owner, managed finding lifecycle, systematic ADR surface, bounded engineering context/query surface and corresponding engineering fitness checks;
- `requirements/` remains a mixed brownfield namespace;
- README still carries more system-development history/current interpretation than a stable orientation file ideally should;
- SD-KA/EKCP target infrastructure is **not implemented**;
- the Human Owner's D-016 admission is durably recorded in `requirements/system-development-bugwave-d016-owner-admission-2026-10-04.md`; WP1 implementation is now active in its admitted branch/PR.

## 3. Material findings are now accounted for

The current bugwave coverage explicitly carries F01–F45.

Especially important recovered/anti-regression findings include:

- audit persistence does not prove material-finding coverage;
- Human feedback is evidence of need/failure, not automatic change authority;
- persisted/reconciled learning is not automatically operationally enforced;
- simplification/migration can correctly remove bad semantics while accidentally deleting useful cognitive/review functions;
- a fresh reviewer can inherit the same contested premise stack;
- a local PASS is not parent/system closure;
- readiness must name the next activity;
- Human strategic overview and Agent execution context are different derived products;
- prompt/work-instruction is a real information class, but not Requirement/Plan/METHOD/Current State/Decision.

The source audit chain is preserved as evidence; current consequences are mapped to bounded work or explicit residual/non-action.

## 4. The proposed architecture in plain language

The proposal is a repository-native **Engineering Knowledge & Configuration Plane (EKCP)**. It does not replace Git, scholarship, Projects or METHOD.

Its job is to make five things explicit and queryable:

1. **What engineering information do we have?**  
   Stable identities and lifecycle/authority metadata for Requirements, audits, designs, results, learnings, prompts and other engineering artifacts.

2. **What engineering configuration is actually accepted/current?**  
   Separate accepted baselines and admitted changes from proposals, history and GitHub work metadata.

3. **What happened to material findings?**  
   Coverage and forward disposition from source finding to Requirement/decision/design/work/defer/reject/no-change, with reversible trace.

4. **Why was the architecture chosen?**  
   Architecture Decision Records (ADRs) preserve context, alternatives, consequences and supersession without replacing the lean accepted `DECISIONS.md` or Current Configuration.

5. **What context does this Human/developer/AI actually need now?**  
   Current-first role/task views with explicit applicability provenance and deeper evidence/history on demand.

The target remains open/repository-native: Markdown, TSV, JSON and Python where sufficient. No external knowledge service is required.

## 5. Proposed material architecture decisions

Existing accepted decisions A-001–A-007 remain governing from current GO/AGENTS/`DECISIONS.md`; this decision does not re-authorize them.

`ADMIT` would accept the following **target architecture package** for SD-KA-01:

- **P-001** separate Engineering Information Management from Engineering Configuration Management;
- **P-002** require explicit material-finding source coverage and forward disposition;
- **P-003** change current engineering configuration only through explicit authority/evidence transitions;
- **P-004** use stable engineering identity independent of physical path movement/supersession;
- **P-005** derive distinct Human strategic and Agent execution views from the same owners;
- **P-006** use current-first progressive context with explicit applicability provenance;
- **P-007** make readiness activity-relative (`ready for design`, `ready for implementation`, etc.);
- **P-008** make material bounded work carry a proportional closeable contract and whole-system return;
- **P-009** add an ADR surface distinct from `DECISIONS.md`, Requirements, Issues and Current Configuration;
- **P-010** establish semantic contracts before physical brownfield migration;
- **P-011** add executable engineering fitness only after those semantics are stable;
- **P-012** adopt `.prompt` as a thin prompt-construction capability, not planning/execution/authority.

Acceptance of these target decisions does **not** assert that the target is already implemented/current. Current Configuration changes only after implementation, verification and Result Review establish the accepted consequence.

## 6. Selected representations and migration

The selected initial representation is a **hybrid**:

- central repository-native registries for cross-artifact identity/current lifecycle/finding/relation responsibilities;
- content remains in the natural semantic owner;
- stable local anchors only where durable sub-document trace is actually needed.

Target surface after admission includes:

```text
requirements/                 # accepted reusable Requirement baselines only

engineering/
  README.md
  configuration.json
  context-profiles.json
  architecture/SYSTEM.md
  decisions/                  # ADR index + records
  catalog/
    artifacts.tsv
    findings.tsv
    relations.tsv
    legacy-paths.tsv
  changes/<change-id>/...
  evidence/{audits,research,learning,work-instructions,...}
  prompts/                    # bounded reusable prompt capability/assets
  generated/{CURRENT_STATE.json,...}
```

Physical migration happens only after an in-place semantic/catalog baseline works. Git moves and legacy-path mapping preserve provenance/navigation. Historical evidence leaves default context after integration but is not deleted.

## 7. Serious alternatives considered

### Keep current dated Markdown/README/Issues only

**Not sufficient.** It preserves evidence but continues chronology/currentness and finding-promotion reconstruction.

### Bounded revision folder only

**Superseded as whole architecture.** Useful change workspace component, but insufficient for repo-wide Information/Configuration Management, trace, DevEx and context.

### Local front matter everywhere

**Not selected as primary representation.** It would require broad brownfield rewrites, works poorly across heterogeneous/external artifacts and risks duplicating cross-cutting currentness/configuration semantics.

### Central catalog only

**Useful but incomplete alone.** Selected hybrid retains central cross-artifact semantics while allowing content to live in natural owners and stable deep anchors only where needed.

### Graph database / Wirknetz runtime / dedicated Bridge

**Not supported by current evidence.** Relations/provenance matter, but a graph runtime is unnecessary for the demonstrated queries; Wissensarbeit comparator evidence also argues against inventing a Bridge without demonstrated need.

### Workflow engine / autonomous planner

**Rejected for current need.** Open applicability and Human authority cannot safely be converted into automatic priority. Bounded state/query/context is sufficient for the demonstrated work.

### Backstage/developer portal

**Not warranted at current scale.** Reuse catalog/current-state/DevEx properties without deploying a portal platform.

### Package/`src`/distributable framework

**Not warranted.** Genericity does not imply distribution; no consumer/install/compatibility contract requires it.

## 8. Review Premise Inheritance residual resolved proportionally

F10 does not require a new subsystem.

The selected safeguard is a **review-evidence-basis + contested-premise descent contract**:

- state what premise is under review;
- state what evidence/owner was actually inspected;
- distinguish inherited premises from re-tested ones;
- do not call a fresh context/second model independent evidence merely because it is new;
- descend to stronger/primary support when the premise itself is contested.

EKCP supports trace/provenance but does not manufacture epistemic independence or specialist competence.

## 9. `.prompt` disposition

Fresh transfer from Wissensarbeit has been adapted and tested at design level.

The capability earns adoption because it solves a repeated Human interaction burden while remaining thin:

```text
.prompt <task>         → return one copy-ready prompt; do not execute
.prompt review ...     → improve prompt without changing authority/purpose silently
.prompt test ...       → evaluate behavior; self-review is not independent proof
```

No universal Skill framework is introduced. Operational activation is included inside SD-KA-01 rather than silently inserted into AGENTS/METHOD.

## 10. Candidate implementation programme — SD-KA-01

If admitted, implementation proceeds in bounded work packages with whole-system return after each.

### WP1 — semantic contracts + in-place managed baseline

Create the admitted `engineering/` foundation and representations without bulk-moving legacy files:

- artifact/configuration/reference schemas;
- finding coverage/disposition representation;
- ADR index/record surface;
- bounded change state;
- populate a representative/current in-place brownfield baseline including F01–F45 coverage and accepted/proposed decision mapping;
- validators for IDs/references/config/finding structural integrity.

**Purpose:** prove semantics over the real brownfield before cosmetic migration.

### WP2 — current configuration + derived current/query views

- populate accepted engineering baseline/current change semantics;
- derive `CURRENT_STATE`/catalog/query outputs;
- implement current-first context selection/applicability provenance;
- prove stale/latest-wins/currentness failure fixtures.

### WP3 — Human / developer / Agent context and `.prompt`

- implement Human system overview and bounded execution/review contexts over the same owners;
- developer bootstrap/navigation;
- one full local assurance entrypoint shared with CI;
- operationalize `.prompt` thin capability and its regressions;
- include review-evidence-basis semantics in consequential review contexts.

### WP4 — engineering fitness / closure assurance

Implement ENG-FIT-01..09 as applicable to the now-stable representations, including seeded stale-current/orphan/coverage/reference/context/local-PASS/exact-head fixtures and explicit assurance-boundary output.

### WP5 — controlled physical information-architecture migration

- classify/move eligible mixed `requirements/` artifacts with `git mv`;
- preserve stable IDs/anchors, Git provenance and legacy-path mapping;
- repair managed links;
- migrate audits/research/learnings/work instructions/ADRs/change results to their selected target responsibilities;
- keep accepted reusable Requirements under narrowed `requirements/`;
- run F45 functional/discoverability loss checks and rollback checks.

### WP6 — adversarial qualification + Result Review

Run the full qualification set against fresh Human/developer/AI journeys and materially different fixtures, then reconcile:

- what actually changed;
- which findings closed/remain;
- which accepted baseline changed;
- what remains residual;
- whether README/history can be reduced from default navigation;
- exact merged-head assurance;
- final result vs admitted scope.

No successor programme is generated automatically.

## 11. First legitimate implementation

The first implementation is **WP1 in-place semantic contracts and representative brownfield validation**, not bulk folder movement.

This is deliberate: if the ID/currentness/finding/ADR semantics are wrong, a physical cleanup would only hide the defect in a prettier tree.

## 12. Verification and validation

### Deterministic/technical verification

Target checks include:

- artifact/reference integrity;
- configuration/currentness transitions;
- finding coverage/disposition structural integrity;
- relation endpoint/evidence integrity;
- generated-view freshness;
- bounded change state consistency;
- context profile/applicability integrity;
- legacy path/link migration integrity;
- `.prompt` behavior boundaries;
- exact-head final assurance.

### Human/developer usability validation

A fresh Senior Developer should be able to find current architecture, proposed work, accepted/proposed ADRs, relevant Requirements, assurance entrypoint and deeper evidence without audit chronology.

The Human system view should explain the bugwave and material decision without requiring Issue sorting, dependency reconstruction or audit replay.

### Specialist/scholarly validation

This change does not replace specialist scholarly validation and does not claim manuscript truth.

## 13. Residuals and explicit non-claims

- **F17 / #225 positive scholarly vertical acceptance remains unresolved by EKCP.** No manuscript work is manufactured to close it.
- F10 is now design-dispositioned as a review-basis safeguard but remains a real-use review risk to exercise in qualification.
- Route B/#90 branch-protection gap remains under its prior Human defer disposition and is not reactivated here.
- current manuscript Projects receive no new scope, gate or `NEXT ACTION`.
- a green engineering CI will not mean scholarly/system whole acceptance by itself.

## 14. Reversibility / lock-in

The proposal intentionally minimizes irreversible infrastructure commitment:

- repository-native open formats;
- Git remains byte/provenance history;
- no external DB/service/portal required;
- migration uses bounded Git changes and legacy mappings;
- generated views are rebuildable;
- rejected/superseded ADRs/findings remain historical evidence;
- physical migration work packages can be reverted with their catalog/path changes together.

The main lock-in is semantic: once stable IDs are referenced, changing ID semantics later has migration cost. That is why identity/reference semantics were fixed before implementation.

## 15. What `ADMIT` would authorize

An explicit Human `ADMIT` to this brief would:

1. accept P-001 through P-012 as the **target architecture decisions for SD-KA-01**;
2. authorize material implementation of WP1–WP6 within the semantics/non-goals above;
3. authorize routine/reversible implementation details necessary to realize those decisions without another approval loop;
4. allow creation of the target `engineering/` surface, validators/context/query tools, CI integration and controlled physical migration;
5. allow accepted-result/current-configuration updates only through the specified Result/transition semantics.

A genuinely new material architecture choice outside this envelope returns for Human decision.

## 16. What `ADMIT` would NOT authorize

It would **not** authorize:

- any manuscript Project purpose, priority, scope, gate or scholarly `NEXT ACTION`;
- a workflow engine, autonomous planner, agent system, graph database, Wirknetz runtime or Bridge;
- a Backstage/developer portal deployment;
- package/`src`/template/distribution work without a new demonstrated trigger;
- automatic closure/acceptance of #225 scholarly whole-system outcome;
- reactivation of #90 branch-protection implementation;
- weakening evidence/source/specialist/Human authority boundaries;
- Slack/cross-chat automation;
- replacing Git with a second history store;
- treating ADRs, generated views, Issues or CI as independent Current Configuration authority outside the admitted contracts.

## 17. Human decision options

### `ADMIT`

Accept the target architecture package and authorize SD-KA-01 WP1–WP6 under Sections 10, 15 and 16.

### `REFINE: <material point>`

Change the named material point before implementation. Only affected design/dependencies re-enter.

### `DEFER`

Keep the complete design/evidence and Issue portfolio, but do not implement it now.

### `REJECT`

Reject the EKCP/SD-KA-01 target. Findings/Requirements/evidence remain available for a replacement design unless the rejection explicitly re-dispositions them.

## 18. Current readiness result

At the present repository/evidence state:

> **BUGWAVE FINDING COVERAGE: ACCOUNTED FOR AT CURRENT EVIDENCE STATE**  
> **MATERIAL ARCHITECTURE/DESIGN: COMPLETE FOR IMPLEMENTATION DECISION**  
> **BROWNFIELD REPRESENTATION/MIGRATION: DESIGNED**  
> **CONTEXT / DEVEX / ASSURANCE / ADR / PROMPT / REVIEW SAFEGUARDS: DESIGNED**  
> **HUMAN D-016 DECISION: READY**  
> **D-016 ADMISSION: GIVEN — see the canonical owner-admission record**
> **IMPLEMENTATION: WP1 ACTIVE; WP2–WP6 NOT STARTED**

The Human Owner does not need to perform another audit or reconstruct the genealogy. The remaining Human action, if implementation is desired, is the material choice in Section 17.
