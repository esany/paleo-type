# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Source identity now established

Witness **A** is `ThHStAW, EGA, Reg. Ii 5`, archival record `stat_visitation_00000128`, titled **Visitation im Amt Leuchtenburg und in Ziegenrück**. User-supplied archival metadata identifies it as a Visitationsprotokoll with page sequence `28r–55r`, in the Ernestinisches Gesamtarchiv, Reg. Ii (Kirchen- und Schulvisitation, Bewidmung), in the 1533 Thüringen visitation context. The same metadata describes A as an **Auszug** from `ThHStAW, Reg. Ii 4 Bd. II`, specifically `249r–293v` (Amt Leuchtenburg) and `295r–300r` (Ziegenrück). Treat that relationship as an archival-metadata claim until the corresponding manuscript passages are collated.

The uploaded archive export `1a03ea161c0-2.pdf` has been inspected: its parsed first page identifies `ThHStAW, EGA, Reg. Ii 5`, and its second page visibly contains the archival cover/image. The file currently available here is only a 2-page export, **not yet the complete Reg. Ii 5 image sequence** needed for full source ingest.

## Scope currently supported

Working manuscript material consists of images 132–135 from witness A. The current working hypothesis is that the Knau entry begins on 132 and continues through the beginning of 135, where a new large heading appears. Exact mapping of these export/working image numbers to archival folios and stable image identifiers/URNs remains to be established from the complete export. Do not infer folio numbers from image numbers.

## Witness model

- **A — ThHStAW, EGA, Reg. Ii 5**: current principal witness and source of working images 132–135.
- **B — ThHStAW, EGA, Reg. Ii 4 Bd. II**: related fuller visitation protocol; archival metadata for A explicitly describes A as an extract from B. B is a potential parallel witness/control, but equivalence of individual passages must be demonstrated by collation rather than assumed.
- **C — ThHStAW, EGA, Reg. Ii 3**: additional DigiRef material mentioning Knau/Laskau/Bahren; relationship to A/B remains to be established from inspected evidence.

## What has been learned reliably enough to continue

- The source contains repeated forms around `Knawe`, `pfarrer/pfarr-`, `wolff`, `von`, land/wood terms and economic obligations.
- The same-hand internal comparison is materially more reliable than whole-word silhouette guessing.
- Numerical/economic notation must be handled as a separate palaeographic subsystem rather than as ordinary running text.
- Earlier chat readings included semantic completion and source-status overstatement; those outputs are not evidence and must not be imported wholesale.
- The first adversarial integrity check proved useful: it promoted one directly visible numeral (`80`) while **downgrading** the exact spelling of the repeated Wolf surname token. Repetition across pages establishes a repeated form, not automatically its exact graphematic reading.

## Current transcription checkpoint

The TSV files preserve current **working/variant/unresolved** readings. They are not a validated edition. The first adversarial check has been persisted in the transcription files and `apparatus/decisions.tsv`.

Important current anchors/limits:

- `Knawe` — working; still to be formally frozen from source.
- `wolff von` — visually supported across repeated occurrences.
- repeated surname-like token after `wolff von` — **variant/unresolved exact spelling**; current candidate strings include `grevendorff`, `greuendorff`, `grefendorff`. Historical identification as Gräfendorf is a separate claim.
- top quantity in `hat ij filial ...` — current working reading `ij`; exact glyph decomposition is not independently validated.
- arabic `1` — directly visible in image 132 economic clauses; surrounding notation is not resolved by that fact.
- arabic `80` — directly reinspected twice in the lower paragraph of image 133 and now `observed` as a numeral form; its unit/meaning remains unresolved.
- `Holtzmarck zu notturfft zu brennen / vnnd zu bawen`, `pfarrlehen`, household/groschen clause, 133 Wolf/descendants/hufen clause, 134 land/use clauses and 135 boundary remain working material requiring later checkpoint control.

## Active problem

Before further palaeographic adjudication, complete **source ingest and provenance mapping for witness A**. We now have authoritative record-level identity but not the complete export sequence needed to map working images 132–135 to folios/URNs and establish the exact Knau entry boundary.

After that ingest, the largest high-value textual block remains the **numerical, monetary, grain and measure notation** in the itemized section of image 132 and comparable notation in the upper part of 133. W1–W6 are real distinct economic/value tokens or groups, but current internal evidence does not safely expand them.

## FIRST INTEGRITY-CHECK RESULT

The continuous research-integrity routine was applied to consequential anchors before further reconstruction.

Passed/promoted:

- image 133 contains the same clear arabic `80` form twice; numeral form promoted to `observed` only.

Downgraded:

- exact manuscript spelling of the repeated surname token after `wolff von`; prior preference for `grevendorff` was not sufficiently independent from repeated model/context reading. It is now represented as `[surname-token]` with explicit candidates until grapheme-level adjudication.

Preserved unresolved:

- W1–W6 on image 132;
- upper economic passage of 133;
- surrounding units/syntax around the `80` occurrences.

## NEXT ACTION — canonical restart point

1. Obtain/ingest the **complete original archive export for A = Reg. Ii 5** without renaming or reordering it.
2. Build a source crosswalk separating: archive/signature, archival folio, export image number, stable object/image identifier or URN, PDF page, and legacy working IDs 132–135.
3. Locate 132–135 exactly and establish the complete Knau entry boundary in A. Do not infer mappings from sequence alone.
4. Register B (`Reg. Ii 4 Bd. II`) and C (`Reg. Ii 3`) as separate witnesses/leads; do not merge their numbering or text with A.
5. Once A is mapped, collate the corresponding Knau passage in B as a genuinely separate textual control where passage equivalence is demonstrable.
6. Return to W1–W6: record visible sign structure, use same-hand A evidence first, B only as a separately labelled parallel witness, and adjudicate each token independently.
7. Freeze a coherent A transcription checkpoint; only then proceed to broader historical identification/context.

## Stop conditions

Pause and mark `unresolved` rather than infer if:

- image/folio identity is not established;
- the image does not distinguish the graphemes/signs;
- only syntax/context supports the completion;
- a supposed parallel has not actually been inspected;
- the reading depends on a historical identification rather than letter/sign forms;
- repeated AI/model readings are the only apparent corroboration.

## User-facing result target

A usable transcription of the Knau entry in witness A with exact source provenance, visible uncertainty and a compact critical apparatus; separately labelled collation with related witnesses where demonstrable; and historical commentary in which every substantive claim can be traced to inspected evidence or is explicitly marked as inference.
