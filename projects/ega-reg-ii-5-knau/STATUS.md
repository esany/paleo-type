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

**Evidence identity is not automatically current target-context readiness.** WP-0 was executed on 2026-09-08 against current repository state: Source/File/SHA/crosswalk identity passed and the artifact-ownership preflight passed. In the current research session the exact uploaded Reg. Ii 5 PDF was staged and its SHA-256 matched `FILE-REG-II-5-00000129-EXCERPT`. The target pages were rendered and visually inspected as source-identical evidence before their respective pixel-dependent readings: fol. 61v = image 132 = PDF page 14, fol. 62r = image 133 = page 15, fol. 62v = image 134 = page 16, and fol. 63r = image 135 = page 17. For each worked target page in that execution context, `STAGED = PASS` and `VISION-INSPECTABLE = PASS`, therefore `VISUAL EVIDENCE READY = PASS` under `methodology/workflow.md`.

Current folio-local first-reading partitions were persisted directly to their canonical owners after independent target-pixel passes:

- `transcription/first-reading/61v.tsv` — commit `e26eaf5fec37b2cc927c033c356a1f514a7c0dc2`;
- `transcription/first-reading/62r.tsv` — commit `e79d679553d3039c582dc99eabdea368d31a193b`;
- `transcription/first-reading/62v.tsv` — commit `7c28026426433df90b67c2420bb7f03c990f9a63`;
- `transcription/first-reading/63r.tsv` — commit `ebb909042813c5886b184522721e6c30e41b73cf`.

For each folio, legacy `transcription/132.tsv`–`135.tsv` was consulted only after the independent Reg. Ii 5 target-pixel pass and only as recovery/verification material. Reg. Ii 4 wording was not used as reading authority.

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

These anchors may be reused as bounded structural evidence, subject to correction if fresh direct inspection finds a structural error. They are not current diplomatic text by themselves.

Established direct source phenomena at this level include:

- list/accounting structure on 61v;
- recurrent visible abbreviation marks;
- cancellation at `61v-L16`;
- cancellation at `62r-L18`;
- Arabic `80` at `62r-L19` and `62v-L01`;
- no hand differentiation was established: it remained `not investigated`.

Checkpoint B and its Domain Review demonstrate that the legacy representation collapses physical lineation in places, omits explicit cancellation phenomena, uses some coarse/ad-hoc targets and lacks legacy coverage for visible `63r-L05–L11`. Those findings are loss/research fixtures; they do not preselect a universal replacement schema.

### Current diplomatic first-reading partitions and whole-locus G2 review

The four folio-local canonical first-reading partitions now represent **all 81 established physical anchors** in Reg. Ii 5 fol. 61v–63r: 20 lines on 61v, 25 on 62r, 25 on 62v and 11 on 63r. The whole-locus review found no missing, doubled or reordered relevant source unit relative to the exact-source structural fixture. Explicitly unresolved readings remain valid representation rather than being completed from grammar, domain expectation or legacy wording.

The current partitions preserve the consequential visible source phenomena required by the target: the 61v list/accounting region and its unresolved quantity/sign notation; cancellation at `61v-L16`; cancellation at `62r-L18`; written Arabic `80` at `62r-L19` and `62v-L01`; the 63r display heading at `L04` separately from its unresolved reading; and current representation of the previously legacy-uncovered visible `63r-L05–L11`. The 63r lower-page show-through is not promoted into a target text stream because no target-text obstruction is established. Hand differentiation remains `not investigated`.

A direct target-graph recheck on 62r also rejected one fluent legacy carry-over: the opening of `62r-L24` is represented as `So`, not as a second Arabic `80`. This is a witness-specific re-adjudication from the Reg. Ii 5 pixels, not a semantic normalization. On 63r, `agustini`, `pfingsten` and `xlvij Jhars` are retained as written date expressions/sign sequence; no calendar date or absolute year is inferred in the diplomatic layer.

The current lean TSV representation carries reading order, line reference, region, source phenomena, research status, alternatives, abbreviation layer, editorial supply and evidence notes without material loss for the findings encountered. The whole-locus semantic-loss check therefore remains **PASS: no Package-B/D-016 representation change is triggered**.

A human-readable whole-locus witness view is now present at `transcription/derived/61v-63r-first-reading.md`. It is explicitly derived/rebuildable from the four folio TSVs by fixed folio order plus `reading_order`; it is not a second canonical text owner and must not be edited to change readings or status.

The #95 preflight/post-write regression fixture passed and Issue #95 is closed as `completed`: no range-named canonical transcription file, no README/state duplicate, no overwrite/promotion of legacy 132–135, and no row-wise duplication of stable Source/File/SHA/crosswalk truth was introduced.

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

After the independent Reg. Ii 5 basis is sufficiently established and the current G3 internal review has been documented, a controlled external comparison may open. Any externally prompted Reg. Ii 5 correction still requires direct Reg. Ii 5 reinspection and target-graph evidence.

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

A current canonical witness-specific first-reading representation now covers **all 81 physical anchors of Reg. Ii 5 fol. 61v–63r** in four folio-local partitions. The gate-evaluated scope is this bounded locus only. No gate claim here applies automatically to the whole Ziegenrück Source fol. 55v–66v or the whole Reg. Ii 5 act.

| Gate / activity | State | Evaluated scope | Meaning / residual limit |
|---|---|---|---|
| G1 source/transmission basis | `reached` | active #115 Knau source group/locus | Principal Reg. Ii 5 Source/File/SHA/crosswalk and separate relevant comparison/context Sources are identified with explicit evidence/provenance limits. |
| #115 source-exact editorial work package | `active` | Reg. Ii 5 fol. 61v–63r | WP-0 through WP-4 and the G2-quality whole-locus representation review are complete; later internal/comparison/consolidation work remains. Issue completion is not implied. |
| G2 diplomatic representation | `reached` | Reg. Ii 5 fol. 61v–63r | All 81 relevant physical anchors are represented in source order with folio/line address, layout region, uncertainty/illegibility, source phenomena, cancellation/numeral handling, abbreviation/supply separation and research status. A derived readable witness view exists. Unresolved readings remain permitted residual uncertainty. |
| G3 internal analysis | `active / not reached` | same locus | Some same-witness tests already exist (recurrent surname-like graph sequence; genuine `80` versus `So`; bounded notation checks), but consequential unresolved loci have not yet been systematically inventoried and tested by evidence class. |
| G4 controlled comparison | `not reached` | Reg. Ii 5 ↔ Reg. Ii 4 Knau loci | Reg. Ii 4 wording remains closed until the independent Reg. Ii 5 internal basis has been systematically reviewed and controlled-comparison release is documented. Historical #99 evidence is not a substitute for current G4 progression. |
| G5 critical consolidation/validation | `not reached` | bounded Knau edition target | No critically consolidated/validated current Reg. Ii 5 text state exists. |
| G6 scholarly edition | `not reached` | bounded Knau edition target | No scholarly edition has been produced. #115 remains an Editionsbaustein. |

The old diplomatic transcription/apparatus/palaeography remains a verification/recovery fixture with unresolved or potentially mixed witness attribution. Separately, the explicitly classified `research/g2-*` artifacts remain usable according to their own bounded evidence roles. G2 is reached now because the current witness-specific four-folio representation and whole-locus review satisfy the current gate requirements for the stated locus, not because historical files were labelled `g2-*`.

Any new diplomatic result or correction must remain established against the explicitly targeted Source/File/locus. Completion of G2 does not imply G3 analysis, G4 collation, a G5 consolidated text or a finished edition.

## NEXT ACTION — canonical restart point

**WP-0–WP-4 and the WP-5 G2-quality whole-locus representation review are complete. G2 is reached for Reg. Ii 5 fol. 61v–63r. The next bounded source-research action is the systematic G3 internal palaeographic/notational review of consequential unresolved loci.**

1. In any fresh execution context, re-establish `STAGED` + `VISION-INSPECTABLE` for the exact Reg. Ii 5 page(s) before pixel-dependent reinspection; prior-context readiness is not inherited.
2. Inventory consequential unresolved/variant loci from the four current `transcription/first-reading/*.tsv` partitions by evidence class rather than attempting to solve every marked uncertainty indiscriminately.
3. Localize grapheme/sign sequences before lexical completion. Use exact Reg. Ii 5 same-witness comparanda only where evidentially relevant; same Source/record still does not prove same hand.
4. Test the recurrent surname-like graph sequence across its current Reg. Ii 5 loci without forcing an exact spelling or historical identity if the graphs do not discriminate.
5. Test consequential numeral/measure/accounting signs, including the 61v list notation and the established contrast between genuine Arabic `80` (`62r-L19`, `62v-L01`) and `So` at `62r-L24`; keep written sign, expansion and interpretation separate.
6. Test the unresolved 63r heading and date/sign sequence only against admissible internal evidence. Preserve `agustini`, `pfingsten`, `xlvij` and any unresolved heading form as manuscript-level evidence unless a stronger reading is graphically demonstrated; do not infer calendar dates, year, role or document stage from wording alone.
7. Persist any justified reading/status/evidence changes directly in the affected folio TSV rows with traceable evidence notes. Do not create a parallel uncertainty/transcription truth merely to conduct G3.
8. If internal evidence does not discriminate, retain the uncertainty explicitly. If a real finding cannot be represented without material semantic loss, route only that bounded loss through the existing minimal D-016 path; otherwise do not add schema/infrastructure.
9. Only after the independent Reg. Ii 5 internal basis is systematically documented may WP-6 open Reg. Ii 4 for controlled witness-to-witness comparison. Any externally prompted correction must return to the Reg. Ii 5 target pixels.

Issue #115 owns the work checklist. This STATUS owns the current scholarly/restart state and formal G1–G6 gate claims.

## Restartability

A fresh capable context must be able to reconstruct without old chat that:

- Reg. Ii 5 is an archival-act Project anchor and #115 is the current bounded source-research task;
- the active target is the separate Reg. Ii 5 Ziegenrück Source at fol. 61v–63r / images 132–135 / PDF pages 14–17;
- exact File/SHA/crosswalk identity is established for `FILE-REG-II-5-00000129-EXCERPT`;
- in the 2026-09-08 research session the exact PDF SHA was re-established and each target page 14–17 was rendered/vision-inspected before its pixel-dependent first-reading work;
- current canonical diplomatic observations are partitioned folio-locally in `transcription/first-reading/61v.tsv`, `62r.tsv`, `62v.tsv`, `63r.tsv`; together they represent all 81 established physical anchors;
- `transcription/derived/61v-63r-first-reading.md` is a derived/rebuildable human-readable view only, not a second text owner;
- legacy `transcription/132.tsv`–`135.tsv`, apparatus and witness-dependent legacy palaeography remain verification/recovery evidence; they were consulted only after independent target-pixel passes and are not current Reg. Ii 5 text truth;
- the whole-locus review found no missing/doubled/reordered relevant source unit and preserved the consequential visible phenomena, including cancellations `61v-L16` and `62r-L18`, Arabic `80` at `62r-L19` and `62v-L01`, and the unresolved 63r heading; hand differentiation remains `not investigated`;
- `62r-L24` is currently read from the Reg. Ii 5 target graph as `So ...`, explicitly rejecting the legacy claim of a second `80` there;
- manuscript date expressions on 63r are not normalized into calendar/date-production claims;
- no material semantic-loss/System trigger arose from WP-0–WP-5 G2 representation work; the existing lean representation remains adequate;
- #95's first-write/post-write ownership fixture passed and Issue #95 is closed `completed`; no artifact ontology/manifest/system was introduced;
- Reg. Ii 4 Bd. II and Reg. Ii 5 are separate Ziegenrück witnesses; Reg. Ii 4 wording remains excluded from current reading authority until controlled G4 release;
- same-witness Reg. Ii 5 internal comparanda are admissible, while same record does not establish same hand;
- reading, identification, contextual role, hand hypothesis and dating claims retain separate evidence/status and do not inherit certainty from one another;
- the current lifecycle for **Reg. Ii 5 fol. 61v–63r only** is **G1 reached / G2 reached / G3 active-not reached / G4–G6 not reached**; #115 remains active and the result is an Editionsbaustein, not a finished edition;
- the immediate cursor is **systematically inventory and test consequential unresolved loci against admissible Reg. Ii 5 internal evidence → persist only justified row-level changes → retain unresolved where evidence does not discriminate → then assess controlled Reg. Ii 4 release**, not renewed provenance work or an abstract schema/migration programme.
