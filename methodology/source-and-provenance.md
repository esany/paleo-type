# Source and provenance methodology

This file defines the generic archival/source-critical core for corpus work in `paleo-type`. It applies to all projects.

## Purpose

Historical research must distinguish the historical record from the way an archive/catalogue describes it and from the digital file through which we inspect it. Ambiguous archive exports, multiple records from the same administrative process and later extracts are normal features of archival transmission, not noise to be flattened away.

The repository therefore keeps three kinds of truth separate:

1. **Archival truth** — what object/record exists, where it belongs, how it is described, and how it relates to other records.
2. **Textual/palaeographic truth** — what signs/words are actually present in a concrete witness.
3. **Historical truth** — what can be inferred about past people, institutions, events and relationships from inspected evidence.

No layer may silently rewrite another.

## Conceptual reference standards

`paleo-type` follows the concepts, not the implementation burden, of established scholarly standards:

- **ICA Records in Contexts (RiC)** for distinguishing records, instantiations, agents/activities and explicit relations between records;
- **TEI P5** for the long-term requirement that witnesses, readings, manuscript/facsimile references, variants and responsibility can be represented without loss;
- normal historical source criticism for provenance, transmission, authorship/agency, context, purpose, authenticity, dependency and evidential limits.

Do not implement RDF/RiC-O, a graph database or TEI authoring merely to claim standards compliance. The lean TSV/YAML/Markdown model remains canonical until a concrete interchange/publication need justifies migration or export.

## Required source levels

Do not use `source` as an undifferentiated term when precision matters. Distinguish:

- **archival unit** — archive/fonds/shelfmark or other holding unit;
- **record** — an intellectually/administratively meaningful document or record unit;
- **witness** — a concrete textual witness relevant to a reading/collation problem;
- **locus** — folio/page/region/line within a witness;
- **instantiation** — scan, image, PDF/export or other representation used for inspection;
- **research source** — catalogue/finding aid, edition, article, book or other secondary/control source.

A portal image number is never a folio merely because both are numbers. A PDF page is never a manuscript page unless demonstrated. Keep every numbering system in a separate field.

## Stable local identity and sigla

Every corpus source gets a stable local `source_id`. **The canonical ID must identify the source, not its temporary research role.** Bare ordinal labels such as `A`, `B`, `C1` or `source-1` are prohibited as corpus primary keys.

Prefer a compact identity-derived ID based on stable archival/catalogue identifiers, conceptually for example:

`ARCHIVE-FONDS-SIGNATURE-RECORD-ID`

The human-readable title, date and folios remain separate fields; do not encode uncertain interpretation into the key. External IDs/URLs/URNs are attributes/evidence for identity, not replacements for the local key.

Witness sigla are allowed only as optional presentation/collation aliases after the witness has been fully identified. A siglum must never be the only durable identifier or corpus foreign key.

A stable source identity should preserve, where available:

`archive + fonds + signature + record_id + title + date range + folios + persistent/digital URL`

For consequential image/file-based work, the exact inspected instantiation must also be recoverable. `corpus/files.tsv` is the canonical manifest for external/digital source files or instantiations and records, where available/applicable, file identity, checksum, source coverage, storage expectation and rights status. Stable portal URLs/URNs remain part of source/digital provenance; project crosswalks map internal image/PDF/export positions to folios without becoming a competing file manifest.

Never invent missing identifiers.

## Corpus inventory

`corpus/sources.tsv` is the canonical corpus-level inventory of archival/source units and their inspection stage.

`corpus/files.tsv` is the canonical corpus-level manifest of external/digital source files or instantiations used in research. A source row identifies the archival/intellectual source; a file row identifies the concrete representation used or expected for inspection.

Discovery is not inspection; inspection is not transcription; transcription is not collation.

Use `inspection_status` descriptively, for example:
- `discovered`
- `metadata-inspected`
- `images-inspected`
- `partially-transcribed`
- `fully-transcribed`
- `collated`

Do not treat a status as a quality score.

## Relationship register

`corpus/relationships.tsv` is the canonical place for explicit relationships between sources/events/entities.

A relationship is itself a research claim and therefore has subject, predicate, object, status, evidence basis and limitation/note.

Useful relationship statuses include:
- `observed`
- `metadata-supported`
- `working`
- `unresolved`
- `rejected`

A catalogue statement such as “extract from X” remains `metadata-supported` until the relevant textual relationship is checked. Do not silently upgrade metadata relationship claims to `copy_of` or textual correspondence.

## Event/activity context

`corpus/events.tsv` records administrative/historical activities that connect records without implying textual identity. Two records may belong to the same activity while being independent reports, lists, extracts, copies or later derivatives. Event co-membership is contextual evidence, not proof of textual dependence.

## Witness and collation discipline

When two records may transmit related text:

1. identify each witness independently by canonical source identity;
2. optionally assign short sigla for a specific apparatus, recording their expansion;
3. locate the putatively corresponding loci;
4. transcribe/read each witness without importing the other's spelling;
5. record structural/textual correspondences and divergences;
6. only then classify the relationship as demonstrated, partial, dependent, independent or unresolved as evidence permits.

A clearer reading in one witness may support identification/interpretation of an unclear token in another, but it does not change the graphemes visible in the latter.

## Digital source criticism

Digitised archives add a second mediation layer that must itself be criticized. For consequential work ask:

- What record did the portal/export actually select?
- Which external/digital file or instantiation was inspected, and is it represented in `corpus/files.tsv` when file-based work is consequential?
- Which numbering system is visible: folio, portal image, PDF page, export sequence, legacy working ID?
- Is the export complete for the claimed range?
- Are metadata from archive, aggregator, editor and researcher distinguishable?
- Is an image original, cropped, scaled, rotated or otherwise derived?
- Can the exact inspected instantiation be recovered without chat?

Do not infer archival completeness from a portal search result or export convenience.

## Entities and authority control

Normalized persons/places/institutions may receive stable local IDs in `entities/` when repeated use makes this useful.

Keep manuscript forms and normalized identities separate. Conceptually:
- transcription: historical manuscript place/name form;
- normalized entity: modern/authority-controlled identity.

An unresolved manuscript token must never be silently overwritten by a historically plausible identity. External authority identifiers are optional and must be verified before entry.

## Corpus completeness

Never claim “all available sources” from accumulated examples alone. Corpus-level completeness claims require a documented search boundary: repositories/catalogues searched, date/geographic limits, query strategies, access dates, inclusion/exclusion criteria and known unavailable/not-digitised material.

Until then prefer bounded language such as:

> all sources identified within the documented repositories/search strategy and access limits

Absence from a search result is not evidence of historical absence.

## Research priority

Source inventory is not an invitation to transcribe everything. Prioritize sources by expected research value to the active question. Full transcription is not a default requirement merely because a source was discovered.

## Maintenance and restartability

When archival/source knowledge changes research truth:
- corpus source identity/stage → `corpus/sources.tsv`;
- external/digital source file identity/checksum/coverage/storage/rights → `corpus/files.tsv`;
- source relationship → `corpus/relationships.tsv`;
- event context → `corpus/events.tsv`;
- normalized recurring entity → `entities/`;
- project-specific exact image/folio/PDF/export mapping and inspection detail → project `sources/`;
- project consequence/next action → project `STATUS.md`.

Do not duplicate these truths in chat, Wiki or parallel notes.

Final test:

> Could another capable researcher identify the exact source and inspected instantiation, understand what was actually inspected, distinguish catalogue claims from demonstrated relationships, and continue without recovering chat?

If not, persist the missing minimum state.