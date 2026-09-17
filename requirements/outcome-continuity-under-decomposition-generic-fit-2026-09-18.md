# Outcome-Continuity under Decomposition — phase-independent Generic-Fit review

Status: **COMPLETE — ALREADY COVERED.** Requirements/review result under #226 and parent #225. This artifact does not create METHOD, a new formal Requirement row, a Project scholarly scope, implementation admission, workflow architecture or a new canonical state owner.

## 1. Review question

#226 tested whether the following phase-independent property requires a new generic invariant/mechanism:

~~~text
DECOMPOSE
authorized higher-level outcome → bounded local work

CONTAIN
local result has only local authority

RECONCILE
local result → explicit consequence for the higher-level outcome

RESUME
if the higher-level outcome remains valid → return to its executable cursor

TERMINATE
only outcome-level acceptance or a real evidence / authority / feasibility / specialist ceiling may end or pause it
~~~

The question was tested after #227 completed #225 Phase 0/1 and explicitly established #226's prerequisite as met.

## 2. Primary disposition

**ALREADY COVERED**

No new generic semantic rule, state object, workflow layer, invariant owner or executable component is warranted.

The property is already covered by the **composition of current canonical owners**, with different owners correctly governing different scales:

- methodology/maintenance.md owns material **programme/phase/result-transition reconciliation**;
- methodology/workflow.md owns bounded task execution, cursor, completion, handoff, return/review, support containment, no-progress redirect, Dev return and state-transition freshness;
- methodology/historical-source-workflow.md requires material scholarly work to serve an authorized research goal/question or required source-representation task;
- methodology/quality-and-learning.md owns Goal Alignment and systemic/Generic-Fit review;
- methodology/research-gates.md and Project STATUS.md own scholarly maturity/terminal state at their respective generic/Project levels;
- AGENTS.md and the Governing Objective preserve authority, local-vs-global scope, Human/specialist/AI boundaries and restartability.

The apparent generic “guard” is therefore real as a **cross-cutting system property**, but it does not need to become a seventh owner or a new universal object.

## 3. Semantic decomposition against existing owners

| Property | Existing owner(s) | Coverage result |
|---|---|---|
| **DECOMPOSE** — bounded work must remain traceable to legitimate higher authority | workflow.md Current-work-target authority + Cross-role work-context contract; historical-source-workflow.md Research-question control; D-016 for material system work | **Covered**. Bounded work has owner, stage, action, cursor, completion and return semantics and may not manufacture target authority. |
| **CONTAIN** — local result has local authority only | maintenance.md programme reconciliation; workflow.md research-workblock terminal semantics; Domain→Dev boundary; technical PASS ≠ scholarly acceptance; support delta ≠ scholarly delta | **Covered**. Local PASS/support/technical completion cannot silently become wider scholarly/programme completion. |
| **RECONCILE** — state the consequence for the owning higher context | maintenance.md explicit programme/phase/result disposition; workflow.md RESULT HANDOFF = persistence + unresolved/non-result + return question; Dev returns to correct domain owner; canonical freshness at state transition | **Covered by scale-specific owners**. Programme consequence is explicit where a programme exists; bounded task/handoff consequence uses the work-context return/review contract. |
| **RESUME** — return when parent remains valid | workflow.md valid-cursor redirect, support-to-support stop, Domain↔Dev return, return/review condition; maintenance.md bounded consistency ends with return to research | **Covered**. Repair/support must not become a self-sustaining objective and execution resumes only from a valid authorized cursor. |
| **TERMINATE** — only legitimate outcome/ceiling may end the higher work | workflow.md Research-workblock terminal semantics; dependency/resource authority; research-gates.md; maintenance.md local STOP containment | **Covered**. Valid terminal meanings are scholarly delta, scholarly evidence ceiling or authorized blocker/escalation at task scale; support-only results are explicitly insufficient. Programme closure remains programme-owned. |

### Important scale distinction

The repository correctly does **not** require one universal “parent outcome” entity for every action.

Three cases remain distinct:

1. **material broader programme/planning context exists** → maintenance.md requires explicit programme reconciliation;
2. **bounded authorized task/work block exists** → workflow.md cursor/completion/handoff/return semantics apply;
3. **no authorized Project/outcome/task exists** → no parent/cursor may be manufactured.

This distinction is evidence for the current distributed ownership model, not a deficiency requiring a central state machine.

## 4. Cross-context Generic-Fit

### F1 — programme/phase/result transition

The completed 2026-09-16 Route-A chain established and implemented the exact material-programme case:

- Requirements resolution: existing-owner refinement warranted;
- Concept: semantic rule in maintenance.md + referential execution hook in workflow.md;
- admitted implementation: two additive METHOD changes only;
- Result Review: PASS;
- positive fixtures included local STOP inside broader programme, phase transition changing selectable work and explicit return without auto-advancement;
- negative fixtures included ordinary task work, unchanged consequence and no established programme owner.

**Result:** phase/programme continuity is already generic METHOD and must not be re-created.

### F2 — ordinary scholarly decomposition: Reg. Ii 4 #96 → #97 → #98 → #99

The Reg. Ii 4 bounded Knau work packages provide a non-Reg.-Ii.-5 scholarly fixture:

- #96 completed an independent first-reading **representation** but explicitly did not claim G2/G3; it handed forward to #97;
- #97 established G2 representation completeness but explicitly did not claim G3/external-release and handed forward to #98;
- #98 completed systematic internal analysis while retaining unresolved evidence and its bounded G3 meaning;
- #99 owned controlled external collation only after its dependencies/release conditions.

Current Project STATUS preserves that the work-package sequence completed without implying every reading was resolved, without implying G5/G6, and without manufacturing a new current scholarly target.

**Result:** bounded task completion, scope containment, dependency-controlled progression and non-upgrading of local completion are already expressible without a universal continuity object.

### F3 — bounded support/repair interruption and return

Current workflow.md explicitly provides:

- sticky prerequisites and invalidation rather than repeated re-entry;
- no-progress detection and redirect to the valid cursor;
- first-scholarly-action protection;
- support-to-support escalation stop using Goal Alignment;
- action-local resource failure instead of task-wide blocker inflation;
- support delta separated from scholarly delta;
- support-only results explicitly excluded from substantive research terminal outcomes.

**Result:** support/repair continuity is already task-locally owned. A second generic repair state machine would duplicate these semantics.

### F4 — Dev/RSE handoff and return: #69 / PR #88 class

#69 and the admitted Source/Project handling implementation show the non-scholarly-execution analogue:

- a demonstrated domain/system problem was narrowed into existing-owner semantics;
- the smallest technical adapter reused the Source Contract rather than creating a parallel intake platform;
- technical/structural results remained narrower than scholarly/project authority;
- exact File routing correctness did not establish Project research function or current research priority;
- the bounded implementation returned to its owning review/authority surface.

workflow.md now encodes the same generic Domain→Dev→Domain contract, including requirement/authority verification and explicit return to the correct domain owner.

**Result:** continuity through technical decomposition is already covered by the handoff/return contract plus D-016 and must remain narrower than scholarly authority.

### F5 — negative case: Reg. Ii 3

Reg. Ii 3 has a valid Project, exact File/crosswalk evidence and rich restart state but no owner-selected current scholarly scope or NEXT ACTION.

Its regression explicitly protects exposing the canonical crosswalk **without creating research priority**.

**Result:** phase-independent continuity must not be interpreted as “always maintain an active parent goal”. Absence of an authorized current outcome is valid.

### F6 — negative case: Corpus-only routing

tests/test_corpus_only_routing.py establishes that valid Source/File/part-of structure may exist with zero Projects and that structural containment does not materialize a Project.

**Result:** a universal parent/outcome hierarchy would be incorrect. No continuity mechanism may invent Project/outcome state merely because lower-level evidence exists.

## 5. Falsification / anti-bloat result

A new generic continuity mechanism is **falsified by current evidence** if it would introduce any of the following:

- a universal parent/outcome entity;
- a manually maintained outcome/cursor truth store;
- mandatory task hierarchy;
- workflow engine/state machine;
- universal completion-status vocabulary;
- mandatory reconciliation artifact for routine work;
- a new formal Requirement row merely restating the current METHOD;
- deterministic rules deciding scholarly validity, Project priority or specialist judgement.

No concrete cross-context failure was found that is **permitted by the current union of owners** and uniquely requires a new continuity semantic.

The remaining end-to-end weakness identified by #225 is elsewhere: reliable operational composition of **R-1…R-4**. In particular, missing outcome binding/unmet-requirement composition can make the correct continuity rules hard to exercise because the system may not yet have a reliably derivable higher-level outcome/state to apply them to. That is an integration problem, not evidence that continuity semantics themselves are missing.

## 6. Executability boundary

### Deterministic checks are appropriate for

Where the relevant states already exist in canonical/structured form, later admitted system work may mechanically check or derive properties such as:

- local completion is not being serialized/rendered as parent completion;
- a referenced task/return owner resolves;
- an existing explicit parent/programme outcome remains open/valid according to its owner;
- a support-only/technical result is not promoted into scholarly acceptance;
- a result handoff points to current canonical state rather than stale state;
- no Project/outcome is generated when authority is absent.

These are **validation properties**, not justification for a separate continuity component.

### AI/contextual reasoning remains appropriate for

- determining whether a non-formal local result materially affects a broader scholarly outcome;
- explaining the scholarly consequence of evidence where applicability is interpretive;
- composing R-1…R-4 when requirement applicability cannot be reduced losslessly.

### Specialist judgement remains required for

- consequential domain conclusions and specialist-validation ceilings defined by existing requirements/METHOD.

### Human Owner remains required for

- non-derivable purpose, priority and materially changed scope;
- material system implementation admission;
- unresolved rights/authority and consequential use decisions.

## 7. Consequence for #225 R-1…R-4

No separate “R-5 continuity component” should be added.

Instead:

- **R-1** must expose a legitimate authorized outcome or explicit absence;
- **R-2** must expose applicable unmet requirements;
- **R-3** must form/route bounded work using existing cursor/handoff/return semantics;
- **R-4** must compose outcome-level continuation/completion/ceiling without allowing local PASS to masquerade as outcome completion;
- the existing continuity semantics serve as a **cross-cutting acceptance constraint over R-1…R-4 and their implementation**, not as another stage.

Phase 2 may therefore proceed without designing a separate continuity service, state store or workflow layer.

## 8. Required Phase-2 treatment

Phase-2 concept comparison under #225 should treat Outcome-Continuity under Decomposition as an acceptance property:

> Any candidate integration concept must preserve existing scale-specific owner semantics such that decomposition into scholarly tasks, support/repair, review or technical implementation cannot replace, terminate or silently redefine the authorized higher-level outcome; when that outcome remains valid, the candidate must permit reconstruction/return to its correct executable cursor; when no outcome exists, it must not manufacture one.

A later vertical acceptance fixture should test this property end-to-end, but #226 establishes **no independent implementation work package** for it.

## 9. Final disposition

~~~text
PRIMARY DISPOSITION: ALREADY COVERED

new generic semantic owner: NO
new formal Requirement row: NO
new continuity component/service/state machine: NO
METHOD refinement from #226: NO
software implementation admission from #226: NO

retain as:
cross-cutting acceptance / falsification property for #225 Phase 2+,
implemented through existing scale-specific owners.

#225 consequence:
LOCAL PHASE RESULT; consume in Phase 2.
~~~

#226 may close after reconciliation to #225.
