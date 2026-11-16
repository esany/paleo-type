# Source and provenance methodology

## Authority and purpose

This file owns the reusable **Source/File provenance, preservation and digital-source-criticism semantics** for `paleo-type`.

Project existence, Project boundary, Project→Source research functions and current priority are owned by `methodology/project-lifecycle.md`; this file states only the Source/File consequences needed to keep provenance correct.

Historical research must distinguish a historical/documentary object from related larger/smaller Source objects, from archival/catalogue description, and from the exact digital File through which evidence was inspected. Several records may lie within one archival act; a record may contain sections/attachments; several exports may represent one Source. None of these may be flattened for convenience.

Keep three truth domains separate:

1. **Archival truth** — what Source/record exists, where it belongs, how it is described and how it relates to other records.
2. **Textual/palaeographic truth** — what signs/words are present in a concrete witness.
3. **Historical truth** — what can be inferred about past people, institutions, events and relationships from inspected evidence.

No layer may silently rewrite another.

## Conceptual reference standards

Use established standards as conceptual/interchange references, not infrastructure mandates:

- ICA Records in Contexts concepts for records, instantiations, agents/activities and explicit relations;
- TEI P5 for witness/readings/facsimile/variant/responsibility concepts;
- historical source criticism for provenance, transmission, purpose, dependency and evidential limits.

Do not implement RDF/RiC-O, a graph database or TEI authoring merely to claim standards compliance.

## Source levels without a fixed hierarchy

Scholarly work may need to distinguish holding context, act, record, protocol, section, attachment, witness, locus and digital instantiation. The repository does not hard-code one universal depth.

- every historical/documentary object needing stable identity is a Source node in `corpus/sources.tsv`;
- `source_type` describes evidenced granularity rather than selecting a schema;
- structural containment is explicit `part_of` in `corpus/relationships.tsv`, directed part → whole;
- deeper/different structures use the same relation recursively;
- intermediate nodes exist only when identity, provenance, citation or research requires them.

A shared shelfmark does not collapse distinct records. A separate provider record ID does not by itself prove a separate archival act or Source level. Provider granularity must be evidenced.

Portal image, export sequence, PDF page, archival folio/page and local working IDs are distinct identifiers unless an evidenced mapping links them.

## Stable Source identity

Every canonical Source node has a stable local `source_id` naming the historical/documentary object itself, not a temporary Project function or assumed hierarchy position.

Prefer provenance-derived identity using stable archive/fonds/signature plus evidenced record identity or a stable local identity where provider-level identity is absent. Human-readable title, date and loci remain separate fields. External provider IDs, URLs and URNs are provenance/access attributes, not replacements for the local key.

Provider identifiers retain their actual evidenced granularity. Never synthesize an identifier or reuse a larger-object identifier as though it identified a smaller Source.

Witness sigla are optional presentation aliases only.

## Canonical Corpus owners

- Source identity and inspection stage → `corpus/sources.tsv`;
- Source→Source and other evidenced relations → `corpus/relationships.tsv`;
- exact digital File identity/provenance → `corpus/files.tsv`;
- reusable Source-wide mappings → `corpus/source-data/<source_id>/`;
- shared event/activity context → `corpus/events.tsv`;
- recurring normalized entities → `entities/`.

Discovery is not inspection; inspection is not transcription; transcription is not collation.

## `part_of` integrity

`part_of` is structural truth, not an identity, research-function or priority shortcut.

For every `part_of` relation:

- subject and object are canonical Source nodes;
- subject is part and object is whole;
- status/evidence remain explicit;
- cycles are invalid;
- multiple parent relations are allowed only when evidence warrants them;
- deterministic ancestry resolution reports valid structure rather than guessing one path.

Do not create type-specific parent tables merely because one current corpus pattern is common.

## Persistent identifiers and exact Files

Persistent identifiers/URLs and exact research Files have different roles:

- persistent identifier/URL → institution-side identity/relocation/citation at the level actually identified;
- exact File ID + SHA-256 → the concrete byte sequence actually inspected or preserved.

Preserve both when available. Neither substitutes for the other.

Never infer URNs/identifiers from neighboring values or apparent naming patterns.

## Original-export preservation

The exact archive export used for consequential research is a first-class research asset.

For every central original export used in research:

1. preserve original filename;
2. compute/record SHA-256;
3. record exact Source coverage;
4. record actual/intended controlled path;
5. preserve original bytes unchanged;
6. keep OCR/crops/renders/rotations/compression as separate derivatives with parent provenance;
7. use the exact controlled `storage_status` vocabulary from `corpus/source-contract.json` rather than defining values in prose;
8. state rights/access blockers explicitly rather than calling a link/checksum an equivalent backup.

## Rights statements and preservation decisions

Record the rights statement actually supplied with the object/export. A rights statement is not automatically a licence or redistribution permission.

For `InC/1.0`, preserve the known protected-rights state and keep public redistribution/storage authority as a separate question. Any `storage_status` used for that situation must come from the executable Source Contract and does not by itself create a legal conclusion beyond the documented authority basis.

Repository visibility, repository privacy and owner storage authorization are distinct from public redistribution rights.

## Identity, preservation, reproducibility and research-ready access

Keep these properties distinct:

- **identifiable** — exact Source/File is known;
- **bytes/preservation available** — exact bytes exist at a verified controlled location;
- **reproducible** — a defined derivative can be regenerated from an established parent;
- **research-ready in target context** — the authorized work context can actually obtain/open/inspect what the current task requires.

File ID/SHA, persistent identifiers, crosswalks and render recipes do not self-certify target-context availability. For visual work, use the operational staging/inspectability gate in `workflow.md`.

These are Source/File/access properties, not Project/task authority. A current-context access failure may show that a concrete evidence-dependent action cannot be executed there; it does not by itself establish task-wide blocker status, `NEXT ACTION`, `STOP`, a roadmap dependency, substitute work or scholarly priority. Any such consequence requires its own authoritative dependency basis under `workflow.md` / Project authority.

## Reusable Source data

Mappings that remain true independent of Project use belong once under:

`corpus/source-data/<source_id>/`

Two additive mapping cases are supported under the same Source owner:

- `crosswalk.tsv` maps `archival_folio ↔ export_image/provider_image ↔ PDF_page ↔ evidenced provider locator/URN` where archival foliation is actually established;
- `digital-crosswalk.tsv` may map an exact provider-image File to a page of an exact PDF File when that digital correspondence is observed but archival foliation is not yet established.

The second case does **not** weaken or replace the first. It exists to avoid fabricating a folio merely to record a useful digital mapping. If foliation is later established, add the folio evidence through the folio-centred mapping owner; preserve the earlier digital mapping and its evidence basis. When several PDF representations exist, PDF page locators remain bound to the exact File identity whose sequence was inspected.

Keep only mappings assignable to that Source. Adjacent pages in an export outside the evidenced Source boundary remain File coverage/provenance, not forced Source mapping.

Project-relative research function/locus belongs to the Project owner defined by `project-lifecycle.md`, not to the Source crosswalk.

## Project interface — reference, do not redefine

Use `methodology/project-lifecycle.md` for Project authority, documentary anchoring, Project→Source use and priority semantics.

Source/File-side invariants are only:

- a Project references canonical Source/File nodes rather than redefining them;
- structural status is derived from an already-selected Project's documentary anchor plus canonical `part_of`;
- Project-relative research functions do not mutate Source identity/structure;
- File availability does not create Project use or current priority;
- concrete Project-use→File binding references canonical File identity rather than duplicating it.

## Relationship register

`corpus/relationships.tsv` stores explicit Source/event/entity relationships as evidence-bearing claims.

A catalogue statement such as “extract from X” remains metadata-level until textual relationship is checked. `part_of` states containment only; it does not imply copying, identical authorship/hand, Project function or current work target.

## Witness and collation discipline

When two records/witnesses may transmit related text:

1. identify each independently;
2. locate corresponding loci;
3. inspect/read each witness independently;
4. compare structure/wording;
5. record correspondence/divergence;
6. upgrade relationship only as far as evidence warrants.

A clearer witness may generate a test for another witness; it does not overwrite that witness's graphemes.

## Digital source criticism

For consequential work establish, as applicable:

- canonical Source identity and relevant `part_of` ancestry;
- archive/fonds/signature/title/bounded locus;
- persistent identifier/URL at the level actually identified;
- exact File ID/SHA of the inspected export;
- preservation/storage state and location;
- target-context access/inspectability when direct inspection is required;
- distinct folio, image, PDF/export and legacy IDs;
- completeness of export coverage for the claim;
- provenance of any derivative used materially.

Do not rely on a transient chat attachment as the only durable evidence identity. Do not call evidence research-ready merely because identity/reproduction metadata is known.

## Entities and completeness

Normalized persons/places/institutions may receive stable local IDs in `entities/` when reuse warrants it. Manuscript forms remain separate.

Never claim corpus completeness from accumulated examples alone. Completeness/absence claims require documented repositories/catalogues, boundaries, queries/filters, access limits, inclusion/exclusion criteria and unavailable/not-digitised material.

## Maintenance and restartability

Follow `methodology/maintenance.md` for propagation. Update the Source/File owner whose truth changed, then only affected dependent state.

Final Source/File restartability test:

> Could a fresh capable researcher identify the exact historical Source and locus, traverse evidenced structure, resolve institutional identifiers at their actual granularity, recover/account for exact inspected Files, distinguish preservation/reproducibility from target-context access, and understand what Source relationships are demonstrated without old chat?

If not, persist the missing minimum in the existing canonical Source/File owner rather than creating a parallel registry.
