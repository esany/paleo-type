# paleo-type

Lean, evidence-based workspace for the transparent transcription, source criticism and scholarly analysis of early modern handwritten sources.

## Purpose

`paleo-type` helps a non-specialist reliably unlock early modern handwritten sources without turning the research task into a software project or requiring the user to become a historian, archivist or palaeographer.

The research source and scholarly result are the product. Tooling is support infrastructure only.

## Three repository layers

### 1. METHOD
`methodology/`, `AGENTS.md`, `DECISIONS.md`

Reusable scholarly method, research gates, evidence rules, AI/human validation rules and durable cross-project decisions. **No concrete pilot-source facts belong here unless used only as a clearly non-normative example.**

### 2. CORPUS
`corpus/`, `entities/`

Canonical identities, digital instantiations, source/event/entity relationships and normalized identities that span individual projects.

### 3. PROJECT
`projects/<id>/`

Concrete source observations, transcription, palaeographic evidence, comparison/collation, historical interpretation, project-specific decisions, current gate state and next action.

Generalisation test:

> valid rule for another comparable manuscript project → METHOD; cross-source identity/context → CORPUS; concrete source/research fact → PROJECT.

The current pilot project is `projects/ega-reg-ii-5-knau/`. It **tests** the generic method; it does not define it.

## Start here

### Human

1. Read this README.
2. For current Knau research state: `projects/ega-reg-ii-5-knau/STATUS.md`.
3. For the generic research path and requirements: `methodology/research-gates.md`.
4. For the authoritative scholarly procedure: `methodology/historical-source-workflow.md`.
5. For scheduled governance/structural work and backlog semantics: `MILESTONES.md`.

### AI continuing research

1. read `AGENTS.md`;
2. read the active project's `STATUS.md`;
3. read the active gate in `methodology/research-gates.md`;
4. inspect relevant corpus/source records when identity, files or relations matter;
5. read relevant project decisions/LEARNINGS and only the methodology needed for the current task;
6. continue from project `NEXT ACTION` unless inspected evidence requires a change.

**Old chat must never be required to reconstruct durable research state.**

## Where truth lives

- `README.md` — repository purpose/map.
- `AGENTS.md` — binding operating/quality guardrails.
- `DECISIONS.md` — consequential cross-project rationale.
- `MILESTONES.md` — sequencing semantics for admitted governance/structural work and backlog; never scholarly research state.
- `methodology/historical-source-workflow.md` — authoritative end-to-end scholarly method.
- `methodology/research-gates.md` — canonical reusable G1–G6 scholarly maturity requirements.
- other `methodology/*.md` — detailed reusable method.
- `corpus/sources.tsv` — canonical archival/source inventory and inspection stage.
- `corpus/files.tsv` — canonical external/digital file/instantiation manifest.
- `corpus/relationships.tsv` — explicit source/event/entity relationship claims.
- `corpus/events.tsv` — shared administrative/historical event context.
- `entities/` — recurring normalized identities; never manuscript readings.
- project `project.yml` — stable project identity/scope.
- project `STATUS.md` — current generic gate state, project-specific gaps, validation state and exact next action.
- project `sources/` — project-specific source/folio/image/export mappings.
- project `transcription/` — source transcription.
- project `apparatus/decisions.tsv` — concrete source/reading revisions/adjudications.
- project `palaeography/` — source-specific palaeographic evidence.
- project `research/` — external-source inspection audit.
- project `LEARNINGS.md` — concrete project failures/corrections and possible generalisation candidates.
- GitHub Issues — bounded deferred/discrete work, never current research truth.
- GitHub Milestones — navigation mirror for work admitted to a bounded governance/structural sequence; never G1–G6 or research state.
- Wiki — optional end-user explanation only.
- Chat — transient workspace only.

## Authoritative scholarly method

`methodology/historical-source-workflow.md` integrates the required professional domains:

- archival science / diplomatics;
- palaeography;
- scholarly editing / textual criticism;
- historical source criticism;
- source-type/domain historical knowledge;
- research-data stewardship / Good Research Practice;
- lean research software/data engineering.

Standards/reference frameworks include ICA Records in Contexts concepts, TEI P5 as an interoperability/conceptual transcription/edition model and applicable Good Research Practice / scholarly-edition guidance. Standards guide scholarly distinctions; they do not force premature RDF, TEI authoring or other infrastructure.

## Generic research gates

`methodology/research-gates.md` defines once for all comparable projects:

`G1 source/transmission basis → G2 diplomatic representation → G3 internal palaeographic analysis → G4 controlled witness comparison → G5 critical consolidation/validation → G6 scholarly edition`

A project records only its concrete state against these requirements in `STATUS.md`. It does not copy/redefine the gates.

**G1–G6 are not GitHub Milestones.** They are evidence-based scholarly maturity states. GitHub Milestones are reserved for bounded admitted work sequences such as the governance/architecture review defined in `MILESTONES.md`.

## Core scientific principles

1. **Evidence before plausibility.** Semantic coherence never creates manuscript text.
2. **Provenance before fusion.** Related records remain distinct until relationships are demonstrated.
3. **Catalogue claims remain catalogue claims.** Metadata does not become manuscript content or textual dependence.
4. **Witness independence.** A clearer parallel may inform analysis but cannot overwrite another witness.
5. **Uncertainty remains visible.** Unresolved is a legitimate scholarly result.
6. **Source phenomenon ≠ reading confidence.** Unclear reading, illegibility/gap, supply, addition, deletion, damage and research status remain distinct when applicable.
7. **Diplomatic text ≠ normalization/identification ≠ historical interpretation.**
8. **Human auditability is required.** A principal transcription must have a human-readable source/locus view; machine fragments alone are insufficient.
9. **AI method compliance ≠ independent expert validation.** Record what qualified human review actually occurred.
10. **No AI self-confirmation.** Repeated model output is not independent evidence.
11. **Digital mediation is part of source criticism.** Folio, portal image, PDF/export and file identity remain distinct.
12. **Research outcome before system development.** Add technology only for demonstrated scholarly/repetitive need.
13. **No chat knowledge monopoly.** Durable facts, decisions, gaps and next actions live in GitHub.

## Decision and learning model

- general method/rule → `methodology/`;
- durable cross-project design rationale → `DECISIONS.md`;
- concrete manuscript/source adjudication → project `apparatus/decisions.tsv`;
- project-specific failure/correction → `LEARNINGS.md`;
- if a project learning is genuinely general → promote the corrective rule to methodology, while the concrete incident remains in the project;
- deferred improvement → GitHub Issue;
- admitted governance/structural sequence → `MILESTONES.md` + GitHub Milestone mirror;
- ordinary implementation detail → Git history.

## Human-in-the-loop

The assistant is responsible for applying historical, archival, palaeographic, editorial and technical expertise, maintaining research state and exposing uncertainty/evidence.

The user controls research purpose, priorities, source access only they can provide, rights/confidentiality facts and consequential publication/use decisions. The user is not expected to adjudicate specialist readings they cannot independently validate.

Qualified independent specialists are an escalation/validation layer for consequential specialist claims. Their review status must be distinguishable from AI-assisted method-compliant work.

## GitHub navigation

GitHub metadata is presentation/navigation only:

- Milestones organize bounded work that has been explicitly admitted into an active/approved governance or structural sequence; the exact M1–M4 semantics live in `MILESTONES.md`;
- open Issues without a Milestone remain backlog/deferred until their documented trigger is met;
- G1–G6 scholarly research gates are **never** mirrored as Milestones; project `STATUS.md` remains canonical for research maturity;
- Issues + topical labels expose deferred/discrete work by subject;
- PRs provide human-readable records for cohesive repo-wide changes;
- tags/releases mark intentionally frozen reproducible research checkpoints.

GitHub metadata never replaces canonical repository records.

## Repository structure

```text
AGENTS.md
DECISIONS.md
MILESTONES.md
README.md
methodology/
  historical-source-workflow.md
  research-gates.md
  transcription-guidelines.md
  source-and-provenance.md
  evidence-policy.md
  quality-and-learning.md
  ai-governance.md
  workflow.md
  maintenance.md
corpus/
entities/
projects/
  ega-reg-ii-5-knau/
    STATUS.md
    LEARNINGS.md
    project.yml
    sources/
    transcription/
    palaeography/
    apparatus/
    research/
    context/
```

Create additional structures only when real evidence/workload requires them.

## Definition of done for repository architecture

Another capable researcher/agent, given only repository + accessible source material, can determine:
- what the generic scholarly method requires;
- which requirements are framework-wide versus corpus- or project-specific;
- what each source/instantiation actually is;
- what was inspected versus merely catalogued;
- what the current project text says and where it is uncertain/incomplete;
- which generic gate is active and which concrete project gaps remain;
- why consequential decisions were made;
- what has/has not received independent expert review;
- what the exact next research action is;
- which governance/structural issues are scheduled versus intentionally deferred in backlog.

If recovering old chat is necessary, the work is not fully persisted.