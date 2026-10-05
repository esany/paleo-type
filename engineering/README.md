# Engineering knowledge and configuration

This repository-native surface is the admitted SD-KA-01 Engineering Knowledge & Configuration Plane implementation. WP1 established the in-place semantic owners; WP2 adds explicit currentness/applicability semantics and rebuildable current/query views without creating a second truth clock.

Existing `requirements/` files remain where they are until the separately ordered WP5 physical migration. The catalog records semantic identity and lifecycle without making a path, filename date, Git recency, Issue/PR state or CI result a currentness rule.

## Owners

- `configuration.json` owns accepted engineering baselines, admitted active changes, explicit current focus/absence and configuration-level applicability provenance.
- `catalog/artifacts.tsv` owns managed engineering-asset metadata.
- `catalog/coverage.tsv` owns source-level finding-coverage accounts.
- `catalog/findings.tsv` owns promoted material-finding dispositions.
- `catalog/relations.tsv` owns only explicit material cross-artifact relations.
- `changes/<change-id>/STATE.json` owns local change lifecycle, work-package cursor and admission state.
- `decisions/` records engineering rationale without replacing `DECISIONS.md` or owning current configuration.
- `tools/engineering.py` validates the contracts and derives/query views on demand; its output is never canonical truth.

The accepted current configuration must never be inferred from dates, filenames, Issue order, Git recency or CI status. Proposed/admitted/implemented/verified/accepted/no-change remain distinct semantics.

## Local commands

```text
python tools/engineering.py validate
python tools/engineering.py current
python tools/engineering.py derive
python tools/engineering.py query --authority-role work-metadata --owner-scope SD-KA-01
```

`current` is a rebuildable current-first view over canonical configuration/change/catalog owners. It exposes accepted baselines, active changes, focus or explicit absence, and applicability provenance. No generated current-state file is required.

These commands establish formal/deterministic properties only. They do not establish scholarly truth, specialist validation, Human acceptance, Project priority or a manuscript `NEXT ACTION`.
