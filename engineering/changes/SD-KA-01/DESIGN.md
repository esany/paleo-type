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

## WP3 context / developer bootstrap / prompt design

WP3 builds **derived interaction products** on top of the WP2 currentness primitives; it does not create a new truth clock or planning authority.

### Context ownership and profiles

`engineering/context/README.md` owns the operational context contract. `tools/engineering_context.py` compiles role/task profiles on demand from configuration, bounded change state and catalog/relation owners. It never writes a generated current-state file.

The implemented profiles are:

- `human-system-overview` — current accepted state, semantically explicit current/next work, readiness, residuals and assurance boundary;
- `system-development-execution` — bounded Agent/Senior-Developer packet with authority reads, applicability, non-goals, acceptance/verification and whole-system return;
- `architecture-review` — accepted/admitted context plus review-evidence-basis semantics;
- `human-material-decision` — plain-language decision/non-decision rendering without creating a Human gate;
- `maintenance-review` — changed-owner/propagation context with review-basis semantics.

Context inclusion remains provenance-bearing. The compiler consumes explicit WP2 applicability entries; it does not infer a universal deterministic applicability ontology.

### Human-visible current-work rendering

A generic invocation may be useful, and multiple contexts may legitimately have different scoped current work. The visible Human result must nevertheless render a meaningful action/claim, scope and basis. A raw Issue number or `WP3` token is not sufficient.

Resolution order is deliberately narrow:

1. explicit scoped work supplied by the caller, without manufacturing global currentness;
2. configured `current_focus`;
3. one uniquely accepted `transitions-to` relation to active work metadata;
4. explicit ambiguity if several candidates remain;
5. explicit absence if none is authorized/resolvable.

This prevents both latest-wins selection and a repository-global cursor singleton.

### Context-starvation / history-growth safeguards

`context_adequacy_errors` checks the structural minimum for derived packets: derived-authority boundary, current/next work resolution, scope/basis where current, applicability provenance and profile-specific execution/review contracts.

Regression fixtures additionally prove that unrelated historical catalog growth does not automatically enter the default execution packet and that multiple plausible next-work relations are exposed as ambiguity rather than silently ranked.

### Review Premise Inheritance

Architecture/maintenance review profiles initialize a `review_evidence_basis` surface containing review target, material premise, basis class/references, inherited/re-tested premises, independence claim and evidence-depth limit.

The default independence claim is `not-established`. The context compiler can expose provenance; it cannot prove that a reviewer inspected deeply enough, is competent or is evidentially independent. A fresh context/second model is therefore never upgraded to independent evidence merely because it is fresh.

### Senior Developer bootstrap and assurance

The target developer path is now executable:

```text
README
→ engineering/README
→ tools/engineering.py current
→ tools/engineering_context.py --profile system-development-execution
→ active bounded work/applicable owners
→ tools/check.py
→ deeper provenance on demand
```

`tools/check.py` is the single documented deterministic full-check entrypoint shared by local use and CI. It runs Source Contract validation, Engineering validation, the full regression suite, fresh Project context compilation and the real Project/Source resolver fixtures. Its success remains technical assurance only.

### Bounded `.prompt` capability

`engineering/prompts/CONTRACT.md` owns the admitted interaction contract and `tools/prompt.py` provides the executable reference/regression surface:

- prompt create returns a copy-ready prompt and does not execute the task;
- prompt review improves a supplied prompt without silently changing purpose/scope/authority;
- prompt test evaluates bounded failure patterns and states the judgement/proof boundary.

Repository-target prompts resolve fresh authority/current owners, stay inside admitted scope, require repo-first persistence and use the shared check where appropriate. Non-repository simple prompts stay simple. The capability does not maintain current Requirements/ADRs/issues, choose priority or become a planner/context compiler.

## Boundary to later work

WP3 implements context/profile/bootstrap/prompt primitives only. WP4 remains responsible for the wider engineering-fitness/CI closure set and additional seeded assurance coverage; WP5 remains the controlled physical information-architecture migration; WP6 remains adversarial qualification and terminal SD-KA-01 Result Review. WP3 technical PASS cannot start, accept or close those later packages by itself.
