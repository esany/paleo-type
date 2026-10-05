# System-development bugwave — Architecture Decision inventory — 2026-10-04

**Status:** NON-NORMATIVE ADR INVENTORY / DECISION-TRACE EVIDENCE — NO NEW ACCEPTANCE  
**Baseline:** `main@68c9536cfc566cd629aeaaae9ba2ad778cf0f9e7`  
**Work owner:** #248; parent #244  
**Current accepted decision owner:** `DECISIONS.md`  
**Purpose:** identify architecture-significant decisions in the bugwave without retroactively laundering audit/design conclusions into accepted authority.

## 1. Why this exists

`DECISIONS.md` explicitly says it is a lean cross-project decision record and intentionally **not** a full ADR system. The 2026-10 bugwave contains architecture-significant context, alternatives, consequences and supersession that are difficult to recover from the lean record alone.

This inventory therefore separates:

- **ACCEPTED / EXISTING** — authority already exists in a current accepted `D-*` decision or governing owner;
- **PROPOSED** — supported design candidate; not governing architecture and not D-016 admission;
- **DEFERRED / TRIGGERED** — option intentionally held until evidence/trigger;
- **SUPERSEDED** — prior design direction replaced as current hypothesis;
- **REJECTED FOR CURRENT NEED** — compared and not selected for the demonstrated problem; not a universal ban.

If an operative ADR layer is later admitted, accepted retrospective ADRs must explicitly say that the ADR file records rather than caused the historical decision.

ADRs must not own Current Configuration. They own architecture rationale/choice. Requirements own required effects; Issues own bounded work; evidence/history remains in source artifacts/Git/GitHub.

---

## 2. Existing accepted architecture decisions that already constrain the bugwave

### A-001 — Governing scholarly objective precedes system architecture

**Status:** ACCEPTED / EXISTING (`D-013`, `GOVERNING_OBJECTIVE.md`).  
**Decision:** software, AI, workflow and repository architecture are subsidiary to scholarly purpose/evidence/auditability.  
**Bugwave consequence:** EKCP/ADR/context/CI changes cannot redefine product purpose or scholarly authority.  
**Related findings:** F12, F16, F20–F25.  
**Issues:** all; especially #248/#249.

### A-002 — Durable state is repository-first; chat is transient

**Status:** ACCEPTED / EXISTING (`D-006`, GO/AGENTS).  
**Decision:** consequential durable state may not depend on old chat; one durable fact/state has a canonical owner; derived views remain non-authoritative.  
**Alternatives already rejected:** chat-memory as durable owner; copied derived truth.  
**Related findings:** F01–F09, F14, F18–F19.  
**Issues:** #245–#247/#251.

### A-003 — Material research-system change requires explicit D-016 admission

**Status:** ACCEPTED / EXISTING (`D-016`, `methodology/maintenance.md`).  
**Decision:** material shared system changes pass analysis → requirements → concept → explicit implementation admission → development → checks → result review. Routine bounded work inside authority does not require repeated Human approval.  
**Related findings:** F20–F22, F34, F37–F39.  
**Issues:** #249 and every later implementation Issue.

### A-004 — Consequential meaning is context-owned; translation must preserve semantics

**Status:** ACCEPTED / EXISTING (`D-019`).  
**Decision:** lexical similarity does not establish semantic equivalence; Domain↔Dev/machine↔human translations preserve claim type, scope, authority/evidence and uncertainty.  
**Related findings:** F01, F16, F21, F31, F34.  
**Issues:** #246/#247/#249.

### A-005 — Outcome/control context is derived over existing owners; readiness cannot manufacture scholarly priority

**Status:** ACCEPTED / EXISTING for the admitted C1R scope (`D-021`).  
**Decision:** read-only/rebuildable derived context can compose stable facts and responsibility boundaries, but does not own scholarly purpose/scope/applicability/priority/NEXT ACTION; broad deterministic planner rejected for the demonstrated slice.  
**Related findings:** F03–F04, F09, F14, F16, F20, F23.  
**Issues:** #247/#249.

### A-006 — Automation/infrastructure requires demonstrated need

**Status:** ACCEPTED / EXISTING (`D-008`; reinforced by AGENTS/quality).  
**Decision:** add tooling/automation for demonstrated correctness, traceability, restartability, usability or repeated workload, not because a model is attractive.  
**Interpretation:** this is subordinate to sufficiency; it is not a `smallest at all costs` rule.  
**Related findings:** F12, F24–F25, F33.  
**Issues:** #248/#251/#250.

### A-007 — Assurance dimensions remain separate

**Status:** ACCEPTED / EXISTING (`D-007`, `quality-and-learning.md`, CI summary).  
**Decision:** technical/formal assurance cannot silently become scholarly adequacy, specialist validation, Human/governance acceptance or restartability.  
**Related findings:** F10–F11, F15–F17, F26, F28.  
**Issues:** #250/#253.

---

## 3. Proposed architecture decisions from the bugwave

These are **not accepted** by this inventory.

### P-001 — Separate Engineering Information Management from Engineering Configuration Management

**Status:** PROPOSED.  
**Context:** persisted audits/Requirements/designs/history and the approved/current system state are currently too entangled operationally.  
**Decision candidate:** manage engineering information lifecycle/identity/discovery separately from the current accepted engineering configuration, baselines and transitions.  
**Drivers:** F02–F09, F14, F18, F29–F33.  
**Alternatives:** history-as-current synthesis; one master document; derived view that silently decides conflicts; external configuration service.  
**Current preference:** repository-native explicit owners + rebuildable views; no external service at demonstrated scale.  
**Consequences:** currentness becomes explicit; more metadata/contracts required; migration must preserve provenance.  
**Reversibility:** high while repository-native/open formats remain.  
**Issues:** #246/#251.

### P-002 — Material findings require explicit coverage and forward disposition

**Status:** PROPOSED.  
**Context:** audit persistence did not prevent insight loss.  
**Decision candidate:** every material audit source must have a coverage account; each material finding has a forward disposition and reversible source trace.  
**Drivers:** F01, F05–F06, F08, F11, F19, F29, F35.  
**Alternatives:** source-file persistence only; manual summary; full knowledge graph.  
**Current preference:** bounded material trace; relation correctness over completeness.  
**Consequences:** prevents orphan insights but adds coverage work; representation remains open.  
**Issues:** #245.

### P-003 — Current engineering configuration changes only through explicit authority/evidence transitions

**Status:** PROPOSED.  
**Context:** `configuration.json` as a file would be another clock unless transition semantics are explicit.  
**Decision candidate:** define proposed/admitted/implemented/verified/result/accepted-current transitions, responsible authority/evidence and no-change outcomes before code.  
**Drivers:** F02–F04, F09, F16, F30, F32.  
**Alternatives:** latest commit wins; newest design file wins; Issue state wins; manually maintained README.  
**Issues:** #246.

### P-004 — Stable engineering identity must survive path movement and supersession

**Status:** PROPOSED.  
**Context:** proposed trace references are ambiguous if physical IA changes.  
**Decision candidate:** define stable artifact/decision/work/reference identity and anchor rules before migration. Paths/Git URLs are evidence/navigation forms, not necessarily semantic identity.  
**Drivers:** F30 plus migration/restart requirements.  
**Alternatives:** path-as-ID; full graph URI scheme; fuzzy filename search.  
**Issues:** #246/#251.

### P-005 — Human overview and Agent execution context are distinct derived views over the same state

**Status:** PROPOSED.  
**Context:** small Agent context can make active work invisible to the Human; broad Human overview is wasteful/noisy for a bounded executor.  
**Decision candidate:** Human gets strategic + concrete open-work visibility; Agent loads only applicable current work/requirements/ADRs/evidence; both derive from the same owners.  
**Drivers:** F20–F23, F27, F31, F34, F41.  
**Comparator:** Portfolio ADR-0011.  
**Alternatives:** one master context for all users; Human uses Agent packet; open every historical Issue for visibility.  
**Issues:** #247.

### P-006 — Context is current-first and progressively expandable; provenance is not default-load history

**Status:** PROPOSED.  
**Decision candidate:** default context contains authority/current configuration/current work/applicable constraints/uncertainty/completion; deeper findings/audits/alternatives/history are retrieved on demand. Applicability itself must have provenance.  
**Drivers:** F01, F04, F08, F14, F23, F31.  
**Alternatives:** whole-repo loading; aggressive deletion/compression; manual prompt-only summaries.  
**Issues:** #247.

### P-007 — Readiness names the next admissible activity

**Status:** PROPOSED for paleo-type; comparator pattern is accepted in Portfolio.  
**Decision candidate:** say `ready to analyse/design/implement/validate/Human-decision` rather than one generic global `DEV-READY`. Work can be ready for one stage while later work is not.  
**Drivers:** F21–F22, F34, F37–F39.  
**Alternatives:** universal formal state machine; one `ready` label.  
**Issues:** #249.

### P-008 — Material bounded Issues carry a proportional work contract and return to the whole

**Status:** PROPOSED.  
**Decision candidate:** where material, an Issue exposes problem/gap, required effect, next-activity readiness, dependencies, relevant constraints, scope/non-goals, acceptance/close condition, Human boundary and whole-system return. These are semantic responsibilities, not mandatory headings for trivial work.  
**Drivers:** F05, F11–F13, F20–F22, F39, F42.  
**Comparator:** Portfolio ADR-0012; current paleo-type workflow already contains similar consequential-Issue semantics.  
**Alternatives:** heavyweight universal template; Programme owns all task details; no shared work contract.  
**Issues:** #244–#253, especially #249/#250.

### P-009 — Introduce an ADR surface distinct from DECISIONS, Requirements, Issues and Current Configuration

**Status:** PROPOSED.  
**Context:** current `DECISIONS.md` is intentionally lean and cannot by itself expose the full bugwave architecture choice space/supersession.  
**Decision candidate:** add a bounded ADR lifecycle/index if #248 confirms it reduces reconstruction without duplicating `DECISIONS.md`. Existing accepted D-* decisions remain authority; retrospective ADRs reference them rather than fabricate acceptance.  
**Drivers:** F06, F18, F36.  
**Alternatives:** extend `DECISIONS.md` into a mega-log; keep design rationale only in dated audits; external ADR tool.  
**Issues:** #248.

### P-010 — Physical brownfield migration follows semantic contracts, not precedes them

**Status:** PROPOSED.  
**Decision candidate:** classify `requirements/` in place; prove identity/currentness/role/promotion semantics; dry-run central metadata vs local metadata vs hybrid; only then migrate physical paths with loss/rollback checks.  
**Drivers:** F07–F08, F18, F30, F33, F40.  
**Alternatives:** immediate folder cleanup; leave physical IA forever regardless of measured developer/context cost.  
**Issues:** #251.

### P-011 — Engineering architecture properties get executable fitness only after semantics stabilize

**Status:** PROPOSED.  
**Decision candidate:** add deterministic checks for currentness/reference/coverage/generated freshness/whole-result reconciliation only where the semantic owner is stable; exact-head final assurance remains required.  
**Drivers:** F09, F11, F15, F28–F32.  
**Alternatives:** prose-only; encode immature taxonomy in CI.  
**Issues:** #250.

### P-012 — `.prompt` is a thin prompt-construction capability, not planning or authority

**Status:** PROPOSED TRANSFER CANDIDATE; NOT YET GENERIC-FIT/ACTIVE.  
**Decision candidate:** adapt the Wissensarbeit `.prompt` contract so `.prompt` creates a copy-ready prompt without executing it; review/test modes remain bounded; no task authority, planning, repo write or independent-review claim.  
**Drivers:** F20–F23, F27, F40 and direct Human workflow need.  
**Comparator limit:** Wissensarbeit's own Skill is candidate/not regression-protected/not Generic-Fit.  
**Issues:** #252.

---

## 4. Current negative / deferred architecture dispositions

These remain current **design evidence**, not universally accepted bans unless an accepted D-* decision already covers the property.

### N-001 — Workflow engine / autonomous planner

**Disposition:** REJECTED FOR CURRENT DEMONSTRATED NEED / future trigger only.  
**Why:** current authority/open applicability cannot safely be compiled into autonomous priority; D-021 already rejects a broad deterministic planner for C1R.  
**Revisit if:** repeated admitted work cannot continue/restart safely using explicit bounded state/derived context.

### N-002 — Graph database / Wirknetz runtime / dedicated Bridge

**Disposition:** NOT SUPPORTED / DEFERRED.  
**Why:** relations/provenance matter, but Wissensarbeit Track-B evidence falsified necessity of a distinct Bridge for its cases; Wirknetz remains a trace/reconstruction lens.  
**Revisit if:** material queries/scale/consistency cannot be satisfied by repository-native relations.

### N-003 — Package / `src/` split / distributable framework/template

**Disposition:** NOT WARRANTED FOR CURRENT EVIDENCE.  
**Why:** scholarly result is product; tools remain repo-local and stable; no consumer/install/compatibility contract. Genericity ≠ Distribution.  
**Revisit if:** real external/internal consumer or coupling/install problem appears.

### N-004 — Developer portal / Backstage-like platform

**Disposition:** NOT WARRANTED.  
**Why:** catalog/current-context properties are useful; a deployed portal is disproportionate at current scale.  
**Revisit if:** repository-native navigation/query repeatedly fails at real scale/consumer count.

### N-005 — Immediate `requirements/` bulk move

**Disposition:** REJECTED AS FIRST IMPLEMENTATION.  
**Why:** would move ambiguous semantics before identity/currentness/promotion contracts are proven.  
**Issue:** #251.

---

## 5. Proposed ADR record shape if #248 selects a full ADR surface

A material ADR should normally make reconstructable:

```text
Title / ID
Status
Record type: contemporary | retrospective
Authority / accepted-by (when accepted)
Context / demonstrated problem
Decision
Decision drivers
Alternatives considered
Consequences / costs
Risks
Reversibility / revisit trigger
Related Findings
Related Requirements
Related Issues / implementation
Supersedes / superseded by
Evidence / provenance pointers
```

Not every field needs a literal heading when meaning is clear. Accepted ADRs are not rewritten to silently change the decision; material change normally supersedes them.

---

## 6. Decision gap before D-016

A future D-016 implementation decision is not yet clean because P-001 through P-011 contain several material design choices still being resolved by #245–#251. P-012 `.prompt` is a bounded capability decision and can be evaluated separately.

The Human decision should eventually answer a **small set of architecture choices**, not approve dozens of findings individually. Findings support Requirements/ADRs; they are not themselves voting items.
