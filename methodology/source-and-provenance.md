# Source and provenance methodology

This file defines the generic archival/source-critical core for corpus work in `paleo-type`. It applies to all projects.

## Purpose

Historical research must distinguish the historical record from the way an archive/catalogue describes it and from the exact digital file through which it was inspected. Multiple protocol/source units may live in one archival act; multiple separately catalogued records may share a holding context; multiple exports may represent the same act or unit. None of these situations may be flattened for convenience.

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
- **archival act/record** — an intellectually/administratively meaningful archival record or act;
- **protocol/source unit** — an evidenced, bounded intellectual/documentary unit within an act, such as one visitation protocol or income register section;
- **witness** — a concrete textual witness relevant to a reading/collation problem;
- **locus** — folio/page/region/line within a witness;
- **instantiation** — scan, image, PDF/export or other representation actually used for inspection;
- **research source** — catalogue/finding aid, edition, article, book or other secondary/control source.

A shared shelfmark does not make genuinely separate acts one record. Conversely, a separate portal/DigiRef record ID does not automatically create a new archival act: a provider may expose a protocol/source unit within a larger act as its own digital record.

A portal image number is never a folio merely because both are numbers. A PDF page is never a manuscript page unless demonstrated.

## Stable source identity

Every parent archival act/record gets a stable local `source_id`. The canonical ID identifies the act/record, not its temporary project role and not automatically a provider-side unit record.

Every reusable protocol/source unit gets a stable local `source_unit_id` once its identity/boundary is evidenced. Project roles normally attach to the source unit actually used, while the unit retains an explicit parent `source_id`.

Prefer provenance-derived identities based on stable archive/fonds/signature/record context. Human-readable titles, dates, folios, provider record IDs and URLs remain separate fields. External URLs/URNs are attributes/evidence for identity, not replacements for local keys.

Provider identifiers must retain their evidenced granularity. If `stat_visitation_x` identifies a protocol unit inside an act, record it on that unit rather than promoting it to the parent-act identity merely because it is persistent.

Witness sigla are optional presentation aliases only and belong at the level they actually abbreviate.

## Corpus inventory

`corpus/sources.tsv` is the canonical inventory of parent archival acts/records and their inspection stage.

`corpus/source-units.tsv` is the canonical inventory of reusable protocol/source units identified within those acts.

`corpus/files.tsv` is the canonical manifest of exact digital instantiations used in research. A file row points to its parent act and, when the file specifically instantiates a known unit, to `source_unit_id` as well.

Discovery is not inspection; inspection is not transcription; transcription is not collation.

## Persistent identifiers and exact instantiations

Persistent identifiers such as URNs and stable archival URLs are **first-class provenance and working identifiers**. They support durable citation, re-location of the archive-provided digital object, comparison with the provider's current representation and linkage back to institutional metadata.

They have a different evidential quality from the exact file used in research. A persistent identifier identifies or relocates the archive-side object/representation; a checksum identifies the concrete byte sequence actually inspected or preserved. Neither replaces the other.

Therefore preserve both when available:

- archive act/unit identity + persistent identifier/URL at the level it actually identifies;
- exact file identity + original filename + SHA-256 + coverage + preservation state.

Do not downgrade a URN to a mere convenience link, and do not treat it as an equivalent backup of the exact export. Never synthesize a URN by extrapolating from neighboring image IDs or URN patterns.

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

Parent-act-wide mapping that remains true regardless of project belongs once under:

`corpus/source-data/<source_id>/`

Typical example: a controlled `export_image ↔ PDF_page ↔ archival_folio` crosswalk. When a mapped row falls within a known protocol/source unit, record `source_unit_id`; when a boundary image lies outside the unit or is unresolved, leave the unit link empty rather than forcing it.

Project-specific statements such as "this investigation uses fol. 61v–63r as principal locus" belong in the project source register.

Do not copy the same source-wide crosswalk into each consuming project.

## Project source groups

A project is an investigation, not a source container. Its source group is declared in:

`projects/<id>/sources/sources.tsv`

That register references the parent act and, when known, the relevant protocol/source unit, then records project role and relevant locus. Multiple project rows may therefore point to different source units within the same parent act. Project role is a relation from project to unit/source use, never an absolute source property.

## Relationship register

`corpus/relationships.tsv` is the canonical place for explicit relationships between historical/source records, protocol units, events and entities.

A relationship is itself a research claim and therefore has subject, predicate, object, status, evidence basis and limitation/note.

Useful statuses include `observed`, `metadata-supported`, `working`, `unresolved`, `rejected`.

A catalogue statement such as “extract from X” remains metadata-level until textual relationship is checked. Do not silently upgrade it to copying/dependence.

## Event/activity context

`corpus/events.tsv` records administrative/historical activities that connect records/units without implying textual identity. Event co-membership is contextual evidence, not proof of textual dependence.

## Witness and collation discipline

When two units/witnesses may transmit related text:

1. identify each independently by canonical source/unit identity;
2. locate corresponding loci;
3. inspect/read each witness independently;
4. compare structure/wording;
5. record correspondences/divergences;
6. upgrade relationship only as far as evidence warrants.

A clearer witness may generate a test for an unclear token in another witness; it does not overwrite that witness's graphemes.

## Digital source criticism

For consequential work determine:

- archive/fonds/signature and parent act/record;
- protocol/source-unit identity and extent when the claim concerns a bounded unit;
- act/unit title and locus;
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

- parent act identity/stage and act-level persistent identifiers → `corpus/sources.tsv`;
- reusable protocol/source-unit identity/extent/provider identifiers → `corpus/source-units.tsv`;
- exact file/checksum/coverage/storage/rights and unit linkage → `corpus/files.tsv`;
- reusable parent-act crosswalk → `corpus/source-data/<source_id>/`;
- source/unit relationship → `corpus/relationships.tsv`;
- project source-unit membership/role/locus → project `sources/sources.tsv`;
- project inspection detail → project `sources/inspection-log.tsv` when needed;
- project consequence/next action → project `STATUS.md`.

Final test:

> Could another capable researcher identify every parent archival act in the investigation, distinguish the protocol/source units actually used, resolve their persistent identifiers at the correct level, recover or account for the exact inspected exports, understand project roles/loci, distinguish catalogue claims from demonstrated relationships, and continue without chat?

If not, persist the missing minimum state.
