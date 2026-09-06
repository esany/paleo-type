# STATUS — ThHStAW, EGA, Reg. Ii 4 Bd. II

Last checkpoint: 2026-09-06

## Project authority and root

The human owner explicitly confirmed on 2026-09-02 that Reg. Ii 4 Bd. II should currently continue as one act-oriented Project, anchored at `ACT-THHSTAW-EGA-REG-II-4-BD-II`, as an application of D-018. This current authority does not retroactively certify the complete historical D-017 wording.

On 2026-09-03 the human owner selected the **Knau passage of the Reg. Ii 4 Bd. II Ziegenrück Source** as the current manuscript/source-research target. This activates a bounded research locus; it does not redefine the Project boundary and does not assign a permanent Project→Source research-function label by itself.

## Known internal section/source node

`THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089` — *Visitation im Amt Ziegenrück*, fol. 294r–313r — is an internal Source node by canonical `part_of` relation. Its identified Knau locus is fol. 306v–309r / export images 667–672.

This is a separate material Source/witness from the Reg. Ii 5 Ziegenrück record fol. 55v–66v. Their archival extract/correspondence relation does not merge witness identity, foliation, image numbering, File provenance or diplomatic readings.

`source-uses.tsv` remains empty until an actual project-relative research function needs to be recorded. The current work target is carried by the owner-selected `active_scope`/`NEXT ACTION`, not by inferring a `principal`, `comparison` or other research function.

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

The current target is the Reg. Ii 4 Knau locus itself. No current diplomatic transcription is declared merely from the legacy Knau/G2 corpus. Any Reg. Ii 4 reading must be established against the Reg. Ii 4 Source/File/locus itself.

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

Conditions 1–4 are materially satisfied by the complete first reading, G2 PASS, merged #98 internal adjudication and stable physical line references. Condition 5 is instantiated by `research/knau-fol306v-309r-controlled-collation.md`, which explicitly identifies itself as controlled collation/checking and currently contains no external comparison entry. Conditions 6 and 7 are carried as binding record/use rules: any externally prompted Reg. Ii 4 correction requires direct Reg. Ii 4 reinspection and graphical basis, and legacy material may be used only where claim-specific Source/File/locus provenance is adequate.

This release does not retroactively alter first-reading provenance and does not make parallel wording an authority for Reg. Ii 4. No external comparison wording has yet been recorded in the #99 collation record.

## NEXT ACTION — canonical restart point

**Run #99: controlled external collation with independently established comparison material.**

First bounded actions:

1. verify the exact Reg. Ii 5 comparison Source/File/locus and current evidence access before reading it for collation;
2. verify that the comparison witness is independently represented/read sufficiently for the intended correspondence claim;
3. only then add explicit mappings/findings to `research/knau-fol306v-309r-controlled-collation.md`;
4. if legacy G2/Knau material is considered, admit it only claim-by-claim where exact Source/File/locus provenance is adequate;
5. reinspect the Reg. Ii 4 target itself before any externally prompted Reg. Ii 4 correction; parallel wording alone is insufficient.

Do not reopen #96/#97/#98 merely because external comparison reveals a variant or motivates a new Reg. Ii 4 reinspection. Preserve the independent first-reading and G3 audit trails.

## Restartability

A fresh context must identify the Reg. Ii 4 Bd. II Project, its separate Ziegenrück Source, exact File/crosswalk state, the complete six-folio first-reading representation, #97 G2 PASS, the completed #98 audit `research/knau-fol306v-309r-g3-adjudication.tsv`, the positive project-local release decision, and the separate #99 record `research/knau-fol306v-309r-controlled-collation.md`.

The current scholarly state on this branch is **G2 PASS / #98 COMPLETE / release gate PASS / #99 controlled external collation next**. No external comparison entry has yet been added. Reg. Ii 5 and adequately provenanced legacy material may now be inspected only within the controlled #99 workflow; they remain separate witnesses/checking material and cannot silently rewrite Reg. Ii 4.
