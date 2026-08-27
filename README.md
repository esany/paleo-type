# paleo-type

Lean, evidence-based workspace for the transparent transcription, source criticism and scholarly analysis of early modern handwritten sources.

## Purpose

The highest-order repository purpose, precedence and human change authority are defined once in `GOVERNING_OBJECTIVE.md`. This README is an orientation map and does not supersede that objective.

`paleo-type` helps a non-specialist reliably unlock early modern handwritten sources without turning the research task into a software project or requiring the user to become a historian, archivist or palaeographer.

The research sources and scholarly result are the product. Tooling is support infrastructure only.

## Three repository layers

### 1. METHOD
`methodology/`, `AGENTS.md`, `DECISIONS.md`, `templates/`

Reusable scholarly method, research gates, evidence rules, project/source lifecycle rules, AI/human validation rules and durable cross-project decisions. Concrete source facts do not belong here.

### 2. CORPUS
`corpus/`, `entities/`

Canonical historical/documentary source nodes, exact digital instantiations, reusable source-wide mappings, structural/historical/textual relationships, events and recurring normalized identities.

### 3. PROJECT
`projects/<id>/`, `projects/relationships.tsv`

A project is scholarly state anchored to **one historically independent source structure** through `project.yml: project_source_id`. In the current archival domain that root is an act. The current active research scope may be narrower than the project root, and the project may use external comparison/control/context sources without making them structural parts of the project.

Generalisation test:

> reusable rule for another comparable manuscript project → METHOD; canonical source/file/relationship truth → CORPUS; concrete work state relative to one historical project root → PROJECT.

The current benchmark directory is `projects/ega-reg-ii-5-knau/`. Its historical project root is `ACT-THHSTAW-EGA-REG-II-5`; `Knau` is the current working focus, not the project boundary.

## Start here

### Human
1. Read this README.
2. Read `GOVERNING_OBJECTIVE.md` when evaluating purpose, precedence, Human-in-the-loop or consequential method/architecture change.
3. For the current Reg. Ii 5 project: `projects/ega-reg-ii-5-knau/project.yml` and `STATUS.md`.
4. For sources used by that project: `projects/ega-reg-ii-5-knau/sources/sources.tsv`.
5. For generic research gates: `methodology/research-gates.md`.
6. For project-root/source-use rules: `methodology/project-lifecycle.md`.
7. For source identity, part–whole structure, exact exports and preservation: `methodology/source-and-provenance.md`.
8. For GitHub work sequencing: `MILESTONES.md`.

### AI continuing research
1. read `GOVERNING_OBJECTIVE.md` and `AGENTS.md`;
2. read the active project's `project.yml` and resolve `project_source_id`;
3. establish and load all canonical rules/requirements applicable to the concrete task;
4. read project `STATUS.md` and `sources/sources.tsv`;
5. read the active gate in `methodology/research-gates.md`;
6. inspect relevant `corpus/sources.tsv`, `corpus/files.tsv`, source-data crosswalks and source relationships;
7. use the source resolver rather than reconstructing project membership from names/chat;
8. continue from project `NEXT ACTION` unless inspected evidence requires a change.

Old chat must never be required to reconstruct durable research state.

## What a project is

A project follows the **historically independent documentary structure**, not the current research bundle.

Every project has one `project_source_id` resolving to a canonical source node. A project may currently work on one passage, protocol, section or problem inside that root; this is `active_scope`, not project identity.

Sources used in the project are classified structurally by the canonical `part_of` graph:

- source = `project_source_id` → project root;
- source `part_of*` project root → internal source;
- otherwise → external research source.

Project roles such as `principal`, `comparison`, `control`, `context` are separate research relations. An external source can be comparison/control/context without becoming part of the historical project structure.

A PDF, portal record, individual protocol or temporary comparison question does not automatically create a project. A distinct historically independent source structure does.

## Generic source structure

`corpus/sources.tsv` contains every historical/documentary object that needs stable identity. `source_type` is descriptive, not a schema switch.

Part–whole structure is expressed generically in `corpus/relationships.tsv`:

`part --part_of--> whole`

This can represent `section → protocol → act`, `attachment → record`, `volume → series` or other evidenced structures without changing the schema. The validator requires valid source endpoints and rejects `part_of` cycles.

Provider/DigiRef IDs, archival hierarchy and repository node boundaries are not assumed to be identical.

## Where truth lives

- `GOVERNING_OBJECTIVE.md` — highest-order scholarly purpose, precedence and human material-change authority.
- `README.md` — repository orientation/map.
- `AGENTS.md` — binding operating/quality guardrails.
- `DECISIONS.md` — consequential cross-project rationale.
- `MILESTONES.md` — GitHub work-planning semantics; never scholarly truth.
- `methodology/historical-source-workflow.md` — authoritative end-to-end scholarly method.
- `methodology/research-gates.md` — canonical reusable G1–G6 requirements.
- `methodology/project-lifecycle.md` — project-root, source-use and restartability rules.
- `methodology/source-and-provenance.md` — source identity, part–whole structure, exact exports and preservation rules.
- `templates/project/` — minimal new-project contract.
- `corpus/sources.tsv` — canonical source-node inventory.
- `corpus/files.tsv` — exact file/instantiation manifest with filename, SHA-256, coverage, storage/preservation state, intended repository path and rights state.
- `corpus/source-data/<source_id>/` — reusable source-wide crosswalks/mappings.
- `corpus/relationships.tsv` — structural `part_of` and historical/archival/textual source relationship claims.
- `corpus/events.tsv` — shared event/activity context.
- `entities/` — recurring normalized identities; never manuscript readings.
- project `project.yml` — project identity (`project_source_id`), scholarly purpose and active scope.
- project `sources/sources.tsv` — sources actually used: source ID, project role, relevant locus and primary file.
- project `sources/inspection-log.tsv` — project-specific inspection audit when useful.
- project `STATUS.md` — actual evidence/gate state, preservation gaps and exact next action.
- project work directories — created only when real work exists.
- `projects/relationships.tsv` — relations only between genuine projects.
- GitHub Issues/Milestones — planning/work metadata, never research truth.
- Chat — transient workspace only.

## Source files and preservation

The exact original archive export actually used in research is a first-class research asset.

A URL or URN is useful provenance but **does not replace the exact PDF/export**. For central source exports `corpus/files.tsv` records the original filename, SHA-256, exact coverage, intended repository path and preservation state.

The preserved original must remain byte-identical. OCR, crops, renders, rotations or other derivatives are stored separately and point back to the original file ID.

The repository is public. Where an archive export is marked `InC/1.0` and no redistribution authority has been established, the exact binary is not committed publicly by default. The preservation blocker remains explicit. A checksum + URN is not labelled equivalent backup.

## Current Reg. Ii 5 project

Historical project root:

- `ACT-THHSTAW-EGA-REG-II-5` — *Registratur für die Superintendenz Neustadt an der Orla (Auszug)*.

Current active scope:

- Knau passage fol. 61v–63r inside the internal Ziegenrück protocol `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`.

Sources currently used:

1. **internal / principal** — Reg. Ii 5 / `00000129`, Ziegenrück protocol 55v–66v; active Knau locus 61v–63r.
2. **external / comparison** — Reg. Ii 4 Bd. II / `00000089`, Knau locus 306v–309r.
3. **external / control** — Reg. Ii 3 / `00000235`, *Pfarreinkommen Gössitz, Knau ...*, 303r–306r.
4. **external / context** — Reg. Ii 3 / Neustadt protocol 41r–63v.

Their canonical identities and structural `part_of` relations live in the corpus. Their research roles live only in the project source register.

## Project relations versus source relations

`projects/relationships.tsv` is only for relations between historically independent projects.

`corpus/relationships.tsv` describes claims about source nodes, including structural `part_of`.

Never use a project relation to encode source structure, and never let a project relation prove a historical/source relation.

## Generic research gates

`methodology/research-gates.md` defines once for comparable projects:

`G1 source/transmission basis → G2 diplomatic representation → G3 internal palaeographic analysis → G4 controlled witness comparison → G5 critical consolidation/validation → G6 scholarly edition`

A project records its actual evidence-based state in `STATUS.md`; it does not copy/redefine the gates.

GitHub may use project-scoped Milestones to group discrete Issues. A Milestone is only a work-planning mirror; closing it does not establish scholarly gate attainment.

## Core scientific principles

1. Evidence before plausibility.
2. Provenance before fusion.
3. Catalogue claims remain catalogue claims.
4. Witness independence.
5. Uncertainty remains visible.
6. Source phenomenon is not reading confidence.
7. Diplomatic text, normalization/identification and historical interpretation remain distinct.
8. Human auditability is required.
9. AI method compliance is not independent expert validation.
10. Repeated model output is not independent evidence.
11. Digital mediation is part of source criticism.
12. Exact inspected exports are part of the evidential chain.
13. Research outcome before system development.
14. No chat knowledge monopoly.
15. One fact, one canonical owner; reference rather than copy.
16. A pilot may change generic method only after explicit generalisability review.

## Feedback and anti-drift

- source identity/file/crosswalk/structure correction → verify → update canonical corpus owner → update affected project consequences;
- project root correction → update `project_source_id` → re-resolve all used sources through `part_of`;
- project source role/locus changes → update project `sources/sources.tsv`, not canonical source identity or structural membership;
- project discovers generic weakness → project learning/status → generalisability check → methodology/DECISIONS → bounded consistency pass;
- deferred improvement → trigger-based GitHub Issue;
- ordinary implementation detail → Git history.

## Human-in-the-loop

The assistant applies historical, archival, palaeographic, editorial and technical expertise, maintains repository state and exposes evidence/uncertainty. The user controls research purpose, source access only they can provide, rights/authority facts and consequential publication/use decisions. Qualified specialists are an escalation/validation layer for consequential specialist claims.

## GitHub navigation

Milestones organize targets/phases, with families defined in `MILESTONES.md`:
- `GOV-*` — governance/architecture work;
- `<project> / G*` — discrete scholarly work toward a project gate.

Labels classify domains. Open Issues without a Milestone remain backlog/deferred. GitHub metadata never replaces canonical repository records.

## Repository structure

```text
GOVERNING_OBJECTIVE.md
AGENTS.md
DECISIONS.md
MILESTONES.md
README.md
methodology/
  historical-source-workflow.md
  research-gates.md
  project-lifecycle.md
  source-and-provenance.md
  transcription-guidelines.md
  evidence-policy.md
  quality-and-learning.md
  ai-governance.md
  workflow.md
  maintenance.md
templates/
  project/
    project.yml
    STATUS.md
corpus/
  sources.tsv
  files.tsv
  relationships.tsv
  events.tsv
  source-data/
    <source_id>/
      crosswalk.tsv
  source-files/
    <source_id>/
      original/
entities/
projects/
  relationships.tsv
  ega-reg-ii-5-knau/
    project.yml
    STATUS.md
    sources/
      sources.tsv
      inspection-log.tsv
    transcription/
    apparatus/
    palaeography/
    research/
    context/
```

Optional project directories exist only when real work requires them.

## Definition of done for repository architecture

Another capable researcher/agent, given repository + controlled source material, can determine:
- which historically independent source node defines each project;
- which used sources are structurally internal versus external;
- what the current active research scope is;
- which source/locus is principal/comparison/control/context;
- which exact PDF/export was inspected, its checksum and preservation state;
- where reusable crosswalks live;
- what source relationships are actually evidenced;
- what was inspected versus catalogued;
- what the current transcription says and where it is uncertain/incomplete;
- which generic gate is active and which concrete gaps remain;
- what the exact next research action is;
- which GitHub items are planning metadata rather than scholarly truth.

If old chat, manually duplicated membership flags, or reconciliation of contradictory project/source truth are required, the architecture has drifted and must be repaired.
