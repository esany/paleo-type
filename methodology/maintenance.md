# Maintenance and documentation ownership

## Purpose

Keep `paleo-type` continuously usable without creating a second documentation project. Maintenance is event-driven: when research or method changes, update the canonical record that owns that information. Do not create periodic process work merely to make the repository look maintained.

## One fact, one canonical home

| Information | Canonical home | Role |
|---|---|---|
| repository purpose/map/required reading path | `README.md` | entry point |
| mandatory AI/research guardrails | `AGENTS.md` | binding rules |
| general research method | `methodology/*.md` | reusable normative method |
| corpus source identity and inspection stage | `corpus/sources.tsv` | corpus inventory |
| explicit source/event/entity relationships | `corpus/relationships.tsv` | relationship claims + evidence status |
| administrative/historical event context | `corpus/events.tsv` | contextual event/activity registry |
| recurring normalized identities | `entities/*.tsv` | authority-like local identities; never manuscript readings |
| project identity/stable scope | `projects/<id>/project.yml` | project identity |
| current project state/exact next action | `projects/<id>/STATUS.md` | restart point |
| project-specific image/folio/export/source inspection detail | `projects/<id>/sources/` | local provenance/crosswalk |
| current line readings | `projects/<id>/transcription/*.tsv` | transcription truth |
| substantive reading changes | `projects/<id>/apparatus/decisions.tsv` | revision trail |
| external literature/source inspection audit | `projects/<id>/research/` | checked-vs-lead distinction |
| hand/source-specific comparisons | `projects/<id>/palaeography/` | empirical internal evidence |
| project-specific failures/lessons | `projects/<id>/LEARNINGS.md` | learning record |
| deferred technical/methodological improvements | GitHub Issues | triggered backlog, never current research truth |
| end-user explanation | GitHub Wiki | handbook only |
| exploratory reasoning | chat | transient workspace only |

Explanations may summarize canonical records, but they must not become parallel truth stores.

## Required reading paths

### Human
Read `README.md` first. Deeper files are opened only as needed.

### AI continuing research

1. read `README.md` if repository structure is not already established;
2. read `AGENTS.md`;
3. inspect relevant `corpus/` rows if source identity/relations matter;
4. read active project `STATUS.md`;
5. read relevant decision rows and `LEARNINGS.md`;
6. read only relevant methodology;
7. continue from `NEXT ACTION` unless inspected evidence justifies a change.

## Maintenance triggers

### Source discovered
- add to `corpus/sources.tsv` at the truthful inspection stage;
- do not create a project or transcribe it automatically;
- record discovery boundary only when it matters to corpus coverage.

### Source identity/inspection stage changes
- update `corpus/sources.tsv`;
- update project `sources/` only for project-specific inspection/crosswalk detail;
- do not duplicate full corpus identity in project files.

### Source relationship changes
- update `corpus/relationships.tsv` with evidence/status;
- catalogue statements stay `metadata-supported` until stronger evidence exists;
- update project `STATUS.md` only if the relation changes active research.

### Event/context changes
- update `corpus/events.tsv`;
- do not infer textual relation from shared event membership.

### Repeated normalized entity becomes useful
- add/update `entities/`;
- keep manuscript form in transcription;
- never normalize the diplomatic reading by editing the entity registry.

### Transcription changes
- update `transcription/*.tsv`;
- log substantive replacement/rejection in `apparatus/decisions.tsv`;
- update palaeographic evidence if anchors change;
- update `STATUS.md` if active uncertainty/next action changes.

### External source/literature inspected
- update project `research/` with exact access level/passages;
- promote source-status codes only under `evidence-policy.md`.

### Project lesson learned
- record concrete failure/correction in `LEARNINGS.md`;
- promote to methodology only when genuinely generalizable.

### Method/governance/structure changes
- update owning methodology/AGENTS file;
- update README only when map/top-level orientation changes;
- update Wiki explanation only if end-user meaning changes and write access exists.

### Useful future idea appears but is not justified now
Create or update a GitHub Issue only if it contains:

`problem/benefit → why not now → trigger → acceptance criteria`.

Close duplicates and ideas that have become core methodology. Do not leave current research requirements deferred as issues.

### Active task changes
Update project `STATUS.md` so another agent can continue without the chat.

## README, Wiki, Issues and chat

### README
Orientation and map, not detailed research status.

### Wiki
Human-facing handbook. It may explain statuses/workflows but never own open readings, corpus identities or next actions.

### Issues
Deferred work whose rationale is worth preserving. They are not a roadmap commitment. An issue's trigger must be reached before implementation is assumed useful.

### Chat
Transient workspace. Any fact/decision/open problem needed for continuation must be persisted before the work is considered durable.

## Human–AI maintenance responsibility

### AI
The assistant owns routine repository/corpus hygiene: identify affected canonical records, update them during the same work block when practical, preserve revision history, repair cross-references, maintain restartability, and surface missing metadata instead of inventing it.

### User
The user owns research purpose, source access only they can provide, rights/authority facts not otherwise verifiable, desired depth and consequential publication/use decisions. The user is not responsible for repository synchronization or specialist adjudication they cannot validate.

### Qualified expert
Escalation/review role when the consequence of error warrants independent specialist judgment.

## End-of-work integrity check

Before completing consequential research ask:

1. What research truth changed?
2. Is it in its one canonical home?
3. Did a source identity/relation change require a corpus update?
4. Did a reading change require transcription/decision/palaeography updates?
5. Did the active problem/next action change?
6. Did a project failure create a real learning?
7. Did a deferred idea become useful enough for an Issue, or did an existing Issue's trigger actually fire?
8. Can another capable agent identify the exact sources, understand evidence status and continue without the chat?

If 8 is no, persist the minimum missing state.

## Lean maintenance rule

`Maintain on change, at the canonical source, with the minimum record needed for reliable continuation.`
