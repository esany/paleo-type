# Corpus — canonical act, protocol and file layer

This directory stores project-independent facts about archival acts/records, intellectually meaningful protocol/source units within them, and exact digital instantiations used for research.

## Human reading order

1. `sources.tsv` — parent archival acts/records;
2. `source-units.tsv` — protocol/source units within those acts;
3. `files.tsv` — exact PDFs/images/exports with filename, SHA-256, coverage, preservation state, rights status and, where applicable, source-unit linkage;
4. `source-data/<source_id>/` — reusable parent-act mappings such as export-image/PDF-page/folio crosswalks, optionally tagged to a source unit;
5. `relationships.tsv` — evidence-status-controlled relationships;
6. `events.tsv` — shared event/activity context.

The minimum hierarchy is:

`archival holding/signature → archival act/record → protocol/source unit → witness/locus → digital instantiation`

A provider/DigiRef record ID may identify either an act or a source unit. Its level must be established from archival context; never infer that all provider IDs have the same granularity.

## Current Knau source group

The project uses **four protocol/source units from three archival acts**:

- `ThHStAW, EGA, Reg. Ii 4 Bd. II` — parent act *Visitation in Thüringen* → *Visitation im Amt Ziegenrück*, fol. 294r–313r;
- `ThHStAW, EGA, Reg. Ii 5` — parent act *Registratur für die Superintendentur Neustadt (Orla) (Auszug)* → *Visitation im Amt Ziegenrück*, fol. 55v–66v;
- `ThHStAW, EGA, Reg. Ii 3` — parent act *Visitation in Jena, Neustadt an der Orla, Pößneck, Saalfeld* → *Visitation in Neustadt an der Orla*, fol. 41r–63v;
- the same `Reg. Ii 3` act → *Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)*, fol. 303r–306r.

The last two are separate source units inside one act, not two archival acts. Archivportal Thüringen independently lists both units under archive signature `3`.

## Machine contract and resolver

`source-contract.json` defines lean machine-readable invariants. Run:

`python tools/source_contract.py validate`

Resolve canonical provenance with either a parent act or, preferably for project work, the source unit:

`python tools/source_contract.py resolve --project <project> --source-unit-id <source_unit_id> [--locus <folio>]`

`--source-id <source_id>` remains available, but if a project uses multiple source units from one act the resolver requires `--source-unit-id` to disambiguate them.

The resolver follows:

`project role → protocol/source unit → parent archival act → exact file → parent-act crosswalk/locus`

Missing mappings are reported rather than guessed.

## Identity and ownership

- parent archival act/record identity → `sources.tsv`;
- reusable protocol/source-unit identity/title/extent/provider record → `source-units.tsv`;
- exact file identity/preservation and optional unit linkage → `files.tsv`;
- reusable act-wide folio/image/PDF mapping → `source-data/<source_id>/`;
- project role and relevant locus → project `sources/sources.tsv`, referencing the relevant source unit;
- project reading/analysis → project work directories.

A shared signature does not collapse genuinely separate acts. Conversely, one act may contain many distinct protocol/source units. Do not create a second act merely because a portal exposes a separate unit-level record ID.

## Persistent identifiers

Stable image URNs are copied only when institutionally evidenced. Never synthesize a URN from neighboring identifiers or image-number patterns. A missing URN is a documented gap, not an invitation to guess.

## Exact original exports

The exact source export used for consequential work is a first-class research asset. `files.tsv` is authoritative for byte identity and preservation state. Preferred repository path when rights/authority permit:

`corpus/source-files/<source_id>/original/<original-filename>`

The preserved original must remain byte-identical. OCR/crops/renders are derivatives and must not overwrite it. Because this repository is public, an `InC` marker is not treated as permission to redistribute archive PDFs; blocked public preservation remains explicit in `files.tsv`.
