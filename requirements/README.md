# Requirements

This directory is the repository surface for **accepted reusable Requirement baselines** plus a small set of explicitly retained cross-project Human-owner decision/admission records whose own change/decision owner has not been physically relocated by SD-KA-01/WP5.

## Current accepted baseline

`domain-requirements.tsv` is the current structured reusable Requirement inventory referenced by the canonical engineering configuration.

A file's presence under `requirements/` is **not** evidence that it is an accepted/current Requirement, an admitted change, or current work. Authority and lifecycle come from the owning contract, decision/admission record and, for managed engineering material, `engineering/catalog/artifacts.tsv`.

## WP5 migration result in this namespace

WP5 has removed the former historical engineering audit/research/learning/work-instruction/coordination accumulation from this namespace after inspecting its actual status/owner headers. Those artifacts now live under `engineering/evidence/`, retain stable managed IDs, and have old-path compatibility mappings in `engineering/catalog/legacy-paths.tsv`.

Current managed migration/rollback evidence lives in:

- `engineering/catalog/artifacts.tsv`
- `engineering/catalog/legacy-paths.tsv`
- `engineering/changes/SD-KA-01/MIGRATION.tsv`

The SD-KA-01 admission material itself now lives with the bounded change under `engineering/changes/SD-KA-01/`.

## Deliberately retained cross-project owner records

These are retained here in WP5 because moving them into the SD-KA-01 change would falsely absorb separately owned authority, while no dedicated replacement change/decision location has been established for them:

- `default-branch-promotion-enforcement-owner-admission-2026-09-17.md` — historical Route-B admission evidence; stable catalog ID `ENG-A-0110`;
- `default-branch-promotion-enforcement-owner-disposition-2026-09-17.md` — current Human-owner defer disposition for that Route-B family; `ENG-A-0111`;
- `outcome-preserving-execution-control-d016-decision-brief-2026-10-05.md` — separately owned execution-control decision brief; `ENG-A-0112`;
- `outcome-preserving-execution-control-d016-owner-admission-2026-10-05.md` — separately admitted execution-control owner record; `ENG-A-0053`;
- `source-project-owner-admission-2026-09-02.md` — cross-project Source/Project Human-owner decision/admission; `ENG-A-0113`.

Their retention is an explicit ownership boundary, not an unclassified brownfield remainder. A later owner-specific change may relocate them only with the same stable-identity/currentness/loss discipline.

Old paths for migrated managed artifacts are compatibility locators only; they are not parallel copies or currentness owners. Use the legacy-path catalog to resolve them.

No Project purpose, scholarly priority, manuscript state or scholarly `NEXT ACTION` is owned by this directory.
