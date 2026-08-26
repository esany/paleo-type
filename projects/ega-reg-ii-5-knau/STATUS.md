# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Scope and canonical corpus references

This project is the first research benchmark inside the broader visitation-source corpus. Canonical source identities and inter-source relationships live at corpus level:

- `corpus/sources.tsv`
- `corpus/relationships.tsv`
- `corpus/events.tsv`
- `corpus/files.tsv`

Canonical source IDs are identity-derived from archive/signature/catalogue record. Ordinal sigla such as `A/B/C1/C2` are legacy/presentation aliases only and must not be used as corpus keys or as the sole source reference.

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

**Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)**, `303r–306r`, approximate archival range 1529-01-01 through 1529-12-31. The uploaded export has been inspected. Its folio/image sequence is now mapped in `sources/reg-ii-3-00000235-crosswalk.tsv`; the directly relevant heading `Knaw Kirch Einkommen` is located at fol. 304r / export image 625. C2 remains a separate accounting/notation comparison source, not a textual witness of the 1533 passage unless demonstrated.

## Current transcription checkpoint

The transcription TSVs 132–135 preserve the current diplomatic working text for `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`, fol. 61v–63r. They are not yet a validated edition.

Direct reinspection in the current work block promoted only clearly controlled material:

- `Knawe` heading on fol. 61v is now `observed`;
- the Knau closing lines on fol. 63r (`Soll auch ein jeder hausgenos ... / ... acht pfennig ... / pfarrrecht geben`) are now `observed`;
- no unresolved token was resolved from context or comparison-source plausibility.

Important remaining anchors/limits:

- `wolff von` is visually supported across repeated occurrences;
- surname token after `wolff von` remains exact-graphematically variant/unresolved; historical identification as Wolf von Gräfendorf is a separate `IDENTIFICATION` claim;
- top quantity in `hat ij filial ...` remains working/variant rather than externally validated;
- arabic `1` is directly visible in economic clauses;
- arabic `80` is directly reinspected twice on fol. 62r; numeral form only;
- W1–W6 on fol. 61v remain unresolved economic/value notation groups;
- fol. 62r upper economic/natural-obligation passage (current 133:01–11) is still not safely reconstructed;
- fol. 62v remains the largest continuous transcription gap: 134:01–07 and much of 134:10–23 are unresolved rather than line-level diplomatic text;
- earlier semantic completions or source-status overstatements from chat are not evidence.

## Edition-completeness inventory

The current bottleneck is not only W1–W6. A coherent edition requires closing all major physical-text gaps in the principal witness before normalization/commentary:

1. fol. 61v: W1–W6 and U1–U2;
2. fol. 62r: upper passage 133:01–11 plus U3–U5 and a few variant lines;
3. fol. 62v: full line-level reconstruction of the currently collapsed/unresolved paragraphs, especially 134:01–07 and 134:10–23;
4. fol. 63r: closing Knau lines are now directly controlled; the following new entry is outside the active edition boundary.

## Evidential roles (not identities)

Research roles remain separate from source identity:

1. `Reg. Ii 5 / stat_visitation_00000129` — principal transcription witness and first source for internal comparison;
2. `Reg. Ii 4 Bd. II / stat_visitation_00000089` — related 1533 parallel/control where correspondence is demonstrated;
3. `Reg. Ii 3 / stat_visitation_00000235` — already available economic/notation comparison source;
4. `Reg. Ii 3 / stat_visitation_00000197` — already available earlier visitational/historical comparison source.

A source may change research role without changing identity. A clearer reading in another source may support identification but never overwrite the graphemes of the principal transcription witness.

## Active research problem

Finish a source-exact diplomatic transcription of Reg. Ii 5, fol. 61v–63r using only the already available source material. No additional source acquisition is part of the current edition plan.

The next evidential work must reduce the actual gaps in the principal text rather than add more corpus architecture or collect new sources.

## NEXT ACTION — canonical restart point

1. Selectively transcribe the `Knaw Kirch Einkommen` subsection at `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235:304r` only far enough to inventory numeral/currency/measure forms that can test concrete W1–W6 candidates; do not treat different-hand forms as proof of A graphemes.
2. Reinspect the existing Reg. Ii 5 comparison loci across fol. 55v–67r and extend `palaeography/numerals.tsv` only with directly controlled forms relevant to W1–W6, `1`, `80`, `viertel`, `grosch`, `pfennig` or related notation.
3. Re-read the principal witness line by line in completeness order: fol. 61v unresolved item list/U1–U2 → fol. 62r upper passage/U3–U5 → fol. 62v collapsed paragraphs. Record signs/options even when a word cannot be resolved; do not leave whole paragraphs as fluent semantic placeholders where individual line structure can be recovered.
4. Perform detailed local collation of `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129:61v–63r` against `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089:306v–309r`, preserving each witness independently and recording only demonstrated correspondences/divergences.
5. Adjudicate individual unresolved readings with evidence order: principal-image graphemes → same-source/hand anchors where demonstrated → relevant C2 notation control → demonstrated Reg. Ii 4 parallel. Leave unresolved when evidence does not discriminate.
6. Freeze a coherent diplomatic transcription checkpoint of fol. 61v–63r, then derive a readable edition layer and compact apparatus without overwriting the diplomatic text.
7. Run the continuous research-integrity gate plus a small adversarial sample before treating the edition checkpoint as stable.

## Stop conditions

Mark `unresolved` rather than infer when image evidence does not discriminate; support is only syntax/history; the relevant external passage was not actually inspected; witness correspondence is assumed rather than shown; archival metadata is being treated as textual proof; or repeated AI readings are the only corroboration.

## User-facing result target

A source-exact Knau transcription in `ThHStAW, EGA, Reg. Ii 5, fol. 61v–63r` with visible uncertainty and compact apparatus; demonstrated and separately labelled use of the Reg. Ii 4 Bd. II parallel and already available Reg. Ii 3 comparison material; and a readable edition layer whose interventions remain traceable to the diplomatic text.
