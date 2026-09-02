# Maintenance and documentation ownership

## Purpose

Keep `paleo-type` continuously usable without creating a second documentation project. Maintenance is event-driven: update the canonical record that owns a changed truth, propagate only material consequences, then return to research.

## One fact, one canonical home

| Information | Canonical home | Role |
|---|---|---|
| highest-order scholarly purpose, precedence and human material-change authority | `GOVERNING_OBJECTIVE.md` | repository constitution / mission boundary |
| repository purpose/map/required reading path | `README.md` | orientation view / entry point |
| mandatory AI/research guardrails | `AGENTS.md` | binding stable rules |
| shared architectural/methodological rationale | `DECISIONS.md` | lean cross-project decision record |
| GitHub Milestone-family/naming/backlog semantics | `MILESTONES.md` | planning/navigation rules only |
| authoritative end-to-end scholarly method | `methodology/historical-source-workflow.md` | reusable normative method |
| generic scholarly maturity gates | `methodology/research-gates.md` | reusable G1–G6 requirements |
| material research-system change-admission workflow | `methodology/maintenance.md` | canonical operational admission rule |
| project/source-use lifecycle and feedback | `methodology/project-lifecycle.md` | reusable Project rules |
| source identity/instantiation/preservation/access method | `methodology/source-and-provenance.md` | reusable Source/File rules |
| minimal new-project contract | `templates/project/` | Project creation template |
| archival/source record identity and inspection stage | `corpus/sources.tsv` | canonical Source inventory |
| exact export/File identity, checksum, coverage, preservation path/state, rights | `corpus/files.tsv` | canonical File manifest |
| reusable source-wide image/PDF/export/folio mapping | `corpus/source-data/<source_id>/` | Source-level canonical mapping |
| historical/archival/textual Source relations | `corpus/relationships.tsv` | relationship claims + evidence status |
| administrative/historical event context | `corpus/events.tsv` | contextual event/activity registry |
| recurring normalized identities | `entities/*.tsv` | corpus-level normalized identities |
| Project research purpose, documentary anchor and active scope | `projects/<id>/project.yml` | canonical Project definition |
| Project-relative Source research functions and relevant loci | `projects/<id>/source-uses.tsv` | normalized Project→Source research-use truth |
| concrete Project-use → File/instance evidence binding | `projects/<id>/research/use-evidence.tsv` | Project-local use-evidence relation; File identity stays in `corpus/files.tsv` |
| project-specific inspection audit | `projects/<id>/sources/inspection-log.tsv` | inspected-vs-metadata trace |
| current Project gate/evidence/access/preservation gaps and authorized next action | `projects/<id>/STATUS.md` | restart point |
| scoped transcription/decisions/analysis | owning Project directories | Project research truth |
| substantive source/reading decisions | Project `apparatus/decisions.tsv` | revision trail |
| external literature/source inspection audit | Project `research/` | checked-vs-lead distinction |
| source/hand-specific comparisons | Project `palaeography/` | empirical comparison evidence |
| Project-specific failures/lessons | Project `LEARNINGS.md` | learning record |
| research-organisational relations between genuine Projects | `projects/relationships.tsv` | optional Project dependency/navigation |
| rebuildable task/Project context | `tools/project_context.py` output | derived view; never canonical truth |
| deferred/discrete tracked work | GitHub Issues | work package/backlog, never current research truth |
| end-user explanation | GitHub Wiki | handbook only |
| exploratory reasoning | chat | transient workspace only |

Explanations, generated views and GitHub metadata may summarize canonical records but must not become parallel truth stores. Volatile Project state should be referenced or derived rather than recopied into orientation surfaces.

## Governing-objective change control

`GOVERNING_OBJECTIVE.md` is not ordinary maintenance. A material change to its purpose, precedence or governing invariants is a special governance event and requires an explicit human owner decision.

- AI/collaborators may analyse or propose an amendment, but must not autonomously weaken, replace or supersede the objective.
- A material amendment must be isolated in a visible, cohesive PR with rationale and consequences; it must not arrive as incidental cleanup or automatic propagation.
- Routine synchronization/refactor machinery must never rewrite the governing objective merely because lower-level method, standards, models or architecture changed.
- Clarifying references in lower-level files should point to the canonical objective rather than copy it.
- Ordinary source research and maintenance remain lean and do not inherit mission-change ceremony.

## Material research-system change admission

This file is the canonical operational owner of the general consequence-based admission workflow for material research-system changes:

`analysis → requirements → concept → owner review / explicit implementation admission → development → deterministic tests / scholarly loss checks → result review`

Apply this workflow when a proposed change materially alters shared METHOD, the CORPUS information model or canonical ownership, Project architecture/invariants, canonical research-data migration semantics, or another research-system rule where error could change provenance, scholarly meaning, auditability or restartability.

The stages have distinct purposes:

1. **Analysis** — inspect the current canonical state and the demonstrated failure/need.
2. **Requirements** — derive the applicable scholarly, epistemic, provenance, usability and technical requirements.
3. **Concept** — state the smallest coherent change, alternatives, dependencies and explicit non-goals.
4. **Owner review / explicit implementation admission** — the human owner decides whether a sufficiently precise material scope may enter development.
5. **Development** — implement only the admitted scope.
6. **Deterministic tests / scholarly loss checks** — verify machine-checkable invariants and proportionate preservation of scholarly meaning, provenance and regression fixtures before treating the implementation as ready.
7. **Result review** — compare the result with the admitted requirements and preserved research meaning; passing deterministic tests alone does not establish scholarly acceptance.

### Lean admission boundary

Only **material research-system changes** require this admission path. Do not turn ordinary scholarship or already admitted bounded implementation into repeated approval loops.

A new material admission is not required merely for:

- source inspection;
- evidence logging;
- bounded research or transcription performed within an already admitted method/scope;
- derived/rebuildable outputs that do not redefine canonical truth;
- routine repository maintenance that does not change research-system semantics;
- implementation details already unambiguously covered by a sufficiently precise admitted scope.

Once a material implementation scope is explicitly admitted, its precise bounded implementation may proceed without owner micromanagement. If apparently routine or admitted work exposes a **new** material architecture or migration choice outside that scope, stop the affected change and return that choice to this admission workflow rather than silently expanding scope.

### Admission is not specialist validation

Owner admission controls purpose, priorities and permission to implement a material research-system change. It does **not** establish archival, palaeographic, historical, philological, editorial or other specialist truth and never substitutes for qualified independent specialist validation where that is required.

AI/HITL-specific obligations for applying this general rule live in `methodology/ai-governance.md`; that file references this canonical workflow rather than duplicating it.

No workflow engine is required. An inspectable admitted scope, bounded implementation, deterministic/proportional tests and explicit result review are sufficient.

## Systemic integration and Generic-Fit

Do not append a new durable rule merely because a new observation, pilot or external reference exists. Before materially integrating a new aspect, compare it with the governing objective, current canonical state, applicable requirements and existing decisions, then state in ordinary language what happens to the existing system.

Useful review dispositions are:

`fuse | refine | reframe | supersede | conflict | reject | defer`

These are review vocabulary, **not** a new lifecycle, schema or mandatory state machine. For a material change, record enough rationale to make clear:

- origin/evidence of the new aspect;
- what existing semantics/requirements it supports, changes or conflicts with;
- the chosen disposition and why;
- required changes;
- deliberate **non-changes**, especially where a pilot-specific fact must remain local;
- the authority/assurance still required.

### Generic-Fit rule

A Project or pilot finding stays Project-specific by default. Promote it into shared METHOD, a generic contract or a generic regression only when the safeguard genuinely applies to comparable investigations and prevents a demonstrated recurring or structurally general failure.

A single case can falsify a bad generic assumption, but it does not automatically define the replacement generic model. Preserve the concrete case in its Project; promote only the general safeguard. Do not require a formal integration-packet file when a PR/Issue/decision record already carries the necessary trace.

## Method / corpus / Project ownership test

Before creating/updating durable state ask:

1. Would the statement remain a valid rule for another comparable manuscript investigation after a Generic-Fit check? → METHOD.
2. Does it identify an archival record, exact export, reusable source-wide mapping, Source relationship, event or normalized entity? → CORPUS / `entities/`.
3. Does it define why a scholarly investigation exists, its current scope, how a Source is used relative to that investigation, what locus/evidence matters, what was read/decided, or what remains open? → PROJECT.
4. Does it describe a relation between two genuine purpose-established Projects? → `projects/relationships.tsv`.

A Project's documentary structure remains CORPUS truth. `project_source_id` anchors an already-established Project to that structure; it does not itself create the Project or define its purpose/priority.

## Project lifecycle

Follow `methodology/project-lifecycle.md` for every Project creation or material Project-structure change.

Key invariants:

- a Project exists because a concrete scholarly research purpose has been established;
- once selected, a Project has exactly one `project_source_id` documentary Source anchor for deterministic structural resolution; the anchor does not establish Project existence, purpose, priority or `NEXT ACTION`;
- structural containment lives in canonical Source→Source `part_of`; internal/external status is derived rather than copied into Project data;
- a Source record, archive section, PDF, current question, upload or temporary comparison task does not automatically become a Project;
- Project-relative Source use is represented as one `source-uses.tsv` row per concrete `research_function`; several functions for the same Source are allowed when evidenced;
- `research_function` and relevant locus are not Source identity or structural membership;
- concrete digital evidence used by a Source use is linked separately through `research/use-evidence.tsv`; `corpus/files.tsv` remains the canonical owner of File identity/provenance;
- reusable source-wide crosswalks live once in `corpus/source-data/<source_id>/`;
- Project→Project relations are explicit only and are never inferred from Source use or structural containment;
- do not create empty future-proof directories.

The former Reg. Ii 5 legacy `sources/sources.tsv` / `primary_file_id` / `principal_source_id` compatibility representation has been loss-checked and migrated. It is historical migration evidence, not an accepted current Project owner and must not be recreated.

### New-Project creation check

Before accepting a new Project verify:

1. a concrete scholarly research purpose justifies durable Project state; Source/File/archival structure alone is insufficient;
2. `project_source_id` resolves to the canonical documentary Source anchor selected for that Project;
3. research object and active scope are explicit and human-readable; an explicit no-current-scope state is valid when no scope has been selected;
4. `source-uses.tsv` exists as the declared Project Source-use owner;
5. `STATUS.md` (or the declared canonical status file) exists as the restart/status owner;
6. every used Source ID resolves to `corpus/sources.tsv`;
7. distinct archival records/sections remain distinct Source rows;
8. every exact evidence export resolves to `corpus/files.tsv` with SHA-256 and preservation state;
9. any Project-use-specific File binding is explicit in `research/use-evidence.tsv` rather than inferred from Source membership;
10. central original exports have an intended/actual repository path or explicit preservation blocker when required;
11. Source-relative relevant locus is separated from full archival Source extent and from an instance-specific evidence locator;
12. generic gates/method are referenced rather than copied;
13. reusable crosswalks have one canonical Corpus source-data owner;
14. historical/Source claims remain in `corpus/relationships.tsv`;
15. Project relations are used only when another genuine purpose-established Project exists;
16. another capable researcher can restart without chat.

Stable machine-checkable parts of this contract are enforced by `corpus/source-contract.json` + `tools/source_contract.py`; do not replace those checks with prose or AI self-certification.

## Exact source-export preservation and evidence availability

The exact original export used for consequential research is part of the evidence chain.

Maintenance must distinguish:

- `repo-preserved` — exact original bytes are stored at the declared repository path and hash-verified;
- `external-controlled` — exact bytes are controlled externally according to the recorded state;
- `preservation-blocked-public-redistribution` — public redistribution is not established and repository-public preservation is blocked under the current contract;
- other states only when their meaning is deliberately admitted and documented.

A URL/URN + checksum is provenance, not equivalent backup. Never claim repository preservation when the binary is absent.

Also keep **identifiability**, **byte availability/preservation**, **reproducibility**, and **research-ready target-context availability** separate. For visual work, a hash-verified local/retrievable File is not by itself proof that a fresh target context has received the object or can inspect its pixels.

When a rights/authority fact changes, update `corpus/files.tsv` and perform the smallest resulting preservation action. The user owns rights/authority facts that cannot otherwise be verified; the assistant owns repository synchronization once authority is established.

## Feedback loops

### Project discovers a Source-level correction

`Project evidence → verify → update canonical Corpus owner → update only affected Project use/status/work products → bounded consistency pass`

Examples: wrong Source title, File checksum/path, folio/export mapping or Source relationship.

### Project Source research use changes

Update `projects/<id>/source-uses.tsv`; update `research/use-evidence.tsv` only when the concrete File/instance evidence for that use changes. Do not modify canonical Source identity or `part_of` merely because a research function/locus/evidence binding changes.

### Project discovers generic methodological weakness

`Project observation → Project LEARNING/status → Generic-Fit/systemic integration check → methodology/DECISIONS/contract only if justified → bounded consistency pass`

Record the concrete failure in the Project. If the generic safeguard is deterministic, add the smallest regression that prevents recurrence; if it requires judgement, keep that boundary explicit rather than encoding false certainty.

## Required reading paths

### Human

Read `README.md` first. Read `GOVERNING_OBJECTIVE.md` when evaluating repository purpose, precedence, Human-in-the-loop or consequential method/architecture change. For a Project read its `project.yml`, `STATUS.md`, `source-uses.tsv` and `research/use-evidence.tsv` when present/relevant. Read `methodology/project-lifecycle.md` for Project/Source-use semantics, `methodology/source-and-provenance.md` for exact Source/File preservation and evidence-access distinctions, and `MILESTONES.md` when interpreting scheduled Issues/Milestones.

### AI continuing research

1. read `GOVERNING_OBJECTIVE.md` and `AGENTS.md`;
2. establish and load all canonical rules/requirements applicable to the concrete task;
3. read `README.md` if repository structure is not already established;
4. read Project `project.yml`, including research purpose/current scope, and resolve `project_source_id` as documentary anchor;
5. read Project `STATUS.md`;
6. read `source-uses.tsv` and explicit `research/use-evidence.tsv` when relevant;
7. read the active generic gate in `methodology/research-gates.md`;
8. inspect relevant `corpus/sources.tsv`, `corpus/files.tsv`, `corpus/source-data/` and `corpus/relationships.tsv`;
9. read additional task-relevant methodology from its canonical owner;
10. continue from an authorized `NEXT ACTION` when one exists; do not invent one from historical work state, Source structure or chat.

Generated Project context may assist this reading path, but it remains a rebuildable derived view and must preserve references to the canonical owners it summarizes.

## GitHub-native human navigation

GitHub metadata is a navigation/planning/review layer over canonical records, never a competing truth store.

### Milestones

Follow `MILESTONES.md`.

Use Milestones for targets/work phases, with explicit families:

- `GOV-*` — repository governance/architecture/structural-review work;
- `<project> / G*` — Project-specific scholarly Issues contributing to generic G1–G6 gates.

A Project G1–G6 Milestone is a work-planning mirror, not the scholarly gate claim. Generic requirements remain in `research-gates.md`; actual Project gate state remains in `STATUS.md`.

Milestone progress/completion does not establish gate attainment. Update `STATUS.md` first when evidence changes gate state, then adjust Issue/Milestone planning if useful. No calendar due dates without real deadlines; no fragmentation for progress percentages; do not pre-create all Project gate Milestones merely for completeness.

### Issues and labels

Issues preserve bounded future work or useful discrete work packages. Labels classify them for filtering only.

- do not encode canonical research status, confidence or Source identity in labels;
- for cross-disciplinary Issues, use multiple labels and one primary target Milestone;
- assign a scholarly Issue to a Project gate Milestone only when completing it materially contributes to that gate and issue tracking adds value;
- trigger-based future infrastructure normally stays without a Milestone until triggered/scheduled;
- do not create Issues for every line reading or routine source action.

**No-dead-issue rule:** every deferred issue must contain research benefit/problem, why it is not current work, an observable trigger, and definition of done/acceptance criteria.

**Trigger audit:** re-check relevant deferred issues on a bounded consistency pass, Project gate change, publication/export start, or evidence that a trigger fired. Outcome: leave deferred, schedule with evidence, keep triggered-but-unscheduled with reason, close completed, or close superseded/duplicate.

### Pull requests

Small/local research or maintenance changes may commit directly to `main`; cohesive repository-wide method/schema/provenance/structural changes preferably use branch + PR. PRs state problem/evidence, affected canonical semantics, material changes, deliberate non-changes, assurance classes and research-state impact. PRs do not replace `DECISIONS.md`.

A material change to `GOVERNING_OBJECTIVE.md` is always a dedicated/cohesive governance PR and requires explicit human owner approval before merge.

### Tags/releases

Use only for intentionally frozen reproducible research/publication checkpoints.

Do not introduce Projects/Kanban or Discussions without observed need. Governance protections such as CODEOWNERS/rulesets require a concrete protection requirement.

## Maintenance triggers

- governing-objective clarification/change proposal → treat as special governance event; never auto-propagate a material mission change;
- Source identity/stage change → update `corpus/sources.tsv`, then affected Project references only;
- exact export/checksum/coverage/storage/rights change → update `corpus/files.tsv`, then preservation/Project-use consequences;
- reusable source-wide crosswalk change → update `corpus/source-data/<source_id>/`, then affected Project references/transcription addresses;
- Project research-purpose/scope change → update `project.yml` with required authority; do not infer it from Source structure;
- Project documentary-anchor change → update `project_source_id`, re-resolve structural consequences, but do not infer new purpose/priority;
- Project Source research-function/locus change → update Project `source-uses.tsv` and affected `STATUS.md`/work products;
- Project-use concrete File/instance evidence change → update Project `research/use-evidence.tsv`, never duplicate File provenance there;
- Source relationship change → update `corpus/relationships.tsv` with evidence status;
- Project relation change → update `projects/relationships.tsv` only when both endpoints are genuine Projects;
- Project creation → run the new-Project creation check;
- transcription change → update transcription, consequential decision/palaeography and status as applicable;
- external Source/literature inspected → update Project research audit at actual access level;
- Project lesson → keep concrete incident in Project; generalise only after Generic-Fit/systemic integration review;
- generic method/gate/contract change → update owning methodology/decision, add appropriate assurance, and run bounded consistency pass;
- active gate/task changes → update `STATUS.md` first and trigger issue audit.

## Bounded repo-wide consistency pass

Run after material canonical changes such as Source-ID/provenance correction, File-manifest/preservation change, Source/Project relation change, crosswalk ownership migration, Project model change, generic method/gate/contract change or repository restructuring.

1. state changed canonical truths/owners and deliberate non-changes;
2. check `corpus/sources.tsv` ↔ `corpus/files.tsv` ↔ `corpus/source-data/` referential integrity;
3. check every Project's declared `source-uses.tsv` and `research/use-evidence.tsv` against canonical Source/File IDs;
4. verify `use-evidence.file_id` belongs to the same canonical Source as the referenced use rather than acting as cross-Source claim evidence;
5. verify no removed legacy `projects/*/sources/sources.tsv` or `principal_source_id` compatibility owner has reappeared;
6. verify separately identified archival records have not been collapsed by shared signature/title shorthand;
7. check Project `project.yml`/`STATUS.md` for stale purpose/scope/path/next-step claims;
8. search for source-as-project leftovers, duplicate crosswalks, stale identifiers and old generic-rule copies;
9. verify `projects/relationships.tsv` contains only genuine Project→Project relations and none inferred from Source use;
10. verify central Source-export preservation claims match actual File state and rights constraints;
11. distinguish File identity/byte availability from target-context evidence readiness where the active task requires inspection;
12. audit relevant deferred Issues against triggers/Milestone targets;
13. apply the fachlich-technisches quality gate from `AGENTS.md`;
14. verify generated/context views retain the canonical references needed for restart and do not promote historical state to current authority/priority;
15. verify restartability;
16. stop when coherent and return to research.

Do not use a consistency pass to invent architecture or re-adjudicate manuscript readings unless a genuine research problem is exposed.

## README, Wiki, Issues, Milestones and chat

- **GOVERNING_OBJECTIVE** — highest-order purpose/precedence/change authority, not an operational handbook.
- **README** — orientation view/map; volatile state belongs in canonical owners or rebuildable views.
- **AGENTS** — binding stable operating guardrails, not a duplicate Project-status store.
- **Wiki** — human-facing handbook, never canonical research truth.
- **Issues** — discrete/deferred work and audit/review metadata, not research truth.
- **Milestones** — target/phase navigation for admitted Issues; not evidence/gate truth.
- **Chat** — transient workspace; durable continuation state must be persisted.

## Human–AI maintenance responsibility

### AI

Own routine repository/Corpus/Project hygiene, propagation of changed truths, Source/File/Project referential integrity, deterministic validation, generated-context refresh, issue-trigger audit, Milestone-assignment consistency and restartability. Surface missing metadata/preservation/access blockers rather than inventing them.

### User

Own research purpose, Source access only they can provide, rights/authority facts not otherwise verifiable, desired depth, material research-system admission and consequential publication/use decisions. The user is not the repository synchronizer or default specialist adjudicator. Material change to the governing objective requires the user's explicit decision.

### Qualified expert

Escalation/review role when consequence/uncertainty warrants independent specialist judgment.

## End-of-work integrity check

Before completing consequential work ask:

1. What research/method truth changed and who owns it?
2. Is canonical Source/File/crosswalk truth in CORPUS rather than copied into Projects?
3. Does each Project have an explicit research purpose, with `project_source_id` used only as its post-selection documentary anchor?
4. Are internal/external statuses still derived from `part_of` rather than stored as competing truth?
5. Does each `source-uses.tsv` expose Project-relative research functions/loci, with concrete File evidence separately bound through use-evidence?
6. Have removed legacy Project source-register/`principal_source_id` owners stayed removed?
7. Are central original exports actually preserved as claimed, with rights blockers explicit?
8. Is evidence needed for the current task actually accessible/staged/inspectable as required rather than merely identifiable/reproducible?
9. Are Project relations distinct from Source relations and never inferred from Source use?
10. Did Project gate/authorized-next-action state change?
11. Did a Project learning pass Generic-Fit before any generic promotion?
12. Did any deferred Issue trigger fire or become obsolete?
13. Is a bounded consistency pass required?
14. Can another capable researcher identify Project purpose, documentary anchor, used Sources/functions, exact evidence/preservation/access state and continue without chat?

If 14 is no, persist the minimum missing canonical state or repair the derived/context surface that failed to expose it.

## Lean maintenance rule

`Maintain on change; Project = purpose-established scholarly work state; project_source_id = post-selection documentary anchor; Source = Source; research function = Project→Source use; exact File identity = Corpus truth; concrete use→File evidence = explicit Project relation; one fact, one owner; derive structural status; distinguish byte availability from target-context readiness; test Generic-Fit before generalising; reference/derive rather than copy; propagate only material consequences; then stop.`
