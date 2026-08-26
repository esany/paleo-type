# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Scope and canonical corpus references

This project is the first research benchmark inside the broader visitation-source corpus. Canonical source identities and inter-source relationships now live at corpus level:

- `corpus/sources.tsv`
- `corpus/relationships.tsv`
- `corpus/events.tsv`

This project must not duplicate those identities except where project-specific inspection/crosswalk detail is required.

### A — principal witness
Corpus source `A`: `ThHStAW, EGA, Reg. Ii 5`, record `stat_visitation_00000129`, **Visitation im Amt Ziegenrück**, archival sequence `55v–66v`, 1533 context. Archival metadata states A is an extract from B.

The uploaded A export (`1a03ea95927-120-143.pdf`) has been inspected. Knau is mapped:

- export image 132 = fol. 61v — Knau begins;
- export image 133 = fol. 62r — folio number 62 directly visible;
- export image 134 = fol. 62v;
- export image 135 = fol. 63r — folio number 63 directly visible; Knau closes at top and next entry begins below.

Exact project mapping lives in `sources/a-crosswalk.tsv`. Keep export image, PDF page, archival folio and stable image/URN as separate fields.

### B — fuller related 1533 protocol
Corpus source `B`: `ThHStAW, EGA, Reg. Ii 4 Bd. II`, **Visitation im Amt Ziegenrück**, `294r–313r`. A/B archival metadata supports `A metadata_says_extract_of B`; exact textual correspondence is still unresolved until passage-level collation.

### C1 — earlier 1529 visitation
Corpus source `C1`: `ThHStAW, EGA, Reg. Ii 3`, record `stat_visitation_00000197`, **Visitation in Neustadt an der Orla**, `41r–63v`, exact archival date range supplied as 1529-05-23 through 1529-06-01. The uploaded 47-page export has been inspected. Separate earlier visitation source; no assumed same hand/textual dependence with A/B.

### C2 — 1529 income/accounting source
Corpus source `C2`: `ThHStAW, EGA, Reg. Ii 3`, record `stat_visitation_00000235`, **Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)**, `303r–306r`, approximate archival range 1529-01-01 through 1529-12-31. The uploaded 9-page export has been inspected. It is a separate accounting/income source and is especially relevant to numerals, measures, money and natural dues.

## Current transcription checkpoint for A

Legacy transcription TSVs 132–135 preserve current `working`, `variant` and `unresolved` readings. They are not a validated edition.

Important anchors/limits:

- `Knawe` — working reading on A 61v;
- `wolff von` — visually supported across repeated A occurrences;
- surname token after `wolff von` — exact graphematic spelling remains variant/unresolved; historical identification as Wolf von Gräfendorf remains a separate `IDENTIFICATION` claim;
- top quantity in `hat ij filial ...` — working `ij`, not externally validated;
- arabic `1` — directly visible in A economic clauses;
- arabic `80` — directly reinspected twice on A 62r; numeral form only;
- W1–W6 on A 61v remain unresolved economic/value notation groups;
- earlier semantic completions or source-status overstatements from chat are not evidence.

## Corpus-method consequence

Evidence order for difficult A readings is now explicit:

1. A internal same-hand/source comparison;
2. demonstrated B textual parallel;
3. separately labelled C2 economic/notation comparison;
4. C1 historical/visitational context where relevant;
5. reliable inspected external edition/reference if still needed.

A clearer reading in B/C2 may support identification of A but never overwrite the graphemes visible in A.

## Architecture state

The corpus/source-criticism foundation is now implemented at repository level:

- stable local source IDs A/B/C1/C2;
- corpus source inventory;
- explicit relationship register with evidence status;
- event/context registry;
- minimal normalized person/place registries;
- generic archival/digital provenance methodology;
- workflow and AGENTS guardrails updated for corpus discovery/collation;
- deferred standards/automation/HTR/publication work preserved as GitHub Issues with lean triggers.

The repository no longer depends on this chat to understand the A/B/C1/C2 source model or the methodological rationale.

## Active research problem

Return to research, not further architecture work.

The highest-value unresolved textual block remains numerical, monetary, grain and measure notation in A 61v and upper A 62r, especially W1–W6. Before resolving them, exploit the newly available source controls correctly.

## NEXT ACTION — canonical restart point

1. **Locate the B locus corresponding to A 61v–63r.** Demonstrate structural/textual correspondence before using B wording as evidence.
2. **Independently map/transcribe the Knau section in C2 (303r–306r)** only to the depth needed for numeral/currency/measure comparison; keep C2 readings separate.
3. **Build an A-internal notation concordance across inspected A 55v–67r** for W1–W6 and known anchors (`1`, `80`, grain/measure/currency terms).
4. Adjudicate W1–W6 individually using the evidence order above.
5. Persist every consequential change in transcription, `apparatus/decisions.tsv`, `palaeography/numerals.tsv`, project source audit and corpus relationship status when appropriate.
6. Run the continuous research-integrity gate plus a small adversarial sample.
7. Freeze a coherent A 61v–63r transcription checkpoint.
8. Then expand systematic visitation-corpus discovery from the current A/B/C1/C2 starting set, recording discovery boundaries rather than claiming unbounded completeness.

## Stop conditions

Mark `unresolved` rather than infer when:

- image evidence does not discriminate;
- support is only syntax/history;
- the relevant external passage was not actually inspected;
- witness correspondence is assumed rather than shown;
- an archival metadata relation is being treated as textual proof;
- repeated AI readings are the only corroboration.

## User-facing result target

A source-exact Knau transcription in A (`Reg. Ii 5, 61v–63r`) with visible uncertainty and compact apparatus; demonstrated and separately labelled B collation; selective C1/C2 controls with explicit evidential roles; and a growing corpus inventory in which archival provenance, textual evidence and historical interpretation remain traceable and distinct.
