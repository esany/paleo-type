# Outcome-preserving execution control — Human-Owner D-016 implementation admission — 2026-10-05

Status: **D-016 ADMIT — Human-Owner decision and bounded implementation admission.**

This record persists the Human Owner's explicit `ADMIT` for the repository-first decision brief `requirements/outcome-preserving-execution-control-d016-decision-brief-2026-10-05.md` and GitHub decision surface #285. It is the durable admission evidence for this bounded shared execution-control change. It does not by itself establish implementation, verification, accepted-current architecture, scholarly truth or Project/manuscript priority.

## 1. Authority and decision basis

- General D-016 admission semantics remain owned by `methodology/maintenance.md` and accepted decision D-016 in `DECISIONS.md`.
- Governing constraints remain `GOVERNING_OBJECTIVE.md` and `AGENTS.md`.
- Whole-system analysis/result-review owner: GitHub #280.
- Requirement/falsification owners: #281 and #282.
- Concrete SStA acquisition fixture: #271 / Draft PR #273.
- Existing engineering assurance comparator/owner: #244 / #259.
- Decision brief: `requirements/outcome-preserving-execution-control-d016-decision-brief-2026-10-05.md`.
- Fresh decision baseline verified at `main@37e59ee0871dacea87bbe9e3161a278e9a6bc1a6` before this admission write.
- The Human Owner explicitly selected **`ADMIT`** after #285 was presented as `READY FOR HUMAN D-016 DECISION / NOT ADMITTED / NO IMPLEMENTATION STARTED`.

GitHub Issues remain work/audit metadata; the decision brief defines the admitted target and this file records the Human-Owner admission event.

## 2. Admitted material target

The Human Owner admits the bounded **outcome-preserving execution-control** refinement defined by the decision brief. The admitted properties include:

- Human/research outcome remains the higher-order control cursor;
- explicit distinction between read/status, retry inside one authorized active operation, resume of persisted operation state and a new top-level mutation/run after terminal state;
- status/read is non-mutating by default;
- internal capability/runtime routing remains internal where derivable;
- capability/resource failure remains action-local absent dependency authority;
- task-relative runtime fitness precedes long-running consequential external side effects;
- material start/control/containment limits are visible before they matter;
- technical operation/result/preservation/acceptance states remain distinct;
- local repair/resume returns to the valid higher-order outcome;
- fresh contexts can reconstruct action class, durable progress, control limits and return condition without old chat.

The admitted response is a **shared semantic refinement plus owner-local mechanics**, not a global orchestrator.

## 3. Authorized implementation locus

Implementation may now proceed without repeated owner micromanagement inside this precise envelope:

1. refine `AGENTS.md` only as needed for the universal consequence/write/control guardrail;
2. refine `methodology/workflow.md` only as needed for read/retry/resume/new-run semantics and the execution-fit/start-control boundary;
3. refine existing applicable Requirements where they can carry the admitted semantics; add a new Requirement only if existing owners would otherwise be distorted;
4. implement owner-local enforcement/regressions at interfaces that can actually enforce the property;
5. use #271/PR #273 for SStA-specific durable destination/interruption-resume/integrity/truthful-completion mechanics;
6. use #259/WP4 only for repository-testable safeguards already compatible with its admitted SD-KA/P-011 scope; WP4 must not become a runtime/orchestration layer;
7. retain #281/#282 as facet-level acceptance/falsification owners and #280 as overordinate Result Review/closure owner.

## 4. Required verification / loss checks

Implementation must preserve the decision brief's falsification set, including:

- terminal failed/cancelled operation + `Fertig?`/`Status?` → read/report only, zero new top-level mutation;
- `Stop` during active/queued long-running work → no new work, authorized cancel where supported, otherwise precise limitation and containment;
- unavailable capability/path remains action-local unless authoritative dependency semantics say otherwise;
- materially different non-SStA repository/GitHub status-read fixture remains non-mutating;
- deterministic long-running side-effect fixture proves interruption/resume, corruption handling, durable-progress semantics and truthful incomplete/secured state;
- real `savesax` full-run acceptance occurs only after the intended productive destination/runtime has been shown fit for the required durability/control properties.

A green CI run, one successful archive run or one local patch does not establish whole-system closure.

## 5. Explicit non-authorizations

This admission does **not** authorize:

- workflow engine, autonomous planner, global agent orchestrator, permission broker or generic persistent job service;
- blanket confirmation before every routine authorized action;
- a ban on bounded automatic retry inside an already authorized operation;
- a requirement that Chat itself possess every capability;
- a blanket GitHub Actions ban;
- a cloud-storage product decision;
- Source/File/Project/CORPUS semantic changes;
- manuscript Project purpose, priority, gate or scholarly `NEXT ACTION`;
- scholarly acceptance or specialist validation;
- reopening verified WP3 merely to absorb the new residual;
- CI claims about model/platform/external-runtime behavior it does not actually execute.

A genuinely new material semantic/architecture/migration/authority choice outside the admitted brief must return through D-016.

## 6. Transition / result-review boundary

This admission authorizes development. It does not establish `implemented`, `verified`, `accepted` or `closed`.

The shared change is complete only after the decision brief's DoD is satisfied and #280 performs the overordinate Result Review across materially different fixtures. #276/#277 must be re-tested/dispositioned against the resulting behavior; they are not solved merely because code or prose changed.

No Source/File/Project truth and no scholarly research priority changes through this admission.
