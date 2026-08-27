# New source — lean intake

Use the existing canonical owners; do not create a source-specific metadata silo.

1. Add the archival record/act to `corpus/sources.tsv` with stable `source_id`, archival identity and title. Record provider record ID and stable URL/PID when available; do not invent them.
2. If the research uses an identifiable protocol/source unit inside that act, add it once to `corpus/source-units.tsv` with parent `source_id`, unit title/type, evidenced extent/date and evidence/status. Do not copy act-wide metadata into the unit unless it is also true of the unit.
3. If a digital file is actually used, add it to `corpus/files.tsv` with exact filename, SHA-256, coverage, rights and preservation state. Do not place protected bytes in the public repository without authority.
4. When consequential work depends on page/image/locus mapping, create `corpus/source-data/<source_id>/crosswalk.tsv` from `crosswalk.tsv` in this directory. Preserve folio, export/image ID, PDF page and stable image URN as separate identifiers when available. Mark mappings as observed/inferred/unresolved; never invent missing identifiers.
5. Add project membership/role in `projects/<project>/sources/sources.tsv`, referencing both `source_id` and `source_unit_id` where the protocol unit is known. Record a relevant locus and primary file only when actually known.
6. Run `python tools/source_contract.py validate`.
7. Resolve the canonical chain with `python tools/source_contract.py resolve --project <project> --source-id <source_id> [--source-unit-id <source_unit_id>] [--locus <folio>]` instead of reconstructing it from chat, aliases or filenames.

The machine contract is `corpus/source-contract.json`. It defines only stable structural invariants. Source interpretation remains scholarly judgement.
