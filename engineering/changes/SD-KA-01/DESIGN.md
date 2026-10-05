# SD-KA-01 bounded implementation design

## WP1 foundation

WP1 uses the admitted hybrid representation: central TSV registries for cross-artifact identity, coverage, findings and relations; JSON for configuration and bounded change state; Markdown remains the natural content owner. Paths are locators, never stable identity.

The validator resolves `artifact:`, `finding:`, `change:`, `decision:`, `adr:`, `github-issue:`, `github-pr:`, `git:` and `path:` references. It checks structural semantics only. It does not infer findings from prose, decide open scholarly applicability, accept architecture or replace scholarly/specialist/Human review.

## WP2 current/configuration design

WP2 keeps `engineering/configuration.json` as the canonical owner for accepted engineering baselines, admitted active changes and optional bounded current focus. The configuration is not a Git mirror and not a planning database.

The version-2 contract adds:

- `change_states` keyed by stable `change:` reference, with transition state, authority/evidence basis, work owner and accepted-consequence disposition;
- structured `current_focus` with explicit applicability/work-contract provenance, or `null` for explicit absence;
- `applicability` entries carrying the designed basis classes and supporting reference;
- exact Git SHAs only inside transition provenance, never as a recency/currentness selector.

The executable transition vocabulary preserves the designed sequence and alternatives:

```text
proposed -> admitted -> implemented -> verified -> accepted
                                   \-> verified -> no-change
proposed/admitted/implemented/verified -> superseded/rejected/re-entered as allowed
```

A transition vocabulary does not itself mutate authority. A baseline changes only when the canonical configuration is explicitly updated on evidence/authority permitted by the admitted result semantics.

## Derived current state

`tools/engineering.py current` compiles a rebuildable current-first view from canonical configuration, change state and catalog identities. It reports:

- accepted architecture and Requirement baselines;
- active changes and their transition state;
- present or explicitly absent current focus;
- applicability entries with their provenance basis;
- transition provenance and an explicit derived/non-authoritative assurance boundary.

No `engineering/generated/CURRENT_STATE.json` is required or committed in WP2. `derive` includes the same current view for compatibility, while `query` remains a bounded catalog query surface with explicit metadata filters. Semantic currentness is exposed only by `current`, never inferred from catalog order.

## Currentness safety

Validation rejects:

- accepted baseline references to artifacts whose authority role is not canonical/accepted;
- active changes without explicit change-state entries;
- invalid transition states or result consequences;
- current focus/applicability without resolvable provenance;
- unsupported applicability basis classes;
- work-metadata/proposed artifacts promoted to accepted baseline by configuration.

Tests additionally prove that adding a newer/proposed artifact does not change the derived accepted baseline, that work metadata cannot manufacture accepted current architecture, and that explicit absence is represented without inventing replacement focus.

## Boundary to later work

WP2 provides currentness/query/applicability primitives only. WP3 remains responsible for Human strategic, developer bootstrap, Agent execution/review products and `.prompt`; WP4 remains responsible for the wider engineering-fitness/CI closure suite; WP5 remains the physical information-architecture migration; WP6 remains adversarial qualification and terminal Result Review.
