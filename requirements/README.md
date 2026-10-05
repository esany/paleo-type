# Requirements

This directory is the repository surface for **accepted reusable Requirement baselines** and any explicitly retained cross-project requirement owner that has not yet been moved under an admitted migration.

## Current accepted baseline

`domain-requirements.tsv` is the current structured reusable Requirement inventory referenced by the canonical engineering configuration.

A file's presence under `requirements/` is **not** evidence that it is an accepted/current Requirement, an admitted change, or current work. Authority and lifecycle come from the owning contract, decision/admission record and, for managed engineering material, `engineering/catalog/artifacts.tsv`.

## WP5 brownfield migration boundary

SD-KA-01/WP5 is migrating already-classified engineering design/audit/admission material out of the former mixed-purpose `requirements/` namespace. Current managed paths and compatibility lookup live in:

- `engineering/catalog/artifacts.tsv`
- `engineering/catalog/legacy-paths.tsv`
- `engineering/changes/SD-KA-01/MIGRATION.tsv`

The current SD-KA-01 admission material now lives with the bounded change under `engineering/changes/SD-KA-01/`. Deep SD-KA design, audit and research evidence lives under `engineering/evidence/`.

Files that remain here during WP5 are not silently reclassified by filename. Historical, cross-project, separately owned or still-unclassified material stays in place until its actual header/owner/status supports a loss-checked destination. In particular, the separately admitted outcome-preserving execution-control family remains under its own owners and is not absorbed into SD-KA-01 merely because both are engineering work.

Old paths for migrated managed artifacts are compatibility locators only; they are not parallel copies or currentness owners. Use the legacy-path catalog to resolve them.

No Project purpose, scholarly priority, manuscript state or scholarly `NEXT ACTION` is owned by this directory.
