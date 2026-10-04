# Engineering knowledge and configuration

This is the repository-native WP1 foundation for SD-KA-01. It separates engineering information metadata, the accepted/current engineering baseline, bounded admitted change state and rebuildable validation from the scholarly Project/Corpus owners.

WP1 is deliberately in-place. Existing `requirements/` files remain where they are until the separately ordered physical migration work package. The catalog records semantic identity and lifecycle without making a path a stable identity.

## Owners

- `configuration.json` owns accepted engineering baselines and admitted active changes.
- `catalog/artifacts.tsv` owns managed engineering-asset metadata.
- `catalog/coverage.tsv` owns source-level finding-coverage accounts.
- `catalog/findings.tsv` owns promoted material-finding dispositions.
- `catalog/relations.tsv` owns only explicit material cross-artifact relations.
- `changes/<change-id>/STATE.json` owns local change lifecycle and admission state.
- `decisions/` records engineering rationale without replacing `DECISIONS.md` or owning current configuration.
- `tools/engineering.py validate` is the deterministic WP1 contract check; it does not establish scholarly or Human acceptance.

The current configuration must never be inferred from dates, filenames, Issue order, Git recency or CI status. Proposed/admitted/implemented/verified/accepted remain distinct states.

## Local check

```text
python tools/engineering.py validate
```

This command validates the in-place baseline, stable references, F01–F45 coverage and the admitted SD-KA-01 transition. It does not perform physical migration, compile a Human/Agent context or claim that the whole SD-KA-01 programme is accepted.
