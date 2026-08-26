# paleo-type

Lean, evidence-based workspace for the transparent transcription, source criticism and scholarly analysis of early modern handwritten sources.

## Purpose

`paleo-type` helps a non-specialist reliably unlock early modern handwritten sources without turning the research task into either a software project or a demand that the user become a trained historian, archivist or palaeographer.

The repository now has two linked scopes:

1. **Corpus layer** — identify, relate and prioritize the available archival records and their digital instantiations.
2. **Research projects** — transcribe, collate and interpret concrete source passages, beginning with the Knau visitation material.

The research source is the product. Tooling and standards implementations are support infrastructure only.

## Start here

### Human

Read this README. It is the shortest complete map of the repository.

### AI continuing research

Before substantive work:

1. read `AGENTS.md`;
2. inspect `corpus/sources.tsv`, `corpus/relationships.tsv` and `corpus/events.tsv` when source identity/relations matter;
3. read the active project's `STATUS.md`;
4. read relevant `apparatus/decisions.tsv` rows and `LEARNINGS.md`;
5. read only the methodology files needed for the current task;
6. continue from the project's `NEXT ACTION` unless inspected evidence justifies changing it.

**The old chat must never be required to reconstruct the durable research state.**

## Where truth lives

One fact should have one canonical home.

- `README.md` — repository purpose, map and reading path.
- `AGENTS.md` — binding operating guardrails.
- `methodology/` — reusable scholarly method and governance.
- `corpus/sources.tsv` — canonical inventory of archival/source units.
- `corpus/relationships.tsv` — explicit claims about relationships between records, witnesses, events and entities.
- `corpus/events.tsv` — administrative/historical activities that contextualize records without implying textual identity.
- `entities/` — normalized recurring identities; manuscript forms remain in transcriptions.
- project `project.yml` — stable project scope metadata.
- project `STATUS.md` — canonical current state and exact restart point.
- project `sources/` — project-specific image/folio/export crosswalks and source inspection records.
- `transcription/` — current line-level readings.
- `apparatus/decisions.tsv` — substantive revisions, rejections and adjudications.
- `palaeography/` — empirical comparison evidence.
- `research/` — external-source inspection audit.
- `LEARNINGS.md` — project-specific failures/corrections worth preserving.
- GitHub Issues — deferred improvements with explicit triggers; not current research truth.
- Wiki — end-user explanation only; never a second status store.
- Chat — transient workspace only.

## Three truths that must remain separate

### Archival truth
What record is this, where does it belong, how is it described, which folio/locus is involved, which digital instantiation was inspected, and what relationships to other records are actually supported?

### Textual / palaeographic truth
What signs and words are actually visible in a concrete witness?

### Historical truth
What can be inferred about past persons, institutions, events, property, economy, administration and transmission?

No layer may silently rewrite another.

## Required source distinctions

Do not use “source” imprecisely when it matters. Distinguish:

`archival unit → record → witness → locus → instantiation`

and separately:

`research source` (catalogue, finding aid, edition, article, book, etc.).

A DigiRef image number is not a folio. A PDF page is not a manuscript page. An archive catalogue statement is not manuscript content. Keep all numbering/identity systems as separate provenance fields.

The generic rules are in `methodology/source-and-provenance.md`.

## Evidence layers

`OBSERVATION → READING → NORMALIZATION → IDENTIFICATION → INTERPRETATION`

A later layer may use an earlier one; it must never silently rewrite it.

Example:

- manuscript reading: `Knawe`
- normalized place identity: `Knau`

Likewise a historical identification such as Wolf von Gräfendorf cannot overwrite an unresolved surname token in the manuscript.

## Source-inspection discipline

A source supports only what was actually inspected.

Source-status codes used in project audits:

| Code | Meaning |
|---|---|
| P | primary source actually inspected |
| E | scholarly edition actually inspected at relevant passage |
| F | research publication actually inspected at relevant passage |
| K | catalogue/finding aid/metadata only |
| R | review only |
| S | search result/snippet/TOC only |
| H | hypothesis/inference, not a source |

Corpus `inspection_status` answers a different question: how far we have worked with a source (`discovered`, `metadata-inspected`, `images-inspected`, `partially-transcribed`, `fully-transcribed`, `collated`). It is not a confidence score.

## Non-negotiable principles

1. **Evidence before plausibility.** Never turn semantic coherence into a reading.
2. **Provenance before source fusion.** Records that concern the same event/place remain separate until their relationship is demonstrated.
3. **Catalogue claims remain catalogue claims.** “Extract from”, “copy”, “parallel”, dating and record relationships are recorded with their actual evidential level.
4. **Witnesses remain independent.** A clearer B reading may help identify an A token; it may not change the graphemes visible in A.
5. **Uncertainty remains visible.** `working`, `variant`, `unresolved` and `rejected` are legitimate outcomes.
6. **No AI self-confirmation.** Repeated model output is not independent evidence.
7. **Digital mediation is part of source criticism.** Export selection, numbering, cropping, file identity and portal metadata must be traceable.
8. **Research outcome before system development.** Build only what improves a current research result, traceability or repeatable workload.
9. **Validation scales with consequence.** Exploration is light; publication-level claims require stronger independent control.
10. **Corpus completeness must be bounded.** Never claim “all sources” without documented repositories, search strategy, scope and access limitations.
11. **Learning feeds back.** Project failures become general rules only when genuinely generalizable.
12. **No chat knowledge monopoly.** Durable facts, decisions, open problems and deferred design knowledge belong in GitHub.

## Conceptual standards, lean implementation

The repository uses established standards as design references without prematurely adopting their full technical machinery:

- **ICA Records in Contexts (RiC)** — conceptual model for records, instantiations, agents/activities and explicit record relationships.
- **TEI P5** — target interoperability model for manuscript description, witnesses, facsimile linkage, readings and critical apparatus.
- **historical source criticism** — provenance, transmission, dependency, purpose, context and evidential limits.

Current canonical formats remain:

- Markdown for method/status/reasoning;
- TSV for corpus records, relationships, transcriptions and apparatus;
- YAML for small stable project metadata.

No RDF, graph database, TEI-authoring environment, HTR pipeline or web application is justified merely because it is state of the art. Future implementations live as issues until their trigger is reached.

## Repository structure

```text
AGENTS.md
README.md
methodology/
  source-and-provenance.md
  evidence-policy.md
  transcription-guidelines.md
  workflow.md
  quality-and-learning.md
  ai-governance.md
  maintenance.md
corpus/
  sources.tsv
  relationships.tsv
  events.tsv
entities/
  places.tsv
  persons.tsv
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

Create additional entity registries only when repeated real data requires them.

## Current corpus starting point

The corpus currently contains four explicitly separate source units:

- **A** — `ThHStAW, EGA, Reg. Ii 5`, 1533 Ziegenrück extract; principal Knau witness.
- **B** — `ThHStAW, EGA, Reg. Ii 4 Bd. II`, fuller 1533 Ziegenrück protocol; archival metadata links A to B, but exact textual correspondence requires collation.
- **C1** — `ThHStAW, EGA, Reg. Ii 3`, 1529 Visitation in Neustadt an der Orla.
- **C2** — `ThHStAW, EGA, Reg. Ii 3`, 1529 Pfarreinkommen Gössitz/Knau/Laskau/Bahren/Liebschütz/Liebengrün; especially relevant for economic notation.

Exact identities, dates, folios, URLs and inspection states live in `corpus/sources.tsv`, not here.

## Research programme

The programme is incremental and evidence-driven:

1. keep the corpus inventory and provenance links complete enough to identify every consequential source independently of chat;
2. establish A/B textual correspondence by actual collation;
3. structurally inspect C1/C2 and transcribe only the portions that materially answer active questions;
4. complete the Knau A transcription with internal evidence first, demonstrated parallels second;
5. expand source discovery across available visitation records while recording discovery boundaries;
6. prioritize new records by expected reduction of consequential uncertainty;
7. automate only proven repetitive bottlenecks.

## Deferred work: GitHub Issue contract

Future improvements belong in Issues when they are useful knowledge but not justified current implementation.

A valid future issue must state:

1. **Problem / research benefit**;
2. **Why not now**;
3. **Trigger** that makes implementation worthwhile;
4. **Definition of Done / acceptance criteria**.

No “nice to have” technology backlog without a research problem.

Current deferred areas include standards export (TEI), formal RiC interoperability, HTR evaluation/training, corpus import automation, binary manifests, authority reconciliation, publication QA, corpus coverage audit and lightweight schema/QA automation. The issues preserve the rationale so a future chat does not need to rediscover it.

## Human–AI division of labour

The assistant is responsible for historical, archival, palaeographic and methodological analysis; source-status discipline; candidate generation; comparison; repository synchronization; restartability; and deciding when a technical extension is actually justified.

The user controls research purpose, source access only they can provide, rights/confidentiality facts, desired depth and consequential publication/use decisions.

The user is **not** expected to maintain repository state, choose data standards, or adjudicate specialist readings they cannot independently validate.

## Continuous integrity gate

After consequential work, apply `methodology/quality-and-learning.md`:

- evidence actually inspected?
- claim layers still separate?
- corroboration genuinely independent?
- changed truth persisted in its canonical record?
- work actually reduced relevant uncertainty?

At useful checkpoints, actively try to falsify a sample of important `working` readings/relationships rather than merely confirming repository consistency.

## Definition of done for repository architecture

The architecture is sufficient when another capable researcher/agent, given only the repository and accessible source material, can determine:

- what the project/corpus contains;
- what each source actually is;
- what was inspected versus merely catalogued;
- how sources are believed to relate and at what evidential level;
- what the current transcription says and where it is uncertain;
- why consequential decisions were made;
- what the next research action is;
- which future improvements were deliberately deferred and what would trigger them.

If recovering the old chat is necessary, the work block is not fully persisted.
