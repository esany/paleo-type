# New source — lean intake

Use the existing canonical owners; do not create a source-specific metadata silo.

1. Identify the **parent archival act/record** first and add it to `corpus/sources.tsv` with stable `source_id`, archival identity and title. A portal/DigiRef record ID belongs here only if it actually identifies the parent act; provider IDs may exist at finer protocol/source-unit level.
2. If the research uses an identifiable **protocol/source unit** inside that act, add it once to `corpus/source-units.tsv` with parent `source_id`, unit title/type, evidenced extent/date, status/evidence and provider record ID/URL when those identify the unit. Do not create a second parent act merely because the portal exposes a separate unit record.
3. If a digital file is actually used, add it to `corpus/files.tsv` with exact filename, SHA-256, coverage, rights and preservation state. Link `source_unit_id` when the export specifically instantiates a known unit. Do not place protected bytes in the public repository without authority.
4. When consequential work depends on page/image/locus mapping, create `corpus/source-data/<source_id>/crosswalk.tsv` from `crosswalk.tsv` in this directory. Preserve folio, export/image ID, PDF page and stable image URN as separate identifiers. Link rows to `source_unit_id` only where the row actually falls within that evidenced unit. Mark mappings as observed/inferred/unresolved; never invent missing identifiers or URNs.
5. Add project membership/role in `projects/<project>/sources/sources.tsv`, referencing the parent `source_id` and the actual `source_unit_id` when known. Project role is relative to the unit/source use, not an absolute source property.
6. Run `python tools/source_contract.py validate`.
7. Resolve the canonical chain preferably by source unit: `python tools/source_contract.py resolve --project <project> --source-unit-id <source_unit_id> [--locus <folio>]`. `--source-id` is also supported; if an act contributes multiple units, the resolver requires unit disambiguation.

The machine contract is `corpus/source-contract.json`. It defines only stable structural invariants. Source interpretation remains scholarly judgement.
