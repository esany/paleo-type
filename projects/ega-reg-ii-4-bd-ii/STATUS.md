# STATUS — ThHStAW, EGA, Reg. Ii 4 Bd. II

Last checkpoint: 2026-09-07

## Project authority and root

The human owner explicitly confirmed on 2026-09-02 that Reg. Ii 4 Bd. II should currently continue as one act-oriented Project, anchored at `ACT-THHSTAW-EGA-REG-II-4-BD-II`, as an application of D-018. This current authority does not retroactively certify the complete historical D-017 wording.

On 2026-09-03 the human owner selected the **Knau passage of the Reg. Ii 4 Bd. II Ziegenrück Source** as a bounded manuscript/source-research target. That target was completed through #96–#99 on 2026-09-06. It did not redefine the Project boundary, and completion does not create a new current research priority.

On 2026-09-07 the admitted A-R reconciliation aligned current Project state with that completed workflow: `project.yml:active_scope` now records that no owner-selected active scholarly scope exists, while the actual completed principal and controlled-comparison Source uses are preserved as `historical` in `source-uses.tsv` with exact File bindings in `research/use-evidence.tsv`. Historical research function remains distinct from current NEXT ACTION.

## Known internal section/source node

`THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — *Visitation im Amt Ziegenrück*, fol. 294r–313r — is an internal Source node by canonical `part_of` relation. Its identified Knau locus is fol. 306v–309r / export images 667–672.

This is a separate material Source/witness from the Reg. Ii 5 Ziegenrück record fol. 55v–66v. Their archival extract/correspondence relation does not merge witness identity, foliation, image numbering, File provenance or diplomatic readings.

The completed Project-relative research functions are now explicitly preserved in `source-uses.tsv`: Reg. Ii 4 Ziegenrück/Knau as the historical principal direct-reading use and Reg. Ii 5 Ziegenrück/Knau as the historical controlled textual-comparison use. These rows document actual completed use only; they do not select current priority. Their concrete File bindings are recorded separately in `research/use-evidence.tsv`.

## Recovered prior work state

Historical snapshot `699fa6eada61db483dfca950193412715d9603a5` recorded the former source-unit state: the primary export had been inspected; the Knau locus had been mapped; the source was not activated for source-wide work; and any later comparison was to begin from an **independent reading** rather than import readings from Reg. Ii 5.

The old source-unit Project files were later removed from `main`, but Source/File/crosswalk evidence survives in `corpus/`. This STATUS restores consequential work-state/audit context without reviving source-as-project semantics.

## Legacy Knau/G2 material from the Li 5 path

The historical diplomatic material preserved under `projects/ega-reg-ii-5-knau/` must **not** be promoted wholesale into Reg. Ii 4 merely because parts of it closely match this witness. The owner clarified on 2026-09-02 that this older material is primarily verification/recovery material, and direct comparison of the separate Reg. Ii 4 and Reg. Ii 5 PDFs showed that legacy witness attribution cannot safely be inferred from old path/page labels.

Current rule:

- after the project-local release gate, old Knau/G2 files may be used only as controlled checking/recovery material where the exact Source/File/locus provenance is adequate for the specific comparison claim;
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

The bounded Reg. Ii 4 Knau target is complete through #99. No current diplomatic transcription is declared merely from the legacy Knau/G2 corpus, and no new active manuscript target is currently selected. Any future Reg. Ii 4 reading must continue to be established against the Reg. Ii 4 Source/File/locus itself.

`Independent first reading` means **witness independence from external/parallel wording, not folio isolation within Reg. Ii 4**. Directly inspected and exactly locatable internal comparanda from the same Reg. Ii 4 locus may be used for graphematic recognition after the target problem is observed. The target graph remains primary evidence; comparison must use discriminating graphical/sign features rather than expected wording or semantic plausibility. Same Source/record does not establish same hand.

The observed correspondence with Reg. Ii 5 remains a separate Source-relationship claim in `corpus/relationships.tsv`; it does not merge witness identity or make parallel wording a basis for Reg. Ii 4 grapheme claims.

## Project-local execution controls

- `research/knau-fol306v-309r-evidence-lock.md` owns the immediate evidence/internal-comparison/external-release lock for this bounded task.
- `research/knau-fol306v-309r-contamination-matrix.tsv` records concrete allowed/forbidden use classes.
- `transcription/README.md` defines transcription-layer conventions and folio-local storage; it does not own Project cursor, progress or release state.
- `research/knau-fol306v-309r-g3-adjudication.tsv` records the project-local #98 internal test paths for consequential loci; it is not a second transcription owner.
- `research/knau-fol306v-309r-controlled-collation.md` is the separate #99 controlled comparison/checking record; it is not an original first-reading or diplomatic-text owner.
- the actual Reg. Ii 4 diplomatic reading/status remains owned by the folio-local TSVs under `transcription/first-reading/`.

## First-reading representation

The complete authorized locus is represented in source order by:

- `306v.tsv`: `306v-01`–`306v-21`;
- `307r.tsv`: `307r-01`–`307r-19`;
- `307v.tsv`: `307v-01`–`307v-22`;
- `308r.tsv`: `308r-01`–`308r-25`;
- `308v.tsv`: `308v-01`–`308v-25`;
- `309r.tsv`: `309r-01`–`309r-05`.

The exact Reg. Ii 4 export and folio/image/PDF mapping were checked during the first-reading work. All 117 relevant visible units are represented. On 309r only the five units belonging to the Knau locus are included; the following Ziegenrück heading is outside the bounded locus.

The representation remains deliberately conservative. `working`/`unresolved` spans are visible, numeral/measure/accounting contexts are not silently converted into values, and no same-hand claim follows from same-witness recurrence.

## 2026-09-06 #97 G2 completeness audit

**G2 diplomatic-representation completeness: PASS.**

The audit traversed all six folio-local TSVs against the directly inspected Reg. Ii 4 images 667–672 and the canonical crosswalk. It verified 117 relevant source units in source order with folio-local line counts `21 / 19 / 22 / 25 / 25 / 5`; sequential and unique `line_ref` values; the common ten-column transcription structure; preserved headings/lists/prose/continuations, abbreviation signs, numeral/accounting/measure problem classes, layout/source phenomena and explicit uncertainty; and the Knau boundary on 309r before the following Ziegenrück heading.

No missing relevant physical unit, hidden semantic supply, normalized replacement of a diplomatic form or external Reg. Ii 5/legacy wording import was found. `unresolved` and `working` readings remain compatible with this G2 result.

A human-readable whole-locus view is stored at `transcription/derived/knau-fol306v-309r-first-reading.md`. It is explicitly non-canonical and deterministically derived from the six folio TSVs; it is not a second manually maintained transcription truth.

## 2026-09-06 #98 systematic internal adjudication

**Systematic Reg. Ii 4 internal G3 adjudication: COMPLETE.**

The #98 inventory was regenerated from the six current folio TSVs and persisted directly in `research/knau-fol306v-309r-g3-adjudication.tsv`. It contains 34 consequential loci/clusters covering all current `working`/`unresolved` problem areas. Every inventory row now records an internal evidential result or an explicit specialist-review condition; no `pending` row remains.

The adjudication used only direct Reg. Ii 4 target inspection and exactly localized internal Reg. Ii 4 comparanda. Reg. Ii 5, legacy G2/Knau and parallel wording were not opened as textual evidence. Same-witness recurrence was not treated as same-hand proof, and accounting/measure signs were not converted into values without an internal graphical basis.

Consequential re-adjudications persisted in the diplomatic owners:

- `307r-02`: promoted from `It̄ ⟦unclear: G…⟧` to working `It̄ Greffendorff`. The earlier negative control against `306v-02 Crependorff` remains part of the audit history; the promotion is based on reinspection of the 307r target against direct internal `Greffendorff` anchors at `307v-20`, `308r-11`, `308r-19`, `308v-05`, `308v-07` and `308v-19`, including the G-initial, paired long-f, central d/or and final ff architecture visible on the target itself.
- `307r-07`: promoted from unresolved `parem|paren` to working `paren`, with `parem` retained as a residual alternative. The p-initial remains internally supported; target-final n/m morphology was tested against local ending controls rather than a historical place-name assumption.
- `307v-16`: narrowed from p/b-initial uncertainty to p-initial uncertainty only; the interior and ending remain unresolved and no normalized place identity is supplied.

Important consciously unresolved/specialist areas remain:

- account, amount, measure and sign systems at `306v-03`–`306v-06`, `306v-17`/`306v-20`, `307r-08`/`307r-10` and the measure/natural-due contexts on `308r`; values/units require specialist metrological/accounting review if they become consequential;
- `306v-19`: the stroke adjacent to `wachs` cannot be internally classified securely as cancellation versus entry flourish/pen movement; qualified palaeographic/diplomatic review is required if deletion status becomes consequential;
- `309r-01`–`309r-04`: heavy overlap/overwriting prevents responsible recovery beyond the surviving alphabetic islands; qualified palaeographic review and/or better imaging is required for consequential fuller recovery;
- `309r-05`: the `Anno`-like opening is followed by a non-ordinary flourish/sign sequence that does not support a year or value from the current evidence; specialist review/better imaging is required if dating becomes consequential.

These unresolved outcomes do not leave an open systematic internal #98 task: the internal Reg. Ii 4 evidence has been exhausted at the required level and the limits are explicitly recorded.

## 2026-09-06 release-gate decision

**Project-local release gate: PASS for #99 controlled external collation.**

Conditions 1–4 are materially satisfied by the complete first reading, G2 PASS, merged #98 internal adjudication and stable physical line references. Condition 5 is instantiated by `research/knau-fol306v-309r-controlled-collation.md`, which explicitly identifies itself as controlled collation/checking. Conditions 6 and 7 remain binding record/use rules: any externally prompted Reg. Ii 4 correction requires direct Reg. Ii 4 reinspection and graphical basis, and legacy material may be used only where claim-specific Source/File/locus provenance is adequate.

This release does not retroactively alter first-reading provenance and does not make parallel wording an authority for Reg. Ii 4.

## 2026-09-06 #99 controlled external collation

**#99 controlled collation: COMPLETE.**

The exact comparison witness was staged in the execution context as the canonical Reg. Ii 5 File and verified before reading:

- Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — *Visitation im Amt Ziegenrück*, fol. 55v–66v;
- canonical File `FILE-REG-II-5-00000129-EXCERPT` / `1a03ea95927-120-143.pdf`;
- verified SHA-256 `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f`;
- Knau locus fol. 61v–63r = export images 132–135 = PDF pages 14–17.

All four Reg. Ii 5 target pages were rendered and directly pixel-inspected. The comparison traversed the entire Reg. Ii 4 Knau locus `306v-01`–`309r-05` against Reg. Ii 5 fol. 61v–63r at explicit textual-unit level. The canonical detailed mappings are owned by `research/knau-fol306v-309r-controlled-collation.md`.

Main collation result:

- both witnesses share the Knau opening/account structure and a substantial sequence of later decree units;
- Reg. Ii 5 is not a line-for-line duplicate: it omits/condenses the Reg. Ii 4 `Lehnherr` / church-account / inventory material and several decree units, and it resegments shared material across different physical lines/folios;
- agreement, variants, omissions, structural/order differences and numeral/measure differences are explicitly represented in the #99 owner;
- no same-hand claim was inferred from textual similarity;
- no legacy `132.tsv`–`135.tsv` wording was used as a substitute for source inspection;
- every externally suggestive Reg. Ii 4 locus remained subject to direct Reg. Ii 4 graphical authority.

No Reg. Ii 4 diplomatic reading changed as a consequence of collation. In particular, the completed #98 results `307r-02 = Greffendorff`, `307r-07 = paren` with residual `parem`, and the p-initial-only unresolved state at `307v-16` remain canonical and were not overwritten from the parallel witness.

The source-relationship claim in `corpus/relationships.tsv` is now sharpened only to the demonstrated level: **selective/condensed textual correspondence with a substantial shared decree sequence plus documented omissions and resegmentation**. It does not assert verbatim copying, complete line equivalence or same hand.

## NEXT ACTION — canonical restart point

The bounded Reg. Ii 4 Knau workflow through #99 is complete. Do **not** reopen #96/#97/#98/#99 absent a concrete new source or specialist finding.

No owner-selected next manuscript/source-research target is currently recorded. The next action, when authorized, is owner/roadmap selection of a new research target or a separately scoped specialist follow-up if one of the consciously unresolved palaeographic/metrological areas becomes consequential. Any such follow-up must preserve the existing first-reading and #98/#99 audit trail rather than rewriting it retrospectively.

## Restartability

A fresh context must identify the Reg. Ii 4 Bd. II Project, its separate Ziegenrück Source, exact File/crosswalk state, the complete six-folio first-reading representation, #97 G2 PASS, completed #98 internal adjudication, release gate PASS, the completed #99 record `research/knau-fol306v-309r-controlled-collation.md`, the historical Project→Source uses and their exact File bindings, and the absence of a current owner-selected manuscript target.

The current scholarly state is **G2 PASS / #98 COMPLETE / release gate PASS / #99 COMPLETE / no Reg. Ii 4 diplomatic correction from external collation / no current owner-selected active scholarly scope**.
