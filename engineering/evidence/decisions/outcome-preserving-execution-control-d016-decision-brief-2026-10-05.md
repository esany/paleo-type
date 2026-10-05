# Outcome-preserving execution control — D-016 decision brief — 2026-10-05

**Status:** HUMAN-OWNER `ADMIT` SELECTED / implementation scope defined below  
**Decision surface:** GitHub #285  
**Evidence / family owners:** #280, #281, #282; incidents #276/#277; acquisition fixture #271/PR #273  
**Existing engineering programme comparator:** #244 / #259

This file is the repository-first decision brief for the shared execution-control residual exposed by #276/#277 and analysed under #280–#282. It is not a scholarly Source/File/Project owner and does not create a research priority or manuscript `NEXT ACTION`.

## 1. Demonstrated problem

Across the incidents, Human intent was decomposed into tool/capability/runtime/storage choices and that technical decomposition gained control authority. Consequences included:

- tool or sandbox state being promoted into archive/task state;
- internal capability/runtime choices becoming Human-facing orchestration work;
- a read-only status question causing a new top-level retry after terminal state;
- a long-running external action being startable although the same work context could not reliably cancel it on a later Human `Stop`;
- an available hosted runner being treated as a suitable productive acquisition runtime without first proving durability/restart/control fitness;
- technical, offline, live, partial and preserved/secured states being at risk of conflation.

The common mechanism is:

```text
Human intent / desired outcome
→ internal tool / capability / runtime / storage decomposition
→ technical decomposition gains control authority
→ local capability/runtime state displaces the authorized outcome cursor
→ retry/workaround/PASS/FAIL drives new action
→ resulting state is harder for the Human to audit, stop or restart
```

## 2. Existing coverage and residual

Existing Governing Objective, `AGENTS.md`, `methodology/workflow.md` and the already-admitted SD-KA-01 programme already require Human authority, action-local resource state, bounded context, restartability and truthful assurance boundaries. WP3 has implemented Human/Developer/Agent context and semantic current-work rendering.

The residual is narrower but material: the shared execution boundary is not yet explicit/operational enough to protect consequence class, terminal retry/new-run authority, long-running external-side-effect runtime fitness and start/control semantics across tool interfaces.

This residual is outside the already-admitted SD-KA P-001..P-012 envelope. Compatible repo-testable assurance may later be exercised by #259/WP4, but WP4 must not become a runtime/orchestration system.

## 3. Admitted target image

The shared execution layer must preserve these properties across Human language → AI/context → tool/runtime execution:

1. **Outcome remains the control cursor.** Internal implementation decomposition may not replace the authorized Human/research outcome.
2. **Consequence class is explicit before mutation.** Distinguish informational/read, continuation/retry inside one already-authorized active operation, resume of persisted operation state, and a new top-level consequential mutation/run after terminal state.
3. **Status/read is non-mutating by default.** `Fertig?`, `Status?`, `läuft es noch?` and equivalent reads do not authorize rerun, push, download, workflow trigger, consequential message send or canonical write.
4. **Retry boundaries are preserved.** A bounded retry may happen inside an authorized operation contract; resume/new-run after terminal state is a distinct consequential transition unless already explicitly authorized by that contract.
5. **Capability routing remains internal where derivable.** The Human is not required to choose Chat/Work/CLI/provider/connector/runtime vocabulary unless a real non-derivable decision exists.
6. **Capability failure remains action-local.** One unavailable path cannot manufacture task-wide STOP, substitute work, priority or source unavailability without dependency authority.
7. **Runtime fitness precedes long-running external side effects.** Relevant task-relative properties include durable destination/progress where required, restart/resume/failure containment, observability/control and least-hop execution. Ability to execute code is not sufficient evidence of fitness.
8. **Start/control limits are known before they matter.** A long-running consequential action must not silently begin with a material stop/containment limitation that undermines Human control. Perfect universal cancellation is not required; truthful known limits are.
9. **Operation/result states remain semantically separate.** Preserve distinctions equivalent to `planned | running | partial/restartable | failed/cancelled | technically complete | preserved/secured | accepted`; one layer's PASS must not launder another.
10. **Repair returns to the outcome.** Local repair/resume cannot silently become the new objective; return to the same valid outcome unless authority/evidence genuinely invalidated it.
11. **Fresh-context restartability.** A fresh capable context can determine authorized action class, operation/result state, control limits, durable progress and return condition without old chat.

These are semantic properties, not a preselected global state-machine implementation.

## 4. Admitted change locus

### Shared canonical semantics

Refine only existing owners necessary to make the residual explicit and stable, expected to include:

- `AGENTS.md` — universal consequence/write/control guardrail;
- `methodology/workflow.md` — operational distinction among read, active retry, resume and new top-level mutation plus long-running execution-fit/start-control boundary;
- applicable existing requirements, using a new requirement only if existing owners cannot carry runtime-fitness semantics without distortion.

Do not duplicate the shared rule into every skill.

### Existing SD-KA-01

- WP3 remains verified and is not reopened.
- #259/WP4 may absorb only repository-owned deterministic assurance that genuinely belongs to its admitted P-011 scope and can actually be executed by repository tests/CI.
- WP4 must not claim to validate external/platform/model behavior it does not execute.

### Owner-local implementations

- #271/PR #273 remains the concrete SStA acquisition fixture for durable destination, interruption/resume, integrity and truthful completion.
- individual tool/connector/skill interfaces implement the shared consequence boundary where they can actually enforce it.
- #281/#282 remain acceptance/falsification owners for the Human-control and runtime-fitness facets.
- #280 remains the overordinate whole-system Result Review/closure surface.

## 5. Alternatives disposition

- **Local fixes only:** rejected. A `savesax` patch plus one `Fertig?` regression would repeat the local-PASS/parent-gap failure pattern.
- **Shared execution-control invariant + owner-local mechanics:** admitted. This addresses the demonstrated common mechanism while preserving subsidiarity and owner boundaries.
- **Central workflow engine / permission broker / persistent runtime service:** rejected at current evidence state. No demonstrated requirement justifies that platform layer.

## 6. Verification / falsification plan

1. Original Human-control fixture: prior operation terminal failed/cancelled; `Fertig?` / `Status?` performs read/report only and starts no mutation.
2. Stop/control fixture: active/queued long-running operation; `Stop` starts no new work, uses available authorized cancel where supported, otherwise reports the precise limitation and contains further mutation.
3. Capability-routing/failure fixture: one unavailable path remains action-local; another adequate authorized path may be routed internally; no task-wide STOP/substitute priority is invented.
4. Materially different non-SStA read/mutation fixture: repository/GitHub status inspection after terminal state remains read-only; no rerun/comment/update/push/merge/workflow follows from the read.
5. Deterministic long-running side-effect runtime fixture: interruption and corruption against a declared durable sink; valid progress survives as required, incomplete state is truthful/restartable, resume differs from new run, ephemeral-only output cannot be described as secured.
6. Real `savesax` acceptance only after deterministic protection exists and the intended productive destination/runtime has been shown fit for durability/control. Verify provider list, every image, checksums, complete manifest and truthful preservation status. One successful live run is not systemic closure by itself.

## 7. Definition of Done

The admitted shared change is done only when:

- canonical shared semantics are implemented in their correct owners without parallel truth stores;
- owner-local interfaces enforce the parts they can actually enforce;
- #281 DoD passes, including the non-SStA fixture;
- #282 deterministic interruption/resume/corruption/runtime-fit DoD passes;
- #271 productive acquisition mechanics and truthful completion semantics conform to the shared contract;
- #259/WP4 includes only applicable repo-testable safeguards and states its assurance boundary honestly;
- #276/#277 are explicitly re-tested/dispositioned against the new behavior rather than merely closed because code changed;
- a fresh-context review reconstructs outcome, action class, control limits, progress/result state and return condition without old chat;
- no local technical PASS, CI green state or successful archive run is presented as whole-system closure;
- #280 performs the overordinate Result Review and determines whether the failure mechanism is removed across materially different fixtures;
- residual platform/model limits remain explicit.

## 8. Explicit non-goals

No workflow engine, autonomous planner, global agent orchestrator or generic job service; no confirmation prompt before every routine authorized action; no ban on bounded retry inside an authorized operation; no requirement that Chat itself possess every capability; no blanket GitHub Actions ban; no cloud-storage product decision; no Source/File/Project/CORPUS semantic change; no scholarly/specialist acceptance claim; no new research priority or manuscript `NEXT ACTION`; no reopening WP3; no CI claim beyond properties it actually executes.

## 9. Admission boundary

The Human Owner has selected **`ADMIT`** for this bounded target. Implementation is authorized only inside the scope and non-goals above. A genuinely new material architecture, semantic owner, migration or authority choice outside this envelope must return through D-016 before implementation.
