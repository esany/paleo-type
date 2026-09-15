# Historical source workflow — authoritative scholarly method

## Purpose and scope

This is the **authoritative end-to-end scholarly method** for `paleo-type` when handwritten historical sources are identified, transcribed, analysed, collated and prepared for edition. It defines method before individual readings are solved and applies across projects.

This method operationalizes `GOVERNING_OBJECTIVE.md`. It is subordinate to that highest-order purpose and may not redefine or weaken it.

The goal is source-exact, human-auditable historical research whose archival, transcriptional, editorial and interpretive claims can be checked by another scholar against the source.

Detailed files implement parts of this method:

- `source-and-provenance.md` — archival/source identity, exact digital instantiations and preservation;
- `project-lifecycle.md` — investigation/source-group boundaries, project creation and feedback;
- `transcription-guidelines.md` — diplomatic source representation;
- `research-gates.md` — generic scholarly maturity requirements;
- `evidence-policy.md` — inspected-source/evidence status;
- `quality-and-learning.md` — continuous integrity and learning;
- `ai-governance.md` — AI use, validation and human review.

If a project-specific file conflicts with this generic method, preserve the project evidence but repair the methodological conflict rather than letting the pilot redefine the framework.

## Framework / corpus / project boundary

`paleo-type` has three distinct levels:

1. **METHOD (`methodology/`, `AGENTS.md`, `DECISIONS.md`)** — rules that should remain valid for another comparable historical-handwriting investigation.
2. **CORPUS (`corpus/`, `entities/`)** — canonical archival/source identities, exact digital instantiations, reusable source-wide mappings, source/event/entity relationships and normalized identities.
3. **PROJECT (`projects/<id>/`)** — a durable scholarly investigation/work container established for a research purpose. It references canonical Sources/Files and carries project-specific source uses/loci, observations, transcription, comparison evidence, decisions and research state. Source/File/archival structure alone does not create a Project.

Generalisation/ownership test:

> Would this statement still be a valid requirement if the next project used a different early-modern manuscript/source group?

- yes → methodology;
- no, but it is canonical source/file/reusable mapping/relationship truth → corpus;
- no, it concerns one investigation's source role/locus/reading/state → project.

A source record or PDF is not automatically a project. Separately identified archival records remain separate sources even when they share a volume/signature. Project facts may illustrate a method in discussion, but they must not become normative method merely because the pilot exhibited them.

## Source/File intake and Project routing

Source/File intake precedes and is independent of Project materialization. A supplied file may be fully registered as canonical Corpus state even when no Project exists yet. `CORPUS_ONLY / NO_PROJECT_YET` is therefore a valid completed routing outcome, not a workflow failure.

Use the following canonical decision order for a newly supplied or discovered digital source representation:

```text
supplied/discovered file
→ establish exact File identity/checksum where consequential
→ match/reuse a known canonical File or keep the File identity unresolved/distinct
→ establish/verify which historical Source the File instantiates
→ establish only evidenced Source→Source structure/relations
→ record/reuse File→Source provenance and rights/preservation state
→ reuse/create source-wide folio/image/PDF correspondence only when evidenced
→ explicit Project routing decision
     ├─ existing Project
     ├─ candidate new Project
     └─ Corpus-only / no Project yet
→ create only project-relative use/evidence/state actually required by the selected route
→ run deterministic integrity checks
→ update Project STATUS/NEXT ACTION only when Project state actually changes and an authorized next action exists
→ test restartability from repository state plus the authorized evidence-access mechanism
```

The route is not inferred from whichever Project is active in chat or from Source structure. Before any Project-specific mutation, establish explicitly which of the three routing outcomes applies. A `candidate new Project` becomes a Project only after a human research-purpose decision establishes that a durable investigation/work container is wanted; `project_source_id` is then selected as the documentary Source anchor for deterministic structural resolution. It does not itself create the Project or select its research priority.

### Deterministic intake facts versus judgement

Once the relevant inputs exist, software may determine or check stable facts such as:

- SHA-256 equality with a canonical File;
- canonical Source/File/Project/use reference integrity;
- Source ancestry and `root | internal | external` status after Project selection;
- whether a canonical source-wide crosswalk exists for the established Source;
- whether explicit use-evidence points to a File of the same canonical Source;
- checksum/path/storage constraints already defined by the Source Contract.

Software must **not** infer from filename, page count, OCR, visual similarity, archival proximity, current chat, or structural containment:

- historical Source identity where the evidence is unresolved;
- a Source relationship not already evidenced;
- whether a Source should be used in a Project;
- a Project's existence, research purpose or current scope;
- `research_function` or relevant scholarly locus;
- rights/redistribution authority requiring human/institutional judgement;
- the current scholarly NEXT ACTION;
- palaeographic, philological, editorial or historical truth.

`python tools/source_intake.py <file>` is a read-only convenience adapter for the deterministic part of this sequence. Its output is a derived inspection/routing view, not canonical research state and not Project-creation authority.

For active visual source work, intake/restartability must also preserve the distinction among **identifiability**, **reproducibility** and **research-ready availability**. Knowing the File ID/SHA/crosswalk or a render recipe does not prove that a fresh authorized work context can actually open the evidence required for the next scholarly action. See `source-and-provenance.md` and the applicable Project status for the concrete access state.

## Research-question control

Method and gates do not justify work by themselves. Every material research activity must serve an explicit question or required source-representation task.

Use this chain:

`research goal → research question → evidence needed → disciplinary method → claim type → permitted conclusion`

**Pre-priority research-direction formation.** When a material decision about the next research direction is actually needed and no Human-Owner-selected **next scholarly scope or research question is in force**, do not infer priority from unresolved, available or easily addressable work. Where the current evidence supports more than one serious direction, form and scholarly challenge multiple evidence-grounded candidate directions before priority selection. For each materially serious candidate, make explicit enough of its scholarly consequence, discriminating or advancing evidence and evidence ceiling, question-dependent analytical scale/context, and materially relevant disciplinary perspective to permit source-critical comparison; source criticism may refine, weaken or reject the candidate itself. Candidate directions are proposals only: they do not create Project scope, priority or `NEXT ACTION`, and `no new scope selected` remains a valid Human-Owner outcome. This requirement does not prescribe a fixed number of candidates, scoring/ranking, a persistent Candidate-Question object, a fixed competence topology, a preferred AI role or a separate Research-Framing layer.

The trigger is deliberately narrow: do not generate candidate research directions automatically at every terminal state.

Before expanding a project, ask:
- what question or gate requirement is being served;
- what evidence can actually answer it;
- which discipline/method governs the inference;
- what stronger claim remains unsupported.

Do not add entity work, metrology, collation, bibliography, software or specialist analysis merely because it could be useful someday. Trigger it when a concrete question, observed phenomenon or gate requires it.

## Normative disciplinary framework

No single discipline is sufficient. Core competencies are always available as methodological lenses; specialist domains are activated by the source/problem rather than pre-built into every project.

| Domain | Required contribution | Activation |
|---|---|---|
| archival description / diplomatics | provenance, record context, document/record identity, instantiations, relationships, transmission | core |
| palaeography | scripts/hands, graphemes, abbreviations, numerals, comparison | core for handwritten sources |
| historical philology / language history / lexicography | historical spelling, morphology, segmentation, lexical forms and semantic change without contaminating graphematic reading | core when linguistic form affects reading/normalisation |
| scholarly editing / textual criticism | diplomatic transcription, witness independence, variants, editorial intervention, apparatus | core |
| historical source criticism | creation context, purpose, dependency, evidential limits, interpretation | core |
| research-data stewardship / GWP | documentation, traceability, versioning, reproducibility | core |
| research software/data engineering | loss-minimising representation, referential integrity, deterministic views, maintainability | core support; subordinate to scholarship |
| codicology/material manuscript study | support, quires, binding, watermarks, material construction | activate only when observable and relevant to dating, transmission, structure or interpretation |
| onomastics/toponymy | person/place-name forms and identification | activate when identification is consequential |
| historical metrology / numismatics | measures, weights, monetary/accounting systems | activate when such notation/values occur and matter |
| legal, ecclesiastical, administrative, economic/social or other domain history | source-type-specific institutions, practices and concepts | activate when a concrete claim requires it |

**Expertise-routing rule:** before a consequential specialist claim, identify the governing domain and whether the evidence/expertise used is adequate. Domain knowledge may generate candidates and tests; it must not manufacture manuscript graphemes.

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

## S1 — Establish investigation source group and provenance
**Question:** Which distinct archival/source records form the investigation, what role/locus does each have, and how can the exact inspected instantiations be recovered?

Required method: for a purpose-established Project, define the bounded investigation source group; independently identify every material source record; preserve separately catalogued/identified records even when they share a volume/signature; distinguish archival unit, record, witness, locus and instantiation; record each source's project role and relevant locus without rewriting canonical source identity; preserve archival/catalogue identifiers and stable digital identifiers; for consequential file-based work record exact original filename, SHA-256, coverage and preservation/storage state; treat URL/URN as secondary provenance rather than equivalent backup; keep folio/page, portal image, export sequence, PDF page and working IDs separate; distinguish catalogue statements from direct observations; model copy/extract/parallel/event relationships as claims with evidential status. Corpus-only Source/File intake may precede this Project activity and does not need to manufacture a Project or research function.

**Completion evidence:** a third party can reconstruct the project source group, distinguish its archival records and their roles/loci, and recover or explicitly account for the exact inspected instantiations without chat.

## S2 — Describe document and material/textual structure
**Question:** What documentary/material structure is relevant to reading, transmission and transcription?

Inspect and record **to the depth justified by the source and research question**:
- document/record type and stage;
- foliation/pagination and boundaries;
- page/folio layout, columns/regions, lists/tables, headings and marginalia;
- writing areas and reading order;
- additions, deletions, corrections, damage, gaps and unusual spatial relations;
- hands/scripts only to the level actually investigated and evidenced;
- consequential digital transformations such as crop/rotation/scaling;
- material/codicological features (support, binding/quires, watermarks etc.) only when observable and relevant.

Use explicit states such as `not investigated`, `not observable from available representation`, `not relevant to current question`, or `not present in inspected locus`. Absence of investigation must never silently become absence of a phenomenon.

**Completion evidence:** the organisation relevant to the current research/transcription task can be reconstructed without silent loss of meaning; material questions beyond the available representation are explicitly bounded.

## S3 — Create diplomatic transcription of the principal witness
**Question:** What is actually written, where, and with what uncertainty?

Required method: address text by archival locus and editor-assigned physical line reference where appropriate; retain folio/page breaks and physical lineation; preserve historical spelling, word division, numerals/signs and materially relevant punctuation/separators; preserve relevant reading order/layout; distinguish secure text, uncertain positive reading, illegible/gap material, supplied text, deletions, additions, damage, abbreviation vs expansion, and hand shifts where those phenomena occur; do not replace visible multi-line text with prose summaries; do not normalize in the diplomatic layer.

The working format need not be TEI XML, but must preserve distinctions needed for a loss-minimising mapping to established scholarly representation.

**Completion evidence:** a human-readable, archival-locus-addressable diplomatic witness view can be derived from canonical transcription data without manual re-transcription or semantic filling.

## S4 — Palaeographically and philologically analyse difficult readings
**Question:** How can uncertain signs/readings/forms be tested from manuscript and language evidence?

Required method:
1. localise the uncertain sign/grapheme sequence;
2. preserve visible evidence before lexical completion;
3. classify the problem (grapheme, abbreviation, numeral, segmentation, historical word form, lexical identification, hand, etc.);
4. route the problem to the relevant method/domain;
5. seek relevant internal comparanda, using “same hand” only when supported;
6. compare discriminating graphical features, not just word silhouette;
7. treat numerals/abbreviations/accounting notation as potentially distinct sign systems;
8. use historical linguistic/lexical evidence to test forms after visible evidence is preserved;
9. use syntax/domain context after candidate formation;
10. record candidates and discriminating/non-discriminating evidence;
11. retain `unresolved` when evidence does not decide.

`Same record` does not automatically mean `same hand`. Lexical plausibility does not prove a graphematic reading.

**Completion evidence:** every consequential uncertain reading/form has a documented evidential test or explicit reason it remains unresolved.

## S5 — Independently establish and collate related witnesses/controls
**Question:** What does each comparison source independently transmit and how does it relate to the principal witness?

Independently identify and inspect each source; independently read/transcribe the relevant locus before importing wording from another witness; map corresponding units only after independent reading; record agreements, variants, additions, omissions, reordered material, numerical/metrological differences and structural divergence; distinguish contextual/control sources from textual witnesses; upgrade source relationships only to the level demonstrated by collation.

**Completion evidence:** a reviewer can distinguish each witness/source and see what relationship is demonstrated versus catalogued/inferred.

## S6 — Normalise, identify and semantically enrich
**Question:** Who/what is meant by the source forms without rewriting the source?

Maintain separate layers for diplomatic manuscript form, abbreviation expansion, normalized spelling/value where useful, person/place/institution identification, concept/term identification, and uncertainty/evidence. Activate onomastic, lexicographic, metrological or other specialist methods only when the observed material/question requires them.

**Completion evidence:** historical entities/concepts are usable without contaminating diplomatic text, and specialist identifications expose their evidence.

## S7 — Apply historical source criticism and interpretation
**Question:** What can the source legitimately tell us about the historical situation?

Assess where supported: creation context, function/purpose, authorship/agency/intended use, record stage and transmission/dependence, genre/formularity/administrative practice, chronological/geographical/institutional context, corroboration/contradiction, and limits from selection, survival, copying/excerpting and digitisation. Domain knowledge supporting substantive claims must be traceable to inspected evidence.

**Completion evidence:** historical claims are separable from transcriptional claims and carry explicit evidence and limits.

## S8 — Critically consolidate and validate
**Question:** Is the research state coherent, auditable and proportionally validated?

Verify complete source representation at the required gate; reconcile conventions without smoothing the source; preserve consequential decision/revision history; adversarially test important readings/relations; check contamination from context/parallel witnesses; verify provenance/referential integrity; distinguish AI-assisted method-compliant work from independent expert validation; identify consequential specialist claims that remain unreviewed.

**Completion evidence:** a competent third party can audit consequential claims from result to source and decision history without chat.

## S9 — Produce scholarly edition/publication layer
**Question:** How should the established research state be presented for intended users?

Before final rendering define an explicit edition concept: purpose/audience; scope/source basis; conventions; treatment of abbreviations, punctuation, normalization and supplied/uncertain text; apparatus policy; source/transmission note; commentary policy; publication/data format and preservation/interoperability requirements; independent human review appropriate to consequence and claims.

The edition is derived from the consolidated research state; undocumented manuscript readings must not appear at presentation stage.

---

# Activities versus maturity gates

S1–S9 are **scholarly activities/methods**. G1–G6 in `research-gates.md` are **maturity/acceptance states**. They are complementary, not competing workflows.

Typical relationship (not a rigid waterfall):

| Activity | Primary maturity effect |
|---|---|
| S1 provenance + relevant S2 description | G1 source basis |
| S2 structure + S3 transcription | G2 diplomatic representation |
| S4 palaeographic/philological testing | G3 internal analysis |
| S5 independent witness/control work | G4 controlled comparison |
| S6 enrichment + S7 criticism + S8 validation | G5 critical consolidation |
| S9 edition/publication | G6 edition |

Work may iterate and a later finding may reopen an earlier gate. A project records gate state; it does not redefine gate requirements.

# Human-in-the-loop and expertise accountability

## Project owner / non-specialist human
The user must be able to see the current source text in a human-readable witness view; what is secure/uncertain/unreadable/supplied/interpreted; evidence/rationale for consequential decisions; active gate and blockers; and what has/not been independently validated. The user is not required to adjudicate specialist questions they cannot independently assess.

## AI research assistant
The AI may perform archival reasoning, transcription, candidate generation, philological analysis, collation, source criticism, research-data maintenance and historical analysis, but must apply the relevant disciplinary method, expose evidential limits, never use model agreement as independent evidence, distinguish its work from independent human expert validation, and persist durable state outside chat.

## Qualified independent specialist
Independent review is an escalation/validation layer, especially for consequential highly uncertain readings, unusual notation, hand/scribe identifications, specialist linguistic/metrological/onomastic claims, strong transmission claims, and editorial choices whose validity cannot be established procedurally. If review has not occurred, state that transparently. Method compliance is not identical to expert validation.

# Gate model and project application

Generic maturity requirements are defined once in `research-gates.md`:

`G1 source basis → G2 diplomatic representation → G3 internal palaeographic analysis → G4 controlled comparison → G5 critical consolidation/validation → G6 edition`

A project does **not** redefine these requirements. Its `STATUS.md` records only which gate is reached/active/reopened, concrete source-specific evidence/gaps, validation state and next action.

A pilot may expose a methodological weakness. Learning path:

`project observation/failure → project LEARNINGS/STATUS → test generalisability → methodology/DECISIONS update if genuinely general`

## Final methodological test

For any new rule, field, structure or workflow step ask:
1. Which research question or required source-representation task does it serve?
2. Which disciplinary requirement/domain governs it?
3. Is it generic method, canonical corpus/source truth, or project-specific investigation evidence?
4. Does it improve scholarly validity, auditability or human usability?
5. Is the leanest adequate representation being used?

If those questions cannot be answered, do not expand the framework.