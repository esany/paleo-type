# Bugwave design closure — material finding coverage, promotion and forward trace — 2026-10-04

**Status:** NON-NORMATIVE DETAILED DESIGN / **#245 DESIGN COMPLETE / FINDING REGISTRY IMPLEMENTATION NOT ADMITTED**  
**Baseline:** `main@b633ac81f65952775d2d203b7b9986903d48365b`  
**Work owner:** #245; parent #244  
**Evidence baseline:** `system-development-bugwave-finding-coverage-2026-10-04.md` accounts for the major audit/research/learning chain at the present evidence state.  
**Depends on:** #246 stable references/currentness; #251 selected hybrid representation  
**This file is not:** an automatic extraction engine, a Requirement generator, a graph ontology, or implementation permission.

## 1. Problem closed by this design

The earlier rule `every registered material finding needs a disposition` had a loophole: a material source finding can disappear before registration. The current coverage pass recovered F43–F45 and demonstrated why the source-level coverage question must itself be owned.

The implementation therefore needs two different but linked responsibilities:

```text
SOURCE COVERAGE ACCOUNT
  proves/records which material findings were considered for a source

FINDING DISPOSITION
  records the current forward consequence of each accepted material finding
```

CI can validate the structure and closure of those records. It cannot reliably infer all material findings from arbitrary prose without a bounded analytical review.

## 2. Source coverage account

Every managed source artifact that materially contributes findings to a current/closed engineering change must have a coverage state.

Minimum logical fields:

```text
coverage_id
source_ref
coverage_scope
review_basis
reviewed_by_role
coverage_state
finding_refs
nonfinding_material_dispositions
reviewed_at_ref
notes_or_rationale
```

Candidate `coverage_state` values:

```text
not-reviewed
in-review
complete-at-evidence-state
superseded
not-required-with-rationale
```

These values describe the coverage process, not scholarly truth.

### 2.1 `complete-at-evidence-state`

Means:

- the stated source/scope was reviewed for material engineering findings against the stated evidence/version;
- every material finding identified in that review is registered or explicitly matched to an already-existing finding;
- material source conclusions intentionally not represented as findings have an explicit disposition/rationale where omission would otherwise be ambiguous.

It does **not** mean no future reading can ever discover another finding. New evidence or a demonstrated missed material finding invalidates/re-enters coverage.

### 2.2 Coverage scope

Coverage must be explicit enough to avoid false completeness. Examples:

```text
whole artifact
sections A–F
specific decision/finding appendix
Issue comments through a stated point
```

Do not claim whole-source coverage after sampling a few paragraphs.

## 3. Material finding record

The selected hybrid representation keeps detailed source prose in its source artifact and stores the promoted lifecycle consequence centrally.

Minimum logical fields:

```text
finding_id
source_ref
summary
failure_family_or_scope
materiality
current_disposition
rationale
disposition_authority_basis
target_refs
verification_or_followup_refs
supersedes_finding_id   # optional
```

The exact column shape may normalize multi-target data through `relations.tsv`; the semantic responsibility is fixed here.

### 3.1 Materiality

Materiality is a reasoned classification, not an automatic keyword rule.

A finding is material to the managed engineering system when omission could materially change one or more of:

- a Requirement;
- architecture/decision rationale;
- current/configuration meaning;
- work scope/dependency/readiness;
- acceptance/verification/validation;
- migration/loss risk;
- Human decision consequence;
- explicit residual risk/non-goal.

Local observations with no such consequence can remain source-local.

### 3.2 Finding identity

A finding keeps its stable ID when its disposition changes. A materially different finding gets a new ID rather than silently rewriting the old one.

F01–F45 are the current pre-migration identities for the active bugwave. The final registry may preserve these IDs directly or map them one-to-one to the stable implementation ID scheme; the migration must not make the current trace ambiguous.

## 4. Disposition contract

Supported semantic dispositions:

```text
open
integrated
promoted
deferred
rejected
superseded
local-only
no-change
controlled
partly-controlled
unresolved
```

Implementation may refine names, but it must preserve these distinctions.

### `open`

Material consequence known but not yet assigned/closed.

### `integrated`

Finding is incorporated into an existing current owner without creating a new independent owner. Must point to that owner/consequence.

### `promoted`

Finding caused a new/changed Requirement, accepted/proposed decision, design constraint, work item, test/fixture or other explicit durable consequence. Must point to target(s).

### `deferred`

No current action; revisit trigger/condition is explicit when material.

### `rejected`

The finding/interpretation or proposed consequence is not accepted. Rationale/evidence retained; rejection is not deletion.

### `superseded`

A later finding/evidence replaces its current interpretation. Must identify replacement/evidence; historical finding stays traceable.

### `local-only`

Valid only in bounded source/change context; intentionally not generalized.

### `no-change`

Material review concluded existing mechanisms are sufficient; point to the current mechanism/evidence.

### `controlled`

Current accepted mechanisms already control the failure class; retain as regression/risk evidence.

### `partly-controlled`

Some mechanisms exist but a residual/work path remains explicit.

### `unresolved`

Material meaning/consequence cannot yet be safely dispositioned. This is valid state and blocks only work whose correctness depends on resolving it.

## 5. Forward and backward trace

Required query semantics:

```text
source artifact / anchor
→ coverage account
→ finding(s)
→ current disposition
→ Requirement / decision / ADR / design / Issue / test / residual / no-change
```

and reverse:

```text
current Requirement / decision / proposed ADR / design constraint / Issue / test
→ supporting finding(s)
→ source artifact/anchor/evidence
```

This does not require every artifact relation in the repository to be represented.

> **Trace correctness outranks trace completeness.**

Unsupported relations are absent or candidate/unresolved; they are not filled for graph aesthetics.

## 6. Multiple consequences

One finding may legitimately influence several current consequences.

Example:

```text
F45 simplification can delete cognitive/review function
→ #247 Human/developer view acceptance
→ #251 migration loss check
→ #248 ADR consequence/reversibility discipline
```

Do not compress several consequences into one ambiguous `target_ref`. The implementation may use multiple relation rows while preserving one primary disposition/rationale.

## 7. Source closure rule

A material audit/change/result cannot be declared reconciled/closed at the engineering knowledge layer when:

- its required source coverage state is incomplete;
- a registered material finding remains without a disposition;
- `promoted/integrated` targets do not resolve;
- an unresolved finding materially affects the claimed closure and has no explicit residual/blocker status.

Historical Issues/files may already be closed under prior rules. Brownfield migration records their present coverage/disposition without retroactively pretending the new contract historically governed them.

## 8. Invalidating coverage

Re-enter the source coverage account when:

- a demonstrated material finding from the covered scope was missed;
- source artifact content materially changes;
- stronger/new evidence invalidates the prior extraction basis;
- the coverage scope was mis-stated;
- a supersession/migration breaks source anchors so the reviewed basis cannot be reconstructed.

A downstream target changing status does not necessarily require re-reading the source; it may only change the finding's disposition/relations.

## 9. Brownfield import of F01–F45

The current source-audit coverage artifact is the migration seed.

Implementation must:

1. register F01–F45 or a lossless one-to-one ID mapping;
2. preserve source family and meaningful anchor/evidence references;
3. carry current dispositions/work paths, including F10/F17 explicit residual semantics;
4. carry F43–F45 recovered findings rather than reverting to F01–F42;
5. record reviewed source families as `complete-at-evidence-state` only for the scope actually covered by the 2026-10 re-audit;
6. not infer that every file in `requirements/` has already received full coverage review.

## 10. Human/AI responsibility

AI may perform bounded extraction/classification/reconciliation work and propose materiality/dispositions from current evidence.

A finding does not become a Requirement, accepted ADR, D-016 admission, Project priority or scholarly truth merely because AI registers it.

If the disposition would make a new Human-reserved material architecture/purpose/priority decision, the finding remains proposed/open until that decision occurs.

## 11. Deterministic assurance boundary

Future validator can prove:

- required coverage fields are present;
- referenced findings/targets resolve;
- dispositions satisfy structural rules;
- coverage declared complete has all declared material finding refs represented;
- no closed managed source has structurally orphaned registered findings;
- anchors/IDs remain resolvable.

It cannot prove from arbitrary source prose that the analyst noticed every material insight. That quality is supported by explicit source coverage review, adversarial sampling/review and real-use recurrence checks.

## 12. Anti-context-swamp behavior

Default system-development context should consume:

- current material finding/residual summary relevant to the task;
- current dispositions/targets;
- source evidence pointers.

It should not load the full source audit text unless the task is reviewing/challenging that finding.

Preserve the source; promote the consequence; retrieve depth on demand.

## 13. Readiness disposition

**#245 design is complete.**

The major source chain has a present-state coverage account in the existing coverage artifact; source-level coverage vs finding-level disposition, materiality, dispositions, trace, multi-target behavior, closure/invalidation and brownfield import semantics are now fixed. The managed registry implementation remains D-016-gated.