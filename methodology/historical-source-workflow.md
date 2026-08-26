# Historical source workflow — authoritative scholarly method

## Purpose and scope

This is the **authoritative end-to-end scholarly method** for `paleo-type` when handwritten historical sources are identified, transcribed, analysed, collated and prepared for edition. It defines method before individual readings are solved and applies across projects.

The goal is source-exact, human-auditable historical research whose archival, transcriptional, editorial and interpretive claims can be checked by another scholar against the source.

Detailed files implement parts of this method:

- `source-and-provenance.md` — archival/source identity and digital provenance;
- `transcription-guidelines.md` — diplomatic source representation;
- `research-gates.md` — generic scholarly maturity requirements;
- `evidence-policy.md` — inspected-source/evidence status;
- `quality-and-learning.md` — continuous integrity and learning;
- `ai-governance.md` — AI use, validation and human review.

If a project-specific file conflicts with this generic method, preserve the project evidence but repair the methodological conflict rather than letting the pilot redefine the framework.

## Framework / corpus / project boundary

`paleo-type` has three distinct levels:

1. **METHOD (`methodology/`, `AGENTS.md`, `DECISIONS.md`)** — rules that should remain valid for another comparable historical-handwriting project.
2. **CORPUS (`corpus/`, `entities/`)** — identities and relationships that span sources/projects.
3. **PROJECT (`projects/<id>/`)** — concrete source observations, transcription, comparison evidence, research state and source-specific decisions.

Generalisation test:

> Would this statement still be a valid requirement if the next project used a different early-modern manuscript?

- yes → methodology;
- no, but it concerns multiple corpus records → corpus;
- no, it concerns the concrete source/research case → project.

Project facts may illustrate a method in discussion, but they must not become normative method merely because the pilot exhibited them.

## Normative disciplinary framework

No single discipline is sufficient. The workflow combines these professional lenses:

| Domain | Required contribution | Reference framework used here |
|---|---|---|
| archival description / diplomatics | provenance, record context, document/record identity, instantiations, relationships, transmission | ICA Records in Contexts (RiC) concepts and archival source criticism |
| palaeography | scripts/hands, graphemes, abbreviations, numerals, comparison | established palaeographic comparison method; source-specific evidence over semantic guessing |
| scholarly editing / textual criticism | diplomatic transcription, witness independence, variants, editorial intervention, apparatus | TEI P5 as conceptual/interchange reference model |
| historical source criticism | creation context, purpose, dependency, evidential limits, interpretation | disciplinary historical source criticism; DFG Good Research Practice principles |
| domain history | source-type-specific administrative, legal, ecclesiastical, economic, monetary/metrological knowledge | inspected sources/scholarship; domain knowledge generates hypotheses/tests, never manuscript graphemes |
| research-data stewardship | documentation, traceability, versioning, reproducibility | DFG Good Research Practice; repository provenance/restartability |
| research software/data engineering | loss-minimising representation, referential integrity, deterministic views, maintainability | technology remains subordinate to scholarly requirements |

## Standards/version policy

Record standards actually used; do not say vaguely “standards based”.

| Reference | Role | What it does not imply |
|---|---|---|
| ICA Records in Contexts Conceptual Model (RiC-CM 1.0) | conceptual distinction of records, instantiations, agents/activities and relationships | no requirement to implement RDF/RiC-O |
| ICA RiC application guidance | practical archival-description guidance when relevant | guidance is not manuscript evidence |
| TEI Guidelines P5 | conceptual/interchange model for manuscript description, source structure, transcription phenomena, witnesses and apparatus | no requirement to author TEI XML during working transcription |
| DFG Code of Conduct / Good Research Practice | transparency, lege-artis work, critical self-checking and traceability | does not replace discipline-specific method |
| applicable scholarly-edition guidance | edition concept, scholarly standards, sustainable text data | does not predetermine source-specific editorial choices |

When a standards version materially changes a repository rule, document the inspected version and the concrete consequence. Standards are reference frameworks, not authority substitutes.

---

# End-to-end scholarly method

## S1 — Identify source and establish provenance

**Question:** What exactly is the source object/record and how can it be recovered?

Required method:
- distinguish archival unit, record, witness, locus and instantiation;
- preserve archival/catalogue identifiers and stable digital identifiers;
- keep folio/page, portal image, export sequence, PDF page and working IDs separate;
- distinguish catalogue statements from direct source observations;
- model copy/extract/parallel/event relationships as claims with evidential status.

**Gate:** a third party can identify and recover the exact source/locus/instantiation without chat.

## S2 — Describe document and material/textual structure

**Question:** What physical/documentary structure must the transcription preserve?

Inspect and record, where observable/relevant:
- document/record type and stage;
- foliation/pagination and boundaries;
- page/folio layout, columns/regions, lists/tables, headings and marginalia;
- writing areas and reading order;
- additions, deletions, corrections, damage, gaps and unusual spatial relations;
- hands/scripts only to the level actually investigated and evidenced;
- consequential digital transformations such as crop/rotation/scaling.

Use `not investigated`, `not observable from digital image` or `not present in inspected locus` rather than filling descriptive fields by expectation.

**Gate:** the physical/textual organisation relevant to transcription can be reconstructed well enough that linearisation will not silently destroy meaning.

## S3 — Create diplomatic transcription of the principal witness

**Question:** What is actually written, where, and with what uncertainty?

Required method:
- address text by archival locus and editor-assigned physical line reference where appropriate, not by export image as the sole scholarly address;
- retain folio/page breaks and physical lineation;
- preserve historical spelling, word division, numerals/signs and materially relevant punctuation/separators;
- preserve relevant reading order/layout structure;
- distinguish secure text, uncertain positive reading, illegible/gap material, supplied text, deletions, additions, damage, abbreviation vs expansion, and hand shifts where those phenomena occur;
- do not replace visible multi-line source text with prose summaries;
- do not normalize names, spelling, measures or values in the diplomatic layer.

The working format need not be TEI XML, but it must preserve the distinctions needed for a loss-minimising mapping to established scholarly representation.

**Gate:** a human-readable, archival-locus-addressable diplomatic witness view can be derived from canonical transcription data without manual re-transcription or semantic filling.

## S4 — Palaeographically analyse difficult readings

**Question:** How can uncertain signs/readings be tested from manuscript evidence?

Required method:
1. localise the uncertain sign/grapheme sequence;
2. preserve visible evidence before lexical completion;
3. classify the problem (grapheme, abbreviation, numeral, monetary/metrological sign, segmentation, hand, etc.);
4. seek relevant internal comparanda, using “same hand” only when hand relevance is supported;
5. compare discriminating graphical features, not just word silhouette;
6. treat numerals/abbreviations/accounting notation as potentially distinct sign systems;
7. record candidates and discriminating/non-discriminating evidence;
8. use syntax/domain context after graphematic candidate formation;
9. retain `unresolved` when evidence does not decide.

`Same record` does not automatically mean `same hand`.

**Gate:** every consequential uncertain reading has a documented evidential test or an explicit reason it remains unresolved.

## S5 — Independently establish and collate related witnesses/controls

**Question:** What does each comparison source independently transmit and how does it relate to the principal witness?

Required method:
- independently identify and inspect each source;
- independently read/transcribe the relevant locus before importing wording from another witness;
- map corresponding units only after independent reading;
- record material agreements, variants, additions, omissions, reordered material, numerical/metrological differences and structural divergence;
- distinguish contextual/control sources from textual witnesses;
- upgrade source relationships only to the level demonstrated by collation.

**Gate:** a reviewer can distinguish each witness/source and see what relationship is demonstrated versus catalogued/inferred.

## S6 — Normalise, identify and semantically enrich

**Question:** Who/what is meant by the source forms without rewriting the source?

Maintain separate layers for:
- diplomatic manuscript form;
- abbreviation expansion;
- normalized spelling/value where useful;
- person/place/institution identification;
- concept/term identification;
- uncertainty/evidence for identifications.

**Gate:** historical entities/concepts are usable without contaminating the diplomatic source text.

## S7 — Apply historical source criticism and interpretation

**Question:** What can the source legitimately tell us about the historical situation?

Assess, where supported:
- creation context, function and purpose;
- authorship/agency, intended use/audience;
- record stage and transmission/dependence;
- genre/formularity and administrative practice;
- chronological/geographical/institutional context;
- independent corroboration/contradiction;
- limits from selection, survival, copying/excerpting and digitisation.

Domain knowledge supporting substantive historical claims must be traceable to inspected evidence.

**Gate:** historical claims are separable from transcriptional claims and carry explicit evidence and limits.

## S8 — Critically consolidate and validate

**Question:** Is the research state coherent, auditable and proportionally validated?

Required method:
- verify complete source representation at the required gate;
- reconcile conventions without smoothing the source;
- preserve consequential decision/revision history;
- adversarially test important working readings/relations;
- check for contamination from context or parallel witnesses;
- verify provenance/referential integrity;
- distinguish AI-assisted method-compliant work from independent expert validation;
- identify consequential specialist claims that remain unreviewed.

**Gate:** a competent third party can audit consequential claims from result to source and decision history without chat.

## S9 — Produce scholarly edition/publication layer

**Question:** How should the established research state be presented for intended users?

Before final rendering define an explicit edition concept:
- purpose/audience;
- scope and source/witness basis;
- edition/transcription conventions;
- treatment of abbreviations, punctuation, normalization and supplied/uncertain text;
- variant-apparatus policy;
- source/transmission note;
- historical commentary policy;
- publication/data format and preservation/interoperability requirements;
- independent human review appropriate to consequence and claims.

The edition is derived from the consolidated research state; undocumented manuscript readings must not appear at the presentation stage.

---

# Human-in-the-loop and expertise accountability

## Project owner / non-specialist human
The user must be able to see:
- the current source text in a human-readable witness view;
- what is secure, uncertain, unreadable, supplied or interpreted;
- evidence/rationale for consequential decisions;
- active scholarly gate and project-specific blockers;
- what has and has not been independently validated.

The user is not required to adjudicate specialist palaeographic questions they cannot independently assess.

## AI research assistant
The AI may perform archival reasoning, transcription, palaeographic candidate generation, collation, source criticism, research-data maintenance and historical analysis, but must:
- apply the relevant disciplinary method;
- expose evidential limits;
- never use model agreement as independent evidence;
- distinguish its work from independent human expert validation;
- persist durable state outside chat.

## Qualified independent specialist
Independent review is an escalation/validation layer, especially for consequential claims involving:
- highly uncertain palaeographic readings central to interpretation;
- unusual/weakly evidenced abbreviation or numeral systems;
- consequential hand/scribe identifications;
- strong textual-dependence/transmission claims;
- editorial choices whose validity cannot be established by procedural consistency alone.

If review has not occurred, state that transparently. Method compliance is not identical to expert validation.

---

# Gate model and project application

Generic maturity requirements are defined once in `research-gates.md`:

`G1 source basis → G2 diplomatic representation → G3 internal palaeographic analysis → G4 controlled comparison → G5 critical consolidation/validation → G6 edition`

A project does **not** redefine these requirements. Its `STATUS.md` records only which gate is reached/active/reopened, the concrete source-specific evidence or gaps against that gate, validation state, and next action.

A pilot may expose a methodological weakness. The learning path is:

`project observation/failure → project LEARNINGS/STATUS → test generalisability → methodology/DECISIONS update if genuinely general`

Do not promote a source-specific fact into method merely because it appeared in the first project.

## Final methodological test

For any new rule, field, structure or workflow step ask:

1. Which disciplinary requirement does it serve?
2. Is it generic method, corpus-level identity/context, or project-specific evidence?
3. Does it improve scholarly validity, auditability or human usability?
4. Is the leanest adequate representation being used?

If those questions cannot be answered, do not expand the framework.