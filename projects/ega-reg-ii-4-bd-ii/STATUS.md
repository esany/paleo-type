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

- use the old Knau/G2 files only as checking/recovery material after the project-local release gate;
- for a Reg. Ii 4 diplomatic claim, inspect the Reg. Ii 4 Source/File/locus itself;
- do not treat similarity to the parallel Reg. Ii 5 transmission as witness identity;
- do not use Reg. Ii 5 or legacy wording to supply graphemes during the independent Reg. Ii 4 first reading or the systematic internal adjudication pass.

The canonical current classification of that legacy corpus is recorded in `projects/ega-reg-ii-5-knau/research/legacy-witness-provenance.tsv`.

## Evidence / crosswalk / URN state

- Exact inspected export: `FILE-REG-II-4-II-00000089-EXPORT` in `corpus/files.tsv`.
- Canonical crosswalk: fol. 306v–309r ↔ export images 667–672 ↔ PDF pages 27–32.
- The six mapped pages each have a distinct page-specific `urn:nbn:...` value in the canonical crosswalk. These values were already present when the crosswalk was first created and are not inferred from the PDF-page sequence.
- The crosswalk is intentionally partial; it does not claim page-level mapping for the full act/protocol.

## Research/gate state

The current target is the Reg. Ii 4 Knau locus itself. No current diplomatic transcription is declared merely from the legacy Knau/G2 corpus. Any new reading must be established against the Reg. Ii 4 Source/File/locus itself.

`Independent first reading` means **witness independence from external/parallel wording, not folio isolation within Reg. Ii 4**. Source-order remains the persistence and traversal order. After a difficult target graph/sign has first been observed and localized in Reg. Ii 4, directly inspected and exactly locatable internal comparanda from the same Reg. Ii 4 locus may be used for graphematic recognition. The target graph remains primary evidence; comparison must use discriminating graphical/sign features rather than expected wording or semantic plausibility. Same Source/record does not establish same hand.

The observed correspondence with Reg. Ii 5 remains a separate Source-relationship claim in `corpus/relationships.tsv`; it does not assign a permanent comparison role and must not supply graphemes for the independent first reading or internal Reg. Ii 4 adjudication.

## 2026-09-04 source-local first-reading locks

To prevent old mixed or parallel material from being reintroduced as silent reading evidence, the Reg. Ii 4 Knau task has project-local execution controls:

- `research/knau-fol306v-309r-evidence-lock.md` owns the immediate evidence/read-order/internal-comparison/legacy-release lock for this bounded first-reading task.
- `research/knau-fol306v-309r-contamination-matrix.tsv` records the concrete allowed/forbidden use classes for Reg. Ii 4 evidence, Reg. Ii 5 parallels, legacy G2/Knau material, the prior chat draft and domain context.
- `transcription/README.md` defines transcription-layer conventions and folio-local storage/representation; it does not own Project cursor, progress or release state.
- independent first readings are stored one folio per file under `transcription/first-reading/`; stable Source/File/image/PDF metadata remains in its canonical corpus/evidence owners instead of being copied into every row.

The active upload/preflight in the 2026-09-03/04 work context showed the target pages visually inspectable, including page 27 / image 667 through page 32 / image 672. Because that upload path is target-context evidence rather than repository preservation, any new execution context must re-establish staging and pixel-inspectability before source inspection.

## 2026-09-04 fol. 306v / image 667 progress

The first independent Reg. Ii 4 working pass for fol. 306v / export image 667 is stored in `transcription/first-reading/306v.tsv` as rows `306v-01` through `306v-21`.

The table is deliberately human-first: `reading_order` and `diplomatic_reading` are the leading columns; line/source structure, phenomena, epistemic status, alternatives and only consequential local notes follow. Repeated Source ID, folio/image/PDF provenance, generic creation provenance and row-level `not_collated` metadata were removed from the row surface because those facts are stable or stage-level and are recoverable from canonical corpus/evidence owners and Git history.

This is not a polished edition and not a collation result. It is a source-exact diplomatic first-reading draft from image 667 itself. Reg. Ii 5, legacy G2/Knau and the prior chat draft did not supply wording. The rows intentionally retain `unresolved`, `unclear`, visible abbreviation layers, layout/divider rows and possible source phenomena.

Main unresolved areas carried forward:

- top-account amount/measure lines `306v-04` through `306v-06`;
- the descriptor after `fuder hauers` in `306v-08`;
- the place/descriptor after `holtzmarck zů` in `306v-09`;
- exact reading of `Lehnherr:` and `Vorsteter` in `306v-12`/`306v-13`;
- the final source term/name in `306v-17`;
- the source phenomenon of the `wachs` line in `306v-19`;
- the internal phrase after `meßing wagen` in `306v-20`.

## 2026-09-05 fol. 307r / image 668 progress

The independent Reg. Ii 4 working first-reading representation for fol. 307r / export image 668 is stored in `transcription/first-reading/307r.tsv` as rows `307r-01` through `307r-19`. The exact export was re-verified against `FILE-REG-II-4-II-00000089-EXPORT`, image 668 was pixel-inspected, and the nineteen relevant physical units were represented in source order.

This is a conservative working representation, not a polished reading and not G2/G3 completion. It preserves unresolved graphemes, abbreviation signs, accounting/numeral sign classes and five physical prose lines without semantic completion. Reg. Ii 5, legacy G2/Knau and prior parallel wording did not supply the text.

Restart-relevant unresolved/problem areas carried forward include:

- `307r-02`: the upper account entry begins with a G-like target sequence, but direct comparison with the Reg. Ii 4 `Crependorff` sequence at `306v-02` does not discriminate enough to justify a `-dorff` completion;
- `307r-07`: the second church heading is securely p-initial by target-first comparison with `307r-11` `pfarr` and `307r-15` `pfarrer`, while `parem` versus `paren` remains unresolved; this is not a same-hand claim;
- `307r-08` and `307r-10`: numeral/accounting notation remains uninterpreted rather than converted into values or units;
- `307r-12` through `307r-14`: inventory entries retain unresolved internal spans;
- `307r-15` through `307r-19`: the prose note is represented line-by-line with unresolved spans rather than syntactic reconstruction.

## 2026-09-06 fol. 307v–309r / images 669–672 progress

The remaining independent Reg. Ii 4 working first-reading representations are now stored in source order as:

- `307v.tsv`: rows `307v-01` through `307v-22`;
- `308r.tsv`: rows `308r-01` through `308r-25`;
- `308v.tsv`: rows `308v-01` through `308v-25`;
- `309r.tsv`: rows `309r-01` through `309r-05`.

The exact Reg. Ii 4 export and folio/image/PDF mapping were rechecked for this execution, and images 669–672 were pixel-inspected before the local working files were persisted. All 77 relevant visible units from these four folio sides are represented. On 309r only the five units belonging to the Knau locus are included; the following Ziegenrück heading is outside the bounded locus and is excluded.

The representation remains deliberately conservative. `working`/`unresolved` spans are visible, numeral/measure/accounting contexts are not silently converted into values, and no same-hand claim follows from same-witness recurrence. Direct target readings of `Greffendorff`/`greffendorff` occur on later Reg. Ii 4 folios, but they have **not** been used to silently revise `307r-02`; that consequential cross-locus question belongs to the systematic #98 internal adjudication.

The full authorized locus fol. 306v–309r is therefore now represented as an independent Reg. Ii 4 **working first-reading representation**. This does **not** by itself establish G2 completeness, G3 completion or external-witness release.

The legacy/parallels release gate is still closed.

## NEXT ACTION — canonical restart point

**Run #97: the G2 completeness audit over the complete Reg. Ii 4 Knau first-reading representation, fol. 306v–309r / images 667–672.**

Audit discipline:

1. traverse all six folio TSVs in source order and verify that every relevant visible physical unit is represented with stable folio-local line references;
2. verify folio/image boundaries, headings, lists, prose/continuations, abbreviations, numeral/accounting/measure signs, source phenomena and explicit uncertainty without semantic filling;
3. verify that 309r ends at the actual Knau boundary and does not absorb the following Ziegenrück heading;
4. verify that no Reg. Ii 5, legacy G2/Knau or parallel wording entered the independent Reg. Ii 4 representation;
5. derive any human-readable whole-locus witness view deterministically from the folio-local data plus canonical source metadata rather than creating a second manually edited transcription truth;
6. if G2 passes, record that state in the canonical owners and proceed immediately to #98 systematic internal palaeographic/philological adjudication; if it does not, repair the actual owning folio/source-state record and rerun the audit;
7. keep Reg. Ii 5 and legacy G2/Knau closed as textual comparison/wording evidence through #98 and until the project-local release gate is explicitly satisfied.

## Restartability

A fresh context must identify the Reg. Ii 4 Bd. II Project, its separate Ziegenrück Source, exact File/crosswalk/URN state, the owner-selected Knau locus fol. 306v–309r / images 667–672, and all six persisted folio-local working first-reading files: `306v.tsv`, `307r.tsv`, `307v.tsv`, `308r.tsv`, `308v.tsv`, `309r.tsv`.

The current scholarly execution state is **#97 G2 completeness audit pending**; there is no further folio cursor inside the bounded first-reading sequence. Internal Reg. Ii 4 comparanda remain available for later #98 target-first adjudication, but Reg. Ii 5, legacy G2/Knau, domain context and unadjudicated prior drafts must not supply manuscript wording before the release gate is satisfied.
