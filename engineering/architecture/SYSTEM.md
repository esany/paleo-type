# Current engineering architecture and admitted change

## Current accepted baseline

The repository's accepted engineering baseline includes the governing objective, guardrails, methodology, accepted cross-project decisions in `DECISIONS.md`, and the terminally qualified SD-KA-01 target package recorded by ADR-0001 / `artifact:ENG-A-0031`. Git remains the byte/provenance history. This architecture entered the accepted baseline only through the explicit implementation → verification → terminal Result Review transition; admission, path movement, recency and CI alone did not promote it.

## Admitted change

`SD-KA-01` was the Human-admitted bounded implementation programme for the Engineering Knowledge & Configuration Plane and Development Readiness operationalization. Its admission remains the stable historical authority artifact `ENG-A-0010`, located with the completed change at:

`engineering/changes/SD-KA-01/D016-OWNER-ADMISSION.md`

The pre-migration locator remains resolvable through `engineering/catalog/legacy-paths.tsv`; it is not a parallel copy or currentness owner.

WP1 established the semantic/catalog foundation; WP2 implemented accepted-baseline/current-change semantics and rebuildable current/query views; WP3 implemented role/task-derived contexts, Senior Developer bootstrap, bounded prompt behavior and the shared full-check entrypoint; WP4 implemented the ENG-FIT engineering-fitness mapping and shared local/CI assurance boundary; WP5 completed and exactly post-merge verified the loss-checked information-architecture migration; **WP6 completed adversarial qualification and terminal Result Review, accepting ADR-0001 as the current engineering architecture baseline**.

The executable current-state surface is derived from `engineering/configuration.json`, `engineering/changes/SD-KA-01/STATE.json` and managed catalogs. `tools/engineering_context.py` builds role/task context views; `tools/prompt.py` implements the bounded prompt interaction contract; `tools/check.py` is the shared local/CI deterministic full check; `tools/engineering_fitness.py` checks the admitted repository-testable ENG-FIT surface. None chooses accepted architecture by newest file, newest path, newest Git commit, Issue/PR state or CI success.

The canonical configuration now records no active SD-KA change and no current focus. WP5 moved 74 classified artifacts into semantic owners while preserving stable IDs, exact pre-move blob identity, legacy-path continuity and rollback evidence. `requirements/` is narrowed to its README and accepted reusable Requirement baseline. Cross-project Human decision/admission records moved to `engineering/evidence/decisions/` without transferring their authority into SD-KA-01.

## Boundaries

- scholarly Project/Corpus truth remains with its existing owners;
- Issues and PRs are work/review metadata, not accepted configuration authority;
- implemented engineering capability or a path move does not by itself promote the full admitted SD-KA-01 target into accepted architecture baseline;
- current/query/context views are derived and rebuildable and do not become a parallel state/priority store;
- legacy paths are compatibility locators, not compatibility copies or semantic owners;
- evidence directory location does not transfer owner scope or decision authority;
- prompt construction is not task execution or authority and does not become a planner/context owner;
- fresh context/model identity does not establish evidential independence; consequential review must state the evidence basis actually inspected;
- explicit absence or ambiguity of active/scoped work is valid and must not manufacture replacement work;
- CI/technical PASS establishes only repository-testable deterministic properties actually exercised; it does not establish scholarly truth, specialist validity, Human acceptance, external runtime/cancellation/preservation fitness or whole-system closure.
