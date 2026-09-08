# STATUS — ThHStAW, EGA, Reg. Ii 5

Last checkpoint: 2026-09-08

## Project authority and identity

The human owner confirmed on 2026-09-02 that **Reg. Ii 5 continues as an act-oriented Project**, anchored at `ACT-THHSTAW-EGA-REG-II-5`. The directory/id `ega-reg-ii-5-knau` is a legacy path from an earlier AI-organized Knau benchmark; `Knau` is not the Project boundary.

On 2026-09-07 the human owner selected a new bounded scholarly target: **source-exact editorial development of the Reg. Ii 5 Ziegenrück witness at fol. 61v–63r**, tracked in #115. This is an Editionsbaustein, not a completed scientific edition and not authority for an abstract transcription/person-role/date ontology.

## Canonical Source structure

Keep archival container, concrete Source record and research use distinct.

- `ACT-THHSTAW-EGA-REG-II-5` — archival act / documentary Project anchor: **ThHStAW, EGA, Reg. Ii 5**.
- `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — concrete internal Source record: **Visitation im Amt Ziegenrück**, fol. 55v–66v, described in archival metadata as an extract related to the Reg. Ii 4 Bd. II Ziegenrück transmission.
- `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — separate Source record in the separate archival act **Reg. Ii 4 Bd. II**, fol. 294r–313r; its Knau passage is fol. 306v–309r / export images 667–672.
- The two Reg. Ii 3 records remain separate Sources inside the Reg. Ii 3 archival act and are not witnesses of the Ziegenrück text merely because they were historically used for context/control.

The Reg. Ii 4 and Reg. Ii 5 Ziegenrück records are separate material witnesses/transmissions. Close textual correspondence does not collapse their identities, dates, hands, production stages or diplomatic readings.

## Current active Source use and exact evidence

The current principal Project-relative Source use is:

- use `USE-REGII5-00000129-PRINCIPAL`;
- Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`;
- relevant locus fol. 61v–63r;
- status `active` for #115.

The exact active File binding is:

- evidence `EVID-REGII5-00000129-PRINCIPAL`;
- File `FILE-REG-II-5-00000129-EXCERPT`;
- export images 132–135;
- SHA-256 `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f` in canonical `corpus/files.tsv`.

The previous Knau-era principal use and File relation remain recoverable through Git/migration history. Reactivation does not retroactively validate any legacy diplomatic line.

**Evidence identity is not automatically current target-context readiness.** WP-0 was executed on 2026-09-08 against current repository state: Source/File/SHA/crosswalk identity passed and the artifact-ownership preflight passed. Later in the same research session the exact uploaded Reg. Ii 5 PDF was staged; its SHA-256 matched `FILE-REG-II-5-00000129-EXCERPT`, and PDF page 14 / export image 132 was rendered and visually inspected. For that exact evidence object/current execution context, `STAGED = PASS`, `VISION-INSPECTABLE = PASS`, therefore `VISUAL EVIDENCE READY = PASS` under `methodology/workflow.md`. Fol. 61v = image 132 = PDF page 14 was re-confirmed against the canonical crosswalk.

The first current witness-specific Reg. Ii 5 diplomatic partition was then persisted at `transcription/first-reading/61v.tsv` in commit `e26eaf5fec37b2cc927c033c356a1f514a7c0dc2`. The independent target-pixel pass preceded any consultation of legacy `transcription/132.tsv`; that legacy file was used only afterwards for recovery/verification. Reg. Ii 4 wording was not used as reading authority.

## Legacy diplomatic material — verification/recovery only

The historical diplomatic and witness-dependent Knau material under this legacy Project path — especially `transcription/132.tsv` through `135.tsv`, `apparatus/decisions.tsv`, the legacy palaeography tables and any claims that depend on their old page/path attribution — is preserved because it documents earlier work and remains useful for checking readings, failure modes and migration loss.

**It is not canonical current Reg. Ii 5 diplomatic transcription state.**

Owner clarification and direct comparison of the separately supplied Reg. Ii 4 Bd. II and Reg. Ii 5 Ziegenrück PDFs on 2026-09-02 showed that the earlier working diplomatic corpus cannot safely be assigned wholesale to one witness from its legacy path/page labels alone. The two transmissions are closely parallel, and historical work phases may have imported or compared readings across them. Until witness provenance is re-established for a concrete reading, the old diplomatic material has status **legacy verification/recovery evidence; witness attribution unresolved or potentially mixed**.

Consequences:

- preserve every old reading, uncertainty, apparatus decision and palaeographic observation;
- do not delete or silently normalize the old material;
- do not cite `transcription/132.tsv`–`135.tsv` as proof of a Reg. Ii 5 reading without fresh witness-specific inspection;
- do not move a legacy reading into Reg. Ii 4 merely because it matches that witness; attribution requires explicit Source/File/locus verification;
- new diplomatic work starts from the explicitly identified Reg. Ii 5 Source, exact File and locus;
- comparison between Reg. Ii 4 and Reg. Ii 5 is witness-to-witness collation, not reuse of a shared transcription.

## Later exact-source G2 research artifacts — bounded direct authority

The legacy directory later accumulated four `research/g2-*` artifacts with evidential roles that are **not** inherited from the unresolved witness provenance of the older diplomatic corpus. The historical `g2-*` filename/phase label does **not** itself mean that the current Reg. Ii 5 Project has reached generic G2. Their authority follows their own Source/File/locus chain and is classified explicitly in `research/legacy-witness-provenance.tsv`:

- `research/g2-baseline-provenance.md` — exact Reg. Ii 5 Source/File/SHA/crosswalk/render and research-access provenance;
- `research/g2-checkpoint-a-physical-inventory.md` — direct Reg. Ii 5 visual observations of physical/source order, layout and bounded source phenomena on fol. 61v–63r;
- `research/g2-checkpoint-b-semantic-loss.md` — source-bound mapping and semantic-loss/adequacy analysis against the accepted Reg. Ii 5 physical anchors and the legacy research records;
- `research/g2-domain-review-checkpoint-b.md` — consequence/requirements classification derived from that source-bound fixture.

These artifacts retain scientific authority **only at the level they actually claim**. Direct Reg. Ii 5 physical observations such as source order and recorded cancellations are not downgraded merely because the files live in the legacy directory. Conversely, none validates `transcription/132.tsv`–`135.tsv` row-by-row, resolves old witness attribution, establishes same hand, or promotes an old diplomatic reading into current Reg. Ii 5 truth.

The 2026-09-07 A-R reconciliation removed the former blanket `research/g2-*` quarantine and replaced it with explicit artifact-level classifications. This was a provenance-boundary correction only; no manuscript reading, source relationship or unresolved scholarly question was re-adjudicated.

## Exact-source structural starting fixture for #115

Checkpoint A directly validated 81 provisional physical/source-order anchors against the exact Reg. Ii 5 baselines:

- 61v: `L01–L20`;
- 62r: `L01–L25`;
- 62v: `L01–L25`;
- 63r: `L01–L11`.

These anchors may be reused as bounded structural evidence, subject to correction if fresh direct inspection finds a structural error. They are not current diplomatic text.

Established direct source phenomena at this level include:

- list/accounting structure on 61v;
- recurrent visible abbreviation marks;
- cancellation at `61v-L16`;
- cancellation at `62r-L18`;
- Arabic `80` at `62r-L19` and `62v-L01`;
- no hand differentiation was established: it remained `not investigated`.

Checkpoint B and its Domain Review demonstrate that the legacy representation collapses physical lineation in places, omits explicit cancellation phenomena, uses some coarse/ad-hoc targets and lacks legacy coverage for visible `63r-L05–L11`. Those findings are loss/research fixtures; they do not preselect a universal replacement schema.

### Current 61v diplomatic partition

`transcription/first-reading/61v.tsv` is now the current canonical first-reading partition for physical lines `61v-L01–L20`. It preserves observed/working/unresolved states, list/accounting layout, unresolved quantity/sign notation, visible abbreviation marks, the cancellation at `61v-L16`, alternatives and illegible/unclear spans without forcing semantic completion.

This first partition is **not** a G2 PASS for the whole target. It represents 20 of the 81 established physical anchors; fol. 62r–63r still lack current first-reading partitions. No hand differentiation has been established. The observed 61v findings fit the authorized lean row representation without material semantic loss, so no Package-B/D-016 representation change is triggered.

The #95 post-write duplicate-owner falsification check passed: no range-named canonical transcription file, no README/state duplicate, no overwrite/promotion of legacy 132–135, and no row-wise duplication of stable Source/File/SHA/crosswalk truth was introduced.

## Project-local editorial execution discipline for #115

The next work follows existing generic method (`historical-source-workflow.md`, `transcription-guidelines.md`, `research-gates.md`) through a **project-specific source-exact editorial vertical slice**. This is not claimed as a standardized four-stage external model.

### 1. Diplomatic source observation / reading

Record the material/source-exact state actually supported by the pixels: physical order, written signs, abbreviations, cancellations/additions/overwriting, relevant layout, damage/unreadability and observable changes in script features.

An observable script-feature change or possible hand change does **not** by itself create a discrete hand identity. A `HAND-X` hypothesis requires separate palaeographic analysis; identification of a hand with a historical person is a still further claim.

### 2. Text-near editorial development

Where present, keep manuscript name/place forms, titles/offices/functions, date formulations, addressing, explicit relationships/statements and textual structure locus-bound. The manuscript form is an editorial finding and must not be replaced by a normalized identity.

### 3. Identification, contextual role, dating and text-critical claims

Each requires its own evidence and status. In particular:

- diplomatic reading confidence does not determine identification confidence;
- identification does not determine contextual role;
- contextual/event association does not determine scribe/hand;
- a date is always a claim about a specified target/context (archival unit, event, textual date, production/excerpt stage, etc.);
- similar/corresponding text does not transfer a date from one witness/context to another;
- textual correspondence/variant/omission/condensation/resegmentation across witnesses is permitted only after the relevant witnesses have been independently established and loci controlled.

### 4. Historical interpretation stays downstream

Visitational organization, administrative process, social/economic interpretation and causal production/redaction history are not silently presented as direct manuscript observations. They may be developed later from the established editoric/source-critical evidence.

## Witness independence and admissible comparison

**Reg. Ii 5 is not folio-isolated.** Exact, source-bound same-witness comparanda elsewhere in Reg. Ii 5 may be used for graphematic/palaeographic testing after the target problem is observed. Same Source/record still does not prove same hand.

**Reg. Ii 4 wording is excluded as reading authority during the independent Reg. Ii 5 basis.** The already completed Reg. Ii 4↔Reg. Ii 5 controlled-collation work remains valid historical research evidence but may not pre-supply the new Reg. Ii 5 wording or be treated as a current G4 gate for this Project.

After the independent Reg. Ii 5 basis is sufficiently established, a controlled external comparison may open. Any externally prompted Reg. Ii 5 correction still requires direct Reg. Ii 5 reinspection and target-graph evidence.

## Source-driven Semantic-Loss / Package-B rule

Person/role/date and related Package-B work is **not a standalone architecture programme**.

Use this loop:

```text
source inspection
→ source finding / reading
→ text-near editorial development where relevant
→ identification / role / date claim only with its own evidence
→ test whether the existing representation preserves the actual finding losslessly
→ if yes: continue source work
→ if no: define the smallest missing information requirement
→ if material: route only that bounded semantic change through D-016 / loss-checked implementation
→ return immediately to the source
```

The currently demonstrated flat `corpus/sources.tsv:persons` / role-note problem is real, but it is not repaired by merely adding/removing names from a flat list. Any role/person/date structural change must be driven by the concrete editoric claims that need preservation, while keeping person identity, text mention, contextual role and hand/scribe hypothesis distinct.

No universal agent/role/date/hand/locus ontology is authorized by #115.

## Historical work-state audit

The earliest repository Project metadata (`251ce9ed39e04bb852e0232dbcce21c68bd4c3a7`) created `ega-reg-ii-5-knau` and the Knau scope as an AI-organized benchmark. Checkpoint `08c08bd6f90635210fbeff3f2d19cd0a485cc0b9` froze useful working readings and uncertainties, but it does not establish their witness provenance or owner authority for Project identity.

Snapshot `699fa6eada61db483dfca950193412715d9603a5` preserves the later source-unit state. Git history remains an audit/recovery source, not current scientific authority.

The former compatibility register `sources/sources.tsv` was loss-checked and removed. Its historical research functions remain in `source-uses.tsv`; the Reg. Ii 5 fol. 61v–63r principal function is now explicitly reactivated for #115 while the other preserved comparison/control/context uses remain historical. Exact File bindings remain in `research/use-evidence.tsv` with the same current/historical distinction.

## Digital addressing / provenance

For the canonical Reg. Ii 5 Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`:

- canonical File identity/provenance is owned by `corpus/files.tsv`;
- canonical Source crosswalk is owned by `corpus/source-data/THHSTAW-EGA-REG-II-5-STAT-VIS-00000129/crosswalk.tsv`;
- Source boundary is fol. 55v–66v;
- the PDF/export may contain adjacent context beyond that Source boundary;
- identifiability/reproducibility do not by themselves establish that evidence is staged and inspectable in a fresh target context.

For the separate Reg. Ii 4 Bd. II Ziegenrück Source, its own File, crosswalk, page-specific URNs and fol. 306v–309r / images 667–672 remain canonical under that Source. Never substitute one witness's image numbering, TIFF labels, folios, dates or readings for the other.

## Current research state / edition lifecycle

A current canonical witness-specific first-reading partition now exists for **fol. 61v only**. Fol. 62r–63r do not yet have current canonical first-reading partitions. The gate-evaluated active target remains **Reg. Ii 5 fol. 61v–63r only**. No gate claim for this target applies automatically to the whole Ziegenrück Source fol. 55v–66v or the whole Reg. Ii 5 act.

| Gate / activity | State | Evaluated scope | Meaning / residual limit |
|---|---|---|---|
| G1 source/transmission basis | `reached` | active #115 Knau source group/locus | Principal Reg. Ii 5 Source/File/SHA/crosswalk and separate relevant comparison/context Sources are identified with explicit evidence/provenance limits. |
| #115 source-exact editorial work package | `active` | Reg. Ii 5 fol. 61v–63r | Current research task. Its eventual Issue completion will not automatically establish every gate it touches. |
| G2 diplomatic representation | `active / not reached` | Reg. Ii 5 fol. 61v–63r | 81 physical anchors exist; current first-reading data now represents 61v-L01–L20 (20/81 anchors), while 62r–63r remain unrepresented in the current witness-specific partition set and unresolved readings remain valid research state. |
| G3 internal analysis | `not reached` | same locus | Historical G2-labelled observations are not a systematic current witness-specific G3 analysis; difficult readings must first be established from Reg. Ii 5 itself and then internally tested. |
| G4 controlled comparison | `not reached` | Reg. Ii 5 ↔ Reg. Ii 4 Knau loci | Reg. Ii 4 wording remains closed until the independent Reg. Ii 5 basis is established; historical #99 comparison evidence is not a substitute for this Project's current G4 progression. |
| G5 critical consolidation/validation | `not reached` | bounded Knau edition target | No consolidated/validated current Reg. Ii 5 text state exists. |
| G6 scholarly edition | `not reached` | bounded Knau edition target | No scholarly edition has been produced. #115 is an Editionsbaustein. |

The old diplomatic transcription/apparatus/palaeography remains a verification/recovery fixture with unresolved or potentially mixed witness attribution. Separately, the explicitly classified `research/g2-*` artifacts remain usable according to their own bounded evidence roles, including direct Reg. Ii 5 physical/source-order observations where actually revalidated.

Any new diplomatic result must be established against the explicitly targeted Source/File/locus. Existing direct physical observation must not be mistaken for diplomatic reading, source-bound semantic-loss/domain analysis must not be mistaken for manuscript text, and completion of a work package must not be mistaken for a higher gate or finished edition.

## NEXT ACTION — canonical restart point

**WP-0 and the first 61v first-reading persistence/post-write ownership check are complete. The next bounded source action is fol. 62r / image 133 / PDF page 15.**

1. In any fresh execution context, stage/supply the exact canonical Reg. Ii 5 export and establish `STAGED` + `VISION-INSPECTABLE` for PDF page 15 / image 133 before pixel-dependent work. Prior-context readiness is not inherited.
2. Verify the staged evidence against Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`, File `FILE-REG-II-5-00000129-EXCERPT`, the canonical SHA/crosswalk and fol. 62r = image 133 = PDF page 15.
3. Independently read `62r-L01–L25` from Reg. Ii 5 itself, preserving uncertainty and source phenomena. In particular preserve the cancellation at `62r-L18` and Arabic `80` at `62r-L19` as source phenomena rather than silently normalizing them.
4. Persist the current folio-local first-reading partition as `transcription/first-reading/62r.tsv`; do not overwrite or silently promote legacy `transcription/133.tsv`.
5. Legacy material may be consulted only after the independent target-pixel pass for recovery/verification. Reg. Ii 4 wording remains closed as reading authority.
6. Add text-near names/titles/functions/date expressions only where actually present and keep identification, contextual role, hand hypothesis and dating claims separate with their own evidence/status.
7. If a real editoric finding cannot be represented without semantic loss, stop only that affected persistence step, define the smallest missing information requirement and route a bounded change; otherwise continue source work without new schema/infrastructure.

Issue #115 owns the work checklist. This STATUS owns the current scholarly/restart state and any formal G1–G6 gate claim.

## Restartability

A fresh capable context must be able to reconstruct without old chat that:

- Reg. Ii 5 is an archival-act Project anchor and #115 is the current bounded source-research task;
- the active target is the separate Reg. Ii 5 Ziegenrück Source at fol. 61v–63r / images 132–135;
- exact File/SHA/crosswalk identity is established;
- the exact PDF identity was re-established in the 2026-09-08 source session and fol. 61v/image 132/page 14 was `STAGED` + `VISION-INSPECTABLE` before reading;
- `transcription/first-reading/61v.tsv` is the current canonical 61v partition; legacy `transcription/132.tsv`–`135.tsv`, apparatus and witness-dependent legacy palaeography remain verification/recovery evidence, not current Reg. Ii 5 transcription truth;
- the first actual `61v.tsv` post-write duplicate-owner check for #95 passed: no range file, no README/state duplicate, no legacy overwrite/promotion, no stable Source/File/SHA/crosswalk duplication, and no material semantic-loss trigger;
- a fresh context must re-establish `STAGED` + `VISION-INSPECTABLE` for the exact next evidence page before new reading; prior-context readiness does not carry forward automatically;
- the exact-source `g2-*` artifacts retain only their stated provenance/physical-observation/loss-analysis authority and do not constitute a current G2 PASS;
- 81 working physical anchors exist for 61v–63r; 20/81 now have a current 61v first-reading partition, while the remaining anchors are still structural evidence rather than current diplomatic text;
- Reg. Ii 4 Bd. II and Reg. Ii 5 contain separate Ziegenrück witnesses and must remain independently read;
- same-witness Reg. Ii 5 internal comparanda are admissible; Reg. Ii 4 wording remains excluded until independent witness basis/release;
- reading, identification, contextual role, hand hypothesis and dating claims retain separate evidence/status and do not inherit certainty from one another;
- Package B is triggered only by demonstrated editoric semantic loss and must return immediately to source work after the smallest adequate repair;
- the current lifecycle is **G1 reached / G2 active-not reached / G3–G6 not reached** for fol. 61v–63r, with #115 as the active work package rather than a gate claim;
- the immediate cursor is **stage/verify exact fol. 62r = image 133 = PDF page 15 → independently read 62r-L01–L25 → persist `first-reading/62r.tsv`**, not WP-0 repetition or an abstract schema/migration programme.
