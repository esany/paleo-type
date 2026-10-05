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
