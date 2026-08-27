# New source — lean intake

Use the existing canonical owners; do not create a source-specific metadata silo.

1. Add the archival/intellectual record to `corpus/sources.tsv` with a stable local `source_id`, archival identity, record ID/title and stable record URL/PID.
2. If a digital file is actually used for research, add it to `corpus/files.tsv` with exact filename, SHA-256, coverage, rights and preservation state. Do not place protected bytes in the public repository without authority.
3. When consequential work depends on page/image/locus mapping, create `corpus/source-data/<source_id>/crosswalk.tsv` from `crosswalk.tsv` in this directory. Preserve folio, export/image ID, PDF page and stable image URN as separate identifiers. Mark mappings as observed/inferred/unresolved; never invent missing identifiers.
4. Add project membership/role/locus only in `projects/<project>/sources/sources.tsv`.
5. Run `python tools/source_contract.py validate`.
6. For source-level work resolve the canonical chain with `python tools/source_contract.py resolve --project <project> --source-id <source_id> [--locus <folio>]` instead of reconstructing it from chat, aliases or filenames.

The machine contract is `corpus/source-contract.json`. It defines only stable structural invariants. Source interpretation remains scholarly judgement.
