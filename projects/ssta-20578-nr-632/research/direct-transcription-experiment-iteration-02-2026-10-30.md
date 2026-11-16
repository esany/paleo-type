# Nr. 632 — Direct transcription experiment, failed first pass and iteration 2 (2026-10-30)

**Classification:** bounded AI-assisted experiment/review evidence, **not canonical diplomatic transcription**, G2 acceptance, independent specialist validation or a new Project NEXT ACTION. Source and Project truth remain with their existing owners.

## Provenance and work boundary

- Project: `projects/ssta-20578-nr-632/`; Source: `SSTA-ARCHIVIALE-EDD69AA1`.
- Exact inspected compact 135-page PDF: `FILE-SSTA-20578-NR632-COMPACT-PDF-20261029`, SHA-256 `8cc44ccf25b78a1174fa78da26f617fb1af39cea4ccb6999c2a616041a5d1a7f`, checked directly again in this execution context.
- Source-owned digital crosswalk: PDF S. 1–135 ↔ provider images 0001–0135. Neither number denotes archival foliation, physical carrier or internal documentary identity; image L/R is a viewing-region convention.
- The current Human request authorizes **one bounded experimental relecture and documentation**. No whole-archive G2 scope, new Project purpose, edition, next iteration or autonomous loop is inferred. `project.yml` and `STATUS.md` are not altered.

## Audit of the earlier direct-transcription attempt (candidate only)

The earlier chat-generated `Lehn_Knau_1704-1781_Teilarbeitsfassung_UNVOLLSTAENDIG.txt` gave partial readings on PDF S. 1–8 and mostly `[noch nicht transkribiert]` for 9–135. The derived PDF was only a presentation of that failed/partial attempt. It had no full physical-line coverage, systematic palaeographic evaluation, or scientific G2 completion.

**Concrete address error:** the old TXT called PDF S. 1 `Aufnahme 0021`, and similarly used 0022 etc. These are visible microfilm frame-counter values; the verified provider image for PDF S. 1 is **0001**. The mismatch compromised the reported source locator. Do not silently reuse old text or labels.

**Structural failure:** sequential PDF views were handled as if they were independent page texts; the pre-existing S2/view map already shows repeat views (0003/0004, 0103/0104, 0132R/0134L) and the Human-confirmed single oversized charter behind 0133–0135. The Human corrections for 0006L/R, 0008L/R and 0131R/0132L remain binding to their exact evidence limit. The discarded 0094–0097 ↔ later-copy chain remains discarded absent new independent collation.

## Executed iteration 2

**Question:** Can already mapped, important text zones be re-read directly from the exact PDF and shown with conservative uncertainty without mistaking an image for a manuscript/document boundary?

**Fresh technical P:** PDF hash verified against `corpus/files.tsv`; 135 PDF pages, each containing a 2500-pixel-wide image. The image areas of PDF S. 1, 2, 3, 4, 6, 7, 8, 42, 61, 69, 71, 102, 115, 131–135 were re-extracted as non-generative viewing crops. The limited **new visual reading targets** are 0001R, 0002R, 0042R, 0061R, 0069R, 0071R, 0102R and 0115L, not the whole 135-page set. This pass did not directly reopen the original JPEG files independently of the hash-identical compact PDF.

**Locally visible textual islands (L, AI working readings, not specialist adjudication):**

| Exact PDF/provider locus | Direct reading/test | Bound |
|---|---|---|
| 0001R | `Acta Privata`, `No. IX`, `Die Lehen, und gesamte Hand ...`, `Lehns-Cantzley`, `de Anno 1704`, `bis ad Annum 1744` | cover has uncertain words, separate modern printed repository sticker |
| 0002R | `Von Gottes gnaden Wir Moritz Wilhelm, Postu- / lirter Administrator des Stiffts Naumburg ...` | beginning only; main paragraph not represented |
| 0042R | marginal `Lehen-Briefs-Concept`; major `Wir Friedrich Augustus` opening | written term `Concept` does not independently determine transmission stage |
| 0061R | decorated `Wir Endes unterschriebene ...` opening and `Revers` marginal label | no demonstrated concrete relation to adjacent Lehnbrief |
| 0069R | `Vollmacht` marginal heading and `Ich` opening | body not read in full |
| 0071R | `Lehn-Schein`, `Den 9ten Januarii 1744`, chancery closing | middle/person names unresolved |
| 0102R | `Dresden den 1. April 1760`; `Daß vorstehende Abschrifft ... original- / supplicat` | written copy/original claim, no photo-to-template identification |
| 0115L | end formula `Ratification sigillando et sub- / scribendo ... den 22. Nov. Anno 1678` | transmitted text date, not carrier date; signatures unresolved |

Direct text portions remain deliberately partial: `[in dieser Iteration nicht transkribiert]` means not attempted, not physically illegible. Some working readings themselves need palaeographic recheck. The file-backed user-facing working PDF includes source crops beside each excerpt but is an **external derived artifact**, not imported canonical research state.

## Learnings and next bounded research test

1. The first experiment failed above all in **evidence/ownership activation**: it did not use the documented S2 object/view work before touching S3 transcription.
2. **Microfilm counter ≠ provider image ≠ PDF page ≠ archival folio**; use the digital crosswalk as the authoritative locator layer.
3. **One visible photo ≠ one documentary object**. Repeat views and overlays must be respected before line assignment.
4. Some text islands, particularly 0102R, are comparatively readable. No whole-archive statement of illegibility follows from model difficulty.
5. Distinguish source `unclear` from `gap` and from **unattempted work**. Large brackets do not complete a physical transcription.
6. S3/G2 must remain **locus-scoped physical line representation**, with S4 graph tests and a rebuildable human view, not a 135-page placeholder file.
7. `Abschrift` / `Original Supplicat` are source-wording observations; concrete Vorlage/copy chains require independent collation.

**Tooling gaps, problem-specific rather than pre-authorized implementation:** (a) crosswalk-driven locator display rather than film counter, (b) S2-linked view/overlap references, (c) region+physical-line anchored transcription work surface with separately typed uncertainty and unattempted status, (d) before/after reading evidence diff, (e) reusable data→PDF renderer and rendering/legibility QA. Existing image crop/render tools are adequate for this bounded test. Generic OCR/HTR, an auto-segmenter or another planner are **not justified merely by this experiment**.

**Ceiling:** This iteration produces eight source-linked **excerpts**, not page-complete S3, G2, G3, independent specialist review, an edition or a revision of the Project cursor. A substantively more discriminating later test, only if authorized, would fully represent **one truly bounded physical text region** with physical-line IDs, S4 check evidence, uncertainty and generated view. No automatic next iteration is created.

## Existing owners preserved

`GOVERNING_OBJECTIVE.md`, `AGENTS.md`, `methodology/historical-source-workflow.md`, `methodology/transcription-guidelines.md`, `methodology/research-gates.md`, existing Project `project.yml`/`STATUS.md`, its S2/object-view and content/function, chronology and source-criticism research files, and `corpus/source-data/SSTA-ARCHIVIALE-EDD69AA1/digital-crosswalk.tsv`. This note reports an experiment; it cannot supersede any of those owners.

**Persistence disposition:** non-canonical research experiment note on a separate review branch. No changes to canonical Project status, source graph, transcriptions, gates or owner-selected current scope.
