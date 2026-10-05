# Bounded `.prompt` capability contract

**Status:** admitted SD-KA-01/WP3 operational support capability.

This contract activates the bounded behavior previously tested under #252. It is not METHOD, a planner, a context compiler, work authority, Project priority, D-016 admission, task execution or independent review.

## User-facing behavior

### `.prompt <task>`

Return a copy-ready prompt for the task and stop. Do not execute the task as part of prompt creation.

### `.prompt review <prompt>`

Review and improve the supplied prompt while preserving its purpose, scope and authority. Return the improved copy-ready prompt plus only material corrections when useful.

### `.prompt test <prompt/result/context>`

Evaluate behavior against explicit failure patterns and state what the test actually demonstrates. Internal/self-review is judgement evidence, not independent proof.

`tools/prompt.py` is the repository-local executable reference implementation and regression surface for these semantics. A chat/product may expose the same interaction syntax without treating this CLI as a global command language.

## Invariants

1. Prompt creation is not task execution.
2. Generated prompts create no Project purpose, priority, `NEXT ACTION`, D-016 admission, accepted Requirement/ADR or scholarly truth.
3. Use the smallest sufficient instruction; fidelity precedes token savings.
4. For consequential `esany/paleo-type` work, require fresh `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, applicable current task/Project owners and canonical rules instead of embedding stale repository state.
5. Complete applicable context is required; `read everything` is not an applicability strategy.
6. Repository-capable work persists restart-relevant results repository-first in the actual owner/working branch.
7. Technical PASS does not create scholarly, specialist or Human acceptance.
8. Human confirmation is requested only at a real authority boundary; routine already-authorized work is not wrapped in approval ceremony.
9. Material work is closeable: prompts state completion/return behavior rather than `continue until done`.
10. A fresh context/second model is not called independent evidence without an actually independent evidence basis.
11. The capability does not maintain current Requirements/ADRs/issues or choose work priority; repository context/configuration owners do that.
12. Non-repository simple prompts stay simple and do not inherit paleo-type engineering ceremony.

## Repository-target prompt minimum

A consequential prompt targeting `esany/paleo-type` should normally require the executor to:

- resolve fresh repository authority/current work rather than trust old chat, date order or latest Git activity;
- stay inside the already-authorized bounded scope and return new material choices instead of silently absorbing them;
- preserve scholarly/Project authority boundaries;
- use `python tools/check.py` for the shared full deterministic assurance entrypoint when code/repository semantics are changed;
- state actual changed state, residual limits and any programme/whole-system consequence required by the existing owner.

These are selection rules, not a requirement to paste the repository's guardrail corpus into every generated prompt.

## Review/test failure patterns

At minimum detect or challenge:

- solution anchoring before the problem/requirements are established;
- missing authority/write boundary;
- `read everything` or another open read scope;
- mega-prompt duplication of canonical prose;
- non-closable `until done` work;
- invented status/owner vocabulary;
- wrong repository/target;
- unavailable capability assumptions;
- self-review mislabeled independent;
- CI/context/Issue state laundering authority or acceptance;
- context starvation that removes material authority/uncertainty solely for compactness.

## Assurance boundary

Regression tests can prove deterministic behavior of this implementation. They cannot prove that every future generated prompt is substantively adequate, that a reviewer is independent, or that a scholarly result is correct. Those claims remain with their actual evidence/authority owners.
