# STATUS — Knau source-group investigation

Last checkpoint: 2026-08-27

## Overall research goal

Produce a source-exact, critically controlled scholarly edition and historical understanding of the Knau material using the bounded source group registered in `sources/sources.tsv`. The principal diplomatic object is `ThHStAW, EGA, Reg. Ii 5, fol. 61v–63r`; related 1533 and 1529 archival records supply the acts within which the relevant protocol/source units are located.

Generic scholarly method is defined in `../../methodology/historical-source-workflow.md`; reusable maturity requirements are in `../../methodology/research-gates.md`; diplomatic requirements are in `../../methodology/transcription-guidelines.md`.

## Archival records and protocol/source-group level

The project currently anchors four distinct archival records/acts. These archival records are **not automatically identical with the protocol/source groups used by the investigation**. Project roles concern the relevant protocol/source unit within an act; where that unit has not yet been canonically delimited, the row is only a record-level routing anchor.

- principal act/record: `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — *Visitation im Amt Ziegenrück*; relevant principal protocol/source locus fol. 61v–63r / export images 132–135;
- comparison act/record: `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — *Visitation im Amt Ziegenrück*; corresponding protocol/source locus fol. 306v–309r / export images 667–672;
- control act/record: `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` — *Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)*, fol. 303r–306r, including `Knaw Kirch Einkommen` on fol. 304r / export image 625;
- context act/record: `THHSTAW-EGA-REG-II-3-STAT-VIS-00000197` — *Visitation in Jena, Neustadt an der Orla, Pößneck, Saalfeld*, fol. 41r–63v. This title identifies the **Akte / archival record**, not the project’s protocol/source-group. The relevant protocol/source unit inside the act is not yet canonically delimited and must not be invented from the act title.

The two Reg. Ii 3 records share the same archival volume/signature but are separate catalogued/identified acts/records with different record IDs, titles and evidential roles. They must not be collapsed into a generic `Reg. Ii 3` source. Conversely, a record title must not be promoted to protocol/source-group identity merely because the project uses material from that act.

Canonical archival record identities remain in `../../corpus/sources.tsv`; exact file identities/checksums remain in `../../corpus/files.tsv`; historical/source relationships remain in `../../corpus/relationships.tsv`.

## Original-export preservation state

The exact four central archive-export PDFs used for this project are checksum-verified locally against `corpus/files.tsv`:

- `1a03ea95927-120-143.pdf` — SHA-256 `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f`;
- `1a03e6fca87-642-681.pdf` — SHA-256 `dc61e65822a34b84c9d88e57690609bbea6eb4537a9efc00294d1520f8f3b86f`;
- `1529-Visitationsprotkolle-ThHStAW-EGA-Reg. Ii 3-Neustadt-O-p41r-63v.pdf` — SHA-256 `451bb32b0bca077c4089966594e2bf234b39e87d9e087d3c1c2e2a569f31fd12`;
- `1529-Visitationsprotkolle-ThHStAW-EGA-Reg. Ii 3-303-306.pdf` — SHA-256 `963a29eff5cc98bb35cecc28e20c6ed3fcb835261e322f991e42b60662d54c06`.

These PDFs are central preservation assets, not replaceable by URNs. The repository is public and the current archive exports are recorded as `InC/1.0`; therefore committing the binary bytes publicly is not treated as authorized by default. Until rights/authority for public redistribution is confirmed, repository preservation is **not complete**. The intended repository paths and this blocked state are recorded in `corpus/files.tsv` rather than falsely claiming the files are safely backed up in Git.

Legacy single-image Reg. Ii 5 PDF exports remain separately checksum-tracked for provenance.

## Generic gate state

- **G1 — Source and transmission basis secured:** substantially reached, but repository-local preservation of the central original exports remains a source-preservation gap pending rights resolution.
- **G2 — Principal witness completely and diplomatically represented:** **ACTIVE — not reached.**
- **G3 — Internal palaeographic and notational analysis completed:** not reached.
- **G4 — Comparison witnesses/controls independently assessed and collated:** not reached.
- **G5 — Critically consolidated and proportionally validated text state:** not reached.
- **G6 — Scholarly edition produced and quality-controlled:** final goal, not reached.

## Existing text checkpoint

The existing `transcription/132.tsv`–`135.tsv` files are legacy working transcription data, not yet the final G2-compliant representation. Controlled anchors include `Knawe` on fol. 61v, closing Knau lines on fol. 63r, repeated `wolff von`, Arabic `1`, and twice-reinspected Arabic `80` on fol. 62r. Known representation gaps remain especially W1–W6/U1–U2 on 61v, the upper economic passage/U3–U5 on 62r, and substantial multi-line gaps on 62v.

## Active G2 project gaps

1. direct folio-by-folio inspection of physical lineation and reading order on 61v–63r;
2. source-specific layout/material description sufficient to preserve list/accounting/spatial meaning;
3. verified mapping from legacy `132–135` working rows to archival folio/physical-line addresses where possible;
4. explicit classification of source phenomena actually present;
5. minimal compliant migration/extension without discarding prior readings/decisions;
6. derived human-readable diplomatic witness view;
7. full representation-completeness check across fol. 61v–63r.

G2 does **not** require every difficult token to be resolved.

## NEXT ACTION — canonical restart point

Using the principal Reg. Ii 5 archival record, its canonical source-data crosswalk and the exact checksum-identified archive export:
1. inspect fol. 61v–63r for physical lineation, reading order, layout, headings/marginalia, corrections, damage/illegibility, abbreviations and any evidenced hand shifts;
2. assign editor line references only from direct physical inspection;
3. map legacy rows to verified folio/physical-line loci while retaining export IDs as provenance;
4. choose the smallest structured representation required by the generic transcription guideline;
5. migrate/extend the principal-witness transcription;
6. produce the derived human-readable diplomatic witness view;
7. run the generic G2 gate.

Do not let comparison-source work displace this active G2 task.

## Human-in-the-loop state

The user must be able to inspect the current diplomatic text and source group without understanding internal TSV architecture. No independent qualified palaeographic expert review of the full Knau transcription has yet been recorded.

## Restartability test

A new capable researcher/agent must be able to determine from repository + preserved/controlled sources: the investigation object, distinct archival acts/records, the protocol/source-group level within those acts, exact exports/preservation state, active gate, remaining G2 gaps, current text evidence and next action without old chat. Where a protocol/source unit has not yet been delimited, that absence must be explicit rather than silently replaced by the act title.
