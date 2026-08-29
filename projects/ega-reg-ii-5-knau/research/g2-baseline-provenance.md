# G2 baseline working-set provenance — Reg. Ii 5 fol. 61v–63r

Status: durable project research/provenance note for the #68 → #64 working path. This file records how the review baselines are recovered; it is not a second owner of Source/File identity or of the canonical folio↔image↔PDF-page crosswalk.

## Canonical parent

The inspected parent is the corpus File already owned by `corpus/files.tsv`:

- File ID: `FILE-REG-II-5-00000129-EXCERPT`
- canonical SHA-256: `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f`

The parent bytes were re-verified against that SHA-256 on 2026-08-29 before the baseline crosswalk was applied. The historical Source identity and full archive/file metadata remain owned by the corpus tables; they are not duplicated here.

## Canonical page correspondence used

The existing Source crosswalk is authoritative for the mapping:

| PDF page | archival folio | export image | baseline working filename |
|---:|---|---:|---|
| 14 | 61v | 132 | `reg-ii-5_fol-61v_img-132_pdf-p14_baseline.png` |
| 15 | 62r | 133 | `reg-ii-5_fol-62r_img-133_pdf-p15_baseline.png` |
| 16 | 62v | 134 | `reg-ii-5_fol-62v_img-134_pdf-p16_baseline.png` |
| 17 | 63r | 135 | `reg-ii-5_fol-63r_img-135_pdf-p17_baseline.png` |

A baseline filename is only a working label. It does not become a second folio-mapping owner.

## Baseline render operation

The retained review set created on 2026-08-29 used:

- Poppler `pdftoppm 25.06.0`;
- `200 dpi`;
- PNG / RGB;
- output dimensions `1654 × 2339 px` per page;
- no crop;
- no rotation;
- no deskew;
- no contrast change;
- no AI enhancement;
- no other automatic image enhancement.

Operationally equivalent extraction:

```sh
pdftoppm -f 14 -l 17 -r 200 -png <verified-parent.pdf> <working-prefix>
```

After rendering, assign/rename the four page outputs only according to the canonical correspondence table above. Never apply this page mapping to a PDF whose bytes have not first been verified as the canonical parent File.

## Persistence and rights boundary

The four PNG baselines existed as a retained local research/review working set during the 2026-08-29 #64 inspection. They are **not committed to the public GitHub repository**.

Reason: the parent archive export is recorded as `InC/1.0` and `preservation-blocked-public-redistribution`; no additional licence, contractual permission, or other public-redistribution authority for these derived page images is currently documented. This is a redistribution/storage decision, not a provenance uncertainty.

For restart by an authorized researcher when the local PNG working set is unavailable:

1. obtain the controlled exact parent export through an authorized/local source-holding context;
2. verify its SHA-256 against `FILE-REG-II-5-00000129-EXCERPT` in `corpus/files.tsv`;
3. use the canonical Source crosswalk for PDF pages 14–17;
4. reproduce the unprocessed baselines with the render operation above;
5. compare against the documented dimensions and inspect visually before continuing #64.

The repository therefore preserves the reproducible derivation and research state without publicly redistributing protected binary derivatives. It does **not** claim that checksum + portal access is equivalent preservation of the parent export.

## Derivative-byte identity

No canonical SHA-256 requirement is established for these baseline PNGs. Their current scientific role is a reproducible unprocessed review representation derived from an exact parent File. Exact derivative-byte identity should be introduced only if a later real use makes the derivative itself a versioned/evidentiary object or requires discrimination among competing render versions.

## Current scholarly use

These baselines support #64 Checkpoint A physical/source-order inspection. The persistent working observations are in `research/g2-checkpoint-a-physical-inventory.md`; project inspection provenance is summarized in `sources/inspection-log.tsv`; the canonical next action remains in `STATUS.md`.

Processed crops/rotation/contrast derivatives are not part of this baseline record. If later #64 work uses such a transformation consequentially, #68 governs the proportional provenance needed for that real case.
