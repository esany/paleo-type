# Corpus — canonical source and file layer

This directory stores facts about historical sources and their exact digital instantiations independently of any one research project.

## Human reading order

1. `sources.tsv` — which archival/source records exist;
2. `files.tsv` — which exact PDFs/images/exports were used, with filename, SHA-256, coverage, preservation state, intended repository path and rights status;
3. `source-data/<source_id>/` — reusable source-wide mappings such as export-image/PDF-page/folio crosswalks;
4. `relationships.tsv` — evidence-status-controlled relationships between historical/source records;
5. `events.tsv` — shared event/activity context.

A project states **which of these sources it investigates and why** in `projects/<id>/sources/sources.tsv`.

## Source record is not project

A source record may be used by one or several projects without becoming a project itself. A shared archive volume/signature also does not collapse separately catalogued source records.

For the current Knau investigation, the two records in `ThHStAW, EGA, Reg. Ii 3` remain separate because the archive identifies different records/titles/loci:

- `THHSTAW-EGA-REG-II-3-STAT-VIS-00000197` — *Visitation in Neustadt an der Orla*, fol. 41r–63v;
- `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` — *Pfarreinkommen Gössitz, Knau ...*, fol. 303r–306r.

## Exact original exports

The exact source export used for consequential work is a first-class research asset. `files.tsv` is authoritative for its byte identity and preservation state.

Preferred repository path when rights/authority permit:

`corpus/source-files/<source_id>/original/<original-filename>`

The preserved original must remain byte-identical. OCR/crops/renders are derivatives and must not overwrite it.

Because this repository is public, an `InC` marker is not treated as permission to redistribute the archive PDF. Where public upload authority is not established, `files.tsv` records `preservation-blocked-rights`. This is an explicit unresolved preservation gap; URL/URN + checksum is not labelled equivalent backup.

## One fact, one owner

- source identity → `sources.tsv`;
- exact file identity/preservation → `files.tsv`;
- reusable source-wide crosswalk → `source-data/<source_id>/`;
- project role/relevant locus → project `sources/sources.tsv`;
- project reading/analysis → project work directories.

Do not duplicate these records merely to make a project self-contained; make the references human-readable instead.
