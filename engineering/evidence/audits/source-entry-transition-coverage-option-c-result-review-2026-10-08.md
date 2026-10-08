# Option C result review — source-entry transition and granular coverage

**Date:** 2026-10-08  
**Engineering artifact:** `artifact:ENG-A-0121`  
**Admission:** `artifact:ENG-A-0120`  
**Concept:** `artifact:ENG-A-0119`  
**Implementation assurance basis:** PR #311 implementation head `192a70eff2d7b5e07069ec8bbb6f00466144f6a6`; GitHub Actions run `37772371547`, validate job `113294825472`

## Result

**Bounded technical implementation:** PASS at the implementation head stated above.  
**Shared deterministic full check:** PASS.  
**Human-readable assurance-boundary step:** PASS.  
**Scholarly/domain validation:** NOT ESTABLISHED by deterministic tests.  
**Real Corpus-only Generic-Fit:** OPEN.  
**Real Nr. 632 positive coverage:** OPEN and belongs to the established-Project / large-composite side after concrete canonical materialization and actual image inspection.

The historical recovered local `66 tests PASS` result is not used as current assurance.

## Currentness corrections applied during reconstruction

The recovered local prototype was not promoted verbatim.

1. The old `requirements/` location was retired because current shared repository architecture narrows that namespace to the accepted reusable Requirement baseline. Concept/admission/result-review evidence now uses the current engineering evidence/catalog surfaces.
2. Nr. 632 is not used as a real `CORPUS_ONLY / NO_PROJECT_YET` acceptance fixture.
3. The stale “rights unknown blocks File materialization by itself” premise is not carried forward.
4. The mutable route `current=yes/no` flag was removed. Current route is derived from the greatest contiguous `transition_sequence`, preserving append-only route history.
5. Every durable coverage row now carries an exact `route_id`. Missing routes and unresolved/candidate routes fail closed, addressing the demonstrated #309 omitted-route case.
6. The source-entry owner explicitly excludes Project scholarly scope, gate and `NEXT ACTION` state and documents the boundary against becoming a parallel Project research-truth store.

## Wirknetz / loss review

| Concern | Result | Claim ceiling |
|---|---|---|
| #309 transition completeness | **technical PASS** | durable coverage without an explicit resolved route fails; no Project is auto-created |
| #267 pre-Project owner | **representation/contract PASS** | synthetic Corpus-only behavior passes; real legitimate Corpus-only Generic-Fit remains open |
| append-only routing | **PASS for snapshot structure / write discipline defined** | sequence continuity/current-route derivation are deterministic; a single snapshot does not prove that historical Git rows were never rewritten |
| later Project transition | **PASS** | earlier coverage keeps its original route reference; later Project-bound coverage uses the matching existing-Project route |
| #265 scope boundary | **PASS for non-ownership** | forbidden scope/gate/`NEXT ACTION` columns fail; no #265 representation was added |
| Source/File identity | **preserved by reference** | source-entry does not own or duplicate Source/File identity |
| locator separation | **preserved structurally by contract/fixtures** | `locator_domain` and `coverage_locus` remain separate; correctness of the chosen domain and any crosswalk remain evidence responsibilities |
| evidence/claim axes | **PASS in deterministic loss checks** | `H + OBSERVATION` and `NOT_INSPECTED + P` are rejected |
| Reg. Ii precedent | **loss-check only** | legacy Source/locus/evidence/support/limitation meanings are explicitly mapped in tests where a canonical Source ID exists; no rows are migrated or copied |
| Nr. 632 | **no fabricated state** | route and coverage tables remain header-only |
| Project research truth | **boundary documented** | mature Project-specific reading/interpretation remains with its natural Project owner |

## Deliberate non-changes

This implementation does not:

- create or materialize the Nr. 632 Project, Source or File rows;
- choose active scholarly scope;
- record any Nr. 632 manuscript observation;
- migrate Reg. Ii inspection logs;
- alter File/package/rights semantics;
- add a workflow engine, planner, event store, graph runtime or page tracker;
- activate #266, #268 or #269;
- claim scholarly/specialist/Human acceptance from CI.

## Remaining acceptance / falsification

The technical owner is not fully real-use accepted until at least:

1. a genuinely legitimate real `CORPUS_ONLY / NO_PROJECT_YET` source-entry case demonstrates that the owner is adequate without Project creation; and
2. real Nr. 632 source-entry coverage, after concrete canonical Project recovery and target-context image inspectability, tests the established-Project / large-composite path.

Any new material semantic or architecture requirement exposed there returns to D-016 if it falls outside `artifact:ENG-A-0120`.

## P0 false-Lean / completeness re-review

After the Human Owner escalated #297 to maximum priority, this PR was re-reviewed against the complete admitted Option C outcome rather than accepted from the earlier local technical PASS alone.

That review found **assurance-coverage gaps, not a need to shrink or expand the admitted architecture**: several stated acceptance properties were present in code/prose but not discriminated explicitly enough by tests, and the earlier result wording overstated what snapshot validation proves about append-only Git history.

The PR therefore now adds explicit checks for:

- `NOT_INSPECTED + P` rejection;
- every forbidden Project-state header (`active_scope`, `gate`, `next_action`, `scholarly_scope`);
- structural separation of provider-image / PDF-page / archival-folio locator domains without inventing a crosswalk;
- a simple-source no-state path so Source existence alone does not create route/coverage bureaucracy;
- a real Reg.-Ii. semantic loss mapping rather than a tautological string-presence test.

The result-review claim is correspondingly narrowed: append-only history is an admitted canonical write discipline with deterministic sequence/reference checks, **not** mechanically certified immutability of prior Git rows by a single-snapshot validator.

This is a completion/assurance repair inside ENG-A-0120, not a new semantic owner, Project rule or D-016 expansion. Merge still requires a fresh exact-final-head shared CI PASS after these P0 corrections.

## Final PR-head assurance boundary

This review is itself a repository mutation after the implementation-head run above. Therefore merge requires a fresh shared deterministic full check on the final PR head. The exact final-head run is GitHub/PR assurance metadata; it must not be backfilled into this file by a self-referential documentation loop.
