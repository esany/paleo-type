# Reg. Ii 4 Bd. II Knau fol. 306v-309r — evidence lock and contamination control

Created: 2026-09-04
Reconciled: 2026-09-06

## Authority and scope

This project-local file records the execution lock for the owner-selected current task in `projects/ega-reg-ii-4-bd-ii/STATUS.md` and `project.yml`.

It does not create a new Project, Source, Project->Source use, research priority or textual-dependence claim. It only constrains how the already-authorized Reg. Ii 4 Bd. II Knau first reading is executed, internally tested and later compared.

Current bounded target:

- Project: `ega-reg-ii-4-bd-ii`
- Source: `THHSTAW-EGA-REG-II-4-BD-II-STAT-VIS-00000089`
- Historical locus: Knau passage, fol. 306v-309r
- Digital locus: export images 667-672 / PDF pages 27-32
- Current execution state: G2 PASS; #98 systematic internal adjudication COMPLETE; project-local gate RELEASED for #99 controlled collation
- Mode: controlled external collation/checking may begin only under the separate #99 collation record and the constraints below

## Evidence state for the active work context

Canonical repository state already records the exact inspected export as `FILE-REG-II-4-II-00000089-EXPORT` and the crosswalk fol. 306v-309r <-> export images 667-672 <-> PDF pages 27-32.

The 2026-09-03/04 active target context additionally had the uploaded PDF `1533-Visitationsprotokoll-Ziegenrueck-ThHStAW, EGA, Reg. Ii 4 Bd. II-294r-313r.pdf` visually inspectable. Its relevant visible pages show:

| folio | PDF page | export image |
|---|---:|---:|
| fol. 306v | 27 | 667 |
| fol. 307r | 28 | 668 |
| fol. 307v | 29 | 669 |
| fol. 308r | 30 | 670 |
| fol. 308v | 31 | 671 |
| fol. 309r | 32 | 672 |

This is a target-context visual-evidence PASS for that work context only. If the work context changes, staging and pixel-inspectability must be re-established for the same evidence object instead of relying on this prose.

For the 2026-09-05 fol. 307r execution, the active context re-verified the staged PDF against the canonical SHA-256 for `FILE-REG-II-4-II-00000089-EXPORT` and pixel-inspected image 668 / PDF page 28 before transcription.

For the 2026-09-06 remaining-folio execution, the same canonical Reg. Ii 4 export and folio/image/PDF mapping were rechecked and images 669–672 were pixel-inspected before the prepared local first-reading files were persisted. The exact first-reading row counts are 22 / 25 / 25 / 5 for 307v / 308r / 308v / 309r respectively; 309r stops at the Knau boundary before the following Ziegenrück heading.

For the 2026-09-06 G2 audit, the full image set 667–672 remained directly inspectable and was checked against all six folio-local TSV partitions and the canonical crosswalk.

For the 2026-09-06 #98 systematic internal adjudication, consequential targets were directly reinspected against the exact Reg. Ii 4 images and exactly locatable same-witness anchors. The project-local audit `research/knau-fol306v-309r-g3-adjudication.tsv` records all 34 consequential loci/clusters with no pending row. The pass retained unresolved and specialist-review outcomes where the internal evidence did not decide, did not infer values from accounting/measure signs, and did not open Reg. Ii 5 or legacy wording as textual evidence.

## Internal Reg. Ii 4 comparison rule

Witness independence means independence from external/parallel wording; it does **not** require folio isolation inside the same Reg. Ii 4 witness.

For a difficult locus:

1. inspect and localize the target graph/sign in Reg. Ii 4 first;
2. classify the actual problem before comparison where useful: grapheme, abbreviation, numeral/accounting sign, segmentation, source phenomenon, possible hand issue, etc.;
3. only then inspect directly and exactly locatable internal Reg. Ii 4 comparanda anywhere in fol. 306v-309r when they are relevant to that problem;
4. compare discriminating graphical/sign features, including evidence that fails to discriminate, rather than searching for or copying an expected word;
5. keep `same witness/source` distinct from `same hand`; hand relevance is a separate palaeographic claim;
6. keep lexical, onomastic, metrological and historical context downstream of graphically viable candidates;
7. if a consequential comparison materially supports, rejects or fails to decide a reading, preserve the exact anchor and concise reasoning in the owning research/transcription record; do not build a general survey register merely because direct inspection was broader.

A later folio may therefore provide an internal comparison anchor for an earlier difficult graph without becoming wording authority for that earlier locus.

## Contamination lock

The following separation remains mandatory before and during #99. Release authorizes controlled comparison; it does not collapse evidence classes.

| Material | Status before external comparison release | Allowed use | Forbidden use |
|---|---|---|---|
| Reg. Ii 4 Bd. II, Source `...00000089`, images 667-672 | primary evidence / same-witness internal comparison space | target-first visual inspection; physical-line inventory; diplomatic first reading; uncertainty marking; exact internal graphematic/sign comparison after target observation | expected-word copying; semantic completion of unread graphs; treating same source/record as same-hand proof |
| Reg. Ii 5 Ziegenrück material | quarantined parallel material | method warning; controlled collation after release gate | wording source for original first reading; silent grapheme supply; same-hand assumption |
| Legacy G2/Knau files and old TSV/apparatus/palaeography | provenance-controlled recovery/checking material after release | checking/collation only where exact Source/File/locus provenance is adequate for the specific claim | promotion as Reg. Ii 4 reading; silent import; automatic witness attribution |
| Prior chat draft of image 667 | unadjudicated local draft | cursor memory and risk signal only | canonical line text unless each row is reinspected against image 667 |
| Early-modern visitation/domain knowledge | contextual hypothesis/control | generate questions; test/rank graphically viable candidates after source inspection | replace unread graphemes; normalize diplomatic spelling; infer names/amounts as manuscript text |

## Release gate for legacy/parallels

Reg. Ii 5 or legacy Knau/G2 material may be opened for **textual comparison/collation** only after all of the following are true for the current Reg. Ii 4 locus:

1. fol. 306v-309r has a complete independent Reg. Ii 4 first-reading representation in source order;
2. the G2 completeness audit has established that every relevant visible source unit is represented and consequential uncertainty/source phenomena remain discoverable;
3. the systematic internal palaeographic/philological pass over consequential `working`/`unresolved` loci is complete for the current roadmap, with unresolved results retained where internal evidence does not decide;
4. physical line references are stable enough to cite and compare;
5. the comparison record identifies itself as collation/checking, not as original first reading;
6. any later promoted Reg. Ii 4 correction explains the inspected Reg. Ii 4 graphical basis and does not rely on parallel wording alone;
7. legacy material is used only where its exact Source/File/locus provenance is adequate for the specific comparison claim.

Gate evaluation after #98 merge and #99 record setup:

- condition 1: **met** — complete six-folio working first-reading representation present;
- condition 2: **met** — #97 G2 completeness audit PASS;
- condition 3: **met** — #98 systematic internal adjudication is merged on `main`; all 34 consequential loci/clusters have an adjudicated or explicit specialist-review result and no pending item remains;
- condition 4: **met** — folio-local physical line references are sequential, unique and source-order stable;
- condition 5: **met** — `research/knau-fol306v-309r-controlled-collation.md` explicitly identifies itself as the #99 controlled collation/checking record, not an original first-reading or diplomatic-text owner, and currently contains no external comparison entry;
- condition 6: **met as a binding #99 record rule** — the collation record requires direct Reg. Ii 4 target reinspection and a Reg. Ii 4 graphical basis before any externally prompted Reg. Ii 4 correction can be promoted; parallel wording alone is explicitly insufficient;
- condition 7: **met as a binding use/provenance rule** — legacy material may enter the collation record only where exact Source/File/locus provenance is adequate for the specific claim; no legacy comparison entry has yet been made.

**Gate decision: RELEASED for #99 controlled external collation.**

This release permits comparison material to be inspected only inside the #99 workflow after the exact comparison Source/File/locus and current evidence access are verified. It does not make Reg. Ii 5 or legacy wording evidence for the original Reg. Ii 4 first reading, does not authorize silent correction of Reg. Ii 4, and does not establish same-hand or textual-dependence claims in advance.

## First-reading representation

First-reading data are stored one archival folio per file under `transcription/first-reading/`. These files are work/data partitions of the authorized Reg. Ii 4 first-reading representation; their directory hierarchy does not create a new scholarly parent entity or a second owner of Project state.

Stable scope/provenance facts — canonical Source ID, folio-to-export/PDF mapping, File identity and generic direct-inspection provenance — are resolved from the Project/corpus/evidence owners and are not repeated on every row. The row table is ordered around the changing scholarly information:

1. `reading_order`;
2. `diplomatic_reading`;
3. `line_ref`;
4. `region` where relevant;
5. `source_phenomena`;
6. `research_status`;
7. graphically viable `alternatives`;
8. separate `abbreviation_layer` / `editorial_supply` where needed;
9. consequential local `evidence_note`.

When an internal same-witness comparison materially affects a consequential reading, `evidence_note` may carry the exact comparison locus and concise discriminating reason. Routine direct inspection that does not affect a decision need not be serialized as a separate survey dataset.

The independent first-reading files do not carry a mutable `collation_status` column. External comparison belongs in the separate #99 collation record so that opening a parallel witness cannot silently redefine first-reading provenance.

A fluent full line with hidden uncertainty is worse than a narrower visible unresolved span.

## First-reading progress

The complete authorized locus is represented by:

- `306v.tsv`: `306v-01`–`306v-21`;
- `307r.tsv`: `307r-01`–`307r-19`;
- `307v.tsv`: `307v-01`–`307v-22`;
- `308r.tsv`: `308r-01`–`308r-25`;
- `308v.tsv`: `308v-01`–`308v-25`;
- `309r.tsv`: `309r-01`–`309r-05`.

The 309r file ends at the Knau boundary and excludes the following new Ziegenrück heading. Working/unresolved spans remain explicit; numeral/measure/accounting contexts are not silently converted into values. Later direct Reg. Ii 4 target forms of `Greffendorff`/`greffendorff` are present. During #98, those forms were used only as internal comparison anchors; `307r-02` was promoted to working `Greffendorff` because direct reinspection established the relevant graphical architecture on the 307r target itself, with the earlier `306v-02 Crependorff` negative-control history retained.

## 2026-09-06 #97 G2 completeness audit

The G2 audit passed after direct image/TSV traversal of all six folio sides. The audit established:

- 117 relevant source units represented in source order, with folio counts `21 / 19 / 22 / 25 / 25 / 5`;
- sequential, unique and stable folio-local line references;
- common ten-column first-reading structure;
- visible headings, lists, prose/continuations, abbreviation signs, numeral/accounting/measure problem classes and source phenomena retained;
- uncertainty remains explicit and no missing source unit was masked by semantic completion;
- the 309r boundary is correctly cut before the next Ziegenrück heading;
- no Reg. Ii 5 / legacy G2/Knau wording was used to fill the Reg. Ii 4 representation.

The human-readable whole-locus presentation `transcription/derived/knau-fol306v-309r-first-reading.md` is explicitly non-canonical and deterministically derived from the six folio TSVs. It is not a second transcription truth.

## 2026-09-06 #98 systematic internal adjudication

The systematic internal G3 pass is complete. Its 34-locus/cluster audit records exact internal anchors, positive and negative discriminators, adjudication outcomes and any specialist-review condition. No pending item remains.

Consequential diplomatic re-adjudications are persisted in their folio owners: `307r-02` is working `It̄ Greffendorff`, `307r-07` is working `Kirchhauß zů paren,` with `parem` retained as a residual graphical alternative, and `307v-16` is narrowed to a p-initial unresolved place form. Remaining unresolved outcomes stay explicit and do not constitute an unfinished systematic #98 task.

## Current execution state

Next executable action:

> Run #99 controlled external collation. First verify the exact comparison Source/File/locus and current evidence access, then add comparison findings only to `research/knau-fol306v-309r-controlled-collation.md`. Reinspect Reg. Ii 4 itself before any externally prompted principal-witness correction, and use legacy material only where claim-specific provenance is adequate.

The first-reading and G3 records remain frozen/traceable independent evidence layers. #99 may discover agreements, variants or reasons to reinspect Reg. Ii 4, but external wording never becomes a substitute for the Reg. Ii 4 graph.

## Invalidation triggers

Re-run the evidence prerequisite if:

- the active work context no longer has the uploaded PDF or render/crop set for a new direct source-inspection claim;
- the inspected image does not match `FILE-REG-II-4-II-00000089-EXPORT` / image 667-672;
- a later corpus/crosswalk correction changes the folio/image/PDF-page mapping;
- visual inspectability fails or a different derivative is substituted.

New model uncertainty alone is not an invalidation trigger. It should narrow the unresolved locus or trigger qualified review, not send the work back into retrieval/governance loops.
