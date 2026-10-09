# Outcome-Preserving Return Gate — D-016 decision brief

Status: PROPOSED / NOT ADMITTED / no executable implementation started
Repository: esany/paleo-type
Decision owner: decision:D-016
Decision surface: existing shared execution-control decision boundary; no new Issue owner
Evidence basis: engineering/evidence/audits/outcome-preserving-spiral-audit-2026-10-09.md
Proposal branch: fix/outcome-preserving-spiral-breaker-2026-10-09
Base: main@a3c865ec60246118206be5dde3aefdbd7f9a77d1

## 1. Decision requested

Decide whether the existing admitted outcome-preserving execution-control change may be refined with an Outcome-Preserving Return Gate.

The requested decision is deliberately narrow:

- authorize a mandatory return tuple at existing consequential action and acceptance boundaries;
- extend existing prompt/engineering fitness assurance only where a deterministic property can actually be checked;
- use existing vertical owners for scholarly meaning, runtime acceptance, provenance and whole-system result review;
- do not create a new universal workflow engine, state machine, Issue lifecycle owner, ontology or parallel truth store.

This is a decision surface, not an automatic admission. The current repository-backed state says implementation is not currently allowed for the cross-project work context.

## 2. Problem the change must solve

The current system can correctly document:

- Human authority;
- semantic distinctions;
- online repository authority;
- technical versus scholarly acceptance;
- residuals and owner boundaries.

Yet fresh use can still perform this invalid conversion:

    complete Human outcome
    → bounded local work
    → technical/local PASS
    → outcome cursor silently replaced by implementation cursor
    → residual is deferred or turned into another comment

The result is the recurring spiral documented in the audit. The system is not protected merely because the relevant rule already exists.

## 3. Required invariant

No consequential local action, technical PASS, PR state, Issue state, package state or owner existence may establish whole-system resolution unless the result is explicitly returned to the protected outcome and the correct acceptance owner.

A recurrence of a documented failure is evidence that the current operative control failed. It may not be dismissed solely because an owner, rule or prior implementation exists.

## 4. Proposed mechanism

### 4.1 Return tuple

Before a consequential work block crosses an action or acceptance boundary, it must make available:

- protected outcome;
- semantic scope and negative distinctions;
- coupled obligations and affected owners;
- authorized action/consequence class;
- Definition of Ready;
- Definition of Done;
- residual and return condition;
- claim ceiling.

The tuple is evidence for the transition. It is not a new canonical state store.

### 4.2 Four control points

**A. Outcome lock:** before decomposition, state the Human/research/product result and the semantic boundaries.

**B. Material-action gate:** before mutation or direction-setting work, resolve current authority, remote state, action class, DOR, DOD and stop criteria.

**C. Local-result return:** after a slice, compare the actual result with the protected outcome, coupled obligations, evidence and acceptance level.

**D. Closure/handoff gate:** block closure or completion reporting when residual, owner, return condition or fresh-context reconstruction is missing.

### 4.3 Fail-closed conditions

The affected transition stops when:

- the protected outcome is absent or has been replaced by a technical subtask;
- context is promoted to content, authority, Project purpose or priority without an evidence bridge;
- local/technical/CI/PR/Issue PASS is used as whole-system acceptance;
- a recurrence is treated as covered only because a rule/owner exists;
- a material decision is absorbed without its authority boundary;
- remote execution or remote mutation proof is missing;
- connector failure is routed to local staging or later promotion;
- a coupled parent obligation is silently dropped;
- residual, claim ceiling or return condition is absent.

## 5. Implementation locus if ADMIT is selected

Implementation must remain inside existing owners:

1. engineering/prompts/CONTRACT.md: make the return tuple and recurrence-stop behavior a bounded prompt contract, without turning prompts into authority.
2. tools/prompt.py and its existing tests: add only deterministic checks that can reject missing outcome/return/claim-ceiling evidence in a consequential paleo prompt. Do not pretend this validates future model behavior.
3. engineering/assurance/fitness.json: extend existing ENG-FIT-09 fixture coverage rather than creating a second assurance system.
4. Existing vertical acceptance owners:
   - #297 / #280 for False Lean, parent outcome and whole-system result review;
   - #292 / #308 for Human-facing meaning and semantic precedence;
   - #307 for source/AI/unresolved provenance separation;
   - #271 / #282 for productive runtime and preservation;
   - #281 for execution-control falsification;
   - source/Project owners for context/content/authority distinctions.
5. tools/check.py remains the repository verification entrypoint for changed repository semantics/code.

No implementation may change Project purpose, scholarly priority, Source/File/Project truth, Nr. 632 identity, Wolkenburg meaning, Wissensarbeit planning state or Issue closure as a side effect.

## 6. Definition of Ready

The change may start only when:

- the Human Owner has selected D-016 ADMIT for this precise scope;
- current main, governance, applicable owners and current acceptance state have been freshly read;
- the existing D-016 execution-control scope is confirmed as the carrier;
- every changed file and test has a named owner;
- the acceptance envelope below is preserved;
- the implementation branch/PR and stop/return conditions are explicit;
- no local checkout, local Git or local fallback is used for repository work.

## 7. Definition of Done

The change is done only when:

- every changed carrier is the existing owner of the property;
- missing return/claim/acceptance evidence is deterministically rejected where the repository can check it;
- adequate minimal work remains accepted;
- False-Lean/local-PASS, context/content, provenance, Human-meaning and remote-proof fixtures are present at the correct owners;
- V1 fresh-context scholarly stage preservation passes;
- V2 productive runtime and preservation acceptance passes;
- #276/#277 and the relevant failure families are dispositioned against observed behavior;
- a fresh context reconstructs the protected outcome, scope, evidence, residual and return condition;
- #280 performs the overordinate result review;
- no technical check is described as scholarly or whole-system acceptance;
- unresolved model/platform/runtime limits remain explicit.

## 8. Falsification

Reject the proposal or return it to a narrower owner if evidence shows that:

- the tuple duplicates an existing canonical state owner;
- it becomes a generic planner or workflow engine;
- it adds ceremony without blocking a demonstrated invalid transition;
- it is used to defer a known outcome failure behind owner language;
- deterministic tests are presented as universal AI or scholarly assurance;
- the real vertical fixtures remain untested while the mechanism is declared complete;
- the mechanism cannot distinguish Wolkenburg context from Nr. 632 content;
- closure still depends on comment volume or Issue age.

## 9. Explicit non-goals

This decision does not authorize:

- a new state-machine architecture;
- a generic autonomous planner;
- a universal permission broker;
- a second Issue/acceptance owner;
- automatic Issue closure, reopening or successor creation;
- a new Source/File/Project ontology;
- scholarly acceptance or specialist validation;
- physical guarantees the GitHub connector/harness cannot provide;
- a claim that future assistant behavior is error-proof.

## 10. Decision boundary

If the Human Owner selects ADMIT, implementation may proceed only within sections 5–7 and must stop when the acceptance envelope or owner boundary is exceeded.

If ADMIT is not selected, the audit remains durable evidence and no executable mechanism is claimed.

The success criterion is outcome-level:

> A future local success must be unable to masquerade as resolution without an explicit return to the protected outcome, semantic scope, coupled obligations, evidence, residual and correct acceptance owner.
