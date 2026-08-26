# Historical source workflow — authoritative scholarly method

## Purpose and scope

This is the **authoritative end-to-end scholarly method** for `paleo-type` when handwritten historical sources are identified, transcribed, analysed, collated and prepared for edition. It exists so that method is defined **before** difficult readings are solved and does not have to be reconstructed from chat, software structure or ad-hoc AI decisions.

The project goal is not to produce machine-readable fragments. It is to produce source-exact, human-auditable historical research whose transcriptional, archival, editorial and interpretive claims can be checked by another scholar against the source.

Detailed files such as `source-and-provenance.md`, `transcription-guidelines.md`, `evidence-policy.md` and `ai-governance.md` implement parts of this method. If they conflict with this file, repair the conflict rather than silently choosing one.

## Normative disciplinary framework

No single discipline is sufficient. The workflow combines these professional lenses:

| Domain | Required contribution | Normative/reference framework used here |
|---|---|---|
| archival description and diplomatics | provenance, record context, document/record identity, instantiations, relationships, transmission | ICA Records in Contexts: RiC-FAD/RiC-CM 1.0; RiC Application Guidelines as current implementation guidance |
| palaeography | script/hand analysis, graphemes, abbreviations, numerals, scribal comparison | established palaeographic method; evidence must be source-specific and comparison-based rather than semantic guessing |
| scholarly editing / textual criticism | diplomatic transcription, witness independence, variants, editorial intervention, apparatus | TEI P5 current release as the interoperability/conceptual reference model for manuscript description, primary-source transcription and critical apparatus |
| historical source criticism | provenance, purpose, dependency, context, evidential limits, interpretation | disciplinary historical source criticism and DFG Good Research Practice principles |
| early-modern domain history | ecclesiastical administration, visitation, legal/economic terminology, money, measures, dues, property and institutional context | inspected primary/secondary evidence; domain knowledge generates hypotheses/tests but never replaces graphematic evidence |
| research-data stewardship | documentation, traceability, versioning, reproducibility, clear distinction between evidence and inference | DFG Good Research Practice; repository provenance and restartability rules |
| research software/data engineering | loss-minimising representation, referential integrity, deterministic views, maintainability | technology is subordinate to the scholarly requirements above; simplest adequate implementation wins |

## Standards/version policy

The repository records the standards actually used rather than saying vaguely that it is “standards based”.

| Reference | Version/status used | Role in paleo-type | What it does **not** imply |
|---|---|---|---|
| ICA Records in Contexts Conceptual Model | RiC-CM 1.0 | conceptual distinction of records, instantiations, agents/activities and explicit relationships | no requirement to implement RDF/RiC-O |
| ICA Records in Contexts Application Guidelines | RiC-AG current published guidance; verify version when used for an implementation decision | practical archival-description guidance | draft/application guidance is not evidence about a manuscript |
| TEI Guidelines P5 | current release; record exact version for publication/export decisions | conceptual/interchange model for manuscript description, facsimile/source structure, transcription phenomena, witnesses and critical apparatus | no requirement to author TEI XML during working transcription |
| DFG Code of Conduct / Good Research Practice | current published DFG Kodex | traceability, lege-artis work, transparency, critical self-checking | does not substitute for discipline-specific method |
| DFG scholarly-edition criteria | current available DFG edition guidance used as cross-disciplinary quality reference where applicable | edition concept, scholarly standards, sustainable standardised text data | literary-edition criteria are not automatically identical to every historical-source edition; project-specific editorial choices still require justification |

Whenever a standard materially changes a repository rule, document the inspected version and the exact consequence. Do not use the word “standard” as an authority substitute.

---

# End-to-end method

## S1 — Identify and establish provenance

### Question
What exactly is the source object/record and how can it be recovered?

### Required method
- distinguish archival unit, record, witness, locus and instantiation;
- preserve archive/fonds/signature/record identifiers and stable digital identifiers;
- keep folio, portal image, export sequence, PDF page and working IDs separate;
- distinguish catalogue statements from direct manuscript observations;
- model relationships such as extract/copy/parallel as claims with evidential status.

### Permitted claims
Archival identity/provenance claims only as strongly as inspected archival/catalogue/manuscript evidence supports them.

### Output/gate
A third party can identify and recover the exact source/locus/instantiation without chat.

## S2 — Describe the document and material/textual structure

### Question
What physical/documentary structure must the transcription preserve?

### Required method
Inspect and record, where observable/relevant:
- document/record type and stage;
- foliation/pagination and boundaries;
- page/folio layout, columns/regions, lists/tables, headings and marginalia;
- writing areas and reading order;
- additions, deletions, corrections, damage, gaps and unusual spatial relations;
- hands/scripts only to the level actually investigated and evidenced;
- digital transformations such as crop/rotation/scaling when consequential.

Use `not investigated`, `not observable from digital image` or `not present in inspected locus` rather than filling descriptive fields by expectation.

### Permitted claims
Material/document description, not lexical interpretation.

### Output/gate
The source's physical/textual organisation relevant to transcription can be reconstructed well enough that linearisation will not silently destroy meaning.

## S3 — Create a diplomatic transcription of the principal witness

### Question
What is actually written, where, and with what uncertainty?

### Required method
- address text by archival locus (folio/page) and editor-assigned physical line reference, not by export image as primary scholarly address;
- retain folio/page breaks and physical lineation in the diplomatic layer;
- preserve historical spelling, word division, numerals/signs and materially relevant punctuation/separators;
- encode/document layout region and reading order when needed;
- distinguish at minimum:
  - secure/controlled reading;
  - uncertain but positively read text (`unclear` concept);
  - text present but not legibly transcribable / omitted (`gap` concept, with reason/extent where possible);
  - editorially supplied text (`supplied` concept);
  - deletion/cancellation (`del` concept);
  - addition (`add` concept);
  - damage affecting reading (`damage` concept);
  - abbreviation sign and expansion as distinct layers where expansion is supplied;
  - hand shift only when empirically supported;
- do not use prose summaries as substitutes for visible multi-line text;
- do not normalize names, spelling, measures or values in the diplomatic reading.

The working format need not be TEI XML, but it must preserve distinctions needed for a loss-minimising mapping to an established scholarly model such as TEI P5.

### Permitted claims
Diplomatic/textual claims only. Historical identification is separate.

### Output/gate
A human-readable, folio- and line-addressable diplomatic witness view can be produced from the canonical transcription without manual re-transcription or semantic filling.

## S4 — Palaeographically analyse difficult readings

### Question
How can uncertain signs/readings be tested from the manuscript evidence?

### Required method
1. localise the uncertain grapheme/sign sequence;
2. preserve what is visible before lexical completion;
3. classify the problem: grapheme, abbreviation, numeral, currency/measure sign, segmentation, hand, etc.;
4. seek comparable forms first in the same demonstrably relevant hand/record context;
5. compare discriminating graphical features, not just word silhouettes;
6. treat numerals/abbreviations/accounting notation as potentially separate sign systems;
7. record candidate readings and what evidence discriminates or fails to discriminate;
8. use syntax/domain context only after graphematic candidate formation;
9. retain `unresolved` when the evidence does not decide.

`Same record` does not automatically mean `same hand`. Hand identity is itself a palaeographic claim.

### Output/gate
Every consequential uncertain reading has a documented evidential test or an explicit reason it remains unresolved.

## S5 — Independently establish and collate related witnesses/controls

### Question
What does each other source independently transmit, and how does it relate to the principal witness?

### Required method
- identify and inspect each source independently;
- transcribe/read the relevant locus before importing wording from the principal witness;
- map corresponding units only after independent reading;
- record agreements, variants, additions, omissions, reordered material, numeral/measure differences and structural divergence;
- distinguish a contextual/control source from a textual witness;
- upgrade relationships only to the level demonstrated by collation.

### Output/gate
A reviewer can distinguish the wording/evidence of each witness and understand what relationship is demonstrated versus merely catalogued/inferred.

## S6 — Normalise, identify and semantically enrich

### Question
Who/what is meant by the source forms, and how can the text be made historically searchable/understandable without rewriting it?

### Required method
Maintain separate layers for:
- diplomatic manuscript form;
- abbreviation expansion;
- normalized spelling/value where useful;
- person/place/institution identification;
- controlled concept/term identification;
- uncertainty and evidence for each identification.

Example: manuscript `Knawe` remains the reading; `Knau` is a separate normalized place identification.

### Output/gate
Historical entities/concepts are usable without contaminating the diplomatic source text.

## S7 — Apply historical source criticism and interpretation

### Question
What can this source legitimately tell us about the historical situation?

### Required method
Assess:
- creation context, administrative function and purpose;
- authorship/agency and intended use/audience where supported;
- record stage and transmission/dependence;
- genre/formularity and administrative practices;
- chronological/geographical/institutional context;
- corroboration and contradiction from independently inspected evidence;
- limits imposed by selection, survival, copying/excerpting and digitisation.

Domain knowledge must be traceable to inspected evidence when it supports a substantive historical claim.

### Output/gate
Historical claims are separable from transcriptional claims and carry explicit source/evidence basis and limits.

## S8 — Critically consolidate and validate

### Question
Is the research state internally coherent, auditable and proportionally validated?

### Required method
- verify that the full source locus is represented;
- reconcile transcription conventions without smoothing the source;
- trace consequential changes through decisions/apparatus;
- adversarially test a sample of important working readings/relations;
- inspect whether context or a parallel witness has contaminated the principal witness;
- verify referential/provenance integrity;
- distinguish AI-assisted scholarly work from independent expert validation;
- identify consequential specialist readings that remain unreviewed.

### Output/gate
A competent third party can audit consequential claims from research output back to source and decision history without chat.

## S9 — Produce the scholarly edition/publication layer

### Question
How should the established research state be presented for its intended users?

### Required method
Define an explicit edition concept before final rendering:
- purpose and user group;
- principal witness/source base;
- transcription/editorial conventions;
- treatment of abbreviations, punctuation, normalization and supplied/uncertain text;
- variant apparatus policy;
- source/transmission note;
- historical commentary policy;
- publication/data formats and preservation/interoperability requirements;
- independent human review appropriate to consequence and claims.

The edition is derived from the consolidated research state; it must not become a new place where undocumented readings appear.

---

# Human-in-the-loop and expertise accountability

## Project owner / non-specialist human
The user must be able to see:
- current source text in a human-readable witness view;
- what is secure, uncertain, unreadable, supplied or interpreted;
- evidence and rationale for consequential decisions;
- which scholarly stage/gate is active;
- what has and has not been independently validated.

The user is **not** required to adjudicate specialist palaeographic questions they cannot independently assess.

## AI research assistant
The AI may perform archival reasoning, palaeographic candidate generation, transcription, collation, source criticism, research-data maintenance and historical analysis, but must:
- identify the disciplinary method being applied;
- expose evidential limits;
- never use model agreement as independent evidence;
- distinguish its own scholarly work from human expert validation;
- persist durable state outside chat.

## Qualified independent specialist
Independent expert review is an escalation/validation layer, especially before consequential/publication claims involving:
- highly uncertain palaeographic readings central to interpretation;
- unusual or weakly evidenced abbreviation/numeral systems;
- consequential hand/scribe identifications;
- strong textual-dependence/transmission claims;
- project-wide editorial choices whose validity cannot be established by procedural consistency alone.

If such review has not occurred, state that transparently. Do not label AI-produced work “expert validated” merely because it follows expert methods.

---

# Current repository standards/gap audit — 2026-08-26

This audit compares the present repository to the method above. It is a **method compliance audit**, not a claim that all scholarly work is complete.

| Requirement | Current support | Assessment | Required correction before/while continuing Knau M2 |
|---|---|---|---|
| canonical archival source identity/provenance | `corpus/`, project crosswalks | strong | maintain |
| record vs instantiation separation | `corpus/sources.tsv`, `corpus/files.tsv` | strong | maintain |
| explicit source-relation evidence status | `corpus/relationships.tsv` | strong | maintain |
| document/material description of working locus | scattered/implicit | **gap** | inspect and record only observable/relevant layout/document features before declaring M2 complete |
| folio as primary scholarly transcription address | folio mapping exists, transcription rows still keyed by export page IDs 132–135 | **gap** | migrate only after direct line/layout reinspection; preserve legacy export IDs as provenance |
| physical lineation | current `line_id` exists but is tied to export working IDs and includes multi-line collapsed ranges | **partial/gap** | establish editor-assigned folio-local physical line references from direct image inspection |
| folio/page breaks visible in diplomatic text | implicit through separate TSVs | **partial** | make explicit in canonical addressing and human witness view |
| layout/region/reading order | coarse `region` field | **partial** | audit whether list/accounting layout needs finer region/order representation; add only if source requires it |
| secure vs uncertain readings | status model exists | strong/partial | retain, but separate textual phenomenon from confidence/status |
| uncertain positive reading vs unreadable gap | not explicitly distinguished | **major gap** | add explicit phenomenon semantics before M2 completion |
| supplied editorial text | not systematically representable | **major gap** | define separate supplied/expansion layer; do not place supplied text indistinguishably in diplomatic reading |
| additions/deletions/damage | no explicit standard representation | **gap/capability missing** | define representation now; populate only when observed |
| abbreviation sign vs expansion | policy says do not silently expand, but schema has no explicit expansion field/model | **gap** | define explicit treatment; migrate occurrences only from source reinspection |
| hand shifts | palaeographic files exist; no transcription representation | **conditional gap** | define capability; do not assert/use until hand evidence exists |
| witness independence/collation | method and relationships exist | strong conceptually | execute at M4 |
| diplomatic vs normalized/identified text | strongly separated by policy | strong | maintain |
| human-readable current witness text | not canonical/derived in repo; human must reconstruct TSV fragments | **major usability/scientific audit gap** | create a deterministic/clearly derived folio-line witness view once compliant line data exist |
| edition concept | M6 has requirements but no final concept yet | appropriate for stage | define before M6 rendering |
| independent expert validation status | general escalation rules exist but not integrated into milestone exit claims | **partial** | M5/M6 must state what specialist review occurred or did not occur |
| standard/version transparency | standards named, versions mostly not operationally tracked | **gap** | this file becomes the reference; inspect/update versions when they materially affect rules/publication |

## Audit conclusion

The repository is already relatively strong in **provenance, evidence separation, revision traceability and AI-governance**. The principal weakness is the **diplomatic transcription layer**: the current `page_id / line_id / region / reading / status / alternatives / evidence_note` working TSV is not yet sufficient as the final M2 scholarly representation because it does not explicitly model several standard primary-source transcription distinctions and is keyed primarily by export-image work IDs rather than archival folio/physical-line scholarly addresses.

Therefore:

1. **Do not discard existing readings.** They are working evidence/history.
2. **Do not invent a large schema before source inspection.** The missing scholarly distinctions are now defined; the exact lean fields must be chosen against the phenomena actually observed on 61v–63r.
3. **Before M2 can pass, re-inspect 61v–63r for layout/lineation/transcription phenomena and minimally migrate the canonical transcription.**
4. **A human-readable diplomatic witness view is an M2 output requirement**, generated/derived from the canonical data rather than manually maintained as a second text truth.
5. **M5/M6 must distinguish method-compliant AI-assisted research from independent qualified human validation.**

This audit is the basis for the next bounded methodological corrections; after those corrections, return to direct source work rather than expanding infrastructure.
