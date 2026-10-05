# Current engineering architecture and admitted change

## Current accepted baseline

The repository's accepted engineering baseline remains the existing governing objective, guardrails, methodology and accepted cross-project decisions. `DECISIONS.md` remains the accepted rationale owner. Git remains the byte/provenance history. The SD-KA-01 target is not silently promoted into this baseline by admission, implementation activity, recency or CI.

## Admitted change

`SD-KA-01` is an admitted bounded implementation programme for the Engineering Knowledge & Configuration Plane and Development Readiness operationalization. Its admission is recorded at:

`requirements/system-development-bugwave-d016-owner-admission-2026-10-04.md`

WP1 established and verified the in-place engineering semantic/catalog foundation. WP2 implemented and exactly post-merge verified accepted-baseline/current-change semantics, rebuildable current/query views and applicability-provenance primitives. WP3 implemented and exactly post-merge verified role/task-derived Human/Developer/Agent contexts, Senior Developer bootstrap, the shared deterministic full-check entrypoint, bounded prompt create/review/test behavior and review-evidence-basis safeguards. No work package is currently executing; #259/WP4 is the next eligible bounded package and is not started by this return. Existing `requirements/` content remains in place; physical migration is still the later WP5 activity after the earlier fitness prerequisite.

The executable current-state surface is derived from `engineering/configuration.json`, `engineering/changes/SD-KA-01/STATE.json` and the managed catalogs. `tools/engineering_context.py` builds role/task context views from those owners; `tools/prompt.py` implements the admitted bounded prompt interaction contract; `tools/check.py` is shared by local developer use and CI. None chooses accepted architecture by newest file, newest Git commit, Issue/PR state or CI success.

The canonical configuration deliberately records no current implementation focus between work packages. The change-state/result/relations surface records #259/WP4 as ready-next. Human-facing context resolves that unique next transition into a meaningful action/scope statement; if multiple candidates later exist, ambiguity remains explicit rather than being collapsed into one repository-global cursor.

## Boundaries

- scholarly Project/Corpus truth remains with its existing owners;
- Issues and PRs are work/review metadata, not accepted configuration authority;
- implemented engineering capability does not by itself promote the full admitted SD-KA-01 target into accepted architecture baseline;
- current/query/context views are derived and rebuildable and do not become a parallel state/priority store;
- prompt construction is not task execution or authority and does not become a planner/context owner;
- fresh context/model identity does not establish evidential independence; consequential review must state the evidence basis actually inspected;
- explicit absence or ambiguity of active/scoped work is valid and must not manufacture replacement work;
- technical validation is scoped assurance, not scholarly, specialist, evidential-independence or Human acceptance.
