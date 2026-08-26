# paleo-type

Lean, evidence-based workspace for transparent transcription, source criticism and scholarly analysis of early modern handwritten sources.

## Purpose

`paleo-type` helps a non-specialist reliably unlock early modern handwritten sources without turning the research task into a software project or requiring the user to become a historian, archivist or palaeographer. The research source and scholarly result are the product; tooling is support infrastructure only.

## Three repository layers

### 1. METHOD
`methodology/`, `AGENTS.md`, `DECISIONS.md`, `templates/`

Reusable scholarly method, research gates, evidence rules, project lifecycle rules, AI/human validation rules and durable cross-project decisions. Concrete pilot-source facts do not belong here.

### 2. CORPUS
`corpus/`, `entities/`

Canonical source identities, digital instantiations, historical/source relationships, events and normalized identities spanning projects.

### 3. PROJECT
`projects/<id>/`, `projects/relationships.tsv`

Concrete source-unit work or bounded research-scope work, including transcription, comparison/collation, interpretation, project-specific decisions, current state and cross-project research organisation.

Generalisation test:

> valid rule for another comparable manuscript project → METHOD; cross-source identity/context → CORPUS; concrete source/research fact → PROJECT.

The Knau benchmark is a `research-scope` pilot. It tests the generic method; it does not define it.

## Start here

### Human
1. Read this README.
2. For current Knau research state: `projects/ega-reg-ii-5-knau/STATUS.md`.
3. For generic research gates: `methodology/research-gates.md`.
4. For the authoritative scholarly procedure: `methodology/historical-source-workflow.md`.
5. For project creation, project kinds, relations and anti-drift rules: `methodology/project-lifecycle.md`.

### AI continuing research
1. read `AGENTS.md`;
2. read the active project's `STATUS.md`;
3. read the active gate in `methodology/research-gates.md`;
4. inspect relevant corpus/source and project-relation records;
5. read only methodology needed for the current task;
6. continue from project `NEXT ACTION` unless inspected evidence requires a change.

Old chat must never be required to reconstruct durable research state.

## Where truth lives

- `README.md` — repository purpose/map.
- `AGENTS.md` — binding operating/quality guardrails.
- `DECISIONS.md` — consequential cross-project rationale.
- `methodology/historical-source-workflow.md` — authoritative end-to-end scholarly method.
- `methodology/research-gates.md` — canonical reusable G1–G6 requirements.
- `methodology/project-lifecycle.md` — canonical project creation/relationship/feedback rules.
- `templates/project/` — minimal project contract; never clone a concrete project as a template.
- `corpus/sources.tsv` — canonical archival/source inventory and inspection stage.
- `corpus/files.tsv` — canonical exact external/digital file/instantiation manifest.
- `corpus/relationships.tsv` — historical/archival/textual source relationship claims.
- `corpus/events.tsv` — shared event/activity context.
- `entities/` — recurring normalized identities; never manuscript readings.
- `projects/relationships.tsv` — research-organisational project-to-project relations only.
- project `project.yml` — stable project identity, kind and bounded scope.
- project `STATUS.md` — actual evidence state, current gate/activity state and exact next action.
- source-unit project `sources/` — reusable source-local image/folio/PDF/export mappings.
- research-scope project `transcription/` — scoped transcription truth.
- project `apparatus/decisions.tsv` — concrete source/reading revisions/adjudications.
- project `palaeography/`, `research/`, `context/`, `LEARNINGS.md` — created only when real evidence/work exists.
- GitHub Issues — bounded deferred work, never current research truth.
- Chat — transient workspace only.

## Project model

A **source is not automatically a project**. A corpus source is inventoried when relevant; a project is created only when there is a bounded research responsibility.

Two project kinds currently exist:

- `source-unit` — reusable source-local work for one canonical archival witness/source, especially crosswalks and source-wide inspection state;
- `research-scope` — a bounded question/locus/edition task that may use one principal source and several comparison/control/context sources.

Create every new project from `templates/project/`, never by copying an existing project. Required invariants and the creation check are in `methodology/project-lifecycle.md`.

### Project relations versus source relations

`projects/relationships.tsv` describes how **our projects** interact, e.g. `scopes-source-unit`, `compares-with`, `uses-as-control`, `uses-as-context`.

`corpus/relationships.tsv` describes claims about **historical/archival/textual sources**.

A project relation never proves a source relation. For example, `compares-with` does not establish copying, dependence or textual equivalence.

## Generic research gates

`methodology/research-gates.md` defines once for all comparable projects:

`G1 source/transmission basis → G2 diplomatic representation → G3 internal palaeographic analysis → G4 controlled witness comparison → G5 critical consolidation/validation → G6 scholarly edition`

A project records only its concrete state against these requirements in `STATUS.md`; it does not redefine the gates.

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
12. Research outcome before system development.
13. No chat knowledge monopoly.
14. One fact, one canonical owner; consumers reference rather than copy.
15. A pilot may feed back a generalisable correction only through explicit generalisability review.

## Feedback and learning

- concrete source/project discovery → owning project record;
- source-level correction discovered in scoped research → verify and update source-unit/corpus owner, then propagate consequences to related projects;
- generic weakness → project learning/status → generalisability check → methodology/DECISIONS update → bounded consistency pass;
- deferred improvement → trigger-based GitHub Issue;
- ordinary implementation detail → Git history.

This feedback loop allows the system to learn without letting one pilot silently define general method.

## Human-in-the-loop

The assistant applies historical, archival, palaeographic, editorial and technical expertise, maintains research state and exposes evidence/uncertainty. The user controls purpose, priorities, source access only they can provide, rights/confidentiality facts and consequential publication/use decisions. Qualified specialists are an escalation/validation layer for consequential specialist claims.

## Repository structure

```text
AGENTS.md
DECISIONS.md
README.md
methodology/
  historical-source-workflow.md
  research-gates.md
  project-lifecycle.md
  transcription-guidelines.md
  source-and-provenance.md
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
entities/
projects/
  relationships.tsv
  ega-reg-ii-5-00000129/      # source-unit
  ega-reg-ii-4-bd-ii-00000089/ # source-unit
  ega-reg-ii-3-00000235/      # source-unit
  ega-reg-ii-3-00000197/      # source-unit
  ega-reg-ii-5-knau/          # research-scope pilot
```

Optional project directories are created only when real work exists. No empty future-proof structure.

## Definition of done for repository architecture

Another capable researcher/agent, given only repository + accessible source material, can determine:
- what the generic scholarly method requires;
- what each source/instantiation actually is;
- what each project is for and whether it is `source-unit` or `research-scope`;
- which project relations exist and why;
- which source relationships are actually evidenced;
- where reusable source-local mappings live;
- what was inspected versus merely catalogued;
- what the current project text says and where it is uncertain/incomplete;
- which generic gate is active and which concrete gaps remain;
- what changed when project findings fed back into corpus or method;
- what the exact next research action is.

If recovering old chat or manually reconciling duplicated project truth is necessary, the architecture has drifted and must be repaired.
