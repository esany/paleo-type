# Source and provenance methodology

This file defines the generic archival/source-critical core for corpus work in `paleo-type`. It applies to all projects.

## Purpose

Historical research must distinguish the historical record from the way an archive/catalogue describes it and from the exact digital file through which it was inspected. Multiple separately catalogued records may live in the same archival volume; multiple exports may represent the same record. Neither situation may be flattened for convenience.

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

- **archival unit** — archive/fonds/shelfmark or other holding unit;
- **record/source record** — an intellectually/administratively meaningful document or catalogued record/section;
- **witness** — a concrete textual witness relevant to a reading/collation problem;
- **locus** — folio/page/region/line within a witness;
- **instantiation** — scan, image, PDF/export or other representation actually used for inspection;
- **research source** — catalogue/finding aid, edition, article, book or other secondary/control source.

A shared shelfmark does not make two separately identified records one source. Conversely, multiple PDFs of the same record do not create multiple historical sources.

A portal image number is never a folio merely because both are numbers. A PDF page is never a manuscript page unless demonstrated.

## Stable source identity

Every corpus source gets a stable local `source_id`. The canonical ID identifies the archival/intellectual source record, not its temporary project role.

Prefer a provenance-derived identity based on stable archive/fonds/signature/record identity. Human-readable title, date and folios remain separate fields. External URLs/URNs are attributes/evidence for identity, not replacements for the local key.

Witness sigla are optional presentation aliases only.

For example, two separately catalogued records in `ThHStAW, EGA, Reg. Ii 3` retain different `source_id`, record ID, archival title and folio range even though they share the same signature.

## Corpus inventory

`corpus/sources.tsv` is the canonical inventory of archival/source records and their inspection stage.

`corpus/files.tsv` is the canonical manifest of exact digital instantiations used in research. A source row identifies the archival/intellectual source; a file row identifies the concrete byte-level representation.

Discovery is not inspection; inspection is not transcription; transcription is not collation.

## Original-export preservation

The exact archive export used to support consequential research is a **first-class research asset**.

A URL or URN can help relocate an archive record but is not equivalent to the exact export that was inspected. Portals can change rendering, sequence, metadata, availability or export behavior.

For every central original export used by a project:

1. preserve the original filename;
2. compute and record SHA-256;
3. record exact source coverage;
4. record the repository path where the original is or is intended to be preserved;
5. preserve the original bytes unchanged — do not overwrite with OCR, compression, crop, rotation or normalization;
6. keep derived renders/crops/OCR as separate derivatives linked back to the original file ID;
7. make preservation state explicit (`repo-preserved`, `external-controlled`, `preservation-blocked`, etc.);
8. if rights/access constraints prevent repository storage, state the blocker explicitly. Do not claim that checksum + URN constitutes equivalent backup.

For a public repository, a rights marker such as `InC` does not itself grant redistribution permission. Public upload of such a binary requires an adequate rights/authority basis. Rights uncertainty is a preservation blocker to record and resolve, not a reason to silently discard the original or pretend a portal reference is enough.

## Reusable source data

Source-wide mapping that remains true regardless of project belongs once under:

`corpus/source-data/<source_id>/`

Typical example: a controlled `export_image ↔ PDF_page ↔ archival_folio` crosswalk for a particular export/source.

Project-specific statements such as "this investigation uses fol. 61v–63r as principal locus" belong in the project source register.

Do not copy the same source-wide crosswalk into each consuming project.

## Project source groups

A project is an investigation, not a source container. Its source group is declared in:

`projects/<id>/sources/sources.tsv`

That register records project role and relevant locus while referencing canonical source/file IDs. It must preserve separately identified archival records as separate rows even when they share a volume/signature.

## Relationship register

`corpus/relationships.tsv` is the canonical place for explicit relationships between historical/source records/events/entities.

A relationship is itself a research claim and therefore has subject, predicate, object, status, evidence basis and limitation/note.

Useful statuses include `observed`, `metadata-supported`, `working`, `unresolved`, `rejected`.

A catalogue statement such as “extract from X” remains metadata-level until textual relationship is checked. Do not silently upgrade it to copying/dependence.

## Event/activity context

`corpus/events.tsv` records administrative/historical activities that connect records without implying textual identity. Event co-membership is contextual evidence, not proof of textual dependence.

## Witness and collation discipline

When two records may transmit related text:

1. identify each independently by canonical source identity;
2. locate corresponding loci;
3. inspect/read each witness independently;
4. compare structure/wording;
5. record correspondences/divergences;
6. upgrade relationship only as far as evidence warrants.

A clearer witness may generate a test for an unclear token in another witness; it does not overwrite that witness's graphemes.

## Digital source criticism

For consequential work determine:

- archive/fonds/signature/record;
- record title and locus;
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

- source identity/stage → `corpus/sources.tsv`;
- exact file/checksum/coverage/storage/rights → `corpus/files.tsv`;
- reusable source-wide crosswalk → `corpus/source-data/<source_id>/`;
- source relationship → `corpus/relationships.tsv`;
- project source membership/role/locus → project `sources/sources.tsv`;
- project inspection detail → project `sources/inspection-log.tsv` when needed;
- project consequence/next action → project `STATUS.md`.

Final test:

> Could another capable researcher identify every distinct archival record in the investigation, recover or account for the exact inspected export, understand its project role/locus, distinguish catalogue claims from demonstrated relationships, and continue without chat?

If not, persist the missing minimum state.