# Maintenance and documentation ownership

## Purpose

Keep `paleo-type` continuously usable without creating a second documentation project. Maintenance is event-driven: update the canonical owner when research/method truth changes, propagate only material consequences, then return to research.

## One fact, one canonical home

| Information | Canonical home |
|---|---|
| repository purpose/map | `README.md` |
| mandatory guardrails | `AGENTS.md` |
| durable cross-project rationale | `DECISIONS.md` |
| end-to-end scholarly method | `methodology/historical-source-workflow.md` |
| generic G1–G6 gates | `methodology/research-gates.md` |
| project creation/kinds/relations/feedback | `methodology/project-lifecycle.md` |
| minimal new-project contract | `templates/project/` |
| source identity/stage | `corpus/sources.tsv` |
| exact digital/external file identity/checksum/coverage/rights | `corpus/files.tsv` |
| historical/archival/textual source relations | `corpus/relationships.tsv` |
| shared events/context | `corpus/events.tsv` |
| normalized recurring identities | `entities/` |
| research-organisational project relations | `projects/relationships.tsv` |
| project identity/kind/scope | `projects/<id>/project.yml` |
| project evidence/gate/activity/next action | `projects/<id>/STATUS.md` |
| reusable source-local mapping | owning `source-unit` project's `sources/` |
| scoped transcription/decisions/analysis | owning research project directories |
| deferred improvements | GitHub Issues |
| exploratory reasoning | chat only |

Explanations may summarize canonical records but must not become parallel truth stores.

## Method / corpus / project ownership test

1. reusable rule for another comparable manuscript → METHOD;
2. identity/relationship spanning historical sources/projects → CORPUS (or `projects/relationships.tsv` for research organisation only);
3. concrete observation/reading/decision/state → PROJECT.

A pilot reveals possible generic weaknesses; it does not define generic method automatically.

## Project lifecycle

Follow `methodology/project-lifecycle.md` for every project creation or structural change.

Key invariants:
- a source is not automatically a project;
- create projects from `templates/project/`, never by cloning a concrete project;
- supported kinds are `source-unit` and `research-scope` until an observed need justifies another;
- source-unit projects own reusable source-local crosswalks;
- research-scope projects reference those mappings instead of copying them;
- project relations never stand in for source relations;
- do not create empty future-proof directories;
- dormant source-unit projects may state `not yet activated` without becoming backlog debt.

### New-project creation check

Before accepting a new project verify:
1. unique project ID and explicit valid kind;
2. canonical source ID exists where applicable;
3. exact binaries used as evidence exist in `corpus/files.tsv`;
4. scope is bounded and does not imply unsupported completeness;
5. `STATUS.md` states actual inspection/evidence level;
6. generic gates/method are referenced rather than copied;
7. local source mapping has exactly one canonical owner;
8. material project-to-project use is in `projects/relationships.tsv`;
9. historical/source claims remain in `corpus/relationships.tsv`;
10. restartability passes without chat.

If the same machine-checkable creation failure recurs, consider activating schema validation under its existing trigger; do not automate pre-emptively.

## Feedback loops

### Research-scope discovers source-level correction
`project evidence → verify → update source-unit/corpus owner → follow projects/relationships.tsv → update only affected project consequences → bounded consistency pass`.

### Project discovers generic methodological weakness
`project observation → project learning/status → explicit generalisability check → methodology/DECISIONS update → bounded consistency pass`.

### Source-unit mapping changes
Update only the source-unit owner first, then related consumer projects whose state/reference actually changes. Never replicate the corrected mapping into every consumer.

## Required reading paths

### Human
Read `README.md`; for current work read project `STATUS.md`; for project structure/relations read `methodology/project-lifecycle.md`.

### AI continuing research
1. read `AGENTS.md`;
2. read project `STATUS.md`;
3. read active generic gate;
4. inspect relevant corpus records and `projects/relationships.tsv`;
5. read source-unit project/crosswalk when a research-scope depends on it;
6. read only relevant methodology;
7. continue from `NEXT ACTION` unless evidence requires a change.

## GitHub-native navigation

GitHub metadata is navigation, never canonical research truth.

### Milestones
May mirror generic G1–G6 names/purposes. Requirements remain in `research-gates.md`; project state remains in `STATUS.md`. No artificial due dates/progress percentages.

### Issues and labels
Issues preserve bounded future/discrete work. Labels classify only.

**No-dead-issue rule:** every deferred issue must contain research benefit/problem, why not now, observable trigger, and acceptance criteria.

**Trigger audit:** re-check relevant deferred issues on gate changes, bounded consistency passes, publication/export start, or evidence that a trigger fired. Outcome must be: leave deferred, activate with evidence, close completed, or close superseded/duplicate. No calendar grooming.

### Pull requests
Small local research/maintenance changes may commit directly to `main`; cohesive repository-wide method/schema/provenance/structural changes preferably use branch + PR. PRs explain problem, changes, deliberate non-changes and research-state impact.

### Tags/releases
Use only for intentionally frozen reproducible research/publication checkpoints.

Do not add Projects/Kanban, Discussions, CODEOWNERS or workflow bureaucracy without observed need.

## Maintenance triggers

- source identity/stage/file/relation change → update corpus owner, then affected project owners;
- project relation change → update `projects/relationships.tsv` and affected statuses only;
- project creation/kind/scope change → run project creation check;
- transcription change → update transcription, consequential decision/palaeography and status as applicable;
- external source/literature inspected → update research audit at actual access level;
- project lesson → keep concrete incident in project; generalise only after explicit review;
- generic method/gate/lifecycle change → update owning methodology/decision and run bounded consistency pass;
- active gate/task changes → update `STATUS.md` and trigger issue audit.

## Bounded repo-wide consistency pass

Run after material canonical changes such as source-ID/provenance correction, file-manifest change, source/project relation change, project-ownership migration, generic method/gate/lifecycle change or repository restructuring.

1. state changed canonical truths/owners;
2. check corpus and project-relation referential integrity;
3. check source-unit mappings and consuming research-scope references;
4. check project `project.yml`/`STATUS.md` for stale scope/kind/path/next-step claims;
5. search for duplicate crosswalks, stale identifiers, old generic-rule copies and contradictory relations;
6. audit relevant deferred Issues against triggers;
7. apply the fachlich-technisches quality gate from `AGENTS.md`;
8. verify restartability;
9. stop and return to research.

Do not use a consistency pass to invent architecture or re-adjudicate manuscript readings unless a genuine research problem is exposed.

## Human–AI responsibility

AI owns routine repository/corpus/project hygiene, propagation of changed truths, relationship integrity, issue-trigger audit and restartability. The user owns research purpose, source access only they can provide, rights/authority facts and consequential use/publication decisions. Qualified experts are escalation/review where consequence and uncertainty require it.

## End-of-work integrity check

Before completing consequential work ask:
1. what truth changed and who owns it?;
2. did source-level truth stay in corpus/source-unit rather than consumer projects?;
3. did project relations stay distinct from source relations?;
4. did a project structure change pass the project creation invariants?;
5. did a change require propagation through `projects/relationships.tsv`?;
6. did gate/next-action state change?;
7. did a project learning justify generalisation?;
8. did any deferred Issue trigger fire or become obsolete?;
9. is a bounded consistency pass required?;
10. can another capable researcher continue from repository + sources without chat?

If 10 is no, persist the minimum missing state.

## Lean maintenance rule

`Maintain on change; one fact, one owner; reference rather than copy; propagate through explicit relations; then stop.`
