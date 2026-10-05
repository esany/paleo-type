# SD-KA-01 bounded implementation requirements

## Preserved WP1 requirements

- Preserve the admitted P-001–P-012 semantics and the WP1–WP6 boundary.
- Give managed engineering artifacts stable IDs independent of physical paths.
- Keep actual Git configuration, accepted engineering baseline, proposed/admitted change state and work metadata distinct.
- Represent source coverage and F01–F45 finding dispositions without copying source prose or hiding F10/F17 residuals.
- Represent only explicit, review-relevant relations with resolvable endpoints.
- Keep proposed/admitted ADR rationale distinct from accepted `DECISIONS.md` authority.
- Validate malformed IDs, references, currentness/configuration, coverage and change-state fixtures deterministically.
- Do not move legacy `requirements/` files before the admitted physical-migration package or alter Project/manuscript state.

## WP2 requirements

- The accepted architecture and Requirement baselines must be directly derivable from canonical engineering configuration, not from chronology or repository recency.
- Active/admitted change semantics must remain distinct from accepted/current baseline semantics.
- The configuration contract must represent explicit current focus or explicit absence, with a provenance basis.
- Applicability entries must expose one of the designed provenance classes: `formal-derived`, `owner-declared`, `work-contract`, `selected-with-basis`, or `candidate/unresolved`, plus the supporting basis reference and scope.
- Proposed/admitted artifacts and ADRs must not enter accepted current baselines without the required accepted transition consequence.
- Git SHA, Issue/PR state and CI results may be preserved as provenance/evidence observations but must not create semantic currentness.
- Current/query views must be rebuilt on demand from canonical owners; no committed generated current-state file may become a second clock.
- Currentness/query fixtures must cover stale/latest-wins pressure, work-metadata-as-current pressure, explicit absence and concurrent/non-current artifacts.
- Derived current state must not duplicate or infer Project scholarly purpose, priority, gate or `NEXT ACTION`.
- WP2 must return its actual capability/reconstruction-cost change and WP3/WP4 readiness to the existing programme owner #244 without claiming programme closure.

## WP3 requirements

- Human, Senior Developer and Agent context products must be rebuildable role/task views over the same canonical/admitted owners; no generated context may become a second current-state or priority store.
- A generic current/start invocation may resolve context-relative work, but the Human-facing result must state a meaningful action/claim, scope and authority/provenance basis rather than only an Issue ID, work-package token or unexplained status.
- If current-work resolution remains ambiguous, the derived view must expose the ambiguity and candidates instead of silently choosing one repository-global cursor.
- Every included task-specific context item must expose an applicability basis where the data supports it; unresolved plausible applicability must remain visible rather than being silently treated as binding or omitted.
- The default system-development execution packet must contain only the applicable current work, authority/rule owners, Requirements/decisions/evidence, non-goals, acceptance/verification and whole-return contract, with deeper history/provenance expandable on demand.
- Unrelated historical artifact growth must not cause equivalent growth in the default current execution packet unless that history becomes applicable.
- A context-starvation fixture must fail when material authority, scope, applicability, uncertainty or the return/assurance boundary is removed.
- Senior Developer bootstrap must expose one bounded entry path from repository orientation through current engineering state/context to one documented local full-check command shared with CI.
- `python tools/check.py` is the shared deterministic full-check entrypoint. Its PASS establishes only the checked technical properties and does not create scholarly, specialist, Human or release acceptance.
- The bounded prompt capability must implement prompt creation, prompt review and prompt test without executing the requested task as part of prompt creation, maintaining work priority, becoming a planner/context owner or manufacturing authority.
- Simple non-repository prompt requests must remain simple; consequential paleo-type prompts must require fresh governing/current-owner resolution rather than paste stale repository state.
- Prompt review/test must detect material failure patterns such as indiscriminate `read everything`, non-closable work, recency-as-authority pressure, capability mismatch and independence overclaim.
- Consequential architecture/maintenance review contexts must expose review target, premise/evidence basis actually inspected, inherited premises, re-tested premises, independence claim and remaining evidence-depth limitation as applicable.
- A fresh context or second model must never be labelled independent evidence merely because it is fresh; initial derived review context must therefore make independence `not-established` until an actual evidence basis supports a stronger claim.
- WP3 must preserve accepted architecture/Requirement baselines, the WP5 physical-migration boundary and all Project/manuscript authority boundaries.
- WP3 must return reconstruction/Human burden, developer bootstrap quality, prompt behavior, F10/F17/residual risk and actual WP4/WP5 readiness to the existing programme owner #244 without claiming SD-KA-01 closure.
