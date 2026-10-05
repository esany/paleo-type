# SD-KA-01 implementation plan

## WP1 — verified and returned

WP1 persisted the Human-Owner admission, established the in-place `engineering/` semantic owners and representative F01–F45 baseline, added deterministic structural validation and returned its exact result/whole-system consequence to #244. No physical migration or scholarly Project state changed.

## WP2 — verified and returned (#257)

Execution baseline: `main@2c683beaefa18bc07810bf91cbbe67a07ef81f6a`. WP2 implemented explicit currentness/change/applicability semantics and rebuildable current/query views, then passed exact PR-head and post-merge assurance and returned the result without promoting the whole target to accepted architecture.

## WP3 — verified and returned (#258)

Execution baseline: `main@ddf289fdf69f3827f287665a2a8c8e4d137fcbba`. WP3 implemented Human/Developer/Agent context profiles, Senior Developer bootstrap, bounded prompt behavior, review-evidence-basis safeguards and the shared `python tools/check.py` entrypoint; exact PR-head and post-merge assurance passed and the result was returned.

## WP4 — verified and returned (#259)

Execution baseline: `main@743f97266260b18b7d179a2b214bff3d86fa4487`. WP4 implemented the ENG-FIT-01..ENG-FIT-09 mapping and fourteen admitted seeded failure families, integrated them into the shared full-check entrypoint, passed exact PR-head/post-merge assurance and returned #260/WP5 as ready-next without changing accepted baselines.

## WP5 — verified and returned (#260)

Execution baseline: `main@b01bfa1b0f523919c1d8dbd45a9b30fd5a66aba0`, the exact WP4-result head with post-merge source-contract run #571 successful.

Completed bounded sequence:

1. advanced current work ownership/focus to #260/WP5 under the existing D-016 admission without changing accepted architecture/Requirement baselines;
2. classified material by existing managed metadata or inspected header/status/owner evidence, never by filename guess;
3. preserved the accepted reusable Requirement baseline `requirements/domain-requirements.tsv` and narrowed the namespace to that baseline plus `requirements/README.md`;
4. moved **74 classified artifacts in three physical slices**: 16 managed SD-KA artifacts, 53 historical engineering evidence artifacts, and 5 separately owned cross-project Human decision/admission records;
5. preserved exact pre-move blob bytes, stable `ENG-A-*` identities, current paths, legacy-path lookup and per-slice rollback evidence in `MIGRATION.tsv`/`legacy-paths.tsv`;
6. preserved cross-project decision authority/owner scope after relocating those records to `engineering/evidence/decisions/`;
7. repaired active navigation and stale old-path consumers so legacy locators are compatibility lookup rather than parallel truth;
8. ran deterministic migration-loss fixtures for stable identity/current-path agreement, exact byte equivalence, Requirements residue, no compatibility copies, ENG-FIT-08, context navigation and accepted/current-baseline invariance;
9. source-contract run #581 exposed three stale recovery consumers of the old Source/Project owner-admission path; those consumers were repaired and the failure/fix retained as loss-check evidence;
10. exact PR head `0c4c94831f3d3266c0a532afc250bd29bf2fbd37` passed source-contract run #582; PR #298 merged at `main@ffc4d3736148987cd30aa805519634287d1b4b6b`; exact post-merge run #583 passed;
11. persisted the WP5 Result/whole-system return with no current implementation focus and #261/WP6 ready-next.

The physical moves changed locations only, not accepted/current meaning. The implementation PR is the bounded rollback unit and the exact physical-slice commits remain recorded in the migration compatibility catalog.

## WP6 — verified, terminal Result Review accepted (#261)

Execution baseline: `main@57f2bc6fdf2c9222d236d265f31433b79f99e866`, the exact WP5-result head.

WP6 completed the admitted terminal qualification across WP1–WP5, including fresh Human/Senior-Developer/Agent journeys, ENG-FIT adversarial fixtures, finding/residual checks, migration/F45 loss checks, prompt/review-premise boundaries and exact-head assurance. Exact PR-head run #588 / `37386628173` passed on `91a07581a2bfeabf5b7c0fb410c4803d0afa5774`; PR #301 merged at `main@b8fcc66a5ad79ce0ba7ca77634a9aec2b0fba9c1`; exact post-merge run #589 / `37386694928` passed. Terminal Result Review accepts ADR-0001 / `artifact:ENG-A-0031` as an engineering architecture baseline while leaving the accepted Requirement baseline unchanged. F10 and F17/#225 remain explicit residual boundaries; no successor work is generated automatically.
