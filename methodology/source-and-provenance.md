# Source and provenance methodology

This file defines the generic archival/source-critical core for corpus work in `paleo-type`. It applies to all projects.

## Purpose

Historical research must distinguish a historical/documentary object from larger or smaller source objects related to it, from the way an archive/catalogue describes any of those levels, and from the exact digital file through which the evidence was inspected. Several protocol records may lie within one archival act; a protocol may contain sections or attachments; several exports may represent one source. None of these situations may be flattened for convenience.

Keep three truth domains separate:

1. **Archival truth** — what object/record exists, where it belongs, how it is described, and how it relates to other records.
2. **Textual/palaeographic truth** — what signs/words are actually present in a concrete witness.
3. **Historical truth** — what can be inferred about past people, institutions, events and relationships from inspected evidence.

No layer may silently rewrite another.

## Conceptual reference standards

`paleo-type` follows the concepts, not the implementation burden, of established scholarly standards:

- ICA Records in Contexts concepts for records, instantiations, agents/activities and explicit relations;
- TEI P5 as a long-term interoperability model for witnesses/readings/facsimile references/variants/responsibility;
- historical source criticism for provenance, transmission, purpose, dependency and evidential limits.

Do not implement RDF/RiC-O, a graph database or TEI authoring merely to claim standards compliance.

## Source levels without a fixed hierarchy

Scholarly work may need to distinguish archival holding context, act, record, protocol, section, attachment, witness, locus and digital instantiation. These are real distinctions, but the repository does **not** hard-code one universal depth or parent column.

Instead:

- every historical/documentary object that needs stable identity is a **source node** in `corpus/sources.tsv`;
- `source_type` describes the node at the granularity actually evidenced;
- structural containment is represented explicitly as `part_of` in `corpus/relationships.tsv`, directed from part to whole;
- deeper or different structures may be represented by chaining the same relation;
- intermediate nodes are created only when they matter for identity, provenance, citation or research.

Examples may include `protocol → act`, `section → protocol`, `attachment → record`, `volume → series`, or other evidenced part–whole structures. These examples do not define a closed ontology.

A shared shelfmark does not collapse distinct protocol records. Conversely, a separate portal/DigiRef record ID does not automatically prove a separate archival act or source level: provider granularity must be established from evidence.

A portal image number is never a folio merely because both are numbers. A PDF page is never a manuscript page unless demonstrated.

## Stable source identity

Every canonical source node gets a stable local `source_id`. The identifier names the historical/documentary object itself, not its temporary project role and not its place in one assumed hierarchy.

Prefer provenance-derived identities using stable archive/fonds/signature together with evidenced record identity or, when no provider-level identifier exists, a stable local identity derived from title and bounded locus. Human-readable title, date and folios remain separate fields. External provider IDs, URLs and URNs are provenance/access attributes, not replacements for the local key.

Provider identifiers must retain their evidenced granularity. If a provider ID addresses a larger act, do not reuse it as though it identified a protocol inside that act. If it identifies the bounded protocol, retain it on that protocol node.

Witness sigla are optional presentation aliases only.

## Corpus inventory

`corpus/sources.tsv` is the canonical inventory of source nodes at all evidenced archival/documentary granularities needed by the corpus.

`corpus/relationships.tsv` is the canonical relationship register. Structural containment uses the generic `part_of` predicate; other relations remain explicit claims with their own predicate, status and evidence basis.

`corpus/files.tsv` is the canonical manifest of exact digital instantiations actually used in research. A file row identifies the source node whose material it instantiates. Exact export coverage may include adjacent pages, but adjacent material outside an evidenced source boundary must not silently become part of that source.

Discovery is not inspection; inspection is not transcription; transcription is not collation.

## Part–whole integrity

`part_of` is a structural relation, not an identity shortcut.

For every `part_of` relation:

- subject and object must both be canonical source nodes;
- subject is the part and object the whole;
- evidence/status remain explicit;
- cycles are invalid;
- multiple parent relations are permitted only when the evidence genuinely warrants them;
- the resolver reports all valid ancestry paths rather than silently choosing one.

Do not create a type-specific parent table or a new parent field merely because one project currently uses a recurring pattern such as act → protocol. Add a new structural concept only when the generic node/relation model cannot express a demonstrated scholarly requirement.

## Persistent identifiers and exact instantiations

Persistent identifiers such as URNs and stable archival URLs are **first-class provenance and working identifiers**. They support durable citation, re-location of the archive-provided digital object, comparison with the provider's current representation and linkage back to institutional metadata.

They have a different evidential quality from the exact file used in research. A persistent identifier identifies or relocates the archive-side object/representation; a checksum identifies the concrete byte sequence actually inspected or preserved. Neither replaces the other.

Therefore preserve both when available:

- source identity + persistent identifier/URL at the level it actually identifies;
- exact file identity + original filename + SHA-256 + coverage + preservation state.

Do not downgrade a URN to a mere convenience link, and do not treat it as an equivalent backup of the exact export. Never synthesize a URN by extrapolating from neighboring image IDs or apparent identifier patterns.

## Original-export preservation

The exact archive export used to support consequential research is a **first-class research asset**.

A URL or URN can help relocate and cite the archive-side digital object, but it is not equivalent to the exact export that was inspected. Portals can change rendering, sequence, metadata, availability or export behavior.

For every central original export used by a project:

1. preserve the original filename;
2. compute and record SHA-256;
3. record exact source coverage;
4. record the repository path where the original is or is intended to be preserved;
5. preserve the original bytes unchanged — do not overwrite with OCR, compression, crop, rotation or normalization;
6. keep derived renders/crops/OCR as separate derivatives linked back to the original file ID;
7. make preservation state explicit (`repo-preserved`, `external-controlled`, `preservation-blocked-public-redistribution`, etc.);
8. if rights/access constraints prevent repository storage, state the blocker explicitly. Do not claim that checksum + URN constitutes equivalent backup.

Identifiability, reproducibility and research-ready availability are separate properties. A known File ID/SHA, stable identifier, crosswalk or render recipe does not by itself prove that a fresh authorized work context can open the evidence needed for the current action. Where direct inspection is required, verify an actual authorized access path before treating the evidence as research-ready.

## Rights statements and preservation decisions

Record the rights statement actually supplied with the object/export. Do not replace a known rights state with generic `rights unclear` wording.

For an object marked `InC/1.0`:

- the object is identified as protected by copyright and/or related rights;
- uses permitted by applicable copyright/related-rights law remain possible;
- further uses may require permission from the rightsholder;
- additional rights or permissions may also matter;
- additional institutional information may exist;
- the rights statement itself is **not a licence** and does not by itself grant a general redistribution permission.

Accordingly, in a public repository `InC/1.0` should be recorded as a **known protected-rights state**, while public redistribution of the exact binary remains a separate authority/use question. If no further licence, contractual permission or other adequate legal basis is documented, use an explicit preservation state such as `preservation-blocked-public-redistribution` rather than pretending the rights state is unknown.

This repository records scholarly provenance and preservation state; it does not convert a rights statement into legal permission.

## Reusable source data

A mapping that remains true for a source node regardless of project belongs once under:

`corpus/source-data/<source_id>/`

Typical example: a controlled `archival_folio ↔ export_image ↔ PDF_page ↔ stable_image_urn` crosswalk. Keep only loci assignable to that source node. If an exact export contains adjacent pages outside the evidenced boundary, record that fact in file provenance rather than forcing those pages into the source crosswalk.

Project-specific statements such as a research function and its source-relative relevant locus belong in the Project's `source-uses.tsv`. A historical use may remain represented there as historical work-state without becoming the current active scope.

Do not copy the same source crosswalk into each consuming project.

## Project anchoring and source use

A Project exists because a human owner has established a durable scholarly purpose/boundary. After Project selection, `project.yml: project_source_id` records the canonical historical Source anchor used for structural resolution. The anchor makes Project↔Source structure reconstructable; Source existence or structure does not itself create a Project.

`projects/<id>/source-uses.tsv` records actual Project→Source research functions/loci. Concrete File evidence for a use is recorded separately in `projects/<id>/research/use-evidence.tsv` when needed. Historical/project-relative functions may be retained with historical status; they do not select the current scholarly priority.

Structural membership is derived from the canonical source graph:

- source equals `project_source_id` → project root;
- source reaches `project_source_id` through one or more `part_of` relations → internal source;
- otherwise → external source when used by the Project.

Research function is independent of structural membership. An external Source may serve comparison/control/context or another function; an internal Source may have no active research function. Neither structural status nor a research-function label chooses the current `NEXT ACTION`.

## Relationship register

`corpus/relationships.tsv` is the canonical place for explicit relationships between source nodes, events and entities.

A relationship is itself a research claim and therefore has subject, predicate, object, status, evidence basis and limitation/note.

Useful statuses include `observed`, `metadata-supported`, `working`, `unresolved`, `rejected`.

A catalogue statement such as “extract from X” remains metadata-level until textual relationship is checked. Do not silently upgrade it to copying/dependence. Likewise, `part_of` states containment only; it does not imply textual dependence, project role or identical authorship/hand.

## Event/activity context

`corpus/events.tsv` records administrative/historical activities that connect records without implying textual identity. Event co-membership is contextual evidence, not proof of textual dependence.

## Witness and collation discipline

When two records/witnesses may transmit related text:

1. identify each independently by canonical source identity;
2. locate corresponding loci;
3. inspect/read each witness independently;
4. compare structure/wording;
5. record correspondences/divergences;
6. upgrade relationship only as far as evidence warrants.

A clearer witness may generate a test for an unclear token in another witness; it does not overwrite that witness's graphemes.

## Digital source criticism

For consequential work determine:

- archive/fonds/signature and the canonical source node actually used;
- relevant `part_of` ancestry when it matters for provenance or project membership;
- source title and evidenced boundary/locus;
- persistent identifier/archival URL at the level it actually identifies, where available;
- exact file ID and SHA-256 of the inspected export;
- whether that exact export is preserved and where;
- whether the required representation is actually accessible in the current authorized work context when direct inspection is needed;
- folio, portal image, PDF page, export sequence and legacy IDs as separate identifiers;
- whether export coverage is complete for the claim;
- whether a working derivative differs from the original.

Do not rely on a transient chat attachment as the only durable evidence identity. Do not report evidence as research-ready merely because its identity and reproduction recipe are known.

## Entities and authority control

Normalized persons/places/institutions may receive stable local IDs in `entities/` when repeated use makes this useful. Keep manuscript forms and normalized identities separate.

## Corpus completeness

Never claim “all available sources” from accumulated examples alone. Corpus-level completeness claims require documented repositories/catalogues, boundaries, queries/filters, access dates, inclusion/exclusion criteria and known unavailable/not-digitised material.

## Research priority

Source inventory is not an invitation to transcribe everything. Prioritize work by the owner-grounded Project purpose/current scope and the research value of the bounded question. Source structure, File availability, old role labels or evidence convenience do not choose the current work target.

## Maintenance and restartability

When source/project knowledge changes:

- source-node identity/type/title/boundary/provider identifiers → `corpus/sources.tsv`;
- part–whole or other source relationship → `corpus/relationships.tsv`;
- exact file/checksum/coverage/storage/rights → `corpus/files.tsv`;
- reusable source crosswalk → `corpus/source-data/<source_id>/`;
- Project purpose/root/current bounded scope → project `project.yml`;
- Project→Source research function/locus → project `source-uses.tsv`;
- concrete Project-use→File binding → project `research/use-evidence.tsv`;
- project inspection detail → existing Project research/inspection owner when needed;
- project consequence/authorized next action or explicit absence of one → project `STATUS.md`.

Derived intake/context helpers may compose these canonical owners for navigation and restart, but they are rebuildable views and must not become parallel truth.

Final test:

> Could another capable researcher identify the Project's human-authorized purpose and documentary anchor, traverse its evidenced part–whole structure without assuming a fixed archival hierarchy, distinguish structural status from Project-relative research use, resolve persistent identifiers at the level they actually identify, recover or account for the exact inspected exports, determine whether required evidence is actually accessible now, distinguish historical work-state from current priority, and continue from the canonical STATUS without old chat?

If not, persist the missing minimum state in the appropriate existing canonical owner.