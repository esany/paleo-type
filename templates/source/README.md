# New source — lean intake

Use the existing canonical owners; do not create a source-specific metadata silo.

1. Identify the **larger parent archival act**. Add it once to `corpus/archival-acts.tsv` if it is not already present. Record only evidenced act-level title/record ID/URL; missing act metadata may remain empty.
2. Add the actual **protocol/source record** used by research to `corpus/sources.tsv` with stable `source_id`, parent `archival_act_id`, protocol title, bounded folio range and provider record ID/URL when those genuinely address the protocol. Do not promote the parent act title to the protocol title.
3. If a digital file is actually used, add it to `corpus/files.tsv` with exact filename, SHA-256, coverage, rights and preservation state, linked to the protocol `source_id`. Do not place protected bytes in the public repository without authority.
4. When consequential work depends on page/image/locus mapping, create `corpus/source-data/<source_id>/crosswalk.tsv` from `crosswalk.tsv` in this directory. Preserve folio, export/image ID, PDF page and stable image URN as separate identifiers. Mark mappings as observed/inferred/unresolved; never invent missing identifiers or URNs. Do not put adjacent pages outside the protocol boundary into its canonical crosswalk.
5. Add project membership/role in `projects/<project>/sources/sources.tsv`, referencing the protocol `source_id`. Project role is relative to this investigation, not an absolute source property.
6. Run `python tools/source_contract.py validate`.
7. Resolve the canonical chain with `python tools/source_contract.py resolve --project <project> --source-id <source_id> [--locus <folio>]` instead of reconstructing it from chat, aliases or filenames.

The machine contract is `corpus/source-contract.json`. It defines only stable structural invariants. Source interpretation remains scholarly judgement.
