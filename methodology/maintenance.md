# Maintenance and documentation ownership

## Purpose

Keep `paleo-type` continuously usable without creating a second documentation project. Maintenance is event-driven: when research or method changes, update the canonical record that owns that information, propagate only material consequences, then return to research.

## One fact, one canonical home

| Information | Canonical home | Role |
|---|---|---|
| repository purpose/map/required reading path | `README.md` | entry point |
| mandatory AI/research guardrails | `AGENTS.md` | binding rules |
| shared architectural/methodological rationale | `DECISIONS.md` | lean cross-project decision record |
| GitHub Milestone-family/naming/backlog semantics | `MILESTONES.md` | planning/navigation rules only |
| authoritative end-to-end scholarly method | `methodology/historical-source-workflow.md` | reusable normative method |
| generic scholarly maturity gates | `methodology/research-gates.md` | reusable G1–G6 requirements |
| project creation/kinds/relations/feedback | `methodology/project-lifecycle.md` | reusable project lifecycle rules |
| minimal new-project contract | `templates/project/` | project creation template |
| corpus source identity and inspection stage | `corpus/sources.tsv` | corpus inventory |
| external/digital source file or instantiation identity/checksum/coverage/storage/rights | `corpus/files.tsv` | canonical file/instantiation manifest |
| historical/archival/textual source relations | `corpus/relationships.tsv` | relationship claims + evidence status |
| administrative/historical event context | `corpus/events.tsv` | contextual event/activity registry |
| recurring normalized identities | `entities/*.tsv` | corpus-level normalized identities |
| research-organisational project relations | `projects/relationships.tsv` | project-to-project use/dependency only |
| project identity/kind/stable scope | `projects/<id>/project.yml` | project identity |
| current project gate state, source-specific gaps and exact next action | `projects/<id>/STATUS.md` | restart point |
| reusable source-local image/folio/export mapping | owning `source-unit` project's `sources/` | source-local canonical mapping |
| scoped transcription/decisions/analysis | owning research project directories | scoped research truth |
| substantive source/reading decisions | project `apparatus/decisions.tsv` | revision trail |
| external literature/source inspection audit | project `research/` | checked-vs-lead distinction |
| source/hand-specific comparisons | project `palaeography/` | empirical comparison evidence |
| project-specific failures/lessons | project `LEARNINGS.md` | learning record |
| deferred/discrete tracked work | GitHub Issues | work package/backlog, never current research truth |
| end-user explanation | GitHub Wiki | handbook only |
| exploratory reasoning | chat | transient workspace only |

Projects do **not** own copies of generic gate requirements. Consumer projects do **not** own copies of reusable source-unit mappings. Explanations and GitHub metadata may mirror/summarize canonical records, but they must not become parallel truth stores.

## Method / corpus / project ownership test

Before creating/updating a durable record ask:
1. Would the statement remain a valid rule for another comparable manuscript project? → METHOD (`methodology/`, `AGENTS.md`, `DECISIONS.md`).
2. Does it concern historical/source identity, source relationships, shared events or normalized entities? → CORPUS / `entities/`.
3. Does it concern how our research projects relate organizationally? → `projects/relationships.tsv`.
4. Does it concern what was found, read, decided or remains open in one concrete project? → `projects/<id>/`.

A pilot may reveal a generic weakness, but project evidence becomes method only after an explicit generalisability check.

## Project lifecycle

Follow `methodology/project-lifecycle.md` for every project creation or material project-structure change.

Key invariants:
- a corpus source is not automatically a project;
- create projects from `templates/project/`, never by cloning a concrete project;
- supported project kinds are `source-unit` and `research-scope` until an observed need justifies another;
- source-unit projects own reusable source-local mappings;
- research-scope projects reference source-unit mappings rather than copying them;
- project relations never stand in for historical/source relations;
- do not create empty future-proof directories;
- dormant source-unit projects may state `not yet activated` without becoming backlog debt.

### New-project creation check

Before accepting a new project verify:
1. project ID is unique and project kind is explicit/valid;
2. canonical source ID exists where applicable;
3. exact digital binaries used as evidence are registered in `corpus/files.tsv`;
4. project scope is bounded and does not imply unsupported completeness;
5. `STATUS.md` states actual inspection/evidence state;
6. generic gates/method are referenced rather than copied;
7. reusable source-local mapping has exactly one canonical owner;
8. material project-to-project use is recorded in `projects/relationships.tsv`;
9. historical/source claims remain in `corpus/relationships.tsv`;
10. another capable researcher can restart without chat.

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
Read `README.md` first. For one project, read its `STATUS.md`; generic maturity requirements live in `methodology/research-gates.md`. Read `methodology/project-lifecycle.md` for project kinds/relations and `MILESTONES.md` when interpreting scheduled Issues/Milestones.

### AI continuing research
1. read `README.md` if repository structure is not already established;
2. read `AGENTS.md`;
3. read project `STATUS.md`;
4. read the active generic gate in `methodology/research-gates.md`;
5. inspect relevant corpus records and `projects/relationships.tsv` when source/project identity or relations matter;
6. inspect owning source-unit mapping when a research-scope depends on it;
7. read only methodology needed for the task;
8. continue from `NEXT ACTION` unless inspected evidence requires a change.

## GitHub-native human navigation

GitHub metadata is a navigation/planning layer over canonical records, never a competing truth store.

### Milestones

Follow `MILESTONES.md`.

Use Milestones for **targets/work phases**, with explicit families:
- `GOV-*` — repository governance/architecture/structural-review work;
- `<project> / G*` — project-specific scholarly Issues contributing to generic G1–G6 gates.

A project G1–G6 Milestone is permitted as a **work-planning mirror**, not as the scholarly gate claim. Generic requirements remain in `research-gates.md`; actual project gate state remains in `STATUS.md`.

Therefore:
- Milestone progress/completion does not establish gate attainment;
- update `STATUS.md` first when evidence changes gate state;
- then adjust Issue/Milestone planning if useful;
- no calendar due dates without real deadlines;
- no fragmentation for progress percentages;
- no need to create all project gate Milestones in advance.

An open Issue with a Milestone is scheduled/admitted work. An open Issue without a Milestone is backlog/deferred. This does **not** require every current research action to become an Issue.

### Issues and labels

Issues preserve bounded future work or genuinely useful discrete work packages. Labels classify them for filtering only.

- use a small topic/domain vocabulary derived from actual Issues;
- do not encode canonical research status, confidence or source identity in labels;
- for cross-disciplinary Issues, use multiple labels while assigning one primary target Milestone;
- assign a scholarly Issue to a project gate Milestone only when completing it materially contributes to that gate and issue tracking adds value;
- trigger-based future infrastructure normally stays without a Milestone until the trigger fires or a governing decision schedules it;
- do not create Issues for every line reading or routine source action.

**No-dead-issue rule:** every deferred issue must contain (a) research benefit/problem, (b) why it is not current work, (c) an observable trigger, and (d) definition of done/acceptance criteria. It is not a roadmap promise.

**Trigger audit:** do not create calendar-based backlog grooming. Re-check open deferred issues whenever a bounded repo-wide consistency pass runs, a project changes gate, publication/export work begins, or evidence suggests an issue trigger fired. For each relevant issue choose exactly one outcome:
1. trigger not met → leave open in backlog without starting work;
2. trigger met and scheduled → update scope/evidence and assign to the appropriate Milestone family;
3. trigger met but not yet scheduled → keep open without Milestone and make the reason visible if consequential;
4. already implemented/absorbed → close `completed`;
5. superseded/irrelevant → close `not_planned` or `duplicate` with rationale.

Remove obsolete body hashtags once equivalent GitHub labels exist. Do not keep issues open merely as memory; durable methodological truth belongs in the repository.

### Pull requests
Small/local research or maintenance change may commit directly to `main`; cohesive repository-wide method/schema/provenance/structural change preferably uses branch + PR. PR descriptions state problem, material changes, deliberate non-changes and research-state impact. PRs do not replace `DECISIONS.md`.

### Tags/releases
Use only for intentionally frozen, reproducible research/publication checkpoints. Do not release ordinary development increments. G5/G6 are natural candidates; earlier gates only when independently useful.

Do not introduce Projects/Kanban or Discussions without an observed need. Governance protections such as CODEOWNERS/rulesets may be introduced only when their concrete protection requirement is established.

## Maintenance triggers

### Source identity/stage/file/relation changes
Update the corresponding canonical corpus/source-unit owner, then affected project status/reference only when project consequence changes.

### Project relation changes
Update `projects/relationships.tsv`; review only directly affected project statuses/references.

### Project creation/kind/scope changes
Run the new-project creation check and verify source-unit/research-scope ownership boundaries.

### Transcription changes
Update project transcription; log consequential replacements/rejections; update palaeographic evidence and `STATUS.md` when active uncertainty/next action changes.

### External source/literature inspected
Update project research audit with actual access level/passages.

### Project lesson learned
Record the concrete failure/correction in `LEARNINGS.md`. Promote only a genuinely general safeguard into methodology.

### Generic method/gate/lifecycle changes
Update the owning methodology file; record durable cross-project rationale in `DECISIONS.md` when needed; then run a bounded repo-wide consistency pass. Re-check project-gate Milestone descriptions/assignments only if the changed gate materially affects planned Issues; do not copy generic requirements into GitHub.

### Active task/gate state changes
Update project `STATUS.md` first; then review whether scheduled scholarly Issues still target the correct project gate Milestone. This also triggers an issue-trigger audit.

### Governance/architecture phase changes
Update the appropriate `GOV-*` Issue/Milestone planning state. Do not infer or modify project scholarly gate state unless research evidence itself changed.

## Bounded repo-wide consistency pass

Run after material canonical changes such as source-ID migration, provenance correction, file-manifest change, source/project relationship change, project-ownership migration, generic gate/method/lifecycle change or repository restructuring.

Start from changed canonical truths:
1. state changed truths/identifiers/owners;
2. check corpus and `projects/relationships.tsv` referential integrity;
3. check source-unit mappings and consuming research-scope references;
4. check project `project.yml`/`STATUS.md` for obsolete scope/kind/path/next-step wording;
5. search for duplicate crosswalks, stale identifiers, old generic-rule copies and contradictory relations;
6. audit relevant open Issues against triggers and check Milestone family/target consistency;
7. apply the fachlich-technisches quality gate from `AGENTS.md`;
8. verify restartability;
9. stop when coherent and return to research.

Do not use a consistency pass to invent new architecture or re-adjudicate manuscript readings unless a genuine research problem is exposed.

## README, Wiki, Issues, Milestones and chat

- **README** — orientation/map, not detailed status.
- **Wiki** — human-facing handbook, never canonical research truth.
- **Issues** — discrete/deferred work, not research truth.
- **Milestones** — target/phase navigation for admitted Issues; not evidence/gate truth.
- **Chat** — transient workspace; durable continuation state must be persisted.

## Human–AI maintenance responsibility

### AI
Own routine repository/corpus/project hygiene, propagation of changed truths, project/source relation integrity, issue-trigger audit, Milestone-assignment consistency and restartability. Surface missing metadata rather than inventing it.

### User
Own research purpose, source access only they can provide, rights/authority facts not otherwise verifiable, desired depth and consequential publication/use decisions. The user is not the repository synchronizer or default specialist adjudicator.

### Qualified expert
Escalation/review role when consequence/uncertainty warrants independent specialist judgment.

## End-of-work integrity check

Before completing consequential work ask:
1. What research/method truth changed and who owns it?
2. Is source-level truth in corpus/source-unit rather than a consumer research-scope project?
3. Are project relations distinct from historical/source relations?
4. Did a project structure change pass project-lifecycle invariants?
5. Did the change require propagation through `projects/relationships.tsv`?
6. Did a generic method change leak source-specific facts into methodology or duplicate generic requirements inside a project?
7. Did project gate state/next action change?
8. If Issue-tracked work changed, is its target Milestone family/assignment still correct without being mistaken for scholarly state?
9. Did a project failure create a generalisable learning?
10. Did a deferred issue trigger fire, become obsolete, or get implemented elsewhere?
11. Is a bounded consistency pass required?
12. Can another capable researcher identify source/project ownership and continue without chat?

If 12 is no, persist the minimum missing state.

## Lean maintenance rule

`Maintain on change; one fact, one owner; reference rather than copy; keep GitHub planning metadata subordinate to canonical research state; propagate through explicit relations; then stop.`
