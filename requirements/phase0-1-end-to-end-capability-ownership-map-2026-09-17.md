# Phase 0/1 — end-to-end capability / ownership / requirements consolidation

Status: **ACTIVE ANALYSIS / REQUIREMENTS WORK under #225 via #227; no D-016 implementation admission.**

Parent system outcome: GitHub #225 — operationalize end-to-end Human-need → scholarly-outcome execution as a generic adaptive mechanism.

Work issue: #227.

## Working prompt / execution contract

> Rehydrate the current repository as authority. Starting from `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, applicable requirements/method owners, #225 and its anti-fragmentation guard, map the complete semantic/control chain from Human need / desired scholarly outcome to usable scholarly result or legitimate ceiling. Do not invent architecture, new roles, a workflow engine, Project priority or scholarly scope. Reuse existing canonical owners and executable components wherever they already satisfy the needed semantics. For each link in the chain, identify: required input meaning; current canonical owner(s); current normative semantics; current executable support; current AI/context dependency; authority boundary; output meaning; dependency on preceding/following links; demonstrated failure mode(s); acceptance/falsification criterion; and disposition `covered | partial | missing | contextual`. Distinguish lack of discoverability from lack of semantics and lack of executable enforcement. Identify only the minimum generic requirements needed to close demonstrated composition gaps. Every local conclusion must state its consequence for #225 and must not be promoted into whole-system success. Treat Reg. Ii 5 only as evidence/fixture; test genericity against non-pilot semantics wherever the repository already provides them. Prefer deterministic derivation/validation over AI reconstruction whenever semantics are stable enough to formalize without loss. Preserve Human Owner authority and specialist judgement boundaries. Stop Phase 0/1 when the capability/ownership map is coherent enough to support competing system concepts without prescribing one.

## Governing constraints

- `GOVERNING_OBJECTIVE.md`: scholarly result/source understanding is the product; transdisciplinary source/problem orientation; Human Owner is not substitute specialist; lean technical subsidiarity; canonical/restartable state.
- `AGENTS.md`: repository authority, one fact/one owner, no invented priority, routine AI work inside authorized bounds, deterministic controls where semantics are stable, research outcome before infrastructure.
- `methodology/maintenance.md`: D-016 sequence; Generic-Fit; one canonical owner; programme/phase/result reconciliation; local PASS is local.
- `methodology/workflow.md`: execution mechanics; reconstructable cursor/task/return state; semantic-boundary preservation; current-target authority; dependency provenance; Domain↔Dev interface.
- `methodology/historical-source-workflow.md`: authoritative S1–S9 scholarly method and dynamic discipline activation.
- `methodology/research-gates.md`: G1–G6 maturity semantics, scope-bound and not priority selectors.
- `methodology/project-lifecycle.md`: Human-Owner Project/purpose/scope authority and canonical Project owner semantics.
- `methodology/quality-and-learning.md`: evidence/layer/independence/persistence/goal-alignment checks; separate assurance dimensions; Generic-Fit and learning loop.
- `methodology/ai-governance.md`: AI provenance, validation scaling, D-016/HITL boundary and specialist escalation.
- `requirements/domain-requirements.tsv`: existing cross-disciplinary requirement inventory and support/gap classifications.

## Parent / child invariant

```text
PARENT SYSTEM OUTCOME: #225
CONTRIBUTION: establish the minimum repository-backed capability/ownership map and generic requirements needed before system concept selection
INPUT / CANONICAL OWNERS: governing objective, guardrails, requirements, methods, executable contracts/tools, #225 audit evidence
BOUNDED RESULT: Phase-0/1 analysis + requirements decision surface
WHAT IT CANNOT ESTABLISH: architecture choice, D-016 admission, implementation readiness, whole-system success, Project scholarly priority
RETURN CONDITION: reconcile findings and unresolved gaps to #225; activate #226 only where its stated prerequisite is met
```

## Phase 0 — capability / ownership map

The map below classifies semantics, not proposed implementation. `Executable` means current repository software/contracts can derive or validate a material part of the link without relying on free-form model reconstruction.

| # | Link / function | Current owner(s) | Normative coverage | Executable support | Main dependency / boundary | Current maturity | Demonstrated composition risk |
|---|---|---|---|---|---|---|---|
| 1 | Human need / desired scholarly outcome capture and preservation | `GOVERNING_OBJECTIVE.md`; Project `project.yml` for Project purpose/scope; Human Owner authority in `AGENTS.md` / `project-lifecycle.md` | strong at mission/authority level; Project purpose can be canonical | little/no generic executable binding from ordinary-language outcome to canonical outcome semantics | must not turn ordinary language into Project scope/status without owner authority; must preserve stable need above local tasks | **partial** | need remains chat-visible but can disappear from operational control once local state/task dominates |
| 2 | Purpose / Project / scope authority resolution | `project-lifecycle.md`; Project `project.yml`; Human Owner | strong | substantial structural validation after owner choice; Source Contract/project context support | Source/File structure and research functions cannot create purpose/scope/priority | **covered for authority; partial for composition** | valid authority rules can yield safe stop without reconnecting the still-valid higher-level need to derivable work |
| 3 | Evidence / Source / File / use / access-state resolution | Source/provenance METHOD; Corpus owners; Source Contract; intake/context tooling | strong | **strong** deterministic identity/reference/resolver support; access/readiness remains context-sensitive | evidence/resource state is descriptive, not priority/task authority | **covered/strong** | structural/evidence PASS can dominate visible progress despite not advancing outcome |
| 4 | Current scholarly maturity / gate-state resolution | `research-gates.md`; Project `STATUS.md` | strong | limited generic derivation; gate state largely human/AI-evaluated from evidence | gate state is scope-bound evidence claim, not task selector | **partial** | fresh context must interpret prose/evidence to connect STATUS to exact unmet gate requirements |
| 5 | Desired outcome → unmet requirements resolution | distributed across Governing Objective, S1–S9, G1–G6, domain requirements, Project state | semantics exist in pieces; no single owner for composition | no demonstrated generic resolver | depends on 1–4; must not invent scope/priority; unresolved evidence can be valid | **major partial / central gap** | AI reconstructs which requirements remain and may over-weight one rule/gate/support state |
| 6 | Question-/claim-/source-relative competence activation | `historical-source-workflow.md`; `domain-requirements.tsv`; specialist triggers; GO transdisciplinary invariant | strong concept/norm | no generic executable routing; AI/manual judgement | activation must follow actual claim/source/problem; no permanent leader/topology | **partial** | relevant expertise can become invisible after lean simplification; user can be asked to select specialist/method steps |
| 7 | Human vs AI vs specialist vs deterministic allocation | GO; `AGENTS.md`; `ai-governance.md`; `workflow.md`; domain requirements validation/specialist-trigger fields | strong boundary principles | isolated deterministic tools; no generic allocation resolver | owner authority and specialist validation cannot be automated; stable control semantics should not remain model-only | **partial** | current model acts as de facto integrator and may inconsistently decide what to derive, ask, automate or escalate |
| 8 | Smallest coherent vertical work-slice formation | GO lean invariant; `workflow.md` task contract; `quality-and-learning.md` goal alignment; D-016 for material system work | principles strong; no generic outcome-to-slice semantics | none generic | must follow authorized target/outcome, not easiest evidence/support issue | **major partial** | “smallest intervention” repeatedly becomes local horizontal optimization instead of smallest end-to-end value slice |
| 9 | Execution / evidence / scholarly method progression | `historical-source-workflow.md`; `workflow.md`; specialist METHOD owners | strong | mixed: strong deterministic support for structure/control; scholarly execution remains judgement/evidence-driven | S1–S9 dependency is not rigid waterfall; evidence controls claims | **covered once task exists** | system is much stronger after a bounded target exists than before/around task formation |
| 10 | Local failure / support / repair containment | `workflow.md`; `AGENTS.md`; maintenance/quality rules | strong | some regression protection for known failure classes; context repair often procedural | resource/support fact cannot create new objective/priority | **covered locally / partial composition** | repair can become visible objective; completion may not restore higher-level flow |
| 11 | Parent-outcome reconciliation and return/resume | `maintenance.md` programme/phase/result reconciliation; `workflow.md` transition hook; #225 guard | semantics exist for established programme contexts; broader decomposition semantics under #226 review | no generic executable parent/outcome resolver | must not invent parent programme/outcome; local result authority stays local | **partial** | local PASS/STOP closes cognitive loop while parent outcome remains unfinished; return currently depends heavily on model discipline |
| 12 | Quality / assurance / specialist-review composition | `quality-and-learning.md`; gates; `ai-governance.md` | strong separated dimensions | deterministic technical checks exist; scholarly/specialist review necessarily mixed/human | technical PASS ≠ scholarly adequacy ≠ specialist validation ≠ owner acceptance | **covered semantically / partial orchestration** | dimensions are well defined but not automatically composed into outcome readiness/next required assurance |
| 13 | Result / maturity validation | `research-gates.md`; quality METHOD; Project `STATUS.md` | strong | deterministic support only for machine-checkable prerequisites/invariants | gate claims require evidence and remain scope-bound | **partial** | AI/manual interpretation still needed to decide whether all relevant gate/outcome requirements are met; local task completion can be confused with result completion |
| 14 | Persistence / restart / fresh-context reconstruction | `maintenance.md`; `workflow.md`; `AGENTS.md`; Project/CORPUS canonical owners; `tools/project_context.py` | strong | **strong for canonical structural/task context already represented** | derived context cannot invent missing purpose/next work/scholarly interpretation | **covered for represented state; partial for integrated outcome** | fresh context faithfully reconstructs local canonical state but not necessarily the Human-need→outcome integration semantics |
| 15 | Legitimate terminal ceiling / completion determination | gates; quality fail/uncertainty rules; workflow dependency authority; Project STATUS; owner/specialist boundaries | strong local semantics | no generic end-to-end completion/ceiling resolver | distinguish evidence ceiling, specialist dependency, owner decision, local inability and whole-outcome completion | **partial** | safe local STOP/ceiling can be mistaken for end-to-end completion or can orphan a still-valid higher-level goal |

## Phase-0 synthesis

### Strong existing substrate

The repository already has high maturity in four areas that a future solution must reuse rather than rebuild:

1. **scholarly epistemic/method semantics** — evidence before plausibility, claim-layer separation, S1–S9 and G1–G6;
2. **authority boundaries** — Human Owner, specialist, AI/implementation agent, Project/Source/evidence/priority distinctions;
3. **canonical structural control** — Source/File/Project-use identity/provenance/references and rebuildable context;
4. **local execution safety** — task contracts, dependency provenance, no-progress detection, support containment, D-016 and separated assurance dimensions.

### Concentrated weakness

The weak links form one dependent cluster rather than fifteen independent gaps:

```text
L1 stable desired outcome representation/binding
        ↓
L4 current maturity usable as input
        ↓
L5 outcome → unmet requirements
        ↓
L6 competence activation
        ↓
L7 execution-mode allocation
        ↓
L8 vertical work-slice formation
        ↓
L9 existing execution machinery
        ↓
L11 parent reconciliation / resume
        ↓
L12–L15 assurance, result, restart and legitimate completion
```

The substrate from L2/L3/L9/L10/L12/L14 is already substantial. The central missing function is therefore **composition/derivation over existing owners**, not a replacement scholarly workflow.

## Phase 1 — minimum candidate generic requirements

These are **requirements candidates for consolidation**, not architecture or implementation choices. Before promotion into another canonical requirements owner, each must be checked for duplication with `domain-requirements.tsv` and existing METHOD wording.

### C-01 — Durable outcome reference without task substitution

**Requirement:** For an owner-authorized scholarly outcome, the system must preserve a restartable reference to that outcome and its authority basis across local task decomposition, support/repair and review, without treating the outcome record itself as permission to invent new Project scope or priority.

**Why needed:** Current Project/task state is strongly canonical, but stable Human need/outcome can remain chat-mediated or be reduced to the latest local target.

**Acceptance:** A fresh context can identify the governing desired outcome, authority/scope relation and whether it remains valid without replaying chat; a local task change does not silently replace it.

**Falsification:** If existing Project purpose/scope/STATUS plus current workflow semantics already provide this generically and reliably across fixtures, no new semantic owner is required; only derivation/discoverability may be needed.

**Dependencies:** L1 → L5/L8/L11/L15.

### C-02 — Outcome-to-unmet-requirements derivation

**Requirement:** Given an authorized desired outcome, applicable Project/scope and current canonical evidence/maturity state, the system must expose the applicable unmet scholarly/system requirements without inventing scope or forcing resolution of legitimate uncertainty.

**Acceptance:** Two fresh contexts given the same canonical state produce materially equivalent unmet-requirement sets and reasons; differences that require scholarly judgement are explicit rather than hidden as routing variance.

**Falsification:** If the derivation cannot be made stable without deciding open scholarly meaning, only the stable subset should be deterministic and the judgement boundary must remain explicit.

**Dependencies:** L1–L5; feeds L6–L8 and L13/L15.

### C-03 — Context-relative capability and responsibility resolution

**Requirement:** For each unmet requirement/claim type, the system must determine or expose the appropriate capability and responsibility mode — deterministic, AI-assisted scholarly reasoning, qualified specialist judgement, or genuine Human-Owner decision — using existing domain/authority semantics and without fixed permanent role topology.

**Acceptance:** Different source/problem fixtures activate materially different capabilities; the non-specialist Human Owner is not asked to choose derivable gate/method/engineering steps.

**Falsification:** Where capability choice itself depends on unresolved scholarly interpretation, the system exposes alternatives/decision basis rather than pretending deterministic certainty.

**Dependencies:** C-02 → L6/L7 → L8/L12.

### C-04 — Vertical-slice selection constrained by outcome

**Requirement:** When more than one bounded action could advance an authorized outcome, selected executable work must be justified by the unmet requirements and current evidence/authority state, and must represent the smallest coherent **vertical** advancement/protection of the outcome rather than merely the smallest locally fixable defect.

**Acceptance:** Addressable support/technical work cannot become the objective solely because it is easy to isolate; every slice exposes which outcome requirement it advances/protects and its return condition.

**Falsification:** If only one action is authorized/possible, no comparative planning mechanism is required; routine execution proceeds directly.

**Dependencies:** C-02 + C-03; feeds existing workflow L9.

### C-05 — Outcome continuity across decomposition and repair

**Requirement candidate:** Local work, PASS/FAIL/STOP/repair and reviews must remain bounded to their authority and reconcile to the still-valid parent outcome; execution resumes that outcome unless real evidence/authority/feasibility invalidates it.

**Status:** Candidate only; #226 owns the post-consolidation Generic-Fit determination of whether existing `maintenance.md`/`workflow.md` already cover this sufficiently or whether a reusable invariant/refinement is warranted.

**Dependencies:** L10/L11/L15; cross-cuts all phases.

### C-06 — Composed outcome acceptance / legitimate ceiling

**Requirement:** Whole-outcome completion or pause must be determined from the applicable scholarly maturity/result requirements, assurance dimensions and explicit evidence/authority/specialist ceilings; component PASS counts, Issue closure or CI success are insufficient.

**Acceptance:** The system can distinguish at least: `usable outcome reached`, `outcome valid but work remains`, `legitimate evidence ceiling`, `specialist validation dependency`, `Human-Owner decision required`, and `local technical inability only`, without fabricating substitute work.

**Falsification:** Do not create a universal status vocabulary if existing owners can provide equivalent semantics through derived views; required meanings matter more than serialization.

**Dependencies:** C-02/C-03 plus L12–L15.

## Dependency graph for concept work

```text
C-01 outcome continuity reference
   ↓
C-02 unmet-requirements derivation
   ↓
C-03 capability / responsibility resolution
   ↓
C-04 vertical-slice formation
   ↓
existing L9 execution machinery
   ↓
C-05 decomposition / repair reconciliation  ← #226 focused check
   ↓
C-06 composed acceptance / legitimate ceiling
   ↓
existing persistence / restart owners
```

This graph is a dependency model for requirements reasoning only. It is **not** a proposed workflow engine or state machine.

## What Phase 0/1 has not yet established

Before Phase 0/1 completion, the following remain necessary:

1. trace C-01–C-06 against the full relevant rows of `requirements/domain-requirements.tsv` and prior programme synthesis/concept artifacts to avoid duplicate requirements;
2. classify which parts of C-01–C-06 are already semantically owned versus genuinely new composition requirements;
3. inspect current executable tools/contracts specifically for reusable inputs/outputs needed by C-02/C-03/C-06;
4. test the dependency graph against at least one non-Reg.-Ii.-5 Project/system case already present in the repository;
5. determine whether #226 prerequisite is met after this traceability pass;
6. reconcile only the completed Phase-0/1 result to #225 as `LOCAL PHASE RESULT`.

## Anti-fragmentation / self-audit criteria

Phase 0/1 FAILS if it:

- produces a new taxonomy/architecture instead of owner mapping;
- copies canonical semantics into a second truth store;
- treats one pilot failure as the generic mechanism;
- equates issue/phase completion with #225 progress without reconciliation;
- proposes deterministic control over open scholarly judgement;
- leaves stable composition semantics dependent on model memory without examining formalization;
- pushes derivable methodological/technical sequencing back to the non-specialist Human Owner;
- expands into implementation before D-016.

## Phase 0/1 exit criteria

Phase 0/1 may be called complete only when:

- every minimum chain link has an owner/support/maturity classification;
- existing semantics and executable support are distinguished from actual gaps;
- partial/missing links have the smallest candidate generic requirements and falsification criteria;
- dependencies among missing links are explicit;
- #226's prerequisite can be judged as met/not met without chat;
- a fresh context can use this artifact plus canonical owners to prepare competing concepts without rediscovering the problem;
- the result is reconciled to #225 as `LOCAL PHASE RESULT`, not whole-system completion.

## Current state

**Phase 0 mapping: FIRST COMPLETE PASS.** All 15 minimum links now have an owner/support/maturity classification and the central gap cluster/dependencies are explicit.

**Phase 1: ACTIVE.** C-01–C-06 are candidate consolidation requirements with falsification boundaries. They are not yet promoted as new canonical requirements because duplicate/coverage traceability against `domain-requirements.tsv`, prior synthesis/concept artifacts and executable tooling is still outstanding.

Consequence for #225: **LOCAL PROGRESS ONLY.** The audit hypothesis is strengthened: the primary deficiency is composition/derivation across existing mature owners, not absence of mission, scholarly method, authority rules or structural control. No architecture, D-016 admission or whole-system acceptance follows from this pass.
