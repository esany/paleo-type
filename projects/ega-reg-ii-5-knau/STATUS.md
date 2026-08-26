# STATUS — Knau benchmark

Last checkpoint: 2026-08-26

## Scope and canonical corpus references

This project is the first research benchmark inside the broader visitation-source corpus. Canonical source identities and inter-source relationships live in:

- `corpus/sources.tsv`
- `corpus/relationships.tsv`
- `corpus/events.tsv`
- `corpus/files.tsv`

Project files retain only project-specific inspection, crosswalk, transcription and decision detail.

### A — principal witness
Corpus source `A`: `ThHStAW, EGA, Reg. Ii 5`, record `stat_visitation_00000129`, **Visitation im Amt Ziegenrück**, `55v–66v`, 1533 context. Archival metadata states A is an extract from B.

A Knau locus is mapped:

- export image 132 = fol. 61v — Knau begins;
- image 133 = 62r;
- image 134 = 62v;
- image 135 = 63r — Knau ends at top and next entry begins.

Exact mapping: `sources/a-crosswalk.tsv`.

### B — fuller related 1533 protocol
Corpus source `B`: `ThHStAW, EGA, Reg. Ii 4 Bd. II`, **Visitation im Amt Ziegenrück**, `294r–313r`.

The corresponding Knau locus has now been directly located and visually controlled:

- image 667 = B 306v — large `Knawe` heading and same distinctive filial/administrative opening as A;
- image 668 = 307r;
- image 669 = 307v;
- image 670 = 308r;
- image 671 = 308v;
- image 672 = 309r — Knau closes and next large heading begins.

Exact image/folio/URN mapping: `sources/b-crosswalk.tsv`.

`corpus/relationships.tsv` now records `B:306v-309r textually_corresponds_to A:61v-63r` as **observed** based on direct visual comparison. This establishes a genuine corresponding passage, but **not yet verbatim copying or complete line-by-line equivalence**. Individual B readings may affect A only after local collation.

### C1 — earlier 1529 visitation
Corpus source `C1`: `ThHStAW, EGA, Reg. Ii 3`, record `stat_visitation_00000197`, **Visitation in Neustadt an der Orla**, `41r–63v`, 1529-05-23 through 1529-06-01. Uploaded 47-page export inspected. Separate source; no assumed same hand/textual dependence with A/B.

### C2 — 1529 income/accounting source
Corpus source `C2`: `ThHStAW, EGA, Reg. Ii 3`, record `stat_visitation_00000235`, **Pfarreinkommen Gössitz, Knau (mit Laskau, Bahren), Liebschütz (mit Liebengrün)**, `303r–306r`, approximate 1529 range. Uploaded 9-page export inspected. Separate accounting/income source, especially relevant for numerals, measures, money and natural dues.

## Current A transcription checkpoint

Legacy TSVs 132–135 preserve current `working`, `variant` and `unresolved` readings; they are not a validated edition.

Key anchors/limits:

- `Knawe` — working on A 61v;
- `wolff von` — visually supported;
- following surname token — exact graphematic spelling still variant/unresolved; historical Wolf-von-Gräfendorf identification remains separate;
- top quantity in `hat ij filial ...` — working `ij`;
- arabic `1` — directly visible;
- arabic `80` — directly reinspected twice on A 62r; numeral form only;
- W1–W6 on A 61v remain unresolved economic/value notation groups.

## Evidence order for A adjudication

1. A internal same-hand/source comparison;
2. local demonstrated B parallel;
3. separately labelled C2 notation comparison;
4. C1 contextual/visitational comparison where relevant;
5. reliable inspected external edition/reference if still needed.

A clearer B/C2 reading may support identification of A but may not overwrite A graphemes.

## Architecture state

Core corpus/source-criticism architecture is implemented:

- stable source IDs A/B/C1/C2;
- source inventory and explicit relationship/event registers;
- durable source-file manifest with SHA-256 for current export binaries;
- A and B image/folio crosswalks;
- minimal person/place registries;
- generic archival/digital provenance methodology;
- corpus-aware workflow, maintenance and AGENTS guardrails;
- future standards/automation/HTR/publication work captured as lean trigger-based Issues and duplicate/granular backlog pruned.

The durable source model and rationale no longer depend on this chat.

## Active research problem

The high-value unresolved block remains the numerical, monetary, grain and measure notation in A 61v and upper A 62r, especially W1–W6.

The strongest immediate gains now come from C2 notation mapping plus A-internal comparison, followed by local B collation.

## NEXT ACTION — canonical restart point

1. **Map/transcribe the C2 Knau income section (`303r–306r`) only to the depth needed for numeral/currency/measure comparison.** Keep C2 readings independent.
2. **Build an A-internal notation concordance across A 55v–67r** for W1–W6 and known numeral/grain/measure/currency anchors.
3. **Collate the locally corresponding B clauses against A** where they bear directly on W1–W6, names or unresolved wording; preserve witness-specific spellings.
4. Adjudicate W1–W6 individually in the evidence order above.
5. Update transcription, `apparatus/decisions.tsv`, `palaeography/numerals.tsv`, source audit and relationship status only where truth changes.
6. Run the continuous research-integrity gate plus a small adversarial sample.
7. Freeze a coherent A 61v–63r transcription checkpoint.
8. Then expand systematic visitation-corpus discovery from A/B/C1/C2, documenting the search boundary rather than claiming unbounded completeness.

## Stop conditions

Mark `unresolved` rather than infer when image evidence does not discriminate; support is only syntax/history; a relevant passage was not inspected; source correspondence is assumed rather than shown; catalogue metadata is being treated as textual proof; or repeated AI readings are the only corroboration.

## User-facing result target

A source-exact Knau transcription in A (`Reg. Ii 5, 61v–63r`) with visible uncertainty and compact apparatus; demonstrated, separately labelled B collation; selective C1/C2 controls with explicit evidential roles; and a growing visitation corpus in which archival provenance, textual evidence and historical interpretation remain traceable and distinct.
