# Maintenance and documentation ownership

## Purpose

Keep `paleo-type` continuously usable without creating a second documentation project. Maintenance is event-driven: when research or method changes, update the canonical record that owns that information. Do not create periodic process work merely to make the repository look maintained.

## One fact, one canonical home

| Information | Canonical home | Role |
|---|---|---|
| repository purpose/map/required reading path | `README.md` | entry point |
| mandatory AI/research guardrails | `AGENTS.md` | binding rules |
| shared architectural/methodological rationale | `DECISIONS.md` | lean cross-project decision record |
| authoritative end-to-end scholarly method | `methodology/historical-source-workflow.md` | reusable normative method |
| generic scholarly maturity gates | `methodology/research-gates.md` | reusable G1–G6 requirements |
| detailed generic method | `methodology/*.md` | reusable specialist rules |
| corpus source identity and inspection stage | `corpus/sources.tsv` | corpus inventory |
| external/digital source file or instantiation identity/checksum/coverage/storage/rights | `corpus/files.tsv` | canonical file/instantiation manifest |
| explicit source/event/entity relationships | `corpus/relationships.tsv` | relationship claims + evidence status |
| administrative/historical event context | `corpus/events.tsv` | contextual event/activity registry |
| recurring normalized identities | `entities/*.tsv` | corpus-level normalized identities |
| project identity/stable scope | `projects/<id>/project.yml` | project identity |
| current project gate state, source-specific gaps and exact next action | `projects/<id>/STATUS.md` | restart point |
| project-specific image/folio/export/source inspection detail | `projects/<id>/sources/` | local provenance/crosswalk |
| project transcription | `projects/<id>/transcription/` | transcription truth |
| substantive source/reading decisions | `projects/<id>/apparatus/decisions.tsv` | revision trail |
| external literature/source inspection audit | `projects/<id>/research/` | checked-vs-lead distinction |
| source/hand-specific comparisons | `projects/<id>/palaeography/` | empirical comparison evidence |
| project-specific failures/lessons | `projects/<id>/LEARNINGS.md` | learning record |
| deferred technical/methodological improvements | GitHub Issues | triggered backlog, never current research truth |
| end-user explanation | GitHub Wiki | handbook only |
| exploratory reasoning | chat | transient workspace only |

Projects do **not** own copies of generic gate requirements. Explanations may summarize canonical records, but they must not become parallel truth stores.

## Framework / corpus / project ownership test

Before creating/updating a durable record ask:

1. Would the statement remain a valid rule for another comparable manuscript project? → `methodology/` (or `AGENTS.md` / `DECISIONS.md`).
2. Does it concern identities/relationships spanning sources or projects? → `corpus/` / `entities/`.
3. Does it concern what was found, read, decided or remains open in one concrete project? → `projects/<id>/`.

A pilot may reveal a generic weakness, but project evidence becomes method only after an explicit generalisability check.

## Required reading paths

### Human
Read `README.md` first. For one project, read its `STATUS.md`; generic maturity requirements live in `methodology/research-gates.md`.

### AI continuing research
1. read `README.md` if repository structure is not already established;
2. read `AGENTS.md`;
3. read project `STATUS.md`;
4. read the active generic gate in `methodology/research-gates.md`;
5. inspect relevant `corpus/` records when source identity/files/relations matter;
6. read relevant project decisions/LEARNINGS and only the methodology needed for the task;
7. continue from `NEXT ACTION` unless inspected evidence requires a change.

## GitHub-native human navigation

GitHub metadata is a navigation layer over canonical records, never a competing truth store.

### Milestones
GitHub Milestones may mirror the generic G1–G6 gate names/purposes for human navigation when useful.
- Requirements/exit gates remain in `methodology/research-gates.md`.
- Project gate state remains in project `STATUS.md`.
- Do not duplicate full checklists in GitHub metadata.
- No calendar due dates unless the research genuinely has one.
- Do not fragment gates merely to produce progress percentages.

### Issues and labels
Issues preserve bounded future work or genuinely useful discrete work packages. Labels classify them for filtering only.
- use a small topic vocabulary derived from actual issues;
- do not encode canonical research status, confidence or source identity in labels;
- assign an issue to a gate only when completing it materially contributes to that gate;
- trigger-based future infrastructure normally stays unassigned until the trigger fires.

### Pull requests
- small/local research or maintenance change → direct commit to `main` is acceptable;
- cohesive repository-wide method/schema/provenance/structural change → branch + PR is preferred;
- PR description states problem, material changes, deliberate non-changes and impact on research state;
- PR does not replace `DECISIONS.md` for durable cross-project rationale.

### Tags/releases
Use only for intentionally frozen, reproducible research/publication checkpoints. Do not release ordinary development increments. G5/G6 are natural candidates; earlier gates only when independently useful.

Do not introduce Projects/Kanban, Discussions, CODEOWNERS or contributor/workflow bureaucracy without an observed need.

## Maintenance triggers

### Source identity/stage/file/relation changes
Update the corresponding canonical corpus record and project crosswalk/status only when the project consequence changes.

### Transcription changes
Update project transcription; log consequential replacements/rejections; update palaeographic evidence and `STATUS.md` when active uncertainty/next action changes.

### External source/literature inspected
Update project research audit with actual access level/passages.

### Project lesson learned
Record the concrete failure/correction in `LEARNINGS.md`. Promote only a genuinely general safeguard into methodology.

### Generic method/gate changes
Update the owning methodology file; record durable cross-project rationale in `DECISIONS.md` when needed; then run a bounded repo-wide consistency pass across dependent projects.

### Active task/gate state changes
Update project `STATUS.md`; do not copy generic gate requirements into the project.

## Bounded repo-wide consistency pass

Run after material canonical changes such as source-ID migration, provenance correction, file-manifest change, relationship-status change, generic gate/method change or repository restructuring.

Start from the changed canonical truths:
1. state changed truths/identifiers;
2. check dependent canonical records/project crosswalks;
3. check derived project state (`project.yml`, `STATUS.md`, research/source audits) for obsolete wording/completed next steps;
4. search for stale identifiers, old generic-rule copies and contradictory claims;
5. check relevant Issues against current implementation/triggers;
6. apply the fachlich-technisches quality gate from `AGENTS.md`;
7. stop when coherent and return to research.

Do not use a consistency pass to invent new architecture or re-adjudicate manuscript readings unless a genuine research problem is exposed.

## README, Wiki, Issues and chat

- **README** — orientation/map, not detailed status.
- **Wiki** — human-facing handbook, never canonical research truth.
- **Issues** — triggered/deferred work, not a roadmap commitment.
- **Chat** — transient workspace; durable continuation state must be persisted.

## Human–AI maintenance responsibility

### AI
Own routine repository/corpus hygiene, propagation of changed truths, cross-reference repair and restartability. Surface missing metadata rather than inventing it.

### User
Own research purpose, source access only they can provide, rights/authority facts not otherwise verifiable, desired depth and consequential publication/use decisions. The user is not the repository synchronizer or default specialist adjudicator.

### Qualified expert
Escalation/review role when consequence/uncertainty warrants independent specialist judgment.

## End-of-work integrity check

Before completing consequential work ask:
1. What research/method truth changed?
2. Is it in the correct method/corpus/project canonical home?
3. Did a generic method change leak source-specific facts into methodology or duplicate generic requirements inside a project?
4. Did a source/file/relation change require corpus updates?
5. Did a reading change require transcription/decision/palaeography updates?
6. Did project gate state/next action change?
7. Did a project failure create a generalisable learning?
8. Did a deferred issue trigger actually fire?
9. Is a bounded consistency pass required?
10. Can another capable researcher identify the source, understand the active generic gate and continue without chat?

If 10 is no, persist the minimum missing state.

## Lean maintenance rule

`Maintain on change, preserve method/corpus/project boundaries, propagate material truth changes, then stop.`