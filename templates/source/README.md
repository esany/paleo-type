# New source — lean intake

Use the existing canonical owners; do not create a source-specific metadata silo.

1. Add every evidenced historical/documentary object that needs stable identity once to `corpus/sources.tsv`. Use a stable `source_id` and a descriptive `source_type`; do not create a new table merely because the object is an act, protocol, section, attachment or other level.
2. Express evidenced containment in `corpus/relationships.tsv` as `part_of` from part to whole. Add intermediate source nodes only when they matter for identity, provenance, citation or research. Do not invent hierarchy for symmetry.
3. If a digital file is actually used, add it to `corpus/files.tsv` with exact filename, SHA-256, coverage, rights and preservation state, linked to the source node the file materially instantiates. Do not place protected bytes in the public repository without authority.
4. When consequential work depends on page/image/locus mapping, create `corpus/source-data/<source_id>/crosswalk.tsv` from `crosswalk.tsv` in this directory. Preserve folio, export/image ID, PDF page and stable image URN as separate identifiers. Mark mappings as observed/inferred/unresolved; never invent missing identifiers or URNs. Do not force adjacent material outside an evidenced source boundary into its crosswalk.
5. Add project membership/role in `projects/<project>/sources/sources.tsv`, referencing the source node actually used by the investigation. Project role is relative to the project, not an absolute source property.
6. Run `python tools/source_contract.py validate`.
7. Resolve the canonical chain with `python tools/source_contract.py resolve --project <project> --source-id <source_id> [--locus <folio>]`. The resolver follows generic `part_of` ancestry and never assumes a fixed archival depth.

The machine contract is `corpus/source-contract.json`. It defines only structural invariants. Source interpretation and the scholarly meaning of a relationship remain evidence-based judgement.
