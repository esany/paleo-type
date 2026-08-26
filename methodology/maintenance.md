# Maintenance and documentation ownership

## Purpose

Keep `paleo-type` continuously usable without creating a second documentation project. Maintenance is event-driven: update the canonical record that owns a changed truth, propagate only material consequences, then return to research.

## One fact, one canonical home

| Information | Canonical home | Role |
|---|---|---|
| highest-order scholarly purpose, precedence and human material-change authority | `GOVERNING_OBJECTIVE.md` | repository constitution / mission boundary |
| repository purpose/map/required reading path | `README.md` | entry point |
| mandatory AI/research guardrails | `AGENTS.md` | binding rules |
| shared architectural/methodological rationale | `DECISIONS.md` | lean cross-project decision record |
| GitHub Milestone-family/naming/backlog semantics | `MILESTONES.md` | planning/navigation rules only |
| authoritative end-to-end scholarly method | `methodology/historical-source-workflow.md` | reusable normative method |
| generic scholarly maturity gates | `methodology/research-gates.md` | reusable G1–G6 requirements |
| project/source-group lifecycle and feedback | `methodology/project-lifecycle.md` | reusable project rules |
| source identity/instantiation/preservation method | `methodology/source-and-provenance.md` | reusable source rules |
| minimal new-project contract | `templates/project/` | project creation template |
| archival/source record identity and inspection stage | `corpus/sources.tsv` | canonical source inventory |
| exact export/file identity, checksum, coverage, preservation path/state, rights | `corpus/files.tsv` | canonical file manifest |
| reusable source-wide image/PDF/export/folio mapping | `corpus/source-data/<source_id>/` | source-level canonical mapping |
| historical/archival/textual source relations | `corpus/relationships.tsv` | relationship claims + evidence status |
| administrative/historical event context | `corpus/events.tsv` | contextual event/activity registry |
| recurring normalized identities | `entities/*.tsv` | corpus-level normalized identities |
| project identity/research object/stable scope | `projects/<id>/project.yml` | investigation identity |
| project source group, roles and relevant loci | `projects/<id>/sources/sources.tsv` | human-readable project source basis |
| project-specific inspection audit | `projects/<id>/sources/inspection-log.tsv` | inspected-vs-metadata trace |
| current project gate/evidence/preservation gaps and exact next action | `projects/<id>/STATUS.md` | restart point |
| scoped transcription/decisions/analysis | owning project directories | project research truth |
| substantive source/reading decisions | project `apparatus/decisions.tsv` | revision trail |
| external literature/source inspection audit | project `research/` | checked-vs-lead distinction |
| source/hand-specific comparisons | project `palaeography/` | empirical comparison evidence |
| project-specific failures/lessons | project `LEARNINGS.md` | learning record |
| research-organisational relations between genuine projects | `projects/relationships.tsv` | optional project dependency/navigation |
| deferred/discrete tracked work | GitHub Issues | work package/backlog, never current research truth |
| end-user explanation | GitHub Wiki | handbook only |
| exploratory reasoning | chat | transient workspace only |

Explanations and GitHub metadata may summarize canonical records but must not become parallel truth stores.

## Governing-objective change control

`GOVERNING_OBJECTIVE.md` is not ordinary maintenance. A material change to its purpose, precedence or governing invariants is a special governance event and requires an explicit human owner decision.

- AI/collaborators may analyse or propose an amendment, but must not autonomously weaken, replace or supersede the objective.
- A material amendment must be isolated in a visible, cohesive PR with rationale and consequences; it must not arrive as incidental cleanup or automatic propagation.
- Routine synchronization/refactor machinery must never rewrite the governing objective merely because lower-level method, standards, models or architecture changed.
- Clarifying references in lower-level files should point to the canonical objective rather than copy it.
- Ordinary source research and maintenance remain lean and do not inherit mission-change ceremony.

## Method / corpus / project ownership test

Before creating/updating durable state ask:

1. Would the statement remain a valid rule for another comparable manuscript investigation? → METHOD.
2. Does it identify an archival record, exact export, reusable source-wide mapping, source relationship, event or normalized entity? → CORPUS / `entities/`.
3. Does it say why/how a source is used in one investigation, what locus matters, what was read/decided, or what remains open? → PROJECT.
4. Does it describe a relation between two genuine investigations? → `projects/relationships.tsv`.

A pilot may reveal a generic weakness, but project evidence becomes method only after an explicit generalisability check.

## Project lifecycle

Follow `methodology/project-lifecycle.md` for every project creation or material project-structure change.

Key invariants:

- a project is a bounded historical investigation / source-unlocking undertaking;
- a source record, archive section or PDF does not automatically become a project;
- a project has an explicit source group in `sources/sources.tsv`;
- separately identified archival records remain separate source rows even when they share volume/signature;
- project role/locus is not source identity;
- reusable source-wide crosswalks live once in `corpus/source-data/<source_id>/`;
- project relations are only between genuine investigations;
- do not create empty future-proof directories.

### New-project creation check

Before accepting a new project verify:

1. project ID/title identify an investigation, not a source/file surrogate;
2. research object and active scope are bounded and human-readable;
3. `sources/sources.tsv` exists and lists the actual source group;
4. every source ID resolves to `corpus/sources.tsv`;
5. distinct archival records/sections remain distinct rows;
6. every exact evidence export resolves to `corpus/files.tsv` with SHA-256 and preservation state;
7. central original exports have an intended/actual repository path or explicit preservation blocker;
8. project-relevant locus is separated from full archival source extent;
9. generic gates/method are referenced rather than copied;
10. reusable crosswalks have one canonical corpus source-data owner;
11. historical/source claims remain in `corpus/relationships.tsv`;
12. project relations are used only when another genuine project exists;
13. another capable researcher can restart without chat.

If the same machine-checkable creation failure recurs, consider the smallest validation that catches it; do not automate pre-emptively.

## Exact source-export preservation

The exact original export used for consequential research is part of the evidence chain.

Maintenance must distinguish:

- `repo-preserved` — exact original bytes are stored at the declared repository path;
- `external-controlled` — exact bytes exist in a controlled external location that is durably identified/recoverable;
- `preservation-blocked-rights` — repository preservation is desired but public upload lacks an adequate rights/authority basis;
- other states only when their meaning is documented.

A URL/URN + checksum is provenance, not equivalent backup. Never claim repository preservation when the binary is absent.

When a rights/authority fact changes, update `corpus/files.tsv` and perform the smallest resulting preservation action. The user owns rights/authority facts that cannot otherwise be verified; the assistant owns repository synchronization once authority is established.

## Feedback loops

### Project discovers a source-level correction

`project evidence → verify → update canonical corpus owner → update only affected project source register/status/work products → bounded consistency pass`

Examples: wrong source title, file checksum/path, folio/export mapping or source relationship.

### Project source role/locus changes

Update `projects/<id>/sources/sources.tsv`. Do not modify canonical source identity merely because a source changes from context to comparison, or because a narrower locus becomes relevant.

### Project discovers generic methodological weakness

`project observation → project LEARNING/status → explicit generalisability check → methodology/DECISIONS update → bounded consistency pass`

## Required reading paths

### Human

Read `README.md` first. Read `GOVERNING_OBJECTIVE.md` when evaluating repository purpose, precedence, Human-in-the-loop or consequential method/architecture change. For one investigation read its `STATUS.md` and `sources/sources.tsv`. Read `methodology/project-lifecycle.md` for project/source-group semantics, `methodology/source-and-provenance.md` for exact source/export preservation, and `MILESTONES.md` when interpreting scheduled Issues/Milestones.

### AI continuing research

1. read `GOVERNING_OBJECTIVE.md` and `AGENTS.md`;
2. establish and load all canonical rules/requirements applicable to the concrete task;
3. read `README.md` if repository structure is not already established;
4. read project `STATUS.md`;
5. read project `sources/sources.tsv`;
6. read the active generic gate in `methodology/research-gates.md`;
7. inspect relevant `corpus/sources.tsv`, `corpus/files.tsv`, `corpus/source-data/` and `corpus/relationships.tsv`;
8. read additional task-relevant methodology from its canonical owner;
9. continue from `NEXT ACTION` unless inspected evidence requires a change.

## GitHub-native human navigation

GitHub metadata is a navigation/planning layer over canonical records, never a competing truth store.

### Milestones

Follow `MILESTONES.md`.

Use Milestones for targets/work phases, with explicit families:

- `GOV-*` — repository governance/architecture/structural-review work;
- `<project> / G*` — project-specific scholarly Issues contributing to generic G1–G6 gates.

A project G1–G6 Milestone is a work-planning mirror, not the scholarly gate claim. Generic requirements remain in `research-gates.md`; actual project gate state remains in `STATUS.md`.

Milestone progress/completion does not establish gate attainment. Update `STATUS.md` first when evidence changes gate state, then adjust Issue/Milestone planning if useful. No calendar due dates without real deadlines; no fragmentation for progress percentages; do not pre-create all project gate Milestones merely for completeness.

### Issues and labels

Issues preserve bounded future work or useful discrete work packages. Labels classify them for filtering only.

- do not encode canonical research status, confidence or source identity in labels;
- for cross-disciplinary Issues, use multiple labels and one primary target Milestone;
- assign a scholarly Issue to a project gate Milestone only when completing it materially contributes to that gate and issue tracking adds value;
- trigger-based future infrastructure normally stays without a Milestone until triggered/scheduled;
- do not create Issues for every line reading or routine source action.

**No-dead-issue rule:** every deferred issue must contain research benefit/problem, why it is not current work, an observable trigger, and definition of done/acceptance criteria.

**Trigger audit:** re-check relevant deferred issues on a bounded consistency pass, project gate change, publication/export start, or evidence that a trigger fired. Outcome: leave deferred, schedule with evidence, keep triggered-but-unscheduled with reason, close completed, or close superseded/duplicate.

### Pull requests

Small/local research or maintenance changes may commit directly to `main`; cohesive repository-wide method/schema/provenance/structural changes preferably use branch + PR. PRs state problem, material changes, deliberate non-changes and research-state impact. PRs do not replace `DECISIONS.md`.

A material change to `GOVERNING_OBJECTIVE.md` is always a dedicated/cohesive governance PR and requires explicit human owner approval before merge.

### Tags/releases

Use only for intentionally frozen reproducible research/publication checkpoints.

Do not introduce Projects/Kanban or Discussions without observed need. Governance protections such as CODEOWNERS/rulesets require a concrete protection requirement.

## Maintenance triggers

- governing-objective clarification/change proposal → treat as special governance event; never auto-propagate a material mission change;
- source identity/stage change → update `corpus/sources.tsv`, then affected project references only;
- exact export/checksum/coverage/storage/rights change → update `corpus/files.tsv`, then preservation/project consequences;
- reusable source-wide crosswalk change → update `corpus/source-data/<source_id>/`, then affected project references/transcription addresses;
- project source-group role/locus change → update project `sources/sources.tsv` and affected `STATUS.md`/work products;
- source relationship change → update `corpus/relationships.tsv` with evidence status;
- project relation change → update `projects/relationships.tsv` only when both endpoints are genuine projects;
- project creation/scope change → run the project creation check;
- transcription change → update transcription, consequential decision/palaeography and status as applicable;
- external source/literature inspected → update project research audit at actual access level;
- project lesson → keep concrete incident in project; generalise only after explicit review;
- generic method/gate/lifecycle change → update owning methodology/decision and run bounded consistency pass;
- active gate/task changes → update `STATUS.md` first and trigger issue audit.

## Bounded repo-wide consistency pass

Run after material canonical changes such as source-ID/provenance correction, file-manifest/preservation change, source/project relation change, crosswalk ownership migration, project model change, generic method/gate/lifecycle change or repository restructuring.

1. state changed canonical truths/owners;
2. check `corpus/sources.tsv` ↔ `corpus/files.tsv` ↔ `corpus/source-data/` referential integrity;
3. check each project `sources/sources.tsv` against canonical source/file IDs;
4. verify separately identified archival records have not been collapsed by shared signature/title shorthand;
5. check project `project.yml`/`STATUS.md` for stale scope/path/next-step claims;
6. search for source-as-project leftovers, duplicate crosswalks, stale identifiers and old generic-rule copies;
7. verify `projects/relationships.tsv` contains only genuine project-to-project relations;
8. verify central source-export preservation claims match actual file state and rights constraints;
9. audit relevant deferred Issues against triggers/Milestone targets;
10. apply the fachlich-technisches quality gate from `AGENTS.md`;
11. verify restartability;
12. stop when coherent and return to research.

Do not use a consistency pass to invent architecture or re-adjudicate manuscript readings unless a genuine research problem is exposed.

## README, Wiki, Issues, Milestones and chat

- **GOVERNING_OBJECTIVE** — highest-order purpose/precedence/change authority, not an operational handbook.
- **README** — orientation/map, not detailed status.
- **Wiki** — human-facing handbook, never canonical research truth.
- **Issues** — discrete/deferred work, not research truth.
- **Milestones** — target/phase navigation for admitted Issues; not evidence/gate truth.
- **Chat** — transient workspace; durable continuation state must be persisted.

## Human–AI maintenance responsibility

### AI

Own routine repository/corpus/project hygiene, propagation of changed truths, source/file/project referential integrity, issue-trigger audit, Milestone-assignment consistency and restartability. Surface missing metadata/preservation blockers rather than inventing them.

### User

Own research purpose, source access only they can provide, rights/authority facts not otherwise verifiable, desired depth and consequential publication/use decisions. The user is not the repository synchronizer or default specialist adjudicator. Material change to the governing objective requires the user's explicit decision.

### Qualified expert

Escalation/review role when consequence/uncertainty warrants independent specialist judgment.

## End-of-work integrity check

Before completing consequential work ask:

1. What research/method truth changed and who owns it?
2. Is canonical source/file/crosswalk truth in CORPUS rather than copied into projects?
3. Does each project still represent a real investigation rather than a source/file wrapper?
4. Are distinct archival records preserved separately even when they share a volume/signature?
5. Does project `sources/sources.tsv` expose role/locus/file clearly to a human?
6. Are central original exports actually preserved as claimed, with rights blockers explicit?
7. Are project relations distinct from source relations?
8. Did project gate/next-action state change?
9. Did a project learning justify generalisation?
10. Did any deferred Issue trigger fire or become obsolete?
11. Is a bounded consistency pass required?
12. Can another capable researcher identify the investigation, source group, exact exports/preservation state and continue without chat?

If 12 is no, persist the minimum missing state.

## Lean maintenance rule

`Maintain on change; project = investigation; source = source; exact export = evidence asset; one fact, one owner; reference rather than copy; propagate only material consequences; then stop.`
