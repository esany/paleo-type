# Corpus — canonical source and file layer

This directory stores facts about historical sources and their exact digital instantiations independently of any one research project.

## Human reading order

1. `sources.tsv` — which archival/catalogued records or acts exist;
2. `files.tsv` — which exact PDFs/images/exports were used, with filename, SHA-256, coverage, preservation state, intended repository path and rights status;
3. `source-data/<source_id>/` — reusable record-wide mappings such as export-image/PDF-page/folio crosswalks;
4. `relationships.tsv` — evidence-status-controlled relationships between historical/source records;
5. `events.tsv` — shared event/activity context.

A project states **which archival records contain the protocol/source units relevant to its investigation and why** in `projects/<id>/sources/sources.tsv`.

## Archival record is not protocol/source group

A catalogued archival record or act can contain one or more intellectually meaningful protocol/source units. Do not treat the act title, record ID or full record extent as automatically identical with the protocol/source group used by a project.

The minimum hierarchy is:

`archival holding/signature → archival record/act → protocol/source unit → witness/locus → digital instantiation`

The current corpus inventory and file/crosswalk resolver are reliable at the **archival record/act and locus provenance levels**. Where a protocol/source unit inside an act has not yet been canonically delimited, that gap must remain explicit; the system must not manufacture a unit identity from the act title.

For the Knau project, `ThHStAW, EGA, Reg. Ii 3 / stat_visitation_00000197` — *Visitation in Jena, Neustadt an der Orla, Pößneck, Saalfeld* — is the archival act/record. It is not itself the name of the project’s relevant protocol/source group.

## Machine contract and resolver

`source-contract.json` is the lean machine-readable contract for stable source/provenance invariants. It does not contain research facts and does not replace scholarly judgement.

Run:

`python tools/source_contract.py validate`

For record/locus-level work, resolve the canonical chain rather than reconstructing it from chat, aliases or filenames:

`python tools/source_contract.py resolve --project <project> --source-id <source_id> [--locus <folio>]`

The resolver follows project membership to the canonical archival record, selected primary file and record-wide crosswalk. A missing exact locus mapping is reported as a gap rather than guessed. If the project marks the protocol/source unit within the archival record as unresolved, the resolver reports that limitation explicitly instead of treating the act title as the unit identity. GitHub runs the validator automatically when source/provenance structures change.

New-source intake guidance and the crosswalk header template live in `templates/source/`.

## Source record is not project

An archival record may be used by one or several projects without becoming a project itself. A shared archive volume/signature also does not collapse separately catalogued archival records.

For the current Knau investigation, the two records in `ThHStAW, EGA, Reg. Ii 3` remain separate because the archive identifies different records/titles/loci:

- `THHSTAW-EGA-REG-II-3-STAT-VIS-00000197` — *Visitation in Jena, Neustadt an der Orla, Pößneck, Saalfeld*, fol. 41r–63v;
- `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` — *Pfarreinkommen Gössitz, Knau ...*, fol. 303r–306r.

This separation is necessary but not sufficient: protocol/source units inside those acts must still be identified at the level warranted by inspection.

## Exact original exports

The exact source export used for consequential work is a first-class research asset. `files.tsv` is authoritative for its byte identity and preservation state.

Preferred repository path when rights/authority permit:

`corpus/source-files/<source_id>/original/<original-filename>`

The preserved original must remain byte-identical. OCR/crops/renders are derivatives and must not overwrite it.

Because this repository is public, an `InC` marker is not treated as permission to redistribute the archive PDF. Where public upload authority is not established, `files.tsv` records `preservation-blocked-public-redistribution`. This is an explicit unresolved preservation gap; URL/URN + checksum is not labelled equivalent backup.

## One fact, one owner

- archival record/act identity → `sources.tsv`;
- exact file identity/preservation → `files.tsv`;
- reusable record-wide crosswalk → `source-data/<source_id>/`;
- project role/relevant protocol/locus → project `sources/sources.tsv` until a reusable protocol/source-unit representation is justified and adopted;
- project reading/analysis → project work directories.

Do not duplicate these records merely to make a project self-contained; make the references human-readable instead. Do not invent a protocol/source-unit identifier merely to fill a structural slot.
