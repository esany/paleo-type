# Corpus — canonical act, protocol and file layer

This directory stores project-independent facts about parent archival acts, the protocol/source records used by research, and the exact digital instantiations used for inspection.

## Human reading order

1. `archival-acts.tsv` — larger archival acts/holding units that contain one or more protocol records;
2. `sources.tsv` — canonical protocol/source records with their parent `archival_act_id` and bounded folio range;
3. `files.tsv` — exact PDFs/images/exports with filename, SHA-256, coverage, preservation state and rights status;
4. `source-data/<source_id>/` — reusable protocol-level folio ↔ export-image ↔ PDF-page ↔ stable-URN crosswalks;
5. `relationships.tsv` — evidence-status-controlled source-to-source claims;
6. `events.tsv` — shared event/activity context.

The minimum hierarchy is:

`archival holding/signature → archival act → protocol/source record → witness/locus → digital instantiation`

For this corpus the project-facing canonical `source_id` identifies the **protocol/source record**, not the larger act. A provider/DigiRef record ID is an external provenance/access identifier and may exist at a different archival level; never infer its semantic level from the number alone.

## Current Knau source group

The project uses **four protocol records from three larger archival acts**:

- `ACT-THHSTAW-EGA-REG-II-4-BD-II` — *Visitation in Thüringen* → `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`, *Visitation im Amt Ziegenrück*, fol. 294r–313r;
- `ACT-THHSTAW-EGA-REG-II-5` — *Registratur für die Superintendenz Neustadt an der Orla (Auszug)* → `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`, *Visitation im Amt Ziegenrück*, fol. 55v–66v;
- `ACT-THHSTAW-EGA-REG-II-3` — *Visitation in Jena, Neustadt an der Orla, Pößneck, Saalfeld* → `THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V`, *Visitation in Neustadt an der Orla*, fol. 41r–63v;
- the same `ACT-THHSTAW-EGA-REG-II-3` → `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235`, *Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)*, fol. 303r–306r.

The two Reg. Ii 3 protocol records therefore share one parent act. A second DigiRef/provider record does not create a second archival act.

## Machine contract and resolver

`source-contract.json` defines the lean machine-readable invariants. Run:

`python tools/source_contract.py validate`

Resolve canonical provenance with:

`python tools/source_contract.py resolve --project <project> --source-id <source_id> [--locus <folio>]`

The resolver follows:

`project role → protocol/source record → parent archival act → exact file → protocol crosswalk/locus`

Missing mappings are reported rather than guessed.

## Identity and ownership

- parent archival-act identity → `archival-acts.tsv`;
- canonical protocol/source identity, title, extent and protocol-level metadata → `sources.tsv`;
- exact file identity/preservation → `files.tsv`;
- reusable protocol-level folio/image/PDF/URN mapping → `source-data/<source_id>/`;
- project role and relevant locus → project `sources/sources.tsv`;
- project reading/analysis → project work directories.

This is deliberately small. There is no second protocol table and no database. Multiple protocols may point to one parent act; the same protocol may have different roles in different projects.

## Persistent identifiers

Stable image URNs are copied only when institutionally evidenced. Never synthesize a URN from neighboring identifiers or image-number patterns. A missing URN is a documented gap, not an invitation to guess.

## Exact original exports

The exact source export used for consequential work is a first-class research asset. `files.tsv` is authoritative for byte identity and preservation state. Preferred repository path when rights/authority permit:

`corpus/source-files/<source_id>/original/<original-filename>`

The preserved original must remain byte-identical. OCR/crops/renders are derivatives and must not overwrite it. Because this repository is public, an `InC` marker is not treated as permission to redistribute archive PDFs; blocked public preservation remains explicit in `files.tsv`.
