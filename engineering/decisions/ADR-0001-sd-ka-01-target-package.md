# ADR-0001 — SD-KA-01 target architecture package

Status: **admitted-for-implementation; not accepted current configuration**

## Decision

Implement the repository-native SD-KA-01 package P-001–P-012 inside the bounded WP1–WP6 scope admitted by:

`requirements/system-development-bugwave-d016-owner-admission-2026-10-04.md`

The package separates engineering information management from configuration management, requires material finding coverage/disposition, uses stable references and explicit transitions, derives distinct current-first contexts, adds an ADR surface, puts semantic contracts before physical migration, adds fitness after semantic stabilization and keeps `.prompt` thin and non-authoritative.

## Authority and boundary

This record is an engineering rationale/trace surface. D-016 in `DECISIONS.md` and `methodology/maintenance.md` own admission semantics; the admission record owns this implementation authorization; `configuration.json` owns accepted engineering baselines and active changes. This ADR does not make the proposed target current by itself.

## Consequences

WP1 proves the contracts against the real brownfield without bulk-moving legacy files. Later work may update accepted configuration only through explicit implementation, verification and Result Review transitions. The design remains repository-native and reversible; graph services, workflow engines, portals, package splits, scholarly Project changes and #90/#225 reactivation remain out of scope.

## Related evidence

- `requirements/system-development-bugwave-d016-decision-brief-2026-10-04.md`
- `requirements/system-development-bugwave-finding-promotion-design-2026-10-04.md`
- `requirements/system-development-bugwave-configuration-reference-design-2026-10-04.md`
- `requirements/system-development-bugwave-adr-surface-design-2026-10-04.md`
- `requirements/system-development-bugwave-brownfield-migration-design-2026-10-04.md`
