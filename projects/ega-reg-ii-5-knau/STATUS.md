# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Scope and canonical corpus references

This project is the first research benchmark inside the broader visitation-source corpus. Canonical source identities and inter-source relationships live at corpus level:

- `corpus/sources.tsv`
- `corpus/relationships.tsv`
- `corpus/events.tsv`
- `corpus/files.tsv`

Canonical source IDs are identity-derived from archive/signature/catalogue record. Ordinal sigla such as `A/B/C1/C2` are now **legacy/presentation aliases only** and must not be used as corpus keys or as the sole source reference.

### ThHStAW, EGA, Reg. Ii 5 — stat_visitation_00000129
Canonical ID: `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` (legacy siglum `A`).

**Visitation im Amt Ziegenrück**, archival sequence `55v–66v`, 1533 context. Archival metadata states this record is an extract from the Reg. Ii 4 Bd. II Ziegenrück protocol.

The uploaded export (`1a03ea95927-120-143.pdf`) has been inspected. Knau is mapped:

- export image 132 = fol. 61v — Knau begins;
- export image 133 = fol. 62r — folio number 62 directly visible;
- export image 134 = fol. 62v;
- export image 135 = fol. 63r — folio number 63 directly visible; Knau closes at top and next entry begins below.

Exact project mapping lives in `sources/reg-ii-5-00000129-crosswalk.tsv`. Keep export image, PDF page, archival folio and stable image/URN as separate fields.

### ThHStAW, EGA, Reg. Ii 4 Bd. II — stat_visitation_00000089
Canonical ID: `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` (legacy siglum `B`).

**Visitation im Amt Ziegenrück**, `294r–313r`. Archival metadata supports the extract relationship to Reg. Ii 5. The corresponding Knau locus has been located at `306v–309r` (export images 667–672). Structural/textual correspondence is observed; detailed line-level collation remains required before individual readings are transferred as evidence.

Exact mapping lives in `sources/reg-ii-4-bd-ii-00000089-crosswalk.tsv`.

### ThHStAW, EGA, Reg. Ii 3 — stat_visitation_00000197
Canonical ID: `THHSTAW-EGA-REG-II-3-STAT-VIS-00000197` (legacy siglum `C1`).

**Visitation in Neustadt an der Orla**, `41r–63v`, exact archival date range supplied as 1529-05-23 through 1529-06-01. The uploaded export has been inspected. This is a separate earlier visitation source; no same-hand/textual-dependence claim with the 1533 records is assumed.

### ThHStAW, EGA, Reg. Ii 3 — stat_visitation_00000235
Canonical ID: `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` (legacy siglum `C2`).

**Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)**, `303r–306r`, approximate archival range 1529-01-01 through 1529-12-31. The uploaded export has been inspected. It is a separate accounting/income source and is especially relevant to numerals, measures, money and natural dues.

## Current transcription checkpoint

Legacy transcription TSVs 132–135 preserve current `working`, `variant` and `unresolved` readings for `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`, fol. 61v–63r. They are not a validated edition.

Important anchors/limits:

- `Knawe` — working reading on fol. 61v;
- `wolff von` — visually supported across repeated occurrences;
- surname token after `wolff von` — exact graphematic spelling remains variant/unresolved; historical identification as Wolf von Gräfendorf remains a separate `IDENTIFICATION` claim;
- top quantity in `hat ij filial ...` — working `ij`, not externally validated;
- arabic `1` — directly visible in economic clauses;
- arabic `80` — directly reinspected twice on fol. 62r; numeral form only;
- W1–W6 on fol. 61v remain unresolved economic/value notation groups;
- earlier semantic completions or source-status overstatements from chat are not evidence.

## Evidential roles (not identities)

Research roles must be described separately from source identity:

1. `Reg. Ii 5 / stat_visitation_00000129` — principal transcription witness and first source for same-source comparison;
2. `Reg. Ii 4 Bd. II / stat_visitation_00000089` — related 1533 parallel/control where correspondence is demonstrated;
3. `Reg. Ii 3 / stat_visitation_00000235` — economic/notation comparison source;
4. `Reg. Ii 3 / stat_visitation_00000197` — earlier visitational/historical comparison source.

A source may change research role without changing identity. A clearer reading in another source may support identification but never overwrite the graphemes of the principal transcription witness.

## Architecture state

The corpus/source-criticism foundation now includes:

- identity-derived canonical source IDs;
- optional legacy sigla only as aliases;
- corpus source inventory;
- explicit relationship register with evidence status;
- event/context registry;
- exact external-file manifest with checksums;
- project-level image/folio crosswalks named for their archival source identity;
- generic archival/digital provenance methodology;
- deferred standards/automation/HTR/publication work preserved as trigger-based GitHub Issues.

The repository no longer depends on this chat to understand the source set or its methodological rationale.

## Active research problem

Return to research, not further architecture work.

The highest-value unresolved textual block remains numerical, monetary, grain and measure notation in Reg. Ii 5, fol. 61v and upper 62r, especially W1–W6.

## NEXT ACTION — canonical restart point

1. Independently map/transcribe the Knau section in `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` only to the depth needed for numeral/currency/measure comparison.
2. Build an internal notation concordance across inspected `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`, fol. 55v–67r for W1–W6 and known anchors (`1`, `80`, grain/measure/currency terms).
3. Perform detailed local collation of `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129:61v–63r` against `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089:306v–309r`, preserving each witness independently.
4. Adjudicate W1–W6 individually using the evidence order above.
5. Persist every consequential change in transcription, `apparatus/decisions.tsv`, `palaeography/numerals.tsv`, project source audit and corpus relationship status when appropriate.
6. Run the continuous research-integrity gate plus a small adversarial sample.
7. Freeze a coherent Reg. Ii 5, fol. 61v–63r transcription checkpoint.
8. Then expand systematic visitation-corpus discovery from the current source set, recording discovery boundaries rather than claiming unbounded completeness.

## Stop conditions

Mark `unresolved` rather than infer when image evidence does not discriminate; support is only syntax/history; the relevant external passage was not actually inspected; witness correspondence is assumed rather than shown; archival metadata is being treated as textual proof; or repeated AI readings are the only corroboration.

## User-facing result target

A source-exact Knau transcription in `ThHStAW, EGA, Reg. Ii 5, fol. 61v–63r` with visible uncertainty and compact apparatus; demonstrated and separately labelled collation with the Reg. Ii 4 Bd. II parallel; selective Reg. Ii 3 controls with explicit evidential roles; and a growing corpus inventory in which archival provenance, textual evidence and historical interpretation remain traceable and distinct.
