# paleo-type

Lean, evidence-based workspace for the transparent transcription, source criticism and scholarly analysis of early modern handwritten sources.

## Purpose

`paleo-type` helps a non-specialist reliably unlock early modern handwritten sources without turning the research task into a software project or requiring the user to become a historian, archivist or palaeographer.

The research sources and scholarly result are the product. Tooling is support infrastructure only.

## Three repository layers

### 1. METHOD
`methodology/`, `AGENTS.md`, `DECISIONS.md`, `templates/`

Reusable scholarly method, research gates, evidence rules, project/source-group lifecycle rules, AI/human validation rules and durable cross-project decisions. Concrete pilot-source facts do not belong here.

### 2. CORPUS
`corpus/`, `entities/`

Canonical archival source records, exact digital instantiations, reusable source-wide mappings, historical/source relationships, events and recurring normalized identities.

### 3. PROJECT
`projects/<id>/`, `projects/relationships.tsv`

A project is a **bounded historical investigation / source-unlocking undertaking over a coherent source group**. It owns project-specific source roles/loci, transcription, comparison/collation, interpretation, decisions, current evidence/gate state and exact next action.

Generalisation test:

> reusable rule for another comparable manuscript project → METHOD; canonical source/file/relationship truth → CORPUS; concrete investigation/source-role/reading/state → PROJECT.

The current benchmark is `projects/ega-reg-ii-5-knau/`. It tests the generic method; it does not define it.

## Start here

### Human
1. Read this README.
2. For the current Knau investigation: `projects/ega-reg-ii-5-knau/STATUS.md`.
3. For its source group: `projects/ega-reg-ii-5-knau/sources/sources.tsv`.
4. For generic research gates: `methodology/research-gates.md`.
5. For project/source-group creation and anti-drift rules: `methodology/project-lifecycle.md`.
6. For source identity, exact exports and preservation: `methodology/source-and-provenance.md`.
7. For GitHub work sequencing: `MILESTONES.md`.

### AI continuing research
1. read `AGENTS.md`;
2. read the active project's `STATUS.md`;
3. read its `sources/sources.tsv`;
4. read the active gate in `methodology/research-gates.md`;
5. inspect relevant `corpus/sources.tsv`, `corpus/files.tsv`, source-data crosswalks and source relationships;
6. read only methodology needed for the current task;
7. continue from project `NEXT ACTION` unless inspected evidence requires a change.

Old chat must never be required to reconstruct durable research state.

## What a project is

A project follows the **historical investigation**, not the storage object.

A new archive record or PDF does **not** automatically create a project. A project is created when there is a coherent investigation / Erschließungsvorhaben over a bounded source group.

The source group may contain:
- one principal source;
- comparison witnesses;
- control sources;
- contextual sources;
- several co-equal sources.

Each source remains an independently identified archival record. If two records share the same volume/signature but have separate archival record IDs/titles/loci, they stay separate sources.

For the current Knau investigation this means, among others, that the two Reg. Ii 3 records are distinct:
- *Visitation in Neustadt an der Orla* (`00000197`, fol. 41r–63v);
- *Pfarreinkommen Gössitz, Knau ...* (`00000235`, fol. 303r–306r).

They are not collapsed merely because both are in `ThHStAW, EGA, Reg. Ii 3`.

## Where truth lives

- `README.md` — repository purpose/map.
- `AGENTS.md` — binding operating/quality guardrails.
- `DECISIONS.md` — consequential cross-project rationale.
- `MILESTONES.md` — GitHub work-planning semantics; never scholarly truth.
- `methodology/historical-source-workflow.md` — authoritative end-to-end scholarly method.
- `methodology/research-gates.md` — canonical reusable G1–G6 requirements.
- `methodology/project-lifecycle.md` — project/source-group creation, relations and feedback rules.
- `methodology/source-and-provenance.md` — source identity, exact exports and preservation rules.
- `templates/project/` — minimal new-project contract; never clone a concrete project.
- `corpus/sources.tsv` — canonical archival/source-record inventory.
- `corpus/files.tsv` — exact file/instantiation manifest with filename, SHA-256, coverage, storage/preservation state, intended repository path and rights state.
- `corpus/source-data/<source_id>/` — reusable source-wide crosswalks/mappings.
- `corpus/relationships.tsv` — historical/archival/textual source relationship claims.
- `corpus/events.tsv` — shared event/activity context.
- `entities/` — recurring normalized identities; never manuscript readings.
- project `project.yml` — investigation identity and bounded research object.
- project `sources/sources.tsv` — human-readable source group: source ID, archival title, project role, relevant locus and primary file.
- project `sources/inspection-log.tsv` — project-specific inspection audit when useful.
- project `STATUS.md` — actual evidence/gate state, preservation gaps and exact next action.
- project `transcription/`, `apparatus/`, `palaeography/`, `research/`, `context/`, `LEARNINGS.md` — created only when real work exists.
- `projects/relationships.tsv` — relations only between genuine research projects; currently it may legitimately be empty.
- GitHub Issues — bounded deferred/discrete work, never current research truth.
- GitHub Milestones — planning mirrors for admitted work, never evidence or gate truth.
- Chat — transient workspace only.

## Source files and preservation

The exact original archive export actually used in research is a first-class research asset.

A URL or URN is useful provenance but **does not replace the exact PDF/export**. For central source exports `corpus/files.tsv` records the original filename, SHA-256, exact coverage, intended repository path and preservation state.

The preserved original must remain byte-identical. OCR, crops, renders, rotations or other derivatives are stored separately and point back to the original file ID.

The repository is public. Where an archive export is marked `InC` and no redistribution authority has been established, `paleo-type` must not pretend a public Git commit is authorized. Such a file is marked `preservation-blocked-rights` until an adequate rights/authority basis permits repository storage or another controlled repository-integrated preservation location is established. A checksum + URN is not labelled equivalent backup.

## Current Knau source group

`projects/ega-reg-ii-5-knau/sources/sources.tsv` currently registers four distinct records:

1. principal — Reg. Ii 5 / `00000129`, Knau fol. 61v–63r;
2. comparison — Reg. Ii 4 Bd. II / `00000089`, Knau fol. 306v–309r;
3. control — Reg. Ii 3 / `00000235`, *Pfarreinkommen Gössitz, Knau ...*, fol. 303r–306r;
4. context — Reg. Ii 3 / `00000197`, *Visitation in Neustadt an der Orla*, fol. 41r–63v.

Their canonical identities remain in `corpus/sources.tsv`; their exact PDFs/checksums remain in `corpus/files.tsv`; reusable crosswalks live under `corpus/source-data/`.

## Project relations versus source relations

`projects/relationships.tsv` is only for relations between **genuine investigations**, for example a later project extending or sharing sources with another project.

`corpus/relationships.tsv` describes claims about **historical/archival/textual sources**.

Never create project nodes merely to express source use, and never let a project relation prove a source relation.

## Generic research gates

`methodology/research-gates.md` defines once for comparable projects:

`G1 source/transmission basis → G2 diplomatic representation → G3 internal palaeographic analysis → G4 controlled witness comparison → G5 critical consolidation/validation → G6 scholarly edition`

A project records its actual evidence-based state in `STATUS.md`; it does not copy/redefine the gates.

GitHub may use project-scoped Milestones such as `ega-reg-ii-5-knau / G2 — Diplomatic representation` to group discrete Issues. A Milestone is only a work-planning mirror; closing it does not establish scholarly gate attainment.

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

- project discovers source identity/file/crosswalk correction → verify → update canonical corpus owner → update only affected project consequences;
- project source-group role/locus changes → update project `sources/sources.tsv`, not canonical source identity;
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
      crosswalk.tsv        # only when source-wide mapping exists
  source-files/
    <source_id>/
      original/            # exact bytes when rights/authority permit
entities/
projects/
  relationships.tsv        # only genuine project-to-project relations
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
- what the investigation is;
- which distinct archival records form its source group and why;
- which record/locus is principal/comparison/control/context;
- which exact PDF/export was inspected, its checksum and preservation state;
- where reusable crosswalks live;
- what source relationships are actually evidenced;
- what was inspected versus catalogued;
- what the current transcription says and where it is uncertain/incomplete;
- which generic gate is active and which concrete gaps remain;
- what the exact next research action is;
- which GitHub items are planning metadata rather than scholarly truth.

If old chat, artificial source-as-project containers, or manual reconciliation of duplicate source truth are required, the architecture has drifted and must be repaired.
