# Corpus — canonical source, protocol and file layer

This directory stores project-independent facts about archival records/acts, intellectually meaningful protocol/source units within them, and the exact digital instantiations used for research.

## Human reading order

1. `sources.tsv` — archival/catalogued records or acts;
2. `source-units.tsv` — protocol/source units within those records when identified;
3. `files.tsv` — exact PDFs/images/exports with filename, SHA-256, coverage, preservation state, intended repository path and rights status;
4. `source-data/<source_id>/` — reusable record-wide mappings such as export-image/PDF-page/folio crosswalks;
5. `relationships.tsv` — evidence-status-controlled relationships;
6. `events.tsv` — shared event/activity context.

The minimum hierarchy is:

`archival holding/signature → archival record/act → protocol/source unit → witness/locus → digital instantiation`

An act title, record ID or full act extent is not automatically the protocol/source-group identity. A protocol/source unit may be coterminous with its parent record, but the levels remain conceptually distinct.

For the Knau project, `ThHStAW, EGA, Reg. Ii 3 / stat_visitation_00000197` — *Visitation in Jena, Neustadt an der Orla, Pößneck, Saalfeld* — is the parent archival act/record. Its relevant protocol/source unit is `UNIT-REG-II-3-00000197-NEUSTADT-VIS` — *Visitation in Neustadt an der Orla*, fol. 41r–63v, with supplied exact range 1529-05-23 to 1529-06-01. These protocol facts belong in `source-units.tsv`, not on the parent act row.

## Machine contract and resolver

`source-contract.json` defines the lean machine-readable invariants. Run:

`python tools/source_contract.py validate`

Resolve canonical provenance with:

`python tools/source_contract.py resolve --project <project> --source-id <source_id> [--source-unit-id <source_unit_id>] [--locus <folio>]`

The resolver follows project use to the parent archival record, protocol/source unit when present, selected primary file and record-wide crosswalk. Missing mappings are reported rather than guessed. If multiple protocol units from one act are used in a project, `--source-unit-id` disambiguates them.

## Identity and ownership

- archival record/act identity → `sources.tsv`;
- reusable protocol/source-unit identity, title, extent and unit-level dates → `source-units.tsv`;
- exact file identity/preservation → `files.tsv`;
- reusable record-wide folio/image/PDF mapping → `source-data/<source_id>/`;
- project role and relevant locus → project `sources/sources.tsv`, referencing both `source_id` and `source_unit_id` where the unit is known;
- project reading/analysis → project work directories.

A shared signature does not collapse separate acts/records. Conversely, one act may contain several protocol/source units. Do not invent a source-unit identifier until the unit is evidenced and delimited.

## Exact original exports

The exact source export used for consequential work is a first-class research asset. `files.tsv` is authoritative for byte identity and preservation state. Preferred repository path when rights/authority permit:

`corpus/source-files/<source_id>/original/<original-filename>`

The preserved original must remain byte-identical. OCR/crops/renders are derivatives and must not overwrite it. Because this repository is public, an `InC` marker is not treated as permission to redistribute archive PDFs; blocked public preservation remains explicit in `files.tsv`.
