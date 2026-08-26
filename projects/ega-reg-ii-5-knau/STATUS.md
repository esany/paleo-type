# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Canonical source model

### A — principal witness
`ThHStAW, EGA, Reg. Ii 5`, DigiRef/ThULB record `stat_visitation_00000129`, **Visitation im Amt Ziegenrück**, archival sequence `55v–66v` according to user-supplied archival metadata. The metadata states that A is an extract from `ThHStAW, EGA, Reg. Ii 4 Bd. II, 294r–313r`.

The complete uploaded A excerpt covering export images 120–143 has been inspected. The Knau entry is now mapped as:

- export image 132 = fol. 61v — Knau entry begins;
- export image 133 = fol. 62r — folio number 62 visible;
- export image 134 = fol. 62v;
- export image 135 = fol. 63r — folio number 63 visible; Knau closes at top and next place begins below.

Keep export image number, PDF page, archival folio and any stable image/URN identifier as separate provenance fields. Never infer folio identity from export numbering alone.

### B — related fuller 1533 protocol
`ThHStAW, EGA, Reg. Ii 4 Bd. II`, **Visitation im Amt Ziegenrück**, `294r–313r` according to user-supplied archival metadata. An archive export of the relevant Ziegenrück sequence has been inspected. A and B metadata point to each other as full protocol/extract, but exact passage dependence and correspondence must be demonstrated by line-level collation.

### C1 — earlier 1529 visitation source
`ThHStAW, EGA, Reg. Ii 3`, record `stat_visitation_00000197`, **Visitation in Neustadt an der Orla**, `41r–63v`, dated by the user-supplied archival record to 1529-05-23 through 1529-06-01. The uploaded 47-page archive export has been inspected and visibly spans folios 41–63. It is a separate earlier visitation source; do not assume same hand, wording, institutional moment or textual dependence on A/B.

### C2 — Reg. Ii 3 income/accounting source
`ThHStAW, EGA, Reg. Ii 3`, record URL supplied as `stat_visitation_00000235`. The uploaded 9-page archive export around folios 303–306 has been inspected. It visibly contains parish/church-income headings for relevant places including Knau and Laskau and dense numeral/measure notation. Exact catalog title/date and relationship to C1/A/B remain to be verified from the archival record; treat C2 as a separate source unit.

## Current transcription checkpoint for A

The TSV files for legacy working images 132–135 preserve current `working`, `variant` and `unresolved` readings. They are not a validated edition.

Important anchors/limits:

- `Knawe` — working reading on A 61v;
- `wolff von` — visually supported across repeated A occurrences;
- repeated surname-like token after `wolff von` — exact graphematic spelling remains variant/unresolved; candidates include `grevendorff`, `greuendorff`, `grefendorff`; historical identification as Gräfendorf is separate;
- top quantity in `hat ij filial ...` — current working `ij`, not externally validated;
- arabic `1` — directly visible in A economic clauses;
- arabic `80` — directly reinspected twice on A 62r and recorded only as numeral form;
- W1–W6 on A 61v remain unresolved economic/value notation groups;
- earlier semantic completions and source-status overstatements from chat are not evidence.

## Methodological consequence of the expanded corpus

The project now has four distinct evidential roles, not one blended pool:

1. **A internal same-hand/source comparison** — first choice for graphematic adjudication of A;
2. **B textual witness/control** — potentially strongest control for content if passage equivalence is demonstrated;
3. **C1 historical/visitational comparison** — earlier independent context and terminology, not automatically palaeographic evidence for A;
4. **C2 economic-notation comparison** — potentially valuable for vocabulary, accounting structures and notation classes, but not evidence that the same glyph in A has the same reading unless the visual/semantic bridge is explicitly shown.

Never use B/C wording to overwrite the diplomatic reading of A.

## Active problem

The highest-value unresolved problem remains the numerical, monetary, grain and measure notation in A 61v and the upper part of A 62r, especially W1–W6. The newly ingested A context and C2 source give substantially more comparison material, while B may provide a textual parallel once the corresponding Knau passage is located.

## NEXT ACTION — canonical restart point

1. Complete provenance records for A/B/C1/C2, including record IDs, folios, export image numbers and stable identifiers where available.
2. Locate the Knau passage in B that corresponds to A 61v–63r. Establish correspondence structurally before using B to resolve wording.
3. Independently locate/transcribe the Knau income section in C2 and catalogue its numeral/currency/measure forms as **C2 evidence**, not A readings.
4. Run an A-internal notation concordance across the inspected A 55v–67r sequence for W1–W6 and known anchors such as `1`, `80`, `viertel`, `grosch`, `pfennig`, grain and measure terms.
5. Adjudicate W1–W6 individually using this evidence order: A-internal same-hand evidence → demonstrated B parallel → separately labelled C2 comparison → reliable external reference if still needed.
6. Update `apparatus/decisions.tsv`, `palaeography/numerals.tsv` and source audit for every consequential change.
7. Run the research-integrity gate and a small adversarial sample, then freeze a coherent A 61v–63r transcription checkpoint.

## Stop conditions

Mark `unresolved` rather than infer if image evidence does not discriminate; if support comes only from syntax/history; if a supposed parallel has not actually been inspected; if textual correspondence between witnesses is assumed rather than shown; or if repeated AI readings are the only corroboration.

## User-facing result target

A usable, source-exact transcription of Knau in A (`Reg. Ii 5, 61v–63r`) with visible uncertainty and compact apparatus; a separately labelled collation with B where correspondence is demonstrated; selectively used C1/C2 controls with explicit evidential role; and historical commentary in which every substantive claim is traceable to inspected evidence or marked as inference.
