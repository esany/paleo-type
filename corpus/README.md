# Corpus — canonical source and file layer

This directory stores project-independent facts about historical/documentary Source nodes, their explicit relationships, and the exact digital instantiations used for inspection.

## Human reading order

1. `sources.tsv` — canonical Source nodes at whatever evidenced granularity is needed (for example archival act, protocol record, section);
2. `relationships.tsv` — explicit evidence-status-controlled relations between nodes, including generic `part_of` containment and source-relative loci where a bounded relation requires them;
3. `files.tsv` — exact PDFs/images/exports with filename, SHA-256, coverage, preservation state and rights status;
4. `source-data/<source_id>/` — reusable source-level folio ↔ export-image ↔ PDF-page ↔ stable-URN crosswalks;
5. `events.tsv` — shared event/activity context.

There is no hard-coded archival hierarchy in the storage model. The generic structural pattern is:

`source node --part_of--> source node`

A node's `source_type` describes what it is; it does not trigger a separate table or special resolver logic. This permits evidenced structures such as protocol → act, section → protocol, attachment → file unit, volume → series, or deeper nesting without schema changes.

`part_of` is directed from part to whole. The validator requires both endpoints to exist and rejects cycles. Multiple parent relations are allowed when the evidence genuinely requires them; the resolver reports all resulting ancestry paths rather than choosing one silently.

## Source identity and relation loci

Source IDs are identifiers of canonical Source nodes, not passage locators. If a Source→Source relationship applies to bounded loci, `subject_id` / `object_id` remain pure canonical IDs and the source-relative loci live separately in `subject_locus` / `object_locus`.

This separation is deliberately modest: it fixes Source identity ≠ locus without defining the final physical-line/span model reserved for source-exact G2 work.

## Current Knau source group

The current corpus has seven relevant Source nodes: three larger archival acts and four project-facing protocol records. The four protocols remain four distinct Sources; their containment is expressed only through `part_of` relations.

- `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — *Visitation im Amt Ziegenrück*, fol. 294r–313r — `part_of` `ACT-THHSTAW-EGA-REG-II-4-BD-II` (*Visitation in Thüringen*);
- `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — *Visitation im Amt Ziegenrück*, fol. 55v–66v — `part_of` `ACT-THHSTAW-EGA-REG-II-5` (*Registratur für die Superintendenz Neustadt an der Orla (Auszug)*);
- `THHSTAW-EGA-REG-II-3-PROT-NEUSTADT-41R-63V` — *Visitation in Neustadt an der Orla*, fol. 41r–63v — `part_of` `ACT-THHSTAW-EGA-REG-II-3`;
- `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` — *Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)*, fol. 303r–306r — `part_of` the same `ACT-THHSTAW-EGA-REG-II-3`.

The shared Reg. Ii 3 whole therefore does not collapse the two protocol records into one Source.

## Machine contract and resolver

`source-contract.json` defines the lean machine-readable invariants. Run:

`python tools/source_contract.py validate`

Resolve a Project/Source combination with:

`python tools/source_contract.py resolve --project <project> --source-id <source_id> [--locus <folio>]`

The resolver derives structural status from the Project's `project_source_id` plus `part_of`, returns all ancestry paths, Project→Source uses/research functions when represented in the target model, explicit use-evidence with canonical File records, and any Project roots that structurally contain the Source.

During the Reg. Ii 5 transition it also exposes the existing legacy Project Source row and `primary_file_id` separately. Legacy file selection is not silently converted into target use-evidence; that conversion belongs to the separately loss-checked migration.

Missing crosswalk mappings are reported rather than guessed.

## Identity and ownership

- canonical Source-node identity/type/title/extent/provenance → `sources.tsv`;
- structural and other Source→Source relationships → `relationships.tsv`;
- exact File identity/preservation/checksum/rights → `files.tsv`;
- reusable source-level folio/image/PDF/URN mapping → `source-data/<source_id>/`;
- Project→Source `research_function` and source-relative relevant locus → project `source-uses.tsv`;
- concrete Project-use→File evidence binding → project `research/use-evidence.tsv` when needed;
- project reading/analysis → project scholarly work records.

Research functions are not Source properties. A Source may serve several different research functions in the same or different Projects without changing its canonical Source node.

`source-uses.relevant_locus` and `use-evidence.evidence_locator` are not interchangeable: the former is source-relative scholarly scope; the latter is an optional locator inside the concrete digital instantiation actually used. Prefer the canonical crosswalk for reusable folio/image/PDF/URN correspondence rather than duplicating it project-locally.

## Persistent identifiers

Stable image URNs are copied only when institutionally evidenced. Never synthesize a URN from neighboring identifiers or image-number patterns. A missing URN is a documented gap, not an invitation to guess.

## Exact original exports

The exact source export used for consequential work is a first-class research asset. `files.tsv` is authoritative for byte identity and preservation state. Preferred repository path when rights/authority permit:

`corpus/source-files/<source_id>/original/<original-filename>`

The preserved original must remain byte-identical. OCR/crops/renders are derivatives and must not overwrite it. Because this repository is public, an `InC` marker is not treated as permission to redistribute archive PDFs; blocked public preservation remains explicit in `files.tsv`.
