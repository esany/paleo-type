# Human-proxy, work-lifecycle and context-efficiency audit — 2026-10-03

**Status:** NON-NORMATIVE SYSTEM ANALYSIS / TARGET-STATE REFINEMENT EVIDENCE — NO D-016 ADMISSION  
**paleo-type baseline:** `main@5a02c9bd61469b457d5af637e00dd2b4c44020a1`  
**Wissensarbeit comparator baseline:** `main@b448915cf774c573dbf82cf2e17bcb03c10a9ed8`  
**Refines analysis of:** `requirements/repository-target-state-implementation-readiness-2026-10-03.md`, `requirements/repository-knowledge-lifecycle-d016-decision-surface-2026-10-02.md`, `requirements/product-co-development-boundary-deep-check-2026-10-03.md`  
**This artifact is not:** METHOD, Project scholarly scope, a manuscript `NEXT ACTION`, D-016 implementation admission, a new workflow engine, an autonomous priority grant, a package/runtime implementation decision, or proof of scholarly/system acceptance.

## A. Executive finding

The Human Owner's recurring role as a manual relay, dispatcher or confirmation proxy is **already prohibited in principle** by current paleo-type governance. `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `methodology/maintenance.md` and `methodology/quality-and-learning.md` consistently assign routine bounded work to AI/tooling and reserve Human intervention for genuinely non-derivable purpose, priority, authority, acceptance, rights/risk or consequential-use decisions. The remaining failure is therefore primarily **operational**, not constitutional.

The strongest current cause is a gap between **authorized work semantics** and **executable/restartable work continuation**. `methodology/workflow.md` already requires task owner, stage, bounded action, prerequisites, cursor, completion, non-goals and return condition, while the lifecycle target-state analysis already calls for closable work/programme semantics and a bounded active context. But the current generic executable integration surface, `tools/outcome_context.py`, deliberately stops before work generation: it exposes a responsibility boundary and authority state while always leaving `generated_next_action = None` and `NO_DETERMINISTIC_WORK_GENERATION`. Thus paleo-type can increasingly reconstruct what is true and what authority is absent, but it does not yet generically encode when an already-authorized work sequence may simply continue without another Human `weiter` / `ausführen` / routing instruction.

The user-side intuition that **planning is already work** is supported with one important qualification. The current D-016 path does not require Human permission before analysis, requirements or concept work; its Human gate is before material development. So the formal authority rule is not simply `Human approves every phase`. However, the generic system-change path remains coarse (`analysis -> requirements -> concept -> admission -> development -> tests -> result review`) and does not make research, detailed design, implementation planning, validation, reconciliation and learning equally explicit as restartable bounded work. The correct refinement is therefore not a longer mandatory waterfall. It is a **phase-neutral authorized-work lifecycle**: analysis, requirements, research, concept, design, implementation, verification, validation and reconciliation can all be bounded work packages with the same authority/continuation/closure semantics, while actual transitions remain need/state-driven.

`Wissensarbeit` is strong comparative evidence for this direction. It explicitly states `Human-in-the-loop, not human-as-workflow-engine`, has an event-capable lifecycle from bootstrap through research/model/decide/build/verify/use/learn, a small execution cursor, derived current-state views, a Context Compiler capability, explicit operational Human-burden rules, and a fail-closed `next` rule that returns a next action only when exactly one ready step is derivable. It also contains much sharper token/context-economy candidates: canonical references instead of history replay, derive-before-asking, smallest sufficient semantic task packets, context economy without material-context starvation, externalization before context compaction, and concise delta/evidence returns from scarce execution contexts. These are reusable **properties**, not authority to copy Wissensarbeit's product architecture or its candidate Skills into paleo-type.

The strongest architecture disposition is therefore:

> **BOUNDed refinement of the existing Class-B lifecycle architecture, not a new architecture class.**
>
> Extend IC-01/IC-03/IC-06 with explicit Human-relay elimination, phase-neutral authorized-work continuation, `decision-needed` semantics, applicability-bounded context compilation and a compact result/return envelope. Keep IC-02 as the current/history/supersession foundation. Test whether a minimal persisted execution cursor is actually needed only after those semantics are explicit; do not preselect a workflow engine or autonomous planner.

D-016 remains **NOT ADMITTED**.

---

## B. Fresh authority and scope boundary

This pass freshly inspected the current paleo-type governing and operational surfaces, including:

- `GOVERNING_OBJECTIVE.md`;
- `AGENTS.md`;
- `README.md`;
- `DECISIONS.md`;
- `MILESTONES.md`;
- `methodology/maintenance.md`;
- `methodology/workflow.md`;
- `methodology/project-lifecycle.md`;
- `methodology/quality-and-learning.md`;
- `methodology/historical-source-workflow.md`;
- the current target-state and D-016 decision-surface analyses;
- `tools/outcome_context.py` and current requirements/context boundaries;
- current GitHub work state for #225/#230 and open PRs;
- current manuscript Project owners.

Current manuscript Project owners all explicitly record **no owner-selected active scholarly scope**. This audit therefore creates no scholarly work target and does not use system-analysis work to manufacture manuscript activity.

Fresh comparator inspection covered current `esany/Wissensarbeit` state including:

- `project/GOVERNING_OBJECTIVE.md`;
- `README.md`;
- `project/CURRENT_STATE.md`;
- `system/lifecycle.json`;
- `system/authority.json`;
- `system/building_blocks.json`;
- `system/material_state.json`;
- `system/reconciliation.json`;
- `project/execution_state.json`;
- `tools/work.py`;
- #48, #52, #53, #55;
- the completed Owner-Burden work #80 / PR #81.

Wissensarbeit is comparative evidence only. Its future-template product identity, persisted cursor shape, Building Blocks and Skill candidates do not become paleo-type authority by analogy.

---

## C. Meat-proxy failure model

### C1. Definition

A Human acts as an **artificial relay/proxy** when no materially Human-owned question is unresolved, yet work cannot continue without the Human doing one of the following:

- saying `weiter`, `ausführen`, `ja` or equivalent merely to advance an already-authorized sequence;
- selecting an execution environment/tool/capability that the system can derive;
- carrying a child result to the parent work context;
- re-supplying known repository state or previously established inputs;
- choosing technical sequencing already entailed by accepted requirements/design;
- manually synchronizing status/current pointers;
- reconstructing the return target after a local repair;
- re-confirming a deterministic next action because no operational cursor/context exists.

This is different from legitimate Human-in-the-loop authority.

### C2. Gate classification

| Gate class | Meaning | Human needed? |
|---|---|---|
| `AUTHORITY GATE` | new/changed purpose, material priority/scope, Project creation/boundary, D-016 admission, unresolved rights/authority, consequential use/publication | **yes** |
| `JUDGEMENT GATE` | genuinely non-derivable owner value/acceptance, or specialist/domain judgement outside AI/tool authority | **Human or qualified specialist as applicable** |
| `EVIDENCE GATE` | required evidence unavailable/insufficient; continuation depends on new evidence or an authority choice | **only if Human action/authority is actually needed** |
| `EXECUTION ONLY` | next work is already entailed by authorized objective/scope/design and prerequisites are satisfied | **no** |
| `ARTIFICIAL HUMAN RELAY` | Human is used as router, copier, confirmer or context bridge despite `EXECUTION ONLY` semantics | **must be removed** |

### C3. Existing paleo-type rule already points to the desired boundary

Current `AGENTS.md` assigns routine bounded source research, deterministic resolution/validation, derived views, repository hygiene, bounded implementation and propagation to AI/implementation agents. `maintenance.md` states that an admitted material scope may proceed without owner micromanagement. `quality-and-learning.md` says Human/governance review must not become routine approval for ordinary scholarship or bounded implementation inside admitted scope.

Therefore a new principle `Human must not be a workflow engine` would mostly restate existing intent. What is missing is a generic operational mechanism that can **demonstrate** when the state is `EXECUTION ONLY`, continue, and stop exactly when that ceases to be true.

---

## D. Planning is work: lifecycle coverage

### D1. Holistic work model

For system/research-system work, the useful conceptual coverage is:

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

This is a **coverage model**, not a required linear pipeline. Real work may loop, omit irrelevant stages, combine stages, return to earlier stages or terminate at a legitimate ceiling.

### D2. paleo-type coverage matrix

| Work phase | Current paleo-type support | Operational maturity |
|---|---|---|
| Problem / need | GO, Project purpose, issue/problem analyses, #225 problem framing | **explicit semantics; work-state handling uneven** |
| Analysis | D-016 analysis stage; audit artifacts; AI reasoning | **explicit METHOD/governance; mostly AI/work-artifact execution** |
| Requirements | `requirements/`, D-016 requirements stage, domain requirements | **explicit and substantial** |
| Research / SOTA / domain evidence | S1-S9 scholarly METHOD; disciplinary activation; research artifacts | **very strong for scholarship; less explicit as generic system-design phase** |
| Concept | D-016 concept stage and historical concept artifacts | **explicit** |
| Detailed design | usually contained in concept/admitted implementation work rather than a generic named lifecycle state | **partly implicit** |
| Implementation planning / decomposition | Issues/PRs, workflow task contract, target-state candidate decomposition | **semantic support exists; no generic executable continuation owner** |
| Implementation | D-016 development; Dev interface; tests/PRs | **explicit once admitted** |
| Verification | deterministic tests, CI, source contract, technical assurance | **strong** |
| Validation | scholarly adequacy, specialist validation, Human/governance review separated | **strong semantically, event-triggered** |
| Reconciliation | maintenance programme/result reconciliation; propagation rules | **explicit, but lifecycle operationalization incomplete** |
| Closure | bounded work/parent reconciliation target-state; Issues close locally | **known structural gap / IC-01/02** |
| Learning | quality/learning loop, Generic-Fit, Project-local-first promotion | **explicit** |

### D3. Key correction to the existing D-016 framing

D-016 is **not** wrong because it gates implementation after analysis/requirements/concept. That is an appropriate material system-change authority boundary. The gap is different:

- analysis, requirements, research, concept and detailed design are already substantive work;
- they need the same restartability, bounded context, parent contribution, closure and Human-relay protection as implementation work;
- `implementation admission` must not be misread as `start of work`;
- autonomous continuation inside already-authorized analytical/design work should not require repetitive Human confirmations either.

Therefore IC-01 should own **generic bounded work lifecycle semantics**, not an implementation-only lifecycle.

---

## E. Wissensarbeit coverage and what is actually operational

### E1. Explicit lifecycle

Current Wissensarbeit publishes the lifecycle:

```text
bootstrap
→ discover
→ understand
→ research
→ model
→ decide
→ build
→ verify
→ use
→ learn
→ maintain
→ archive
```

Its allowed transitions are deliberately non-linear: research can return to understanding/model, verification can return to build/model, and learning can reactivate several earlier stages. This is stronger evidence for a **state/need-driven lifecycle** than for a waterfall.

### E2. Capability coverage

Current Building Blocks explicitly include:

- Context Compiler;
- Competence Discovery;
- SOTA/Fit Research;
- Systemic Integration;
- Requirements and Criteria;
- Concept and Architecture;
- Implementation;
- Assurance;
- Trace and Explain;
- Derived Views;
- Operations/DevOps;
- Use and Learn.

Automation levels are already differentiated: context and derived views are declared full automation; research/competence high; Requirements/Design high with material Human gate; implementation high; assurance maximum except judgement.

### E3. What is operational versus candidate

Wissensarbeit already has a small executable cursor and guard:

- `project/execution_state.json` references a planning source and current work;
- allowed actions and implementation permission are explicit;
- `work.py preflight` fails when action/dependency/authority does not permit execution;
- `work.py next` returns a next step only if exactly one ready step is derivable;
- otherwise it fails closed with `no deterministic next action`;
- `complete` requires repository/Git-persisted completion evidence.

However, richer capabilities remain candidates rather than proven runtime:

- #48 quality-preserving execution routing;
- #52 modular-organic Skill-system development model;
- #53 Intent/Gap Semantic Fidelity;
- #55 Task Compilation / Bounded Interaction.

Thus Wissensarbeit does **not** establish that a complete autonomous planner already exists. It demonstrates that useful operational semantics can be made explicit without such a planner.

---

## F. What capable AI already does out of the box

A capable model/agent can often perform, when the needed evidence/tools are available:

- problem decomposition and analysis;
- requirements drafting and acceptance-condition formulation;
- SOTA/Best-Practice research;
- competing concept generation and comparison;
- detailed design;
- implementation planning;
- implementation/code/data/document work;
- test design and self-review;
- synthesis of results and residual risks.

That capability does **not** mean the research system already supports the lifecycle. The system still has to supply and preserve:

```text
correct purpose / authority
+ current bounded work
+ applicable rules / requirements
+ evidence / provenance
+ allowed actions
+ material decision boundary
+ completion condition
+ return / reconciliation target
+ current/history/supersession semantics
+ restart without chat
```

The key distinction is:

> `the model can reason about the phase` != `the repository can reliably authorize, contextualize, persist, resume, review, reconcile and close that work`.

This explains why simply using a stronger model does not remove the Human-relay failure.

---

## G. Token and context efficiency

### G1. The dominant cost is reconstruction, not evidence itself

Current paleo-type already says complete **applicable** context is required and indiscriminate repository loading is not. But the present authority/method surface is large enough that an unspecialized fresh-agent bootstrap can become expensive if applicability is not compiled.

Current file sizes give a useful lower-bound illustration:

- root governing/orientation/decision surfaces (`GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `README.md`, `DECISIONS.md`, `MILESTONES.md`) total about **67,067 characters**;
- the ten current `methodology/` files total about **143,519 characters**;
- loading both indiscriminately is therefore about **210,586 characters before any Project state, requirements table, Issue history, audit artifacts or evidence**.

This is not a token count and not all tasks require all of it. It is evidence that applicability-driven loading can produce large savings without deleting knowledge.

### G2. Transferable Wissensarbeit efficiency principles

The strongest reusable principles are:

1. **Bounded context compilation** — compile objective, current state, evidence, methods, authority and constraints for the actual work item rather than replaying the project.
2. **Canonical references over history replay** — persisted decisions/evidence are pointed to; deep rationale is loaded on challenge/need.
3. **Derive before asking** — never use Human input to recover facts already derivable from authority/current state.
4. **Context economy is not maximal compression** — uncertainty, authority, evidence and system-coherence context must survive.
5. **Externalize material state before context compaction** — compaction/session/environment change is safe only after recognized material state has durable provenance; persistence does not equal promotion.
6. **Delta/evidence return** — a child/scarce execution context returns the bounded result, evidence, residuals and impact, not a replay of every reasoning token.
7. **Smallest quality-preserving execution slice** — reduce scarce execution cost only where system-level coherence and reviewability remain intact.
8. **No convenience escalation** — use a stronger/scarcer environment only for non-substitutable capability/quality gain.
9. **Fail closed on ambiguous next action** — efficiency must not become unauthorized autonomy.

### G3. paleo-type target context

The existing target-state C6 already points toward the right active context:

```text
purpose / authority
→ current programme or explicit absence
→ current bounded work or explicit absence
→ applicable accepted decisions / requirements
→ evidence / rationale pointers
→ completion / return condition
```

This audit refines it with two additional meanings:

```text
→ permitted / entailed continuation
→ decision-needed state and reason
```

Deep audit history, rejected alternatives, old closed work and full provenance should be **reachable**, not loaded by default.

### G4. Result envelope

A bounded child/work result should normally return only:

```text
RESULT
EVIDENCE / PROVENANCE
CHANGED ASSUMPTIONS / STATE
RESIDUALS / CEILING
DECISION NEEDED? + exact reason
PARENT CONSEQUENCE: changed | unchanged | needs-decision
RETURN / CLOSE CONDITION
```

This does not hide history; history stays in Git/Issue/PR/artifact evidence. It prevents history from becoming the runtime packet.

### G5. Efficiency safety rule

> **Reduce reconstruction, not evidence.**

No context/token optimization is valid if it removes material uncertainty, provenance, Human/specialist authority boundaries, direct-evidence distinctions or the ability to expand rationale on demand.

---

## H. Failure map

| Proxy point | Primary cause | Desired response |
|---|---|---|
| Human says `weiter/ausführen` after no new decision | missing continuation semantics / artificial gate | continue automatically inside bounded authority |
| Human selects Chat/Work/Codex/tool merely because system did not route | missing operational responsibility/routing | derive route/capability; ask only if material permission/risk remains |
| Human re-supplies known repo state | missing/expensive context compilation | derive bounded context from canonical owners |
| Human moves result between worker and parent | missing return/reconciliation mechanism | result envelope + parent reconciliation |
| Human confirms deterministic technical next step | no explicit ready-next semantics | execute when exactly one authorized next action is entailed; otherwise fail closed |
| Human reconstructs what changed after local PASS | current/history/parent gap | IC-01/02 reconciliation + derived current view |
| Human resolves rights, purpose, material priority or D-016 admission | genuine authority | Human remains required |
| Human must provide inaccessible credential/permission or external evidence | platform/evidence boundary | expose smallest unavoidable Human action; do not dump workflow |
| unresolved palaeographic/domain judgement | specialist judgement | qualified specialist, not owner-as-substitute-specialist |
| post-result publication/use decision | consequential owner authority | Human remains required |

---

## I. Architecture options

### Option A — Contracts only over current tooling

Clarify authorized-work DoR/DoD, return and Human-decision rules in METHOD/owner contracts; let capable AI execute them without new runtime state.

**Strengths:** low new machinery; preserves current repo shape.  
**Weakness:** may still leave fresh contexts reconstructing current bounded work/continuation from Issue prose and chronology.  
**Disposition:** necessary semantic base; likely insufficient alone for the demonstrated reconstruction/token burden.

### Option B — Derived bounded work/context view

Extend the Class-B derived surface so it compiles current work + applicable authority/requirements/evidence + completion/return + decision-needed state from existing owners.

**Strengths:** directly reduces chat/history reconstruction and token load; no second truth store if rebuildable.  
**Weakness:** can only be correct after lifecycle/currentness semantics are stable; GitHub work-owner availability/boundary must be explicit.  
**Disposition:** strongly supported after IC-01/02 semantics.

### Option C — Event/state-driven continuation rule

When a result or transition occurs, derive one of:

```text
continue already-authorized work
return/reconcile to parent
close
wait for evidence/specialist
ask exact Human decision
```

Do not create successor priority automatically.

**Strengths:** directly removes repeated Human confirmations.  
**Weakness:** false autonomy risk if `entailed by scope` / material-choice detection is underspecified.  
**Disposition:** strongly supported as semantics/qualification property; representation remains open.

### Option D — Small persisted execution cursor / harness

Use a minimal current cursor analogous in spirit, not shape, to Wissensarbeit: current work reference, permitted actions, dependencies, implementation/admission state, completion evidence and return target.

**Strengths:** very strong restart/preflight semantics; easy deterministic `next/preflight/complete` testing.  
**Weakness:** paleo-type already warns against a second planning clock; a persisted cursor can drift from GitHub work owner / canonical state.  
**Disposition:** **conditional**. First test whether IC-03 can derive sufficient state from existing work owner + repository owners. Add a persisted cursor only if derivation is demonstrably insufficient or too fragile.

### Option E — General work runner

An execution harness accepts one already-authorized work package and carries it through inspection/reasoning/research/design/implementation/check/persistence/reconciliation until its bounded completion or a real gate.

**Strengths:** removes manual relay across multiple routine steps.  
**Weakness:** depends on reliable Work Contract, context compilation and gate detection; otherwise becomes an unsafe autonomous planner.  
**Disposition:** future implementation form to evaluate after semantics; not a new planning authority.

### Option F — Universal workflow engine / autonomous planner

Persistent engine owns broad transition logic and/or selects future work.

**Strengths:** could make complex orchestration explicit.  
**Weakness:** high second-clock/authority/semantic-formalization risk; no current evidence that A-E cannot close the failure.  
**Disposition:** **not warranted now**, but not rejected merely because it is large; reconsider only if the simpler non-duplicative architecture fails qualification.

---

## J. Recommended sufficient architecture

The best-supported design direction is the existing Class-B architecture with the following refinements.

### J1. Phase-neutral Authorized Work Contract — refine IC-01

A bounded work package should expose meanings equivalent to:

```text
PARENT / AUTHORIZED OBJECTIVE
WORK PURPOSE / CONTRIBUTION
WORK TYPE / PHASE (descriptive, not mandatory pipeline)
CANONICAL INPUT OWNERS
APPLICABLE REQUIREMENTS / CONSTRAINTS
EVIDENCE / PREREQUISITES
PERMITTED WORK BOUNDARY
RESULT / ACCEPTANCE CONDITION
OUT OF SCOPE / NON-GOALS
DECISION-NEEDED CONDITIONS
RETURN / RECONCILIATION TARGET
CLOSURE CONDITION
```

The phase may be analysis, requirements, research, concept, design, implementation, verification, validation, reconciliation, learning or another evidenced work type. The representation must not require every work item to pass through every phase.

### J2. `decision-needed` semantics — refine IC-01/03

The system should continue routine work without asking the Human while all of the following remain true:

```text
objective/scope remains authorized
AND current action stays inside the bounded work contract
AND the action is entailed by accepted requirements/design/current state
AND no new material semantic/architecture/risk choice is introduced
AND no Human/specialist authority boundary is crossed
AND required evidence/prerequisites remain satisfied
AND completion/return semantics are known
```

If those conditions fail, continuation becomes one of:

- `needs-human-decision`;
- `needs-specialist-judgement`;
- `needs-evidence/resource`;
- `needs-replanning/reframing` within an existing authorized parent;
- terminal legitimate ceiling.

A literal persisted boolean is **not** required. The required property is that a fresh context can reconstruct whether Human intervention is genuinely necessary and why.

### J3. Bounded Context Compiler / derived operational surface — refine IC-03

Compile only:

```text
purpose / authority
current programme / work owner
work type / contribution
applicable requirements / accepted decisions
current evidence/prerequisite state
permitted actions / continuation
completion / return
exact decision-needed surface if any
evidence/history expansion pointers
```

Do not load whole audit/Issue history by default. Do not invent authority when source owners are ambiguous.

### J4. Compact result/return envelope — IC-01/02/03 interface

Return the bounded result and its parent consequence rather than full process replay. Current/history/supersession semantics under IC-02 ensure the original evidence/history remains reachable after the active context drops it.

### J5. Minimal cursor/harness only on demonstrated threshold

No new `execution_state.json` analogue is pre-authorized for paleo-type. The design phase should test two treatments:

- **B0:** derive work state from current GitHub work owner + repository canonical owners;
- **B1:** add the minimum persisted cursor only if B0 cannot reliably satisfy restart/preflight/continuation requirements.

Choose B1 only if it removes real reconstruction burden without becoming a competing planning owner.

### J6. Qualification — extend IC-06

A fresh-agent fixture must prove both **autonomy inside authority** and **correct stopping at authority**:

1. give the fresh context an already-authorized analysis/design/implementation work package with no material open choice;
2. verify it continues through multiple routine actions without repeated Human `weiter`;
3. verify it derives applicable context without history dump;
4. inject a new material architecture/priority/rights question and verify it stops with one exact decision request;
5. inject a specialist judgement dependency and verify it routes to specialist rather than owner-as-proxy;
6. complete a child result and verify parent reconciliation/closure without Human relay;
7. verify no automatic successor priority after closure;
8. verify deeper evidence/history remains expandable on challenge;
9. compare context/reconstruction burden with a baseline fresh-agent replay.

---

## K. Hypothesis disposition

| Hypothesis | Disposition | Finding |
|---|---|---|
| H1 — Human proxy arises primarily from missing operational work state | **PARTLY SUPPORTED / STRONG** | major cause, but genuine authority, specialist judgement, evidence access and platform permission can still require Human action |
| H2 — IC-01/02/03 suffice with bounded additions | **SUPPORTED WITH REFINEMENT** | add phase-neutral work continuation, decision-needed, context economy/result envelope; no new architecture class yet |
| H3 — full Problem→Learning lifecycle needed; implementation focus is too narrow | **PARTLY SUPPORTED** | coverage must span all substantive work, but not as mandatory waterfall; D-016 already allows pre-implementation analysis/requirements/concept without admission |
| H4 — Wissensarbeit provides enough reusable context/efficiency semantics to avoid a new paleo mechanism class | **SUPPORTED WITH DOMAIN REFINEMENT** | reuse properties, not runtime/product identity |
| H5 — token waste and Human relay are two faces of the same reconstruction gap | **PARTLY SUPPORTED** | strong overlap; token cost can also be legitimate evidence cost, and Human action can be genuinely authoritative/platform-bound |
| H6 — model can perform most phases out of box; system gap is state/authority/context/closure | **SUPPORTED** | subject to evidence/tool/specialist availability |
| H7 — workflow/execution runner is unnecessary | **UNRESOLVED / UNIVERSAL ENGINE NOT WARRANTED** | a universal engine lacks evidence; a small harness/cursor may later be justified if derived state cannot meet qualification |

---

## L. Revised candidate map

No new standalone `Human Proxy` implementation candidate is required at current evidence level.

- **IC-01 — REFINE:** generic work/programme lifecycle must explicitly be phase-neutral and support autonomous continuation within already-authorized work, with exact Human/specialist/evidence stop conditions.
- **IC-02 — KEEP:** current/history/supersession and decision promotion remain necessary so dropping history from active context does not lose provenance.
- **IC-03 — REFINE/STRENGTHEN:** bounded operational view should compile applicability-limited context plus continuation/decision-needed/return semantics.
- **IC-04 — KEEP CONDITIONAL:** stable checks may later validate allowed continuation/currentness/closure only after semantics settle.
- **IC-05 — KEEP CONDITIONAL:** migrate only surfaces needed by accepted design.
- **IC-06 — REFINE/STRENGTHEN:** qualification must include Human-relay elimination, bounded context/reconstruction comparison and correct stop-at-authority behavior.
- **IC-07 — KEEP SEPARATE:** review-premise/direct-evidence provenance remains a distinct scholarly assurance problem.
- **new persisted execution cursor:** **CONDITIONAL DESIGN OPTION, not new IC yet**.
- **universal workflow engine/autonomous planner:** **NOT WARRANTED**.
- **Wissensarbeit #48/#52/#53/#55:** comparator/candidate evidence only; no 1:1 promotion into paleo-type.

---

## M. System Definition of Done refinement

A lifecycle revision addressing this audit is sufficient only if it demonstrates all applicable properties below:

1. an already-authorized bounded work package can progress through multiple routine actions without repeated Human continuation confirmations;
2. Human intervention occurs only for a reconstructable non-derivable Human-owned decision/acceptance/authority fact;
3. qualified specialist judgement is not shifted to the non-specialist owner;
4. resource/platform inability is reported action-locally and only escalates to Human when an unavoidable Human action actually exists;
5. planning/analysis/research/concept/design work can be owned, resumed, returned and closed just as implementation work can;
6. no fixed phase pipeline is required when evidence/need warrants different transitions;
7. a fresh context can reconstruct current authorized work without originating chat or long Issue chronology;
8. default context is bounded by applicability/current work rather than total repository history;
9. material provenance/history remains recoverable on demand;
10. a child/local result reconciles to its parent without Human acting as message bus;
11. local `PASS`/closure cannot become parent/programme acceptance implicitly;
12. no automatic successor work/priority is invented after completion;
13. when exactly one authorized continuation is entailed, the system may continue it; when continuation is ambiguous/material, it fails closed;
14. a Human request, when unavoidable, is reduced to the smallest unavoidable action/decision with what is and is not being decided;
15. context/token optimization never removes material evidence, uncertainty or authority semantics;
16. the revision itself can close and leave only durable owners plus inactive history.

---

## N. Target-state / D-016 consequence

Disposition: **BOUNDED REFINEMENT; CORE CLASS-B ARCHITECTURE UNCHANGED.**

The existing target-state and D-016 decision surface already contain most structural prerequisites: closable work, parent reconciliation, bounded active context, derived views, Human/AI/specialist separation and fresh-maintainer qualification. They should be refined before admission to make four properties explicit:

1. **Work begins before implementation.** IC-01 applies to analysis, requirements, research, concept and design as well as implementation/assurance.
2. **Autonomy inside authority.** A bounded admitted/authorized work package should continue without repeated Human confirmation until a real authority/evidence/specialist/material-choice boundary is reached.
3. **Context efficiency as a target property.** Compile applicable current context and expand provenance/history on demand; avoid reconstructing accumulated history in every worker.
4. **Human-relay qualification.** IC-06 must prove that the Human is not required as dispatcher/message bus while also proving fail-closed behavior at genuine gates.

This refinement does **not** itself change `methodology/maintenance.md`, `methodology/workflow.md`, Project state, code, schemas or the existing D-016 admission status.

D-016 remains:

`DECISION READY / NOT ADMITTED`.

---

## O. Human decision surface

No additional Human architecture choice is required merely to accept the analytical finding. The evidence supports refining the existing lifecycle decision surface before implementation admission.

The next genuinely consequential Human decision remains the lifecycle-revision D-016 disposition after that decision surface incorporates the refinements above:

`ADMIT | REFINE | DEFER | REJECT`

If `ADMIT` is later selected, the admitted scope should permit design to determine whether a derived existing-owner treatment is sufficient or whether a minimal persisted cursor/harness is required. It should **not** pre-authorize a universal workflow engine, autonomous scholarly priority selection or a second planning truth store.

---

## P. Deliberate non-changes

This audit does not:

- create manuscript Project scope or `NEXT ACTION`;
- reopen #225/#230;
- infer #225 whole-system acceptance from Issue closure;
- change D-016 status;
- change GO/AGENTS/METHOD;
- add a runtime, planner, scheduler, workflow engine or package;
- import Wissensarbeit Building Blocks/Skills as paleo-type owners;
- promote #48/#52/#53/#55;
- turn token minimization into a quality objective;
- treat model capability as system authority;
- select a successor programme automatically.

## Closing synthesis

The target is not `more autonomous AI` in the abstract. The target is a research system that can distinguish:

```text
THIS WORK IS ALREADY AUTHORIZED AND DETERMINATE ENOUGH TO CONTINUE
```

from:

```text
A MATERIAL HUMAN / SPECIALIST / EVIDENCE DECISION IS NOW GENUINELY REQUIRED
```

and can carry the first case through execution, persistence, review, reconciliation and closure without using the Human as transport infrastructure.

The same architecture that reduces that Human burden also reduces token/context waste: current applicable work is compiled, history is referenced rather than replayed, material state is externalized before continuity boundaries, and deep provenance is expanded only when needed. The quality boundary is unchanged: efficiency is valid only while evidence, uncertainty, authority, reviewability and restartability remain intact.