# Result — documented learning vs claimed operational learning repair — 2026-09-23

Status: **COMPLETED REPAIR ANALYSIS / HISTORICAL CORRECTION / NO NEW METHOD OR IMPLEMENTATION ADMISSION**

Parent owner: #225  
Execution prompt: `requirements/learning-integration-claim-repair-execution-prompt-2026-09-23.md`  
Underlying work prompt: `requirements/learning-integration-claim-repair-work-prompt-2026-09-19.md`

## 1. Scope

This result closes the specific repair requested by the Human Owner:

> After a learning was persisted only as learning/audit evidence, the assistant described the future behavior as if the learning had already become operationally reliable.

This result does **not** execute the broader user-research/design/project-development methodology branch.

## 2. Fresh repository basis

The execution freshly re-read the current owners in `paleo-type`:

- `GOVERNING_OBJECTIVE.md`
- `AGENTS.md`
- `methodology/maintenance.md`
- `methodology/workflow.md`
- `methodology/quality-and-learning.md`
- `methodology/ai-governance.md`
- current #225
- the Human-feedback learning
- the design-methodology learning
- the repair work prompt

It also freshly re-read the relevant current owners in `esany/Wissensarbeit`, including:

- Governing Objective
- current execution state
- REQ-003 / REQ-004 / REQ-007 / REQ-011
- `system/authority.json`
- `system/reconciliation.json`
- BB-INTEGRATE / BB-LEARN / BB-ASSURE / BB-TRACE
- `tests/evals/failure_corpus.json`
- the 2026-09-18 Human-intent audit
- the 2026-09-19 design-methodology audit

Current `Wissensarbeit` implementation authority is active only for its separately admitted P2 Context-Fidelity correction scope. This repair does not alter or consume that implementation scope.

## 3. The two failures remain separate

### Failure A — existing semantics were not applied

Before the Human asked to persist the learning, existing repository semantics already required:

- Human input is not automatic scope/priority/solution authority;
- new aspects must be reconciled against the governing whole;
- material semantic ambiguity is a Human decision boundary;
- local correction returns to the prior valid cursor;
- Generic-Fit precedes generic framework growth.

The assistant nevertheless interpreted symptom feedback as product/system redirection.

This remains documented in:

`requirements/human-feedback-intent-classification-learning-2026-09-18.md`

### Failure B — persisted learning was overstated as future operational behavior

After the Human explicitly asked to secure the learning:

1. the learning was persisted;
2. it was explicitly classified as **SYSTEM LEARNING / FAILURE EVIDENCE ONLY**;
3. no METHOD rule was changed;
4. no executable regression was promoted;
5. no independent/fresh-context behavioral fixture was passed;
6. the assistant nevertheless told the Human, in substance, that this rule would apply “going forward”.

That statement was stronger than the repository-backed assurance state.

## 4. Assurance reconstruction

| Question | Result |
|---|---|
| Failure observed? | **YES.** Concrete chat/repository incident and Human correction. |
| Failure A persisted? | **YES.** Human-feedback learning + cross-repo audit. |
| Failure B persisted before this repair? | **PARTIALLY.** It existed in the repair prompt, but not yet as a completed result/historical correction. |
| Systemically reconciled? | **YES after this result and #225 reconciliation.** |
| Corrective Human-feedback behavior already normative? | **YES in substance.** Existing authority, workflow and quality rules already prohibit silent promotion and unsupported claims. |
| Did this repair change a normative owner? | **NO.** No missing generic METHOD rule was demonstrated. |
| Is the precise future-behavior claim executable/enforced? | **NO.** Natural-language claim calibration remains judgement-based. |
| Is there an executable regression proving this behavior? | **NO.** Only a regression/eval candidate exists for the semantic behavior. |
| Has an independent fresh-context fixture proven changed future behavior? | **NO.** |
| What may now be claimed? | The failure and correction are persisted and reconciled; existing rules already require evidence-calibrated claims; future perfect compliance is **not proven**. |

## 5. Existing owner analysis

### `methodology/quality-and-learning.md` — **UNCHANGED / SUFFICIENT NORMATIVE OWNER**

Existing semantics already state:

- no single model/chat/CI result certifies every dimension of a consequential change;
- reviews must state only what they can establish;
- technical PASS certifies only tested properties;
- a pass in one dimension must not be represented as a pass in another;
- concrete failures are recorded first and generic safeguards promoted only after Generic-Fit;
- deterministic generic safeguards should prefer executable regression over extra prose.

Failure B violates this existing assurance discipline.

**Disposition:** no new METHOD sentence needed merely to restate the same certification boundary.

### `methodology/maintenance.md` — **UNCHANGED / SUFFICIENT PROMOTION OWNER**

Existing semantics already require:

- new learning/failures to be compared against existing owners;
- one pilot/AI-session finding not to become a durable generic rule automatically;
- promotion only after Generic-Fit;
- explicit separation of analysis, requirements, admission, development, tests and result review for material changes.

**Disposition:** no change.

### `methodology/workflow.md` — **UNCHANGED**

Existing workflow already owns return-to-cursor and prevents local support results from becoming higher-level outcome completion.

Failure B is not a missing workflow transition.

**Disposition:** no change.

### `AGENTS.md` — **UNCHANGED**

Existing guardrails already require canonical/restartable state, authority separation and consequence-scaled claims.

A new always-on prose rule would duplicate existing owners.

**Disposition:** no change.

### #225 — **RECONCILE ONLY**

#225 owns the system-operationalization problem and is the correct parent for this failure evidence.

**Disposition:** add completed repair result; do not change the main #225 outcome cursor.

## 6. Generic-Fit against Wissensarbeit

The failure maps most directly to:

### FF-FALSE-ASSURANCE — primary

Existing definition:

> Evidence is described more strongly than it supports.

Existing open gap:

> Natural-language claims need evidence-calibrated regression grading.

Failure B is direct real-world evidence for this family.

### FF-AUTHORITY-PROMOTION — secondary

The assistant implicitly promoted a non-normative learning state into a stronger operational status without the required evidence/authority boundary.

### FF-EXECUTION-PROGRESS — secondary

The original Human-intent failure remains relevant to the existing open gap in free-text intent reconstruction, but that is Failure A rather than the main Failure B.

### BB-LEARN / BB-ASSURE / BB-TRACE

The existing blocks already allocate the required semantics:

- BB-LEARN: failure/feedback → validated learning / regression candidate;
- BB-ASSURE: keep verification/review/acceptance classes separate;
- BB-TRACE: explain what actually changed and with which authority/evidence;
- BB-INTEGRATE: do not call a material change integrated before reconciliation.

**Generic-Fit disposition: CONFIRM / REFINE EVIDENCE.**

No new Requirement, Building Block or lifecycle stage is justified.

## 7. Claim calibration for this case

This is a reasoning rule derived from existing assurance semantics, **not a new canonical status ontology**.

### Observed

Permitted claim:

> We have evidence of this failure.

Not permitted:

> The system has learned it.

### Persisted

Permitted claim:

> The failure/learning is documented and recoverable from the repository.

Not permitted:

> The behavior is now operationally fixed.

### Reconciled against owners

Permitted claim:

> The learning has been checked against current owners and its disposition is persisted.

Not permitted:

> The relevant behavior is enforced.

### Already normative

Permitted claim:

> Existing repository rules already require this behavior / prohibit the overclaim.

Not permitted:

> Therefore the AI will reliably comply in future.

### Executable / regression-tested

Permitted only when an actual mechanism/fixture exists:

> The specified stable invariant is covered by the named executable check.

Not permitted:

> The full semantic behavior is solved, if the test covers only a narrower invariant.

### Real/fresh-context demonstrated

Permitted only after an actual independent fixture:

> The behavior was demonstrated under this tested context/fixture.

Still not permitted:

> It can never recur.

## 8. Regression / executable safeguard decision

### Safe to mechanize now?

**No new deterministic regression is justified inside `paleo-type` at this point.**

Reason:

- the actual defect is a natural-language assurance claim about the meaning/effect of heterogeneous repository evidence;
- there is no canonical machine-readable “learning state” surface whose status the assistant incorrectly rendered;
- adding a test that merely asserts the presence of words such as `FAILURE EVIDENCE ONLY` would test prose shape, not the demonstrated semantic failure;
- pretending this solves free-text claim calibration would itself repeat the false-assurance error.

### Stable negative invariants for future eval work

A future model/eval fixture can test that a context does not silently collapse:

- learning evidence → normative rule;
- candidate regression → executable regression;
- repository persistence → behavioral enforcement;
- local PASS → higher-level acceptance;
- restartability → correctness;
- generic-fit evidence → implementation admission.

This belongs naturally to the already-existing `Wissensarbeit` FF-FALSE-ASSURANCE eval gap.

### What remains judgement-based

- interpreting the semantic force of a Human statement;
- calibrating natural-language assurance to heterogeneous evidence;
- deciding whether a learning is merely evidence, already-covered semantics, or warrants material promotion.

## 9. Historical correction

The prior assistant claim that the Human-feedback rule would apply “going forward” is recorded here as an **assurance overclaim**.

The repository state at that moment supported only:

- concrete failure evidence persisted;
- generic-fit analysis completed;
- existing rules identified as already semantically sufficient;
- candidate regression identified but not promoted.

It did **not** support:

- a newly integrated normative METHOD change;
- a new executable enforcement mechanism;
- an executable regression for the semantic behavior;
- an independent fresh-context behavioral proof;
- a guarantee of future model compliance.

## 10. Result disposition

**REPAIR ANALYSIS: PASS**

The specific missing historical/restartable distinction is now persisted and reconciled.

**NORMATIVE CHANGE: NOT REQUIRED**

The existing quality/authority/promotion owners already cover the safeguard.

**EXECUTABLE REGRESSION: NOT ADDED**

The demonstrated failure is not safely reducible to a deterministic repo test without semantic loss. The appropriate generic eval gap already exists in `Wissensarbeit`.

**REAL FUTURE-BEHAVIOR PROOF: NOT ESTABLISHED**

No claim of guaranteed future compliance is permitted.

**#225 MAIN CURSOR: UNCHANGED**

This local repair does not become a new programme or manuscript Project priority.

## 11. Final assurance statement

What changed in the repository:

- the historical overclaim is now explicitly persisted as a completed repair result;
- its relationship to existing normative owners is explicit;
- the exact claim-calibration boundary is reconstructable;
- the cross-project Generic-Fit is explicit;
- #225 can point to this result without relying on the originating chat.

What behavior is now required:

- the already-existing repository assurance rules continue to require that claims do not exceed their evidence/verification/authority state.

What is now tested:

- **no new executable behavioral regression was added by this repair**.

What remains only learning/expectation:

- that a future AI instance will correctly perform the semantic claim calibration every time.

Therefore the strongest justified Human-facing statement is:

> **The failure is now documented, analyzed against the current owners, and reconciled. Existing rules already prohibit the overclaim. We have not proven that future AI behavior is mechanically prevented from repeating it.**
