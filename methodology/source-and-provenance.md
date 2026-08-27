# Source and provenance methodology

This file defines the generic archival/source-critical core for corpus work in `paleo-type`. It applies to all projects.

## Purpose

Historical research must distinguish a bounded historical/source record from the larger archival act that contains it, from the way a catalogue or portal describes either level, and from the exact digital file through which the source was inspected. Several protocol records may lie within one archival act; several exports may represent one protocol; provider record IDs may occur at different descriptive levels. None of these may be flattened for convenience.

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

## Required source levels

Distinguish:

- **archival unit / holding context** — archive/fonds/shelfmark or other holding unit;
- **archival act** — a larger archival/documentary unit that may contain one or several bounded records/protocols;
- **record/source record** — an intellectually/documentarily meaningful bounded record used as a research source, for example one visitation protocol or one income record;
- **witness** — a concrete textual witness relevant to a reading/collation problem;
- **locus** — folio/page/region/line within a witness;
- **instantiation** — scan, image, PDF/export or other representation actually used for inspection;
- **research source** — catalogue/finding aid, edition, article, book or other secondary/control source.

A shared shelfmark does not collapse distinct protocol records. Conversely, a separate portal/DigiRef record ID does not automatically prove a separate archival act: a provider may expose a bounded protocol inside a larger act as its own digital record.

A portal image number is never a folio merely because both are numbers. A PDF page is never a manuscript page unless demonstrated.

## Stable source identity

Every canonical protocol/source record gets a stable local `source_id`. The ID identifies that bounded historical/intellectual record, not its temporary project role and not its parent act.

Where several canonical sources share a larger archival act, the parent is represented once by `archival_act_id`. The parent relation does not make the protocols one source.

Prefer provenance-derived source identity using stable archive/fonds/signature together with evidenced record identity or, when no protocol-level provider ID exists, a stable local identity derived from title and bounded locus. Human-readable title, date and folios remain separate fields. External provider IDs, URLs and URNs are provenance/access attributes, not replacements for the local key.

Provider identifiers must retain their evidenced granularity. If a provider ID identifies a parent act, do not reuse it as though it were a protocol-level identity. If it identifies a bounded protocol, retain it on that protocol.

Witness sigla are optional presentation aliases only.

## Corpus inventory

`corpus/archival-acts.tsv` is the lean parent register for larger archival acts when this distinction is needed.

`corpus/sources.tsv` is the canonical inventory of bounded protocol/source records and their parent `archival_act_id`.

`corpus/files.tsv` is the canonical manifest of exact digital instantiations actually used in research. A file row identifies the protocol/source record whose material the export instantiates; exact export coverage may include adjacent pages, but adjacent material outside the source boundary must not silently become part of that source.

Discovery is not inspection; inspection is not transcription; transcription is not collation.

## Persistent identifiers and exact instantiations

Persistent identifiers such as URNs and stable archival URLs are **first-class provenance and working identifiers**. They support durable citation, re-location of the archive-provided digital object, comparison with the provider's current representation and linkage back to institutional metadata.

They have a different evidential quality from the exact file used in research. A persistent identifier identifies or relocates the archive-side object/representation; a checksum identifies the concrete byte sequence actually inspected or preserved. Neither replaces the other.

Therefore preserve both when available:

- parent act and protocol/source identity + persistent identifier/URL at the level it actually identifies;
- exact file identity + original filename + SHA-256 + coverage + preservation state.

Do not downgrade a URN to a mere convenience link, and do not treat it as an equivalent backup of the exact export. Never synthesize a URN by extrapolating from neighboring image IDs or apparent URN patterns.

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

A mapping that remains true for a protocol/source record regardless of project belongs once under:

`corpus/source-data/<source_id>/`

Typical example: a controlled `archival_folio ↔ export_image ↔ PDF_page ↔ stable_image_urn` crosswalk. Keep only loci assignable to that source record. If an exact export contains adjacent pages outside the evidenced protocol boundary, record that fact in file provenance rather than forcing those pages into the protocol crosswalk.

Project-specific statements such as "this investigation uses fol. 61v–63r as principal locus" belong in the project source register.

Do not copy the same source crosswalk into each consuming project.

## Project source groups

A project is an investigation, not a source container. Its source group is declared in:

`projects/<id>/sources/sources.tsv`

That register references canonical protocol `source_id` values and records project role and relevant locus. Several project sources may share one parent archival act. Project role is a relation from project to source use, never an absolute source property.

## Relationship register

`corpus/relationships.tsv` is the canonical place for explicit relationships between historical/source records, events and entities.

A relationship is itself a research claim and therefore has subject, predicate, object, status, evidence basis and limitation/note.

Useful statuses include `observed`, `metadata-supported`, `working`, `unresolved`, `rejected`.

A catalogue statement such as “extract from X” remains metadata-level until textual relationship is checked. Do not silently upgrade it to copying/dependence.

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

- archive/fonds/signature and parent archival act;
- canonical protocol/source identity and evidenced extent;
- title and locus;
- persistent identifier/archival URL at the level it actually identifies, where available;
- exact file ID and SHA-256 of the inspected export;
- whether that exact export is preserved and where;
- folio, portal image, PDF page, export sequence and legacy IDs as separate identifiers;
- whether export coverage is complete for the claim;
- whether a working derivative differs from the original.

Do not rely on a transient chat attachment as the only durable evidence identity.

## Entities and authority control

Normalized persons/places/institutions may receive stable local IDs in `entities/` when repeated use makes this useful. Keep manuscript forms and normalized identities separate.

## Corpus completeness

Never claim “all available sources” from accumulated examples alone. Corpus-level completeness claims require documented repositories/catalogues, boundaries, queries/filters, access dates, inclusion/exclusion criteria and known unavailable/not-digitised material.

## Research priority

Source inventory is not an invitation to transcribe everything. Prioritize sources by expected research value to the active investigation.

## Maintenance and restartability

When source knowledge changes:

- parent act identity → `corpus/archival-acts.tsv`;
- canonical protocol/source identity, extent and protocol-level provider identifiers → `corpus/sources.tsv`;
- exact file/checksum/coverage/storage/rights → `corpus/files.tsv`;
- reusable protocol crosswalk → `corpus/source-data/<source_id>/`;
- source relationship → `corpus/relationships.tsv`;
- project source membership/role/locus → project `sources/sources.tsv`;
- project inspection detail → project `sources/inspection-log.tsv` when needed;
- project consequence/next action → project `STATUS.md`.

Final test:

> Could another capable researcher identify every protocol/source record in the investigation, place it in its parent archival act, resolve persistent identifiers at the level they actually identify, recover or account for the exact inspected exports, understand project roles/loci, distinguish catalogue claims from demonstrated relationships, and continue without chat?

If not, persist the missing minimum state.
