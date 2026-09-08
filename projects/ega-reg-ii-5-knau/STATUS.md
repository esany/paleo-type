# STATUS — ThHStAW, EGA, Reg. Ii 5

Last checkpoint: 2026-09-08

## Project authority and identity

The human owner confirmed on 2026-09-02 that **Reg. Ii 5 continues as an act-oriented Project**, anchored at `ACT-THHSTAW-EGA-REG-II-5`. The directory/id `ega-reg-ii-5-knau` is a legacy path from an earlier AI-organized Knau benchmark; `Knau` is not the Project boundary.

On 2026-09-07 the human owner selected a bounded scholarly target: **source-exact editorial development of the Reg. Ii 5 Ziegenrück witness at fol. 61v–63r**, tracked in #115. That bounded work package was completed on 2026-09-08 as an **Editionsbaustein**, not a completed scientific edition and not authority for an abstract transcription/person-role/date ontology.

`project.yml:active_scope` now records that **no owner-selected active scholarly scope exists after #115 completion**. A later G5/G6 or source-wide target requires fresh human-owner selection rather than being inferred automatically from gate progression.

## Canonical Source structure

Keep archival container, concrete Source record and research use distinct.

- `ACT-THHSTAW-EGA-REG-II-5` — archival act / documentary Project anchor: **ThHStAW, EGA, Reg. Ii 5**.
- `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — concrete internal Source record: **Visitation im Amt Ziegenrück**, fol. 55v–66v, described in archival metadata as an extract related to the Reg. Ii 4 Bd. II Ziegenrück transmission.
- `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — separate Source record in the separate archival act **Reg. Ii 4 Bd. II**, fol. 294r–313r; its Knau passage is fol. 306v–309r / export images 667–672.
- The two Reg. Ii 3 records remain separate Sources inside the Reg. Ii 3 archival act and are not witnesses of the Ziegenrück text merely because they were historically used for context/control.

The Reg. Ii 4 and Reg. Ii 5 Ziegenrück records are separate material witnesses/transmissions. Close textual correspondence does not collapse their identities, dates, hands, production stages or diplomatic readings.

## Completed #115 Source use and exact evidence

The completed Project-relative principal use is preserved in `source-uses.tsv` as historical:

- use `USE-REGII5-00000129-PRINCIPAL`;
- Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`;
- relevant locus fol. 61v–63r;
- status `historical` after #115 completion.

The exact evidence binding is likewise preserved as historical in `research/use-evidence.tsv`:

- evidence `EVID-REGII5-00000129-PRINCIPAL`;
- File `FILE-REG-II-5-00000129-EXCERPT`;
- export images 132–135;
- SHA-256 `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f` in canonical `corpus/files.tsv`.

Historical status means completed research use, not invalidated evidence. It does not imply future target-context pixel readiness.

During the 2026-09-08 research session the exact uploaded Reg. Ii 5 PDF was staged and its SHA-256 matched `FILE-REG-II-5-00000129-EXCERPT`. The target pages were rendered and visually inspected as source-identical evidence before their respective pixel-dependent readings: fol. 61v = image 132 = PDF page 14, fol. 62r = image 133 = page 15, fol. 62v = image 134 = page 16, and fol. 63r = image 135 = page 17. For each worked target page in that execution context, `STAGED = PASS` and `VISION-INSPECTABLE = PASS`, therefore `VISUAL EVIDENCE READY = PASS` under `methodology/workflow.md`.

Current folio-local first-reading partitions were persisted directly to their canonical owners after independent target-pixel passes:

- `transcription/first-reading/61v.tsv` — initial commit `e26eaf5fec37b2cc927c033c356a1f514a7c0dc2`;
- `transcription/first-reading/62r.tsv` — initial commit `e79d679553d3039c582dc99eabdea368d31a193b`;
- `transcription/first-reading/62v.tsv` — initial commit `7c28026426433df90b67c2420bb7f03c990f9a63`, later G3 refinement commit `b5644250c813fa756c5c4995b5cc22d965bc6674`;
- `transcription/first-reading/63r.tsv` — initial commit `ebb909042813c5886b184522721e6c30e41b73cf`.

For each folio, legacy `transcription/132.tsv`–`135.tsv` was consulted only after the independent Reg. Ii 5 target-pixel pass and only as recovery/verification material. Reg. Ii 4 wording was not used as reading authority until the independent Reg. Ii 5 G2/G3 basis was complete and controlled comparison was formally opened.

## Legacy diplomatic material — verification/recovery only

The historical diplomatic and witness-dependent Knau material under this legacy Project path — especially `transcription/132.tsv` through `135.tsv`, `apparatus/decisions.tsv`, the legacy palaeography tables and any claims that depend on their old page/path attribution — is preserved because it documents earlier work and remains useful for checking readings, failure modes and migration loss.

**It is not canonical current Reg. Ii 5 diplomatic transcription state.**

Owner clarification and direct comparison of the separately supplied Reg. Ii 4 Bd. II and Reg. Ii 5 Ziegenrück PDFs on 2026-09-02 showed that the earlier working diplomatic corpus cannot safely be assigned wholesale to one witness from its legacy path/page labels alone. The two transmissions are closely parallel, and historical work phases may have imported or compared readings across them. Until witness provenance is re-established for a concrete reading, the old diplomatic material has status **legacy verification/recovery evidence; witness attribution unresolved or potentially mixed**.

Consequences:

- preserve every old reading, uncertainty, apparatus decision and palaeographic observation;
- do not delete or silently normalize the old material;
- do not cite `transcription/132.tsv`–`135.tsv` as proof of a Reg. Ii 5 reading without fresh witness-specific inspection;
- do not move a legacy reading into Reg. Ii 4 merely because it matches that witness; attribution requires explicit Source/File/locus verification;
- current Reg. Ii 5 diplomatic truth is owned by `transcription/first-reading/*.tsv`;
- comparison between Reg. Ii 4 and Reg. Ii 5 is witness-to-witness collation, not reuse of a shared transcription.

## Later exact-source G2 research artifacts — bounded direct authority

The legacy directory later accumulated four `research/g2-*` artifacts with evidential roles that are **not** inherited from the unresolved witness provenance of the older diplomatic corpus. The historical `g2-*` filename/phase label does **not** itself mean that the current Reg. Ii 5 Project has reached generic G2. Their authority follows their own Source/File/locus chain and is classified explicitly in `research/legacy-witness-provenance.tsv`:

- `research/g2-baseline-provenance.md` — exact Reg. Ii 5 Source/File/SHA/crosswalk/render and research-access provenance;
- `research/g2-checkpoint-a-physical-inventory.md` — direct Reg. Ii 5 visual observations of physical/source order, layout and bounded source phenomena on fol. 61v–63r;
- `research/g2-checkpoint-b-semantic-loss.md` — source-bound mapping and semantic-loss/adequacy analysis against the accepted Reg. Ii 5 physical anchors and the legacy research records;
- `research/g2-domain-review-checkpoint-b.md` — consequence/requirements classification derived from that source-bound fixture.

These artifacts retain scientific authority **only at the level they actually claim**. Direct Reg. Ii 5 physical observations such as source order and recorded cancellations are not downgraded merely because the files live in the legacy directory. Conversely, none validates `transcription/132.tsv`–`135.tsv` row-by-row, resolves old witness attribution, establishes same hand, or promotes an old diplomatic reading into current Reg. Ii 5 truth.

## Exact-source structural fixture and current G2 representation

Checkpoint A directly validated 81 provisional physical/source-order anchors against the exact Reg. Ii 5 baselines:

- 61v: `L01–L20`;
- 62r: `L01–L25`;
- 62v: `L01–L25`;
- 63r: `L01–L11`.

The four folio-local canonical first-reading partitions now represent **all 81 established physical anchors** in source order. The whole-locus review found no missing, doubled or reordered relevant source unit relative to the exact-source structural fixture. Explicitly unresolved readings remain valid representation rather than being completed from grammar, domain expectation or legacy wording.

The current partitions preserve the consequential visible source phenomena required by the target: the 61v list/accounting region and its unresolved quantity/sign notation; cancellation at `61v-L16`; cancellation at `62r-L18`; written Arabic `80` at `62r-L19` and `62v-L01`; the 63r display heading at `L04` separately from its unresolved reading; and representation of the previously legacy-uncovered visible `63r-L05–L11`. The 63r lower-page show-through is not promoted into a target text stream because no target-text obstruction is established. Hand differentiation remains `not investigated`.

A direct target-graph recheck on 62r rejected one fluent legacy carry-over: the opening of `62r-L24` is represented as `So`, not as a second Arabic `80`. On 63r, `agustini`, `pfingsten` and `xlvij Jhars` are retained as written date expressions/sign sequence; no calendar date or absolute year is inferred in the diplomatic layer.

The current lean TSV representation carries reading order, line reference, region, source phenomena, research status, alternatives, abbreviation layer, editorial supply and evidence notes without material loss for the findings encountered. The whole-locus semantic-loss check therefore remains **PASS: no Package-B/D-016 representation change is triggered**.

A human-readable whole-locus witness view is present at `transcription/derived/61v-63r-first-reading.md`. It is explicitly derived/rebuildable from the four folio TSVs by fixed folio order plus `reading_order`; it is not a second canonical text owner. It was refreshed after the G3 `62v-L11` promotion.

The #95 preflight/post-write regression fixture passed and Issue #95 is closed as `completed`: no range-named canonical transcription file, no README/state duplicate, no overwrite/promotion of legacy 132–135, and no row-wise duplication of stable Source/File/SHA/crosswalk truth was introduced.

## G3 internal palaeographic/notational review

`research/g3-internal-review-61v-63r.md` owns the bounded G3 analytical record; it is not a second transcription owner. The review systematically inventoried consequential uncertainty classes and tested them against admissible Reg. Ii 5 internal evidence without opening Reg. Ii 4 wording.

Key results:

- the recurrent surname-like graph sequence is demonstrably recurrent but exact spelling remains unresolved; repetition does not establish historical identity or same hand;
- the two genuine Arabic `80` forms (`62r-L19`, `62v-L01`) discriminate graphically from lexical `So` at `62r-L24`;
- 61v accounting signs remain unresolved because current internal evidence does not support a lossless sign→value mapping;
- deleted text at `61v-L16` and `62r-L18` remains unresolved while the cancellation phenomena remain secure;
- higher-resolution exact-source reinspection justified one row-level promotion: `62v-L11 = acker / zu seinem steinbruch gemacht`;
- remaining dense 62v and 62r prose uncertainties were reinspected and explicitly handed forward unresolved where no internal comparator discriminated them;
- the 63r heading remains `⟦unclear heading: Zulage?⟧`; `agustini`, `pfingsten` and `xlvij` remain manuscript-level wording/sign evidence only;
- no same-hand comparator group was established; same Source/record was not treated as same-hand proof;
- no material semantic-loss/System trigger arose.

**G3 is reached for fol. 61v–63r at the current internal-evidence level.** This means the internal test paths and residual limits are explicit; it does not mean every difficult sign or word is solved.

## G4 controlled Reg. Ii 4 comparison

After the independent Reg. Ii 5 G2/G3 basis was complete, Reg. Ii 4 was opened for controlled comparison using its independently established G2/G3 diplomatic state. Pairwise comparison truth remains owned in the pre-existing canonical cross-witness record:

`projects/ega-reg-ii-4-bd-ii/research/knau-fol306v-309r-controlled-collation.md`

The 2026-09-08 revalidation deliberately reused that owner rather than creating a second collation file under this Project.

Current mapping confirms:

- selective/condensed textual correspondence with a substantial shared decree sequence;
- substantial Reg. Ii 4 Lehnherr/church-account/inventory and decree material absent as separate units from Reg. Ii 5;
- different physical segmentation/resegmentation across shared units;
- agreement/variant/numeral and source-phenomenon differences without cross-witness copying of unresolved diplomatic text;
- no basis for same-hand, same-date, direct-copy or priority claims from similarity alone.

The revalidation also corrects the historical #99 lower-boundary description. Reg. Ii 5 `63r-L04` is **not** a demonstrated next-place heading: it is the unresolved display heading `⟦unclear heading: Zulage?⟧`, followed by Knawe/pfarrer text through `63r-L11`. The shared short closing decree is narrowed to Reg. Ii 4 `308v-23`–`308v-25` ↔ Reg. Ii 5 `63r-L01`–`63r-L03`. Reg. Ii 4 `309r-01`–`309r-05` and Reg. Ii 5 `63r-L04`–`63r-L11` are treated as divergent ending material with no secure current correspondence.

Externally tempting completions were not imported: Reg. Ii 4 `Greffendorff` does not settle the Reg. Ii 5 surname spelling; Reg. Ii 4 parallel wording does not complete the dense 62v spans, cancellations, accounting signs or date interpretation. No comparison-driven Reg. Ii 5 row change was justified beyond the already logged internal G3 promotion.

**G4 is reached for the bounded pair Reg. Ii 5 fol. 61v–63r ↔ Reg. Ii 4 fol. 306v–309r.**

## Project-local editorial execution discipline

The completed #115 work followed existing generic method (`historical-source-workflow.md`, `transcription-guidelines.md`, `research-gates.md`) through a project-specific source-exact editorial vertical slice.

Keep these distinctions for any future reuse:

- source observation / diplomatic reading ≠ identification;
- identification ≠ contextual role;
- contextual/event association ≠ scribe/hand;
- written date expression/sign sequence ≠ normalized calendar date or production date;
- textual correspondence ≠ same hand, direct copy, same date or priority;
- historical interpretation remains downstream of the established source-critical evidence.

## Source-driven Semantic-Loss / Package-B rule

Person/role/date and related Package-B work is **not a standalone architecture programme**.

Use this loop if future source work exposes a real loss:

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

No universal agent/role/date/hand/locus ontology is authorized by #115.

## Historical work-state audit

The earliest repository Project metadata (`251ce9ed39e04bb852e0232dbcce21c68bd4c3a7`) created `ega-reg-ii-5-knau` and the Knau scope as an AI-organized benchmark. Checkpoint `08c08bd6f90635210fbeff3f2d19cd0a485cc0b9` froze useful working readings and uncertainties, but it does not establish their witness provenance or owner authority for Project identity.

Snapshot `699fa6eada61db483dfca950193412715d9603a5` preserves the later source-unit state. Git history remains an audit/recovery source, not current scientific authority.

The former compatibility register `sources/sources.tsv` was loss-checked and removed. Completed Project-relative uses are preserved as `historical` in `source-uses.tsv`; exact File bindings remain in `research/use-evidence.tsv` with the same completed/historical distinction.

## Digital addressing / provenance

For the canonical Reg. Ii 5 Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`:

- canonical File identity/provenance is owned by `corpus/files.tsv`;
- canonical Source crosswalk is owned by `corpus/source-data/THHSTAW-EGA-REG-II-5-STAT-VIS-00000129/crosswalk.tsv`;
- Source boundary is fol. 55v–66v;
- the PDF/export may contain adjacent context beyond that Source boundary;
- identifiability/reproducibility do not by themselves establish that evidence is staged and inspectable in a fresh target context.

For the separate Reg. Ii 4 Bd. II Ziegenrück Source, its own File, crosswalk, page-specific URNs and fol. 306v–309r / images 667–672 remain canonical under that Source. Never substitute one witness's image numbering, TIFF labels, folios, dates or readings for the other.

## Current research state / edition lifecycle

The gate-evaluated textual scope below is **Reg. Ii 5 fol. 61v–63r only**, with G4 comparison against the bounded Reg. Ii 4 Knau locus. No gate claim here applies automatically to the whole Ziegenrück Source fol. 55v–66v or the whole Reg. Ii 5 act.

| Gate / activity | State | Evaluated scope | Meaning / residual limit |
|---|---|---|---|
| G1 source/transmission basis | `reached` | completed #115 source group/locus | Principal Reg. Ii 5 Source/File/SHA/crosswalk and separate comparison/context Sources are identified with explicit evidence/provenance limits. |
| #115 source-exact editorial work package | `complete` | Reg. Ii 5 fol. 61v–63r | WP-0–WP-6 and the acceptance checks were carried through. Work-package completion is not a G5/G6 claim. |
| G2 diplomatic representation | `reached` | Reg. Ii 5 fol. 61v–63r | All 81 relevant physical anchors are represented in source order with uncertainty and source phenomena preserved; a derived readable view exists. |
| G3 internal analysis | `reached at current internal evidence level` | consequential uncertainties in the same locus | Consequential uncertainty classes were systematically inventoried/tested; justified promotion was persisted; residual non-discriminating loci are explicitly handed forward unresolved. |
| G4 controlled comparison | `reached` | Reg. Ii 5 fol. 61v–63r ↔ Reg. Ii 4 fol. 306v–309r | Both witnesses are independently represented/reviewed; corresponding units, variants, omissions, resegmentation and divergent lower ending are explicitly mapped without cross-witness rewriting. |
| G5 critical consolidation/validation | `not reached` | bounded Knau edition target | No owner-selected G5 task or critically consolidated/validated text state is claimed. Residual specialist/editorial validation remains possible but is not automatically authorized by G4 attainment. |
| G6 scholarly edition | `not reached` | bounded Knau edition target | No scholarly edition has been produced. #115 produced an Editionsbaustein only. |

Reading resolution remains incomplete in places and this is compatible with G2–G4. Residual uncertainty includes the Reg. Ii 5 surname-like spelling, 61v accounting values/signs, deleted text at two cancellations, several 62r/62v prose spans, exact 63r heading spelling, date normalization/interpretation, and hand differentiation.

## NEXT ACTION — canonical restart point

**No owner-selected next scholarly action is currently authorized after completion of #115.**

Do not infer automatic progression to G5/G6, source-wide transcription, historical interpretation, ontology work or software work from the fact that G1–G4 are reached for this bounded target. The next action requires human-owner selection of a new research target.

If a future owner-selected task returns to this Editionsbaustein:

1. reconstruct the current text from the four folio-local `transcription/first-reading/*.tsv` owners and the derived view;
2. use `research/g3-internal-review-61v-63r.md` for the internal-test audit and the existing Reg. Ii 4 controlled-collation record for G4 mappings;
3. re-establish `STAGED` + `VISION-INSPECTABLE` before any new pixel-dependent Reg. Ii 5 reinspection;
4. preserve residual uncertainties unless new evidence discriminates them;
5. any externally prompted diplomatic correction must return to the relevant target witness graph;
6. any new G5/G6 claim must satisfy the generic gate requirements and receive explicit owner-selected scope rather than being inferred from #115 completion.

Issue #115 owns the completed work checklist/history. This STATUS owns the current scholarly/restart state and formal G1–G6 claims.

## Restartability

A fresh capable context must be able to reconstruct without old chat that:

- Reg. Ii 5 remains an archival-act Project anchor, but no owner-selected active scholarly scope exists after #115 completion;
- the completed Editionsbaustein target was the separate Reg. Ii 5 Ziegenrück Source at fol. 61v–63r / images 132–135 / PDF pages 14–17;
- exact File/SHA/crosswalk identity is established for `FILE-REG-II-5-00000129-EXCERPT`;
- in the 2026-09-08 source session each target page 14–17 was staged/rendered/vision-inspected before its first-reading work;
- canonical diplomatic observations are owned by `transcription/first-reading/61v.tsv`, `62r.tsv`, `62v.tsv`, `63r.tsv`; together they represent all 81 established physical anchors;
- `transcription/derived/61v-63r-first-reading.md` is derived/rebuildable only, not a second text owner;
- legacy `transcription/132.tsv`–`135.tsv`, apparatus and witness-dependent legacy palaeography remain verification/recovery evidence, not current Reg. Ii 5 text truth;
- the whole-locus review found no missing/doubled/reordered relevant source unit and preserved cancellations `61v-L16`/`62r-L18`, Arabic `80` at `62r-L19`/`62v-L01`, and the unresolved 63r heading;
- `62r-L24` is `So ...`, not a second `80`;
- G3 systematically tested consequential internal uncertainties; `62v-L11 = acker / zu seinem steinbruch gemacht` is the current justified G3 promotion, while many other loci remain explicitly unresolved;
- hand differentiation remains `not investigated`; recurrence never became same-hand proof;
- controlled Reg. Ii 4 comparison was opened only after the independent Reg. Ii 5 G2/G3 basis; pairwise mappings are owned by `projects/ega-reg-ii-4-bd-ii/research/knau-fol306v-309r-controlled-collation.md`;
- the historical #99 lower-boundary claim was corrected: Reg. Ii 5 `63r-L04` is not a next-place heading; Reg. Ii 5 `63r-L04`–`L11` has no secure current counterpart in Reg. Ii 4 `309r-01`–`309r-05`;
- textual correspondence remains selective/condensed with omissions/resegmentation and does not prove direct copy, same hand, date or priority;
- no material semantic-loss/System trigger arose; no artifact ontology/manifest/system was introduced;
- completed Project-relative Source/File uses are now historical; no current priority is inferred from them;
- the current lifecycle for the bounded target is **G1 reached / G2 reached / G3 reached at current internal evidence / G4 reached / G5 not reached / G6 not reached**;
- #115 is a completed **Editionsbaustein**, not a finished edition;
- the immediate cursor is **none until a human owner selects a new scholarly target**.
