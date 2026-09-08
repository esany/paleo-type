# STATUS — ThHStAW, EGA, Reg. Ii 4 Bd. II

Last checkpoint: 2026-09-08

## Project authority and root

The human owner explicitly confirmed on 2026-09-02 that Reg. Ii 4 Bd. II should currently continue as one act-oriented Project, anchored at `ACT-THHSTAW-EGA-REG-II-4-BD-II`, as an application of D-018. This current authority does not retroactively certify the complete historical D-017 wording.

On 2026-09-03 the human owner selected the **Knau passage of the Reg. Ii 4 Bd. II Ziegenrück Source** as a bounded manuscript/source-research target. The scheduled work-package sequence #96–#99 for that target ended on 2026-09-06. This is **workflow/task completion**, not a claim that every Knau reading is resolved, that the whole Ziegenrück Source is transcribed, or that G5/G6 has been reached. The bounded work did not redefine the Project boundary and does not create a new current research priority.

On 2026-09-07 the admitted A-R reconciliation aligned current Project state with that completed work sequence: `project.yml:active_scope` records that no owner-selected active scholarly scope exists, while the actual historical principal and controlled-comparison Source uses are preserved as `historical` in `source-uses.tsv` with exact File bindings in `research/use-evidence.tsv`. Historical research function remains distinct from current NEXT ACTION.

On 2026-09-08 #115 completed the independent Reg. Ii 5 fol. 61v–63r G2/G3 basis that had been missing from the 2026-09-06 #99 comparison. The pre-existing pairwise collation owner was then revalidated against both independently established witness states. This clears the former G4 blocker for the bounded witness pair without selecting a new active Reg. Ii 4 research target.

## Known internal section/source node

`THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — *Visitation im Amt Ziegenrück*, fol. 294r–313r — is an internal Source node by canonical `part_of` relation. Its identified Knau locus is fol. 306v–309r / export images 667–672.

This is a separate material Source/witness from the Reg. Ii 5 Ziegenrück record fol. 55v–66v. Their archival extract/correspondence relation does not merge witness identity, foliation, image numbering, File provenance or diplomatic readings.

The historical Project-relative research functions are explicitly preserved in `source-uses.tsv`: Reg. Ii 4 Ziegenrück/Knau as the principal direct-reading use of the bounded locus and Reg. Ii 5 Ziegenrück/Knau as the controlled textual-comparison use. These rows document actual historical use only; they do not select current priority. Their concrete File bindings are recorded separately in `research/use-evidence.tsv`.

## Recovered prior work state

Historical snapshot `699fa6eada61db483dfca950193412715d9603a5` recorded the former source-unit state: the primary export had been inspected; the Knau locus had been mapped; the source was not activated for source-wide work; and any later comparison was to begin from an **independent reading** rather than import readings from Reg. Ii 5.

The old source-unit Project files were later removed from `main`, but Source/File/crosswalk evidence survives in `corpus/`. This STATUS restores consequential work-state/audit context without reviving source-as-project semantics.

## Legacy Knau/G2 material from the Li 5 path

The historical diplomatic material preserved under `projects/ega-reg-ii-5-knau/` must **not** be promoted wholesale into Reg. Ii 4 merely because parts of it closely match this witness. The owner clarified on 2026-09-02 that this older material is primarily verification/recovery material, and direct comparison of the separate Reg. Ii 4 and Reg. Ii 5 PDFs showed that legacy witness attribution cannot safely be inferred from old path/page labels.

Current rule:

- old Knau/G2 files may be used only as controlled checking/recovery material where the exact Source/File/locus provenance is adequate for the specific comparison claim;
- for a Reg. Ii 4 diplomatic claim or externally prompted correction, inspect the Reg. Ii 4 Source/File/locus itself;
- do not treat similarity to the parallel Reg. Ii 5 transmission as witness identity;
- do not use Reg. Ii 5 or legacy wording as a substitute for Reg. Ii 4 graphical evidence.

The canonical current classification of that legacy corpus is recorded in `projects/ega-reg-ii-5-knau/research/legacy-witness-provenance.tsv`.

## Evidence / crosswalk / URN state

- Exact inspected export: `FILE-REG-II-4-II-00000089-EXPORT` in `corpus/files.tsv`.
- Canonical crosswalk: fol. 306v–309r ↔ export images 667–672 ↔ PDF pages 27–32.
- The six mapped pages each have a distinct page-specific `urn:nbn:...` value in the canonical crosswalk. These values were already present when the crosswalk was first created and are not inferred from the PDF-page sequence.
- The crosswalk is intentionally partial; it does not claim page-level mapping for the full act/protocol.

## Research/gate state

The gate-evaluated textual scope below is **only the bounded Knau locus fol. 306v–309r**, with G4 comparison against Reg. Ii 5 fol. 61v–63r. No gate claim here applies automatically to the whole Ziegenrück Source fol. 294r–313r or the whole Reg. Ii 4 Bd. II archival act.

| Gate / activity | State | Evaluated scope | Meaning / residual limit |
|---|---|---|---|
| G1 source/transmission basis | `reached` | Knau investigation source group | Reg. Ii 4 principal and Reg. Ii 5 comparison Source/File/locus/provenance are reconstructable; preservation blockers remain explicit where applicable. |
| G2 diplomatic representation | `reached` | Reg. Ii 4 fol. 306v–309r | All 117 relevant visible units are represented in source order. This is representation completeness, not full reading resolution. |
| reading resolution | `incomplete / residual uncertainty explicit` | Reg. Ii 4 fol. 306v–309r | Numerous `working`/`unresolved` readings, accounting/measure signs, overwriting and other difficult loci remain. This is compatible with G2–G4. |
| G3 internal analysis | `reached at current internal evidence level` | consequential uncertainties within fol. 306v–309r | #98 systematically tested all inventoried consequential uncertainties internally and handed unresolved cases forward; G3 does not mean every reading was solved. |
| #99 controlled collation work package | `complete` | Reg. Ii 4 fol. 306v–309r ↔ Reg. Ii 5 fol. 61v–63r | Historical 2026-09-06 bounded comparison completed; current pairwise owner was revalidated 2026-09-08 after the independent Reg. Ii 5 basis became canonical. |
| G4 controlled comparison | `reached` | same bounded witness pair | Both witnesses are now independently represented and internally reviewed; corresponding units, agreements, variants, omissions, resegmentation and the divergent lower ending are explicitly mapped without cross-witness rewriting. |
| G5 critical consolidation/validation | `not reached` | bounded Knau edition target | No critically consolidated/validated text state is claimed and no owner-selected G5 task is active. |
| G6 scholarly edition | `not reached` | bounded Knau edition target | No scholarly edition has been produced. |

No new active manuscript target is currently selected in this Project. Any future Reg. Ii 4 reading must continue to be established against the Reg. Ii 4 Source/File/locus itself.

`Independent first reading` means **witness independence from external/parallel wording, not folio isolation within Reg. Ii 4**. Directly inspected and exactly locatable internal comparanda from the same Reg. Ii 4 locus may be used for graphematic recognition after the target problem is observed. The target graph remains primary evidence; comparison must use discriminating graphical/sign features rather than expected wording or semantic plausibility. Same Source/record does not establish same hand.

The observed correspondence with Reg. Ii 5 remains a separate Source-relationship claim in `corpus/relationships.tsv`; it does not merge witness identity or make parallel wording a basis for Reg. Ii 4 grapheme claims.

## Project-local execution controls

- `research/knau-fol306v-309r-evidence-lock.md` owns the historical immediate evidence/internal-comparison/external-release lock for the bounded #96–#99 task.
- `research/knau-fol306v-309r-contamination-matrix.tsv` records concrete allowed/forbidden use classes.
- `transcription/README.md` defines transcription-layer conventions and folio-local storage; it does not own Project cursor, progress or release state.
- `research/knau-fol306v-309r-g3-adjudication.tsv` records the project-local #98 internal test paths for consequential loci; it is not a second transcription owner.
- `research/knau-fol306v-309r-controlled-collation.md` is the canonical pairwise comparison owner for both the historical #99 mapping and the 2026-09-08 current G4 revalidation; it is not an original first-reading or diplomatic-text owner.
- the actual Reg. Ii 4 diplomatic reading/status remains owned by the folio-local TSVs under `transcription/first-reading/`.
- the actual Reg. Ii 5 diplomatic reading/status remains owned separately under `projects/ega-reg-ii-5-knau/transcription/first-reading/`.

## First-reading representation

The entire bounded authorized locus is represented in source order by:

- `306v.tsv`: `306v-01`–`306v-21`;
- `307r.tsv`: `307r-01`–`307r-19`;
- `307v.tsv`: `307v-01`–`307v-22`;
- `308r.tsv`: `308r-01`–`308r-25`;
- `308v.tsv`: `308v-01`–`308v-25`;
- `309r.tsv`: `309r-01`–`309r-05`.

The exact Reg. Ii 4 export and folio/image/PDF mapping were checked during the first-reading work. All 117 relevant visible units are represented. On 309r only the five units belonging to the bounded Knau locus are included.

The representation remains deliberately conservative. `working`/`unresolved` spans are visible, numeral/measure/accounting contexts are not silently converted into values, and no same-hand claim follows from same-witness recurrence.

## 2026-09-06 #97 G2 completeness audit

**G2 diplomatic-representation completeness: PASS for the bounded Knau locus.**

Here `completeness` means that every relevant visible source unit in fol. 306v–309r is represented at the required diplomatic level. It does **not** mean that every word/sign is securely read or that a finished diplomatic/critical edition exists.

The audit traversed all six folio-local TSVs against the directly inspected Reg. Ii 4 images 667–672 and the canonical crosswalk. It verified 117 relevant source units in source order with folio-local line counts `21 / 19 / 22 / 25 / 25 / 5`; sequential and unique `line_ref` values; the common ten-column transcription structure; preserved headings/lists/prose/continuations, abbreviation signs, numeral/accounting/measure problem classes, layout/source phenomena and explicit uncertainty; and the bounded Knau transition on 309r.

No missing relevant physical unit, hidden semantic supply, normalized replacement of a diplomatic form or external Reg. Ii 5/legacy wording import was found. `unresolved` and `working` readings remain compatible with this G2 result.

A human-readable whole-locus view is stored at `transcription/derived/knau-fol306v-309r-first-reading.md`. It is explicitly non-canonical and deterministically derived from the six folio TSVs; it is not a second manually maintained transcription truth.

## 2026-09-06 #98 systematic internal adjudication

**#98 systematic internal adjudication: COMPLETE; G3 reached for the bounded locus at the current internal-evidence level.**

The #98 inventory was regenerated from the six current folio TSVs and persisted directly in `research/knau-fol306v-309r-g3-adjudication.tsv`. It contains 34 consequential loci/clusters covering all current `working`/`unresolved` problem areas. Every inventory row records an internal evidential result or an explicit specialist-review condition; no `pending` row remains.

The adjudication used only direct Reg. Ii 4 target inspection and exactly localized internal Reg. Ii 4 comparanda. Reg. Ii 5, legacy G2/Knau and parallel wording were not opened as textual evidence. Same-witness recurrence was not treated as same-hand proof, and accounting/measure signs were not converted into values without an internal graphical basis.

Consequential re-adjudications persisted in the diplomatic owners:

- `307r-02`: promoted to working `It̄ Greffendorff` from direct Reg. Ii 4 internal comparison;
- `307r-07`: promoted to working `paren`, with `parem` retained as a residual alternative;
- `307v-16`: narrowed to p-initial uncertainty only, without a normalized place identity.

Important consciously unresolved/specialist areas remain:

- account, amount, measure and sign systems at `306v-03`–`306v-06`, `306v-17`/`306v-20`, `307r-08`/`307r-10` and the measure/natural-due contexts on `308r`;
- `306v-19`: the stroke adjacent to `wachs` cannot be internally classified securely as cancellation versus entry flourish/pen movement;
- `309r-01`–`309r-04`: heavy overlap/overwriting prevents responsible recovery beyond surviving alphabetic islands;
- `309r-05`: the `Anno`-like opening is followed by a non-ordinary flourish/sign sequence that does not support a year or value from the current evidence.

These unresolved outcomes do not leave an open systematic internal #98 task: the internal Reg. Ii 4 evidence has been exhausted at the required level and the limits are explicitly recorded.

## 2026-09-06 release-gate decision and #99 historical collation

**Project-local release gate: PASS for #99 controlled external collation.** This was a contamination-control decision, not by itself a generic G4 claim.

#99 then traversed the full bounded Reg. Ii 4 locus against directly inspected Reg. Ii 5 fol. 61v–63r, recorded explicit comparison units and found selective/condensed textual correspondence with substantial shared decree sequence, documented omissions and resegmentation. No Reg. Ii 4 diplomatic reading was silently changed from the external witness.

At that time Reg. Ii 5 did not yet have a current independent canonical whole-locus diplomatic representation, so **#99 completion was correctly not promoted to G4**. That historical limitation remains part of the audit trail.

## 2026-09-08 current G4 revalidation after #115

The former G4 blocker is now cleared. #115 independently established Reg. Ii 5 fol. 61v–63r from its own exact Source/File/pixels, represented all 81 physical anchors, completed G3 internal testing at the available evidence level, and only then opened Reg. Ii 4 for controlled comparison.

The existing canonical pairwise owner `research/knau-fol306v-309r-controlled-collation.md` was revalidated rather than duplicated. Its current mapping now explicitly relates the independently owned witness units and records:

- the shared Knau opening/account material;
- Reg. Ii 4 Lehnherr/Gotshauß/church-account/inventory material omitted as separate units from Reg. Ii 5;
- shared decree units across different physical segmentation;
- variants, numeral/measure/source-phenomenon differences and residual uncertainty without copying one witness into the other;
- the lower-end divergence that the historical #99 description had treated too coarsely.

The lower-boundary correction is consequential: Reg. Ii 5 `63r-L04` is **not** a demonstrated next-place heading. It is currently `⟦unclear heading: Zulage?⟧`, followed by text explicitly concerning the pfarrer at Knawe through `63r-L11`. The securely shared short closing decree is narrowed to Reg. Ii 4 `308v-23`–`308v-25` ↔ Reg. Ii 5 `63r-L01`–`63r-L03`. Reg. Ii 4 `309r-01`–`309r-05` and Reg. Ii 5 `63r-L04`–`63r-L11` are currently treated as **divergent ending material with no secure correspondence established**.

Comparison did not force unresolved text: Reg. Ii 4 `Greffendorff` does not settle the Reg. Ii 5 surname spelling; parallel wording does not complete Reg. Ii 5 cancellations, accounting signs or dense 62v passages; and Reg. Ii 5 date wording/signs are not converted into a date/year claim. Likewise no Reg. Ii 4 diplomatic row was rewritten merely because the Reg. Ii 5 parallel is clearer.

**Current assessment: G4 reached for the bounded pair Reg. Ii 4 fol. 306v–309r ↔ Reg. Ii 5 fol. 61v–63r.** This does not establish verbatim copying, same hand, same date, direction of dependence, priority, G5 consolidation or G6 edition status.

## NEXT ACTION — canonical restart point

The scheduled Reg. Ii 4 Knau work-package sequence through #99 is complete, and the later #115-enabled G4 revalidation is also complete. This does **not** mean that every Knau reading is resolved or that a G5/G6 edition state exists. Do **not** reopen #96/#97/#98/#99 absent a concrete new source or specialist finding.

**No owner-selected next manuscript/source-research target is currently recorded.** Do not infer automatic progression to G5/G6 from the G4 gate result. The next scholarly action requires owner selection of a new target or a separately scoped specialist follow-up if one of the consciously unresolved palaeographic/metrological areas becomes consequential.

## Restartability

A fresh context must identify:

- the Reg. Ii 4 Bd. II act-oriented Project and its separate Ziegenrück Source;
- exact File/crosswalk state and the bounded six-folio Knau first-reading representation;
- G1/G2/G3 reached for Reg. Ii 4 fol. 306v–309r with explicit residual uncertainty;
- historical #99 controlled-collation completion and its original limitation;
- the later independent Reg. Ii 5 G2/G3 basis produced under #115;
- the 2026-09-08 revalidated pairwise comparison in `research/knau-fol306v-309r-controlled-collation.md` and **G4 reached** for the bounded witness pair;
- the corrected lower comparison boundary: Reg. Ii 5 `63r-L04` is not a next-place heading and Li5 `63r-L04`–`L11` has no secure current counterpart in Reg. Ii 4 `309r-01`–`309r-05`;
- G5 and G6 remain not reached;
- historical Project→Source uses and exact File bindings remain historical evidence, not current priority;
- no current owner-selected active scholarly scope exists.

The current scholarly state is **Knau fol. 306v–309r only: G1 reached / G2 reached as representational completeness with unresolved readings remaining / G3 reached at current internal evidence / G4 reached for controlled comparison with Reg. Ii 5 fol. 61v–63r / G5 not reached / G6 not reached / no current owner-selected active scholarly scope**.
