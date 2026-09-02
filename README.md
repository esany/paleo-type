# paleo-type

Lean, evidence-based workspace for the transparent transcription, source criticism and scholarly analysis of early modern handwritten sources.

## Purpose

The highest-order repository purpose, precedence and human change authority are defined once in `GOVERNING_OBJECTIVE.md`. This README is an **orientation view**, not a second canonical state store.

`paleo-type` helps a non-specialist reliably unlock early modern handwritten sources without turning the research task into a software project or requiring the user to become a historian, archivist or palaeographer.

The research sources and scholarly result are the product. Tooling is support infrastructure only.

## Three repository layers

### METHOD

`methodology/`, `AGENTS.md`, `DECISIONS.md`, `templates/`

Reusable scholarly method, research gates, evidence rules, Project/Source lifecycle rules, AI/human validation rules and durable cross-project decisions. Concrete source facts do not belong here.

### CORPUS

`corpus/`, `entities/`

Canonical historical/documentary Source nodes, exact digital File instantiations, reusable source-wide mappings, structural/historical/textual relationships, events and recurring normalized identities.

### PROJECT

`projects/<id>/`, `projects/relationships.tsv`

A Project is durable scholarly state created because a concrete research purpose has been established. Source/File existence, archival structure, `part_of`, upload order, place focus or a temporary comparison bundle does not create a Project.

Once a Project exists, `project.yml: project_source_id` supplies its canonical documentary Source anchor for deterministic structural resolution. The anchor does **not** establish Project existence, purpose, current priority or `NEXT ACTION`.

Project-relative Source use is represented in `source-uses.tsv`; explicit Project-use→File evidence is represented separately in `research/use-evidence.tsv` when needed. Structural `root/internal/external` status is derived from `project_source_id + part_of*`, never copied as Project truth.

Generalisation test:

> reusable rule for another comparable manuscript investigation → METHOD; canonical Source/File/relationship truth → CORPUS; concrete scholarly state for one purpose-established investigation → PROJECT.

A pilot tests generic method; it does not define it. Project-specific findings are promoted to METHOD only after a generalisability check.

## Start here

### Human

1. Read this README for orientation.
2. Read `GOVERNING_OBJECTIVE.md` for purpose, precedence and Human-in-the-loop authority.
3. Open the relevant `projects/<id>/project.yml` for Project purpose, documentary anchor and current scope.
4. Open that Project's `STATUS.md` for actual gate state, gaps, evidence-access limits and authorized `NEXT ACTION` if one exists.
5. Open `source-uses.tsv` and `research/use-evidence.tsv` for Project-relative Source use and concrete File evidence.
6. Use `methodology/project-lifecycle.md`, `methodology/source-and-provenance.md` and `methodology/research-gates.md` for reusable rules.

### AI continuing research

1. read `GOVERNING_OBJECTIVE.md` and `AGENTS.md`;
2. read the active Project's `project.yml` and `STATUS.md`;
3. establish and load all canonical rules/requirements applicable to the concrete task;
4. read Project `source-uses.tsv` and explicit use-evidence when relevant;
5. inspect relevant `corpus/sources.tsv`, `corpus/files.tsv`, source-data crosswalks and Source relations;
6. use the source resolver / generated Project context rather than reconstructing Project membership, research functions, File evidence or priorities from names/chat;
7. continue from an authorized `NEXT ACTION` when one exists; do not invent one from historical work state or Source structure.

Old chat must never be required to reconstruct durable research state.

## What a Project is

A Project exists because a scholarly investigation is worth maintaining as durable work state.

Every Project therefore records at least:

- `research_object` — why the investigation exists;
- `project_source_id` — its post-selection documentary Source anchor;
- `active_scope` — the currently declared scope, including an explicit statement when no new owner-selected active scope exists;
- `source_register` — the canonical Project→Source use owner, currently `source-uses.tsv`;
- `canonical_status_file` — the restart/status owner.

A Source may be internal to several purpose-established Projects by structure; that structural fact does not itself create, merge or prioritize those Projects.

## Current Project directories

The current corpus has three owner-accepted Projects:

- `projects/ega-reg-ii-3/`;
- `projects/ega-reg-ii-4-bd-ii/`;
- `projects/ega-reg-ii-5-knau/` — legacy directory/id retained for lossless path continuity; its current Project purpose and scope are defined only by its `project.yml` and `STATUS.md`, not by the string `knau` in the directory name.

Do not copy their current scopes into this README. Read the Project owners directly or use the rebuildable `tools/project_context.py` view.

## Where truth lives

- `GOVERNING_OBJECTIVE.md` — highest-order scholarly purpose, precedence and human material-change authority.
- `AGENTS.md` — binding stable operating/quality guardrails.
- `DECISIONS.md` — consequential cross-project rationale and authority history.
- `methodology/historical-source-workflow.md` — authoritative end-to-end scholarly method.
- `methodology/research-gates.md` — canonical reusable G1–G6 requirements.
- `methodology/project-lifecycle.md` — Project creation, documentary anchoring, Project→Source use and restartability rules.
- `methodology/source-and-provenance.md` — Source identity, part–whole structure, exact exports and preservation/access distinctions.
- `corpus/source-contract.json` + `tools/source_contract.py` — deterministic Source/File/Project-use contract and resolver.
- `corpus/sources.tsv` — canonical Source-node inventory.
- `corpus/files.tsv` — exact File/instantiation identity, SHA-256, coverage, storage/preservation and rights state.
- `corpus/source-data/<source_id>/` — reusable source-wide crosswalks/mappings.
- `corpus/relationships.tsv` — structural `part_of` and other evidenced Source-relation claims.
- `entities/` — recurring normalized identities; never manuscript readings.
- project `project.yml` — Project purpose, documentary anchor and current scope.
- project `source-uses.tsv` — Project-relative Source research functions and relevant loci.
- project `research/use-evidence.tsv` — explicit concrete Project-use→File binding when needed.
- project `STATUS.md` — actual evidence/gate/restart state and authorized `NEXT ACTION` when one exists.
- project scholarly work files — observations, transcription, apparatus, palaeography, research evidence and decisions.
- `tools/project_context.py` — rebuildable Project-context view; never canonical truth.
- GitHub Issues/Milestones/PRs — work, review and authority/audit metadata; never manuscript or Source truth.
- Chat — transient workspace only.

## Source files, preservation and research-ready evidence

The exact original archive export actually used in research is a first-class research asset.

A URL or URN is useful provenance but does **not** replace the exact PDF/export. `corpus/files.tsv` records exact File identity, SHA-256, coverage, storage/preservation and rights state.

Keep these properties distinct:

- **identifiable** — the exact File/Source is known;
- **preserved/bytes available** — exact bytes are held at a verified path;
- **reproducible** — a defined derivative can be recreated from an established parent;
- **staged/inspectable in the target context** — the current authorized work context can actually open the evidence needed for the task.

For visual source work, byte availability alone is not proof that evidence is research-ready in a fresh target context.

Repository visibility is not a rights conclusion. Redistribution/storage decisions follow the recorded rights/authority state, not whether the GitHub repository happens to be public or private.

## Project relations versus Source relations

`projects/relationships.tsv` is only for explicit relations between genuine Projects.

`corpus/relationships.tsv` describes claims about Source nodes, including structural `part_of`.

Never use a Project relation to encode Source structure, derive Project→Project relations from Project→Source use, or let a Project relation prove a historical/Source relation.

## Generic research gates

`methodology/research-gates.md` defines once for comparable projects:

`G1 source/transmission basis → G2 diplomatic representation → G3 internal palaeographic analysis → G4 controlled witness comparison → G5 critical consolidation/validation → G6 scholarly edition`

A Project records only its actual evidence-based state against those gates in `STATUS.md`. GitHub Milestones are work-planning mirrors and do not prove scholarly gate attainment.

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
15. One fact, one canonical owner; reference or derive rather than copy.
16. Project-specific evidence changes generic method only after a generalisability review.
17. Deterministic PASS, procedural assurance, scholarly judgement and Human Owner acceptance are different evidence classes.

## Feedback and anti-drift

- Source identity/File/crosswalk/structure correction → verify → update canonical Corpus owner → update affected Project consequences;
- Project purpose/scope change → update `project.yml` with required authority; do not infer it from Source structure;
- Project documentary-anchor correction → update `project_source_id` → re-resolve structural consequences;
- Project→Source research-function/locus changes → update `source-uses.tsv`;
- concrete use→File evidence changes → update `research/use-evidence.tsv`;
- Project discovers generic weakness → project learning/status → generalisability check → methodology/DECISIONS/contract if justified → regression when deterministic;
- human-facing summaries/context → derive/reference canonical owners rather than maintaining parallel truth;
- deferred improvement → trigger-based GitHub Issue;
- ordinary implementation detail → Git history.

## Repository structure

```text
GOVERNING_OBJECTIVE.md
AGENTS.md
DECISIONS.md
README.md
methodology/
templates/
corpus/
  sources.tsv
  files.tsv
  relationships.tsv
  source-contract.json
  source-data/
entities/
projects/
  relationships.tsv
  ega-reg-ii-3/
    project.yml
    STATUS.md
    source-uses.tsv
  ega-reg-ii-4-bd-ii/
    project.yml
    STATUS.md
    source-uses.tsv
  ega-reg-ii-5-knau/
    project.yml
    STATUS.md
    source-uses.tsv
    sources/
      inspection-log.tsv
    research/
      use-evidence.tsv
    transcription/
    apparatus/
    palaeography/
tools/
  source_contract.py
  source_intake.py
  project_context.py
tests/
```

Optional Project directories exist only when real work requires them.

## Definition of done for repository architecture

Another capable researcher/agent, given repository + controlled source material, can determine without old chat:

- why each Project exists and what its current scope is;
- which canonical Source anchors it documentarily;
- which used Sources are structurally internal versus external by derivation;
- which project-relative research functions/loci each used Source serves;
- which exact File supports each use when explicit use-evidence exists;
- where reusable crosswalks live and what they actually establish;
- what Source relations are evidenced;
- what was inspected versus catalogued;
- what the current transcription says and where it is uncertain/incomplete;
- what evidence is identifiable/reproducible versus actually accessible/staged for the next task;
- which generic gate is active and which concrete gaps remain;
- whether an authorized `NEXT ACTION` exists;
- which outputs are canonical versus rebuildable/derived;
- which GitHub items are planning/review metadata rather than scholarly truth.

If old chat, duplicated structural flags, inferred File evidence, stale orientation prose or reconciliation of contradictory Project/Source truth is required, the architecture has drifted and must be repaired.
