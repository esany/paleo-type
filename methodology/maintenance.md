# Maintenance and documentation ownership

## Purpose

Keep `paleo-type` continuously usable without creating a second documentation project. Maintenance is event-driven: when research or method changes, update the canonical record that owns that information. Do not create periodic process work merely to make the repository look maintained.

## One fact, one canonical home

| Information | Canonical home | Role |
|---|---|---|
| repository purpose/map/required reading path | `README.md` | entry point |
| mandatory AI/research guardrails | `AGENTS.md` | binding rules |
| shared architectural/methodological rationale | `DECISIONS.md` | lean cross-project decision record |
| general research method | `methodology/*.md` | reusable normative method |
| corpus source identity and inspection stage | `corpus/sources.tsv` | corpus inventory |
| external/digital source file or instantiation identity, checksum, coverage, storage expectation and rights status | `corpus/files.tsv` | canonical file/instantiation manifest |
| explicit source/event/entity relationships | `corpus/relationships.tsv` | relationship claims + evidence status |
| administrative/historical event context | `corpus/events.tsv` | contextual event/activity registry |
| recurring normalized identities | `entities/*.tsv` | authority-like local identities; never manuscript readings |
| project identity/stable scope | `projects/<id>/project.yml` | project identity |
| project research gates/requirements | `projects/<id>/MILESTONES.md` | canonical scholarly maturity criteria |
| current project state/exact next action | `projects/<id>/STATUS.md` | restart point |
| project-specific image/folio/export/source inspection detail | `projects/<id>/sources/` | local provenance/crosswalk; does not replace `corpus/files.tsv` |
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
Read `README.md` first. Deeper files are opened only as needed. GitHub-native navigation may expose milestones, labelled issues, larger change reviews and frozen checkpoints, but the linked repository files remain authoritative for scholarly state.

### AI continuing research

1. read `README.md` if repository structure is not already established;
2. read `AGENTS.md`;
3. read `DECISIONS.md` only when a shared method/data-model choice matters;
4. inspect relevant `corpus/` rows, including `corpus/files.tsv` when exact inspected files/instantiations matter;
5. read active project `STATUS.md` and its referenced `MILESTONES.md` requirements;
6. read relevant decision rows and `LEARNINGS.md`;
7. read only relevant methodology;
8. continue from `NEXT ACTION` unless inspected evidence justifies a change.

## GitHub-native human navigation

GitHub metadata is a **navigation layer over canonical research records**, never a competing truth store.

### Milestones

Use GitHub Milestones only when a project already has explicit scholarly gates in its canonical `MILESTONES.md`.

- Mirror the milestone name and a short human-readable purpose.
- Link/refer to the project `MILESTONES.md` for requirements and exit gates; do not duplicate the checklist in GitHub metadata.
- Milestone completion is a navigation/progress signal. The scholarly basis for declaring a gate reached remains in repository state (`MILESTONES.md`, `STATUS.md`, research records).
- Do not create calendar deadlines unless the research genuinely has one.
- Do not fragment a scholarly gate into many issues merely to produce a progress percentage.

### Issues and labels

Issues preserve bounded future work or a genuinely useful discrete work package. Labels classify issues for human filtering only.

- Derive a small label vocabulary from actual recurring issue themes rather than designing a taxonomy in advance.
- Prefer topical labels such as `corpus`, `palaeography`, `provenance`, `publication`, `automation`, `standards`, `bibliography`, `data-quality` only where the current issue set justifies them.
- Do not encode canonical research status, reading confidence or source identity in labels.
- GitHub open/closed state is enough for issue lifecycle; do not add redundant status labels.
- Replace body hashtags with labels only after the corresponding real GitHub labels exist.
- Assign an issue to a research milestone only when completing that issue materially contributes to that scholarly gate. Trigger-based future infrastructure issues normally remain unassigned until their trigger fires and they become gate-relevant.

### Pull requests

Use PRs as human-readable change records for consequential repository-wide work, not as ceremony for every research correction.

- Small/local research or maintenance change → direct commit to `main` is acceptable.
- Cohesive repository-wide method, schema, provenance-model or structural change → branch + PR is preferred.
- PR description should state the problem, material changes, deliberate non-changes and impact on existing research state.
- Prefer a coherent/squashed merge history for such structural changes when practical.
- A PR does not replace `DECISIONS.md` when a durable cross-project rationale is required.

### Tags and releases

Use tags/releases only for intentionally frozen, reproducible research/publication checkpoints.

- Do not release ordinary development increments.
- A checkpoint should identify the project/research state being frozen and point to the canonical source/transcription/apparatus state in that commit.
- M5/M6 are natural candidates; earlier milestones warrant a release only when the checkpoint has independent research value.
- A release does not make unresolved readings certain and does not replace provenance or edition documentation.

### Projects, Discussions and other GitHub structures

Do not introduce GitHub Projects/Kanban, Discussions, CODEOWNERS, contributor governance or workflow templates until an actual collaboration/navigation problem requires them. The default is absence, not preconfiguration.

## Maintenance triggers

### Source discovered
- add to `corpus/sources.tsv` at the truthful inspection stage;
- do not create a project or transcribe it automatically;
- record discovery boundary only when it matters to corpus coverage.

### Source identity/inspection stage changes
- update `corpus/sources.tsv`;
- update project `sources/` only for project-specific inspection/crosswalk detail;
- do not duplicate full corpus identity in project files.

### External/digital source file or instantiation changes
- update `corpus/files.tsv` for file identity, checksum, source coverage, storage expectation and rights status;
- keep project `sources/` for local folio/image/PDF/export mappings and inspection details;
- do not create a second file manifest inside a project.

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
- record a cross-project rationale in `DECISIONS.md` only when it would otherwise need rediscovery;
- update README only when map/top-level orientation changes;
- update Wiki explanation only if end-user meaning changes and write access exists.

### Canonical truth or structure changes materially
Run a **bounded repo-wide consistency pass** after changes such as source-ID migration, corrected source identity/provenance, file/instantiation manifest changes, relationship-status change, status-model change or repository restructuring.

Start from the changed canonical truths, not from a ritual reread of every file:

1. state the changed truths/identifiers;
2. check dependent canonical records and project crosswalks;
3. check derived state (`project.yml`, `STATUS.md`, research/source audits) for obsolete wording or completed `next_step`s;
4. search for stale identifiers/aliases and contradictory folio/image/date/source/file-relation claims;
5. check relevant open Issues against current implementation/triggers;
6. apply the fachlich-technisches quality gate from `AGENTS.md`;
7. stop when the repository is coherent and return to research.

Do not use a consistency pass to invent new architecture or re-adjudicate manuscript readings unless the inconsistency exposes a genuine research problem.

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
4. Did an external/digital source file or instantiation change require a `corpus/files.tsv` update?
5. Did a reading change require transcription/decision/palaeography updates?
6. Did the active problem/next action change?
7. Did a project failure create a real learning?
8. Did a deferred idea become useful enough for an Issue, or did an existing Issue's trigger actually fire?
9. Did a material canonical/structural change require a bounded repo-wide consistency pass?
10. Can another capable agent identify the exact sources/files, understand evidence status and continue without the chat?

If 10 is no, persist the minimum missing state.

## Lean maintenance rule

`Maintain on change, propagate material truth changes across dependent records, then stop.`
