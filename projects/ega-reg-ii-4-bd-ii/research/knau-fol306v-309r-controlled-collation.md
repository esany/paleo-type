# Reg. Ii 4 Bd. II Knau fol. 306v–309r — controlled collation record

Status: **#99 ACTIVE — exact Reg. Ii 5 comparison evidence staged and pixel-inspected; controlled witness-specific collation started.**

## Role and ownership

This is the project-local canonical record for **#99 controlled collation/checking** of the independently established Reg. Ii 4 Knau witness against separately identified comparison material.

It is **not an original first-reading record and not a second owner of Reg. Ii 4 diplomatic text**. The Reg. Ii 4 diplomatic readings remain owned by the folio-local files under `transcription/first-reading/`. Project/gate state remains owned by `STATUS.md` and the project Evidence Lock.

This record owns only explicit comparison mappings/findings and any traceable consequence of that comparison.

## Mandatory comparison constraints

Before any comparison wording is entered:

1. verify the exact comparison Source/File/locus and the evidence actually inspected;
2. ensure the comparison witness is independently represented/read sufficiently for the intended collation claim;
3. map corresponding units explicitly rather than assuming line equivalence from similar wording;
4. classify agreements, variants, additions, omissions, order/structural differences, numerals/measures and source phenomena without collapsing witness identity;
5. preserve the independent Reg. Ii 4 first-reading/G3 audit trail;
6. if external comparison triggers a possible Reg. Ii 4 correction, reinspect the Reg. Ii 4 target itself and record the Reg. Ii 4 graphical basis; parallel wording alone is insufficient;
7. use legacy G2/Knau material only where its exact Source/File/locus provenance is adequate for the specific comparison claim;
8. never infer same hand from textual agreement, same record or same office context.

## 2026-09-06 #99 comparison-evidence preflight

The comparison witness identity is unchanged:

- comparison Source: `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129` — *Visitation im Amt Ziegenrück*, fol. 55v–66v;
- canonical File: `FILE-REG-II-5-00000129-EXCERPT` / `1a03ea95927-120-143.pdf`;
- canonical File SHA-256: `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f`;
- Knau comparison locus: fol. 61v–63r;
- digital locus: export images 132–135 / PDF pages 14–17.

In the current execution context an uploaded PDF named `1533-Visitationsprotokoll-Ziegenrueck-ThHStAW-EGA-Reg. Ii 5-28r-55r(2).pdf` was byte-checked locally before use. Its SHA-256 is exactly `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f`, i.e. the canonical File identity above. The export metadata page identifies `ThHStAW, EGA, Reg. Ii 5`; direct rendering confirms PDF pages 14–17 are images 132–135. Image 132 carries the `Knawe` heading and image 135 closes the Knau passage immediately before the next place heading. All four target pages are pixel-inspectable.

**Preflight result: PASS.** The prior evidence-access blocker is cleared for this execution. No legacy `132.tsv`–`135.tsv` wording was used as a substitute for witness inspection.

## Comparison entries

The Reg. Ii 5 readings below are limited to directly inspected anchors sufficient for the stated comparison claim. They are not a second diplomatic transcription owner.

| ID | Reg. Ii 4 target | Reg. Ii 5 exact locus | directly inspected Reg. Ii 5 anchor / phenomenon | class | Reg. Ii 4 reinspected? | Reg. Ii 4 changed? | finding |
|---|---|---|---|---|---|---|---|
| C99-001 | `306v-01`–`306v-10` | Source `THHSTAW-EGA-REG-II-5-STAT-VIS-00000129`; File `FILE-REG-II-5-00000129-EXCERPT`; fol. 61v; image 132; PDF p.14 | `Knawe` heading followed by the filial/lehnher formula and a short accounting block; visible recurring anchors include `laßa`, the second filial place, `wolff von ...`, `gelt...`, grain/measure entries and a final `holtzmarck...`-type account line | agreement + variant + numeral/measure difference | yes, Reg. Ii 4 image 667 / fol. 306v | no | The opening and account sequence are recognizably corresponding, but wording/orthography and quantity notation are not line-identical. Reg. Ii 5 is therefore not copied into unresolved Reg. Ii 4 cells. |
| C99-002 | `306v-11`–`307r-14` | same Source/File; fol. 61v; image 132; PDF p.14, interval between the upper account block and first prose paragraph | after the short Knau account block, Reg. Ii 5 proceeds into prose; no inspected counterpart is present there for the Reg. Ii 4 ruled separator plus `Lehnherr`, `Gotshauß zů knaw`, the Laßa/paren church-account subsections, or `Inventarium der pfarr knaw` | omission + structural difference | yes, Reg. Ii 4 images 667–668 | no | This is a substantive witness-level structural omission in Reg. Ii 5 relative to Reg. Ii 4, not evidence that the Reg. Ii 4 sections are secondary mistakes. |
| C99-003 | `307r-15`–`307v-05` | same Source/File; fol. 61v; image 132; PDF p.14, transition from account block to first prose paragraph | the first Reg. Ii 5 prose paragraph begins with a `Das dem pfarrer ...` construction corresponding to a later Reg. Ii 4 decree; the preceding Reg. Ii 4 prose/instruction sequence has no intervening inspected paragraph in Reg. Ii 5 | omission + order/structural difference | yes, Reg. Ii 4 images 668–669 | no | Reg. Ii 5 compresses/skips material before the next shared decree. Exact sub-line wording is intentionally not backfilled into Reg. Ii 4. |
| C99-004 | `307v-06`–`307v-09` | same Source/File; fol. 61v; image 132; PDF p.14, first prose paragraph | paragraph initial `Das dem pfarrer ...`; visible internal anchors include `zů knawen`, `jerlich ein ...` and the pfarrer-income context | agreement + variant | yes, Reg. Ii 4 image 669 | no | Clear paragraph-level correspondence. Reg. Ii 5 supports the structural identification of the Reg. Ii 4 decree but does not by itself resolve the unclear spans in `307v-06`–`307v-08`. |
| C99-005 | `307v-10`–`307v-19` | same Source/File; fol. 61v; image 132; PDF p.14, between first prose paragraph and following `Das wolff ...` paragraph | Reg. Ii 5 moves directly to a paragraph beginning `Das wolff ... dem pfarrer zů knawen ...`; no separate inspected counterparts intervene for the Reg. Ii 4 Laßa and kirchner paragraphs | omission + structural difference | yes, Reg. Ii 4 image 669 | no | Two Reg. Ii 4 decree units are absent as separate units from this Reg. Ii 5 sequence. This does not justify altering `307v-16` or any other Reg. Ii 4 reading. |
| C99-006 | `307v-20`–`308r-10` | same Source/File; fol. 61v–62r; images 132–133; PDF pp.14–15 | paragraph begins on 61v with `Das wolff ... dem pfarrer zů knawen ...` and continues across the folio turn; on 62r the continuation contains repeated Knau/pfarrer/land-account vocabulary and closes before the next large initial | agreement + variant + order/structural difference + numeral/measure difference | yes, Reg. Ii 4 images 669–670 | no | Strong long-form correspondence across a different physical line/folio segmentation. Reg. Ii 5 is useful for identifying the shared decree unit, but unresolved Reg. Ii 4 numerals/measures remain unresolved absent Reg. Ii 4 graphical support. |
| C99-007 | `308r-11`–`308r-18` | same Source/File; fol. 62r; image 133; PDF p.15, middle paragraph | large-initial paragraph `Vnd ob wolff ... oder seine nachkommen ...`; the paragraph continues with Knau obligations and ends before the `Von des pfarrholtz...` paragraph | agreement + variant | yes, Reg. Ii 4 image 670 | no | Direct structural correspondence with the Reg. Ii 4 `und ob wolff vom Greffendorff, vnd seine nachkommen ...` unit. No same-hand inference is made. |
| C99-008 | `308r-19`–`308r-25` | same Source/File; fol. 62r–62v; images 133–134; PDF pp.15–16 | paragraph initial `Von des pfarrholtz ...`; the paragraph runs over the folio turn and continues on 62v before the next large initial | agreement + variant + order/structural difference | yes, Reg. Ii 4 image 670 | no | Same decree topic with different physical segmentation and apparently fuller/redistributed wording in Reg. Ii 5. The parallel does not authorize filling the unresolved Reg. Ii 4 spans. |
| C99-009 | `308v-07`–`308v-17` | same Source/File; fol. 62v; image 134; PDF p.16, middle paragraph | large-initial `Das wolff ... dem pfarrer ... zů knawen ...`; internal visible anchors include the pfarrer, house/beer-use context and the closing conditional language | agreement + variant | yes, Reg. Ii 4 image 671 | no | Clear correspondence with Reg. Ii 4 decree_j. The external witness supports unit identification only; it is not used to silently reconstruct Reg. Ii 4 unclear words. |
| C99-010 | `308v-18`–`308v-22` | same Source/File; fol. 62v; image 134; PDF p.16, lower paragraph | large-initial `Von dem andern ...`; visible later anchors include `wolff ...`, `pfarrer`, `ander...` and `gebrauch... lassen` | agreement + variant | yes, Reg. Ii 4 image 671 | no | Clear correspondence with Reg. Ii 4 decree_k; no Reg. Ii 4 correction is warranted from parallel wording alone. |
| C99-011 | `308v-23`–`309r-05` | same Source/File; fol. 63r; image 135; PDF p.17, top paragraph ending immediately before new place heading | `Es soll auch ein ... zů knawen ...`-type closing decree; after a few lines the Knau unit ends and the next place heading begins | agreement + variant + structural difference | yes, Reg. Ii 4 images 671–672 | no | This is the closing shared Knau decree. Reg. Ii 4 fol. 309r is graphically obscured/overwritten, so the Reg. Ii 5 wording is not promoted into those unresolved Reg. Ii 4 lines without an independent Reg. Ii 4 graphical basis. |

## Controlled-collation consequences so far

1. The exact Reg. Ii 5 witness is now directly inspectable and the former #99 access blocker is cleared.
2. The witnesses share the Knau opening/account material and a substantial sequence of later decree units, but Reg. Ii 5 is **not** a line-for-line duplicate: it omits/condenses several Reg. Ii 4 church-account/inventory and decree units and uses different physical segmentation.
3. The comparison strongly confirms that line equivalence must not be assumed from textual similarity; paragraph/unit mappings are the safer collation level where physical lineation diverges.
4. No Reg. Ii 4 first-reading cell has been changed. In particular, the completed #98 readings `307r-02 = Greffendorff`, `307r-07 = paren` (residual `parem`) and the p-initial-only status at `307v-16` remain untouched.
5. Several external parallels could suggest completions for unresolved Reg. Ii 4 prose, numeral or measure spans, but none has been promoted because comparison wording alone is insufficient under #99 rule 6.

Further comparison should continue at the remaining sub-unit/variant level only where the Reg. Ii 5 graph can support an explicit claim beyond the paragraph mappings above; any proposed Reg. Ii 4 correction must trigger direct target reinspection first.
