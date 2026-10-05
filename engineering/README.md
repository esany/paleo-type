# Engineering knowledge and configuration

This repository-native surface is the admitted SD-KA-01 Engineering Knowledge & Configuration Plane implementation. WP1 established the semantic/catalog owners; WP2 added explicit currentness/applicability semantics and rebuildable current/query views; WP3 added role/task context products, Senior Developer bootstrap, a shared deterministic full check and bounded prompt interaction; WP4 added the ENG-FIT mapping, seeded falsification fixtures and explicit local/CI assurance boundaries. **WP5 is currently executing under #260** as the bounded loss-checked brownfield information-architecture migration. WP6 remains terminal adversarial qualification/Result Review.

WP5 moves only already-classified material or material whose actual owner/status supports a destination. Path movement never creates semantic currentness or acceptance. Stable IDs remain in `catalog/artifacts.tsv`; old managed paths resolve through `catalog/legacy-paths.tsv`; the concrete migration/rollback evidence is in `changes/SD-KA-01/MIGRATION.tsv`. The accepted reusable Requirement baseline remains `requirements/domain-requirements.tsv`.

## Owners

- `configuration.json` owns accepted engineering baselines, admitted active changes, explicit current focus/absence and configuration-level applicability provenance.
- `catalog/artifacts.tsv` owns managed engineering-asset identity and current paths.
- `catalog/coverage.tsv` owns source-level finding-coverage accounts.
- `catalog/findings.tsv` owns promoted material-finding dispositions.
- `catalog/relations.tsv` owns only explicit material cross-artifact relations.
- `catalog/legacy-paths.tsv` owns migration compatibility lookup for moved managed artifacts; legacy paths are locators, never parallel truth.
- `changes/<change-id>/STATE.json` owns local change lifecycle, work-package cursor and admission state.
- `changes/SD-KA-01/MIGRATION.tsv` records the classified WP5 physical-migration slice, pre-move blob identity and rollback boundary.
- `decisions/` records engineering rationale without replacing `DECISIONS.md` or owning current configuration.
- `evidence/audits/` and `evidence/research/` contain migrated non-default engineering evidence; their presence does not make them accepted/current baselines.
- `context/README.md` owns the derived context/profile and Human-visible cursor contract; generated context output remains derived.
- `prompts/CONTRACT.md` owns bounded `.prompt` create/review/test behavior; it creates no work authority or task execution.
- `tools/engineering.py` validates the contracts and derives/query current engineering state on demand.
- `tools/engineering_context.py` compiles role/task-specific derived context profiles on demand.
- `tools/prompt.py` is the executable reference/regression surface for the bounded prompt capability.
- `tools/engineering_fitness.py` checks the repository-testable ENG-FIT surface, including legacy-path continuity when applicable.
- `tools/check.py` is the shared local/CI deterministic full-check entrypoint.

The accepted current configuration must never be inferred from dates, filenames, paths, Issue order, Git recency or CI status. Proposed/admitted/implemented/verified/accepted/no-change remain distinct semantics.

## Senior Developer start path

Use this bounded path rather than replaying dated audits:

```text
README.md
→ this file
→ python tools/engineering.py current
→ python tools/engineering_context.py --profile system-development-execution
→ active/next bounded work and applicable owners
→ python tools/check.py
→ deeper provenance only when needed
```

For a concise Human-readable current/next work rendering:

```text
python tools/engineering_context.py --profile human-system-overview --format text
```

The visible result must be a meaningful action with scope and authority basis, not only an Issue/work-package token. Context-relative currentness is allowed; unresolved ambiguity is exposed rather than hidden behind one repository-global cursor. Between packages, `configuration.json` may carry explicit no-current-focus while `STATE.json`/relations expose one ready-next transition. **Ready-next is navigation/readiness, not an active focus or automatic work start.**

## Local commands

```text
python tools/engineering.py validate
python tools/engineering.py current
python tools/engineering.py derive
python tools/engineering.py query --authority-role work-metadata --owner-scope SD-KA-01

python tools/engineering_context.py --profile human-system-overview --format text
python tools/engineering_context.py --profile system-development-execution
python tools/engineering_context.py --profile architecture-review

python tools/prompt.py create --repo esany/paleo-type "<task>"
python tools/prompt.py review --repo esany/paleo-type "<prompt>"
python tools/prompt.py test --self-review "<prompt>"

python tools/engineering_fitness.py
python tools/check.py
```

`current` is a rebuildable current-first view over canonical configuration/change/catalog owners. It exposes accepted baselines, active changes, focus or explicit absence, and applicability provenance. Context profiles select from those owners for a role/task and keep deeper provenance expandable; no generated current-state/context file is required.

`tools/check.py` runs Source Contract validation, Engineering validation, the engineering-fitness contract, the full regression suite, fresh-process Project context compilation and managed real-data resolver fixtures. CI calls the same entrypoint.

All these commands establish only their stated formal/deterministic properties. They do not establish manuscript truth, specialist validation, Human acceptance, Project priority, a scholarly `NEXT ACTION`, evidential independence, external runtime fitness or whole-system closure.
