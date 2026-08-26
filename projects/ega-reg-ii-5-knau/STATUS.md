# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Overall research goal

Produce a source-exact, critically controlled scholarly edition of the Knau passage in `ThHStAW, EGA, Reg. Ii 5, fol. 61v–63r`, with visible uncertainty, traceable editorial decisions, controlled use of the demonstrated Reg. Ii 4 parallel and the already available Reg. Ii 3 comparison material.

Milestone requirements and gates live in `MILESTONES.md`. This file records only the current project state and restart point.

## Milestone state

- **M1 — Source and transmission basis secured:** substantially reached. Canonical source identities, digital-file provenance, project crosswalks and the relevant comparison-source roles are recorded. The exact textual/transmission relationship to Reg. Ii 4 may be strengthened later by M4 collation without blocking M1.
- **M2 — Principal witness completely represented:** **ACTIVE — not reached.**
- **M3 — Internal palaeographic and notational analysis completed:** not yet the active gate; existing palaeographic work is supporting evidence and does not substitute for M2 completeness.
- **M4 — Existing comparison witnesses/controls independently assessed and collated:** not yet reached; the Reg. Ii 4 corresponding locus is located but detailed collation remains open.
- **M5 — Critically consolidated text state:** not reached.
- **M6 — Scholarly edition produced and quality-controlled:** final goal, not current work.

## Canonical source basis

Canonical corpus identity/provenance lives in `corpus/`; project-specific folio/image/export mappings live in `sources/`. Legacy sigla `A/B/C1/C2` are aliases only.

### Principal witness

`THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — ThHStAW, EGA, Reg. Ii 5, **Visitation im Amt Ziegenrück**, 1533 context.

Knau project locus:

- export image 132 = fol. 61v — Knau begins;
- export image 133 = fol. 62r;
- export image 134 = fol. 62v;
- export image 135 = fol. 63r — Knau closes at top; following entry is outside scope.

Exact mapping: `sources/reg-ii-5-00000129-crosswalk.tsv`.

### Existing comparison/control sources

- `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — related 1533 Ziegenrück record; corresponding Knau locus located at fol. `306v–309r` / export images 667–672. Structural/textual correspondence is observed; detailed line-level collation remains for M4.
- `THHSTAW-EGA-REG-II-3-STAT-VIS-00000235` — 1529 Pfarreinkommen record; relevant `Knaw Kirch Einkommen` at fol. `304r` / export image 625. It is comparison/control evidence for economic/notation questions, not a textual witness of the 1533 passage unless demonstrated.
- `THHSTAW-EGA-REG-II-3-STAT-VIS-00000197` — separate earlier 1529 visitation source; no same-hand/textual-dependence claim is assumed.

## Active milestone — M2

### M2 target

Every relevant physical text area of Reg. Ii 5, fol. 61v–63r must be represented as conservative line-level diplomatic working text. **M2 does not require every token to be solved.** `variant` and `unresolved` are valid outcomes; paragraph-level descriptions standing in for visible source text are not.

### M2 requirements already satisfied / controlled

- Project boundary 61v–63r is established sufficiently for the current text scope.
- `Knawe` heading on fol. 61v has been directly reinspected and is `observed`.
- Closing Knau lines on fol. 63r (`Soll auch ein jeder hausgenos ... / ... acht pfennig ... / pfarrrecht geben`) have been directly controlled and are `observed`.
- The transcription TSVs 132–135 provide the structured container for the principal witness.
- Known uncertain readings are not to be repaired from historical/semantic plausibility or by silently copying a comparison witness.

### Unmet M2 requirements / known gaps

These are completeness gaps, not a demand that every word be adjudicated:

1. **fol. 61v:** W1–W6 and U1–U2 still require source-level representation precise enough that unresolved signs/options are localized rather than hidden by coarse description.
2. **fol. 62r:** upper economic/natural-obligation passage, currently 133:01–11, plus U3–U5 and remaining variant lines require complete conservative line-level representation.
3. **fol. 62v:** largest continuous M2 gap. 134:01–07 and much of 134:10–23 remain collapsed/unresolved instead of complete line-level diplomatic representation.
4. Every remaining multi-line placeholder/semantic summary must be replaced by the narrowest source-based representation possible, even where individual words remain unreadable.
5. After filling these physical-text gaps, perform an M2 completeness pass from 61v through 63r to confirm that no relevant visible line/text unit is omitted.

### Important current evidence limits

- `wolff von` is visually supported across repeated occurrences; the following surname token remains graphematically variant/unresolved. Historical identification as Wolf von Gräfendorf is a separate identification claim.
- The top quantity in `hat ij filial ...` remains working/variant rather than externally validated.
- Arabic `1` is directly visible in economic clauses.
- Arabic `80` has been directly reinspected twice on fol. 62r as a numeral form only.
- W1–W6 remain unresolved economic/value notation groups.
- Existing C2 and Reg. Ii 4 material may later help discriminate readings, but they do not remove the M2 requirement to represent what is visible in the principal witness itself.

## NEXT ACTION — canonical restart point

**Advance M2 only:** re-read the principal witness in physical completeness order and replace coarse unresolved placeholders with conservative line-level source representations:

1. fol. 61v — unresolved item list / W1–W6 / U1–U2;
2. fol. 62r — upper passage 133:01–11 / U3–U5 / remaining variant lines;
3. fol. 62v — 134:01–07 and 134:10–23, then all remaining lines;
4. run a fol. 61v–63r completeness pass against the images.

Record visible signs, partial strings and alternatives even when no lexical solution is possible. Do **not** make detailed C2 notation analysis, Reg. Ii 4 collation, final W1–W6 adjudication or edition-layer production the controlling task until the M2 representation gate is satisfied. Such evidence may be consulted only when necessary to segment/represent the principal source without importing its reading.

## What comes after M2

Only after M2 passes:

- **M3:** systematically test consequential unresolved/variant loci using internal palaeographic and notational evidence, with C2 only in its explicitly limited comparison/control role where relevant.
- **M4:** independently read/collate Reg. Ii 4 Bd. II 306v–309r against Reg. Ii 5 61v–63r and record demonstrated agreements/divergences without witness contamination.
- **M5:** consolidate the critically controlled text, preserve residual uncertainty and adversarially test consequential working readings.
- **M6:** derive and quality-control the scholarly edition from that consolidated research state.

## Stop conditions

Mark `unresolved` rather than infer when image evidence does not discriminate; support is only syntax/history; a comparison passage was not actually inspected; witness correspondence is assumed rather than demonstrated; archival metadata is being treated as textual proof; or repeated AI readings are the only corroboration.

## Restartability test

A new capable agent should be able to determine from `MILESTONES.md`, this file, the transcription TSVs and the canonical corpus/source records:

- the final research goal;
- which milestone is active and why;
- which M2 requirements remain unmet;
- the exact physical loci to inspect next;
- which tempting later-stage activities must not displace M2 completeness.

If old chat is required to recover any of that state, this checkpoint is incomplete.
