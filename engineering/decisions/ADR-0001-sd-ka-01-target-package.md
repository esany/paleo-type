# ADR-0001 — SD-KA-01 target architecture package

Status: **accepted current engineering architecture baseline after terminal WP6 Result Review**

## Decision

Implement the repository-native SD-KA-01 package P-001–P-012 inside the bounded WP1–WP6 scope admitted by:

`engineering/changes/SD-KA-01/D016-OWNER-ADMISSION.md`

The stable managed identity of that admission remains `artifact:ENG-A-0010`; its former `requirements/` locator is retained only in `engineering/catalog/legacy-paths.tsv`.

The package separates engineering information management from configuration management, requires material finding coverage/disposition, uses stable references and explicit transitions, derives distinct current-first contexts, adds an ADR surface, puts semantic contracts before physical migration, adds fitness after semantic stabilization and keeps `.prompt` thin and non-authoritative.

## Authority and boundary

This record is an engineering rationale/trace surface. D-016 in `DECISIONS.md` and `methodology/maintenance.md` own admission semantics; the admission record owns this implementation authorization; `configuration.json` owns accepted engineering baselines and active changes. This ADR became an accepted architecture baseline only through the completed implementation, exact-head qualification and terminal Result Review recorded in `engineering/changes/SD-KA-01/RESULT.md` and `engineering/configuration.json`; the ADR file did not make itself current by admission or recency.

## Consequences

WP1 proved the contracts against the real brownfield without bulk-moving legacy files. WP5 changed classified physical locators only with stable identity, compatibility/rollback evidence and loss checks. WP6 then qualified the composed WP1–WP5 system and terminal Result Review accepted P-001..P-012 as an engineering architecture baseline. This acceptance changes engineering configuration only; it does not establish manuscript truth, specialist validation, evidential independence, #225 scholarly acceptance or external runtime fitness. The design remains repository-native and reversible; graph services, workflow engines, portals, package splits, scholarly Project changes and #90/#225 reactivation remain out of scope.

## Related evidence

- `engineering/changes/SD-KA-01/D016-DECISION-BRIEF.md`
- `engineering/evidence/research/system-development-bugwave-finding-promotion-design-2026-10-04.md`
- `engineering/evidence/research/system-development-bugwave-configuration-reference-design-2026-10-04.md`
- `engineering/evidence/research/system-development-bugwave-adr-surface-design-2026-10-04.md`
- `engineering/evidence/research/system-development-bugwave-brownfield-migration-design-2026-10-04.md`
