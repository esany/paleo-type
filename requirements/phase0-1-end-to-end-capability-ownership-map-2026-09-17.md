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


## Next major work block — execution prompt

Use this prompt as the next **single coherent Phase-1 work block** under #227. Execute it repository-first and persist the completed result into this artifact before treating the block as complete.

> **Mission.** Rehydrate the current repository as authority and complete the Phase-1 traceability / deduplication / executable-reuse / non-pilot falsification block for C-01…C-06 under #227. Preserve #225 as the parent system outcome. Do not choose architecture, admit implementation, create Project scholarly scope/priority, or treat any local PASS as whole-system success.
>
> **Required fresh inputs.** Read `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, #225 including its anti-fragmentation guard, #227, this artifact, `methodology/maintenance.md`, `methodology/workflow.md`, `methodology/historical-source-workflow.md`, `methodology/research-gates.md`, `methodology/project-lifecycle.md`, `methodology/quality-and-learning.md`, `methodology/ai-governance.md`, the relevant rows of `requirements/domain-requirements.tsv`, the system-operationalization audit/problem-frame, prior whole-system synthesis/concept artifacts, and the executable tools/contracts needed to test reuse claims. Read only additional files that become materially necessary.
>
> **Part A — Requirement traceability and deduplication.** For each C-01…C-06:
> 1. identify every existing canonical requirement/method/decision that already owns any part of its semantics;
> 2. distinguish exactly among:
>    - `ALREADY OWNED / NO NEW SEMANTIC`,
>    - `DISTRIBUTED BUT COMPOSITION MISSING`,
>    - `SEMANTIC EXISTS BUT EXECUTABLE/DISCOVERABILITY GAP`,
>    - `GENUINELY MISSING GENERIC REQUIREMENT`,
>    - `CONTEXTUAL / NOT SAFE TO GENERALIZE`;
> 3. cite the exact owner(s) and do not copy their semantics into a second truth store;
> 4. state the smallest residual requirement, if any, after deduplication;
> 5. state what would falsify that residual requirement.
>
> **Part B — Executable reuse audit.** Inspect the current executable control plane, especially `tools/project_context.py`, `tools/source_contract.py`, `corpus/source-contract.json`, intake/resolver/validation helpers and relevant regression tests. For each C-01…C-06 determine:
> - which required inputs are already machine-readable or derivable;
> - which outputs are already derivable/validated;
> - which semantics remain only prose/model-mediated;
> - which repeated inference appears stable enough for deterministic derivation/validation without scholarly loss;
> - which inference must remain AI-assisted, specialist, or Human-Owner controlled.
>
> Do **not** infer that something needs new software merely because it is not currently executable. First determine whether better derivation/discoverability from existing owners is sufficient.
>
> **Part C — Non-pilot falsification.** Select at least one materially different repository case outside Reg. Ii 5 using repository evidence, not convenience. Test the candidate residuals and dependency graph against it. The counter-case should differ in source/problem structure, maturity, or system-development context enough that Reg.-Ii.-5-specific assumptions would fail. For each candidate record:
> - what survives unchanged;
> - what is pilot-specific and must be removed/reframed;
> - what additional generic semantic is actually demonstrated, if any.
>
> Do not patch the counter-fixture into a growing universal model. A failure is evidence against the candidate abstraction.
>
> **Part D — Dependency challenge.** Challenge the current graph
>
> ```text
> C-01 → C-02 → C-03 → C-04 → existing execution → C-05 → C-06
> ```
>
> For every edge classify it as `hard dependency | conditional dependency | useful ordering only | unsupported coupling`. Remove any dependency that exists only because of the current pilot/history or because the previous analysis presented it that way. Record parallelizable or independently resolvable functions where demonstrated.
>
> **Part E — #226 admission check.** After A–D, determine whether #226's stated prerequisite is met. Do not perform #226 itself inside this block. Return only:
> - `PREREQUISITE MET` with the specific Phase-0/1 evidence now available; or
> - `PREREQUISITE NOT MET` with the exact missing evidence.
>
> **Required output in this artifact.** Produce:
> 1. a C-01…C-06 traceability/deduplication matrix;
> 2. an executable-reuse matrix;
> 3. a non-pilot falsification result;
> 4. a challenged dependency graph;
> 5. the smallest residual generic-requirement set, if any;
> 6. explicit deterministic / AI / specialist / Human-Owner boundaries for those residuals;
> 7. #226 prerequisite disposition;
> 8. a Phase-1 exit assessment against every #227/this-artifact exit criterion.
>
> **Acceptance rules.**
> - No candidate survives merely because it sounds desirable.
> - No new requirement is accepted when an existing owner already expresses the needed semantics adequately.
> - No new executable component is proposed in this block.
> - Stable semantics that could be derived mechanically must be identified as such; open scholarly judgement must not be forced into determinism.
> - The non-specialist Human Owner must not be made responsible for derivable method/engineering sequencing.
> - Reg. Ii 5 is evidence only.
> - Local completion is `LOCAL PHASE RESULT`, never #225 completion.
>
> **Stop condition.** Stop this block only when the residual gap set is small, deduplicated, cross-fixture challenged, and precise enough that a fresh context could move to #226 (if admitted) and then prepare Phase-2 competing concepts **without rediscovering the problem or relying on this chat**. If that condition is not met, persist the exact unresolved evidence/traceability deficit and keep #227 active; do not compensate by inventing architecture.

### Cursor after this prompt

Current executable cursor for #227:

```text
C-01…C-06 traceability/deduplication
→ executable reuse audit
→ non-pilot falsification
→ dependency challenge
→ #226 prerequisite disposition
→ Phase-1 exit assessment
→ reconcile completed LOCAL PHASE RESULT to #225
```

No new child Issue is required for this block.


## Executed Phase-1 block — traceability, executable reuse and falsification result

Status: **COMPLETE LOCAL PHASE RESULT under #227.** This section executes the persisted Phase-1 block. It is requirements/analysis evidence for #225, not architecture selection, D-016 implementation admission, Project scholarly priority or whole-system acceptance.

### A. C-01…C-06 traceability / deduplication

| Candidate | Existing semantic owners / evidence | Deduplicated disposition | Smallest residual after deduplication | Falsification boundary |
|---|---|---|---|---|
| **C-01 Durable outcome reference** | Governing Objective human auditability + restartability; project-lifecycle.md and Project project.yml own Project purpose/current scope; Project STATUS.md owns current gate/restart/authorized next action; REQ-GWP-008; REQ-UX-007; workflow.md work-context/cursor semantics | **DISTRIBUTED BUT COMPOSITION MISSING** | When a Human-Owner-authorized desired scholarly outcome exists, a fresh context must be able to bind/reference that outcome to its canonical purpose/scope authority without allowing the outcome reference itself to manufacture scope/priority. Absence of an authorized outcome remains a valid explicit state. | If existing Project purpose/scope/STATUS plus derived context already recover the governing desired outcome reliably across materially different authorized-outcome fixtures, no additional integration semantic is needed. |
| **C-02 Outcome → unmet requirements** | S1–S9 in historical-source-workflow.md; G1–G6 in research-gates.md; domain-requirements.tsv; Project STATUS/gate/gap state; GO precedence | **GENUINELY MISSING GENERIC COMPOSITION REQUIREMENT** — not missing scholarly rules | Given authorized outcome + applicable scope + current canonical evidence/maturity, expose the applicable unmet requirements and their basis, reusing existing owners. Stable portions should be derivable; open scholarly applicability/judgement must remain explicit. | If current canonical owners can already yield materially equivalent unmet-requirement sets in fresh contexts without free-form model reconstruction, only discoverability/derived-view work remains. |
| **C-03 Capability / responsibility resolution** | GO transdisciplinary invariant and Human/specialist/AI boundaries; historical-source-workflow.md expertise routing; domain-requirements.tsv already carries domain, validation_mode, specialist_trigger; REQ-DOM-001; REQ-GWP-005; REQ-AI-010; REQ-UX-011; ai-governance.md | **SEMANTIC EXISTS BUT EXECUTABLE / COMPOSITION GAP** | For an applicable unmet requirement, expose the governing competence and responsibility mode from existing semantics: deterministic where controlled, AI-assisted where genuinely non-deterministic, specialist where qualified judgement is required, Human Owner only for non-derivable authority/purpose/use decisions. No new permanent role topology is justified. | If the existing requirement metadata + METHOD already provide a sufficiently reliable derived routing surface, no new semantic requirement survives. |
| **C-04 Outcome-constrained vertical work slice** | GO technical subsidiarity/lean structure; quality-and-learning.md Goal Alignment; workflow.md current-target authority, first-scholarly-action protection and support-to-support escalation stop; historical-source-workflow.md research-question control; AGENTS research-outcome-before-infrastructure | **DISTRIBUTED BUT COMPOSITION MISSING** | A newly selected bounded work slice must be traceable to one or more applicable unmet outcome requirements and state its bounded completion/return condition; the smallest local defect is not sufficient justification. Already-authorized routine work need not be replanned. | If current target/first-scholarly-action/Goal-Alignment semantics already prevent horizontal local optimization across real fixtures, no additional composition semantic is needed. |
| **C-05 Outcome continuity across decomposition / repair** | **Programme/phase/result subset already requirements-resolved, concepted, implemented and Result-Review PASS** in the 2026-09-16 continuity arc; current semantic owner is maintenance.md with a narrow execution hook in workflow.md. Task-local workflow also owns execution cursor, return/review condition, support containment, no-progress redirect, first scholarly action and support-chain stop. #225 adds a programme-local anti-fragmentation guard. | **ALREADY OWNED for material programme/phase/result transitions; PARTIAL / REVIEW-REQUIRED for broader phase-independent decomposition** | No new requirement is accepted here. #226 now has sufficient evidence to test whether the already-owned programme/task-local pieces fully cover arbitrary outcome-preserving decomposition/repair, require a bounded existing-owner refinement, or remain contextual. | If #226 finds existing maintenance/workflow semantics sufficient across task, repair, review and programme contexts, C-05 creates no additional generic requirement/mechanism. |
| **C-06 Composed outcome acceptance / legitimate ceiling** | Gate completion/residual-uncertainty semantics in research-gates.md; assurance-status separation in quality-and-learning.md; dependency/resource authority in workflow.md; specialist boundary in ai-governance.md; Project STATUS restart/gate owner; #225 T10/T11 | **DISTRIBUTED BUT COMPOSITION MISSING** | For an authorized outcome, compose applicable requirement satisfaction, maturity and assurance/authority/evidence limits into a restartable outcome-level disposition. Required meanings include usable outcome reached, valid outcome with work remaining, evidence ceiling, specialist dependency, Human-Owner decision required, and action-local technical inability. This does not imply one universal status enum. | If existing owners can already derive these distinctions reliably as a view without new semantics, no new canonical status model is justified. |

### Deduplication conclusion

The six initial candidates do **not** justify six new Requirements or six components.

The smallest residual requirement surface after deduplication is:

**R-1 — Authorized outcome binding / explicit absence**

An authorized desired scholarly outcome must remain restartably bound or derivably linked to the canonical authority/scope that legitimates it; when no such outcome/scope is authorized, the system must return that absence rather than generate work.

**R-2 — Outcome/state → applicable unmet requirements**

Given R-1 plus current canonical evidence/maturity, the system must expose the applicable unmet requirements by reusing S1–S9, G1–G6 and existing domain requirements, with stable derivation separated from scholarly applicability/judgement.

**R-3 — Requirement → capability/responsibility + bounded vertical execution route**

For each applicable unmet requirement, the system must expose the appropriate competence/responsibility boundary and, where execution is authorized, the smallest coherent outcome-linked work slice. It must reuse existing domain/validation/specialist semantics and must not make the non-specialist Human Owner choose derivable method/engineering steps.

**R-4 — Composed outcome disposition / legitimate ceiling**

Whole-outcome continuation, completion or pause must be derived/explained from applicable requirement satisfaction plus scholarly/technical assurance and evidence/authority/specialist limits. Local task/CI/Issue completion is insufficient.

**C-05 is deliberately not duplicated into R-1…R-4.** Its programme/phase subset is already METHOD; #226 owns the remaining Generic-Fit question for broader decomposition/repair continuity.

No new formal requirement family, domain-requirements.tsv domain, workflow engine, role registry, outcome schema or state machine follows from this consolidation. Exact canonical ownership/serialization of R-1…R-4 is a Phase-2 design question, not a Phase-1 assumption.

---

### B. Executable-reuse audit

| Existing executable surface | Already machine-readable / derivable | What it does **not** establish | Reuse consequence for #225 |
|---|---|---|---|
| corpus/source-contract.json + tools/source_contract.py | Source/File/Project/use/crosswalk referential structure; Project root; structural status; Project-source uses; use evidence; controlled File/crosswalk values | desired scholarly outcome, scholarly applicability, gate achievement, research priority, reading/interpretation | Keep as structural/provenance substrate; do not rebuild under integration abstraction |
| tools/project_context.py | Project definition, documentary anchor, internal Sources, uses/evidence, File readiness facts, crosswalk references, canonical STATUS text, explicit do-not-infer boundary | Project purpose not already represented; scholarly NEXT ACTION; evidence access/readiness beyond observed fields; witness attribution; readings/interpretation; unmet requirements | Strong input/context assembler for R-1/R-2/R-4, but currently stops before the integration derivation |
| tools/source_intake.py | SHA-first File identity path; Source/structural Project context; evidence-readiness distinctions; explicit routing alternatives; unresolved-file stop | Source identity when unresolved; Project materialization/use/priority; research function; target-context scholarly readiness | Positive precedent: stable distributed semantics can become a small derived adapter without becoming authority |
| requirements/domain-requirements.tsv | Requirement IDs, domain, requirement text, information needed, current support, failure/risk, validation mode, specialist trigger, source issue, architecture handoff | dynamic applicability to a concrete outcome/scope/claim; proof that requirement is currently unmet; scholarly truth | Important reusable structured input for R-2/R-3; do not create a parallel competence registry by default |
| Project project.yml / STATUS.md | purpose/root/scope text, current gate/restart/gaps/NEXT ACTION when recorded | ordinary-language need→purpose binding if not already owner-authorized; automatic outcome target; automatic task generation | Reuse as canonical Project authority/restart owners; integration must derive/reference rather than copy |
| Existing regression tests | structural ownership, context restart, Corpus-only validity, Source/File routing boundaries, local recovery classes | end-to-end Human-need→outcome composition | Reuse as negative/structural fixtures; #225 still needs later vertical composition acceptance |

#### Deterministic / AI / specialist / Human boundary after reuse audit

**Stable enough to derive/validate mechanically where inputs are established:**
- canonical Source/File/Project/use/crosswalk facts;
- Project/corpus structural relationships and known evidence bindings;
- existing controlled gate/requirement dependencies where semantic applicability is fixed;
- requirement metadata such as owning domain, validation mode and specialist trigger;
- whether an existing owner records no authorized scope/NEXT ACTION;
- whether a local result is being promoted beyond its stated authority;
- generated restart/context views and referential consistency.

**AI-assisted / scholarly synthesis remains appropriate for:**
- translating an ordinary-language scholarly need into candidate scholarly result semantics before/while Human authority is made explicit;
- deciding applicability of open-ended disciplinary requirements when this depends on source/question meaning;
- forming/assessing scholarly hypotheses and source-critical interpretations;
- explaining and composing non-deterministic alternatives without converting plausibility into evidence.

**Qualified specialist remains required for:**
- consequential palaeographic, philological, editorial, archival, historical or other domain judgement where METHOD/requirements trigger independent review;
- claims that cannot be validated from controlled evidence plus ordinary scholarly process alone.

**Human Owner remains required only for genuinely non-derivable authority decisions:**
- Project/purpose/material priority/scope decisions where not already established;
- unresolved rights/authority facts;
- consequential use/publication;
- D-016 material system implementation admission;
- material Governing Objective amendment.

The integration problem is therefore not solved by “more AI”. Stable portions of R-1…R-4 should stop depending on model memory once Phase 2 identifies a lossless minimal representation/derivation path.

---

### C. Non-pilot falsification

The Phase-1 candidates were challenged against three non-Reg.-Ii.-5 contexts.

#### Fixture F1 — Reg. Ii 3: rich canonical evidence, no authorized current scholarly outcome

Current Reg. Ii 3 state contains:
- a Human-Owner-established Project and documentary root;
- exact File provenance and substantial canonical crosswalks;
- recovered historical work state;
- **no owner-selected active scholarly scope**;
- **no current G1–G6 progression for an edition target**;
- **no owner-selected manuscript/source-research NEXT ACTION**.

tests/test_regii3_crosswalk_restart.py additionally protects that a complete crosswalk is exposed **without creating research priority**.

**Falsification consequence:**
- R-1 must support an explicit “no authorized current outcome/scope” result.
- R-2/R-3/R-4 must not activate merely because evidence, crosswalks, gate semantics or unresolved possibilities exist.
- Any architecture that treats “available evidence + generic method” as sufficient to generate work is falsified.

This fixture removes the pilot-specific assumption that an unresolved manuscript locus always implies a desired continuation.

#### Fixture F2 — Corpus-only routing: valid Source/File structure with no Project

tests/test_corpus_only_routing.py demonstrates that:
- Source/File/part_of structure can validate with **zero Projects**;
- structural containment does not materialize a Project.

**Falsification consequence:**
- R-1 must be authority-gated above structural evidence.
- R-2 cannot treat Corpus completeness/availability as a research outcome.
- R-3 cannot assign a Project-level execution route without Project authority.
- “No Project / Corpus-only” is a legitimate terminal routing result.

This fixture falsifies any generic model that presumes every Source has an active Project/outcome hierarchy.

#### Fixture F3 — #69 intake/routing: same integration class outside manuscript-reading progression

#69 documented a generic research-intake need where the correct semantics already existed across Source/File/Project/maintenance/contract owners, yet a fresh researcher/AI still had to synthesize the execution order from distributed prose.

The bounded admitted solution:
- retained existing semantic owners;
- made the sequence explicit in existing METHOD;
- reused the Source Contract;
- added the small read-only tools/source_intake.py adapter;
- preserved explicit Human decisions only where non-derivable;
- added regressions;
- rejected a new intake platform/schema/workflow engine.

Its later correction also established:

~~~text
correct File identity
!= correct Project→Source research function
!= correct current work target / NEXT ACTION
~~~

**Generic consequence:**
- the #225 composition problem is not Reg.-Ii.-5-specific;
- “semantics exist but are distributed/model-mediated” is a demonstrated system failure class;
- a successful future solution should prefer a thin derived composition surface over duplicating canonical owners;
- deterministic operationalization is justified only for the stable subset;
- support/execution correctness must not select scholarly priority.

No additional generic semantic beyond R-1…R-4 is introduced by F3.

---

### D. Dependency challenge

The initial linear chain

~~~text
C-01 → C-02 → C-03 → C-04 → execution → C-05 → C-06
~~~

is **too linear** and contains unsupported coupling.

| Edge | Disposition | Reason |
|---|---|---|
| C-01 → C-02 | **hard dependency inside an outcome-driven path; conditional globally** | Unmet requirements require a legitimate target/outcome. Reg. Ii 3 and Corpus-only prove that absence of authorized outcome is a valid stop. |
| C-02 → C-03 | **conditional dependency** | In the #225 path, unmet requirements normally drive capability/responsibility. But an already-authorized bounded claim/task can activate a domain directly without globally recomputing all unmet requirements. |
| C-03 → C-04 | **useful ordering / partial co-dependency, not hard** | Capability knowledge can constrain a slice, but slice formation can also expose which competencies are needed. Do not impose a permanent router-before-planner pipeline. |
| C-04 → existing execution | **hard only for newly formed work; not for already-authorized routine tasks** | Existing workflow.md can execute a valid bounded task directly. |
| execution → C-05 | **unsupported as serial edge** | Outcome continuity is a cross-cutting invariant around decomposition/repair/return, not a phase after execution. |
| C-05 → C-06 | **not hard** | Outcome acceptance can be assessed when no repair occurred; repair continuity must not be a prerequisite ceremony for every result. |
| C-02 → C-06 | **hard/conditional for outcome-level disposition** | Completion/ceiling must be tested against applicable requirements; where no authorized outcome exists, the valid disposition is absence rather than acceptance. |
| C-01 → C-06 | **hard for any whole-outcome completion claim** | Whole-outcome acceptance has no meaning without a legitimate outcome/authority basis. |

#### Challenged dependency shape

~~~text
                 ┌────────────────────────────────────┐
                 │  R-1 authorized outcome / absence  │
                 └────────────────┬───────────────────┘
                                  ↓
                 ┌────────────────────────────────────┐
                 │ R-2 applicable / unmet requirements│
                 └──────────┬───────────────┬─────────┘
                            │               │
                            ↓               ↓
                  R-3 capability +      R-4 outcome
                  bounded vertical       disposition /
                  execution route        legitimate ceiling
                            │
                            ↓
                  existing execution
                  METHOD / workflow

C-05 / #226 question:
cross-cuts decomposition, local PASS/FAIL, support/repair and return;
it is not a downstream phase.

Persistence / restartability:
cross-cuts the entire graph and remains owned by existing canonical/restart owners.
~~~

This is a dependency model only, not a proposed state machine.

---

### E. #226 prerequisite disposition

**PREREQUISITE MET.**

Repository-backed basis now exists without this chat:

1. all 15 end-to-end links have owner/support/maturity classifications;
2. C-05 has been traced against the already-completed 2026-09-16 programme-continuity Requirements → Concept → admitted METHOD refinement → Result Review chain;
3. current maintenance.md / workflow.md programme/phase semantics are known to be implemented, not merely conceptual;
4. task-local cursor/return/support semantics in workflow.md have been separately identified;
5. Reg. Ii 3 and Corpus-only provide negative fixtures where continuity/routing must **not** manufacture work;
6. #69 provides a materially different system-development/intake fixture for distributed-semantics→thin-operationalization;
7. #225's anti-fragmentation tests define the broader composition failure that #226 is to challenge.

#226 may therefore execute its own Generic-Fit review. This Phase-1 result does **not** pre-judge its disposition.

---

## Phase-1 exit assessment

| #227 / artifact exit criterion | Result |
|---|---|
| every minimum chain link has owner/support/maturity classification | **PASS** — Phase-0 table covers all 15 |
| existing semantics/executable support distinguished from actual gaps | **PASS** — dedup + executable-reuse matrices above |
| partial/missing links reduced to smallest candidate generic requirements with falsification | **PASS** — R-1…R-4; C-05 routed to #226 rather than duplicated |
| dependencies among residuals explicit | **PASS** — challenged non-linear graph above |
| #226 prerequisite judgeable without chat | **PASS — PREREQUISITE MET** |
| fresh context can prepare competing concepts without rediscovering the problem | **PASS at Requirements level** — residuals, reuse substrate, authority boundaries, counter-fixtures and non-goals are persisted |
| result reconciled to #225 as local phase result | **PENDING ISSUE RECONCILIATION at time of this artifact write; required before #227 close** |

### Phase-1 conclusion

Phase 0/1 does **not** support a new holistic workflow engine or six new system objects. It narrows #225 to a small integration problem over mature existing owners:

~~~text
authorized desired outcome / explicit absence
        ↓
applicable + unmet requirements
        ↓
capability / responsibility + smallest outcome-linked work
        ↓
existing scholarly/execution machinery
        ↓
composed outcome disposition / legitimate ceiling
~~~

with outcome continuity under decomposition handled as a separate cross-cutting Generic-Fit check in #226 because a substantial subset is already generic METHOD.

**Consequence for #225: LOCAL PHASE RESULT.** Phase 0/1 is complete once this result is returned to #225/#227 issue state. It does not establish architecture, D-016 admission, implementation readiness or whole-system success.
