# G2 baseline working-set provenance — Reg. Ii 5 fol. 61v–63r

Status: durable project research/provenance note for the #68 → #64 working path. This file records exact parent identity, the reproducible review baselines and the current recovery/access result. It is not a second owner of Source/File identity or of the canonical folio↔image↔PDF-page crosswalk.

## Canonical parent

The inspected parent is the corpus File already owned by `corpus/files.tsv`:

- File ID: `FILE-REG-II-5-00000129-EXCERPT`
- canonical SHA-256: `e989fe614c715e417e3586e29628d67d274964f195b3f1e66a8682bfcde54f6f`

On 2026-08-30 a newly supplied copy named `1533-Visitationsprotokoll-Ziegenrueck-ThHStAW-EGA-Reg. Ii 5-28r-55r(1).pdf` was SHA-256 verified as byte-identical to this canonical File. The supplied filename is therefore local provenance only and does not redefine File identity or coverage.

PDF metadata of the verified parent records title `Registratur für die Superintendenz Neustadt an der Orla (Auszug)`, subject `120-143`, creator `mets-printer v0.1`, 25 pages, and provider file object `stat_file_00000033` on the export metadata page. Provider file identity is distinct from the Source/provider record `stat_visitation_00000129` and from the local canonical `file_id`.

## Canonical page correspondence used

The Source crosswalk remains authoritative:

| PDF page | archival folio | export image | baseline working filename | directly observed provider image label |
|---:|---|---:|---|---|
| 14 | 61v | 132 | `reg-ii-5_fol-61v_img-132_pdf-p14_baseline.png` | `stat_derivate_00000416:/ThHStAW_RegIi_5_0130.tif` |
| 15 | 62r | 133 | `reg-ii-5_fol-62r_img-133_pdf-p15_baseline.png` | `stat_derivate_00000416:/ThHStAW_RegIi_5_0131.tif` |
| 16 | 62v | 134 | `reg-ii-5_fol-62v_img-134_pdf-p16_baseline.png` | `stat_derivate_00000416:/ThHStAW_RegIi_5_0132.tif` |
| 17 | 63r | 135 | `reg-ii-5_fol-63r_img-135_pdf-p17_baseline.png` | `stat_derivate_00000416:/ThHStAW_RegIi_5_0133.tif` |

The provider labels above are visibly printed below the corresponding manuscript images in the verified export. They are recorded as provider derivative/TIFF locators, **not as stable image URNs**. No `urn:` identifier was established from this PDF, so the canonical `stable_image_urn` cells remain empty.

## Baseline render operation

The review set uses:

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

Operational command:

```sh
pdftoppm -f 14 -l 17 -r 200 -png <verified-parent.pdf> <working-prefix>
```

Never apply this page mapping to a PDF whose bytes have not first been verified as the canonical parent File.

## 2026-08-30 exact recovery verification

Re-running the documented Poppler command against the newly supplied byte-identical parent reproduced the earlier retained review set exactly at the byte level:

| folio | PDF page | dimensions | SHA-256 of Poppler 25.06.0 / 200-dpi baseline |
|---|---:|---|---|
| 61v | 14 | 1654 × 2339 | `cf573a4e0317715d231cd6555139a12fa0ea84d886d6856feeabe65e043b5c45` |
| 62r | 15 | 1654 × 2339 | `05c3cf88ae010e89d5ce0b904a516415e076c53c708a7ed5c3dbecb6e67efe4c` |
| 62v | 16 | 1654 × 2339 | `00191662d00d38e58bd02ef3b6ae0ff0353030d7e19169380e84dcc3b08e6487` |
| 63r | 17 | 1654 × 2339 | `9244b87dfa07eab5fd93923a266399a15c84dc793b958b7c6e1146bdaafb25a3` |

These hashes are useful fingerprints for identifying this specific historical Poppler working set. They do **not** establish the generic false invariant that every conforming renderer must produce byte-identical PNGs. The scientific invariant remains exact parent + exact page + disclosed rendering method/parameters → reproducible visual inspection.

## Persistence, rights and research-ready access

The parent archive export is recorded as `InC/1.0`; this rights statement is not itself a public-redistribution licence.

On 2026-08-30 the repository was changed from public to **private**, and the human project owner explicitly authorized controlled storage of this exact research source in the private project repository. This resolves the project's prior governance uncertainty about whether controlled private-repository storage is intended for this source. It does **not** create or assert public redistribution authority.

Canonical intended parent repository path:

`corpus/source-files/THHSTAW-EGA-REG-II-5-STAT-VIS-00000129/original/1a03ea95927-120-143.pdf`

A directory-level control note exists at the corresponding `original/README.md`. The exact parent PDF binary is **not yet verified present at that repository path**. Therefore do not change `corpus/files.tsv:storage_status` to `repo-preserved` until the binary exists there and its SHA-256 has been re-verified.

For direct visual research, the four baseline images are now attached to private Issue #84. GitHub exposes them as private `private-user-images` resources. On 2026-08-30 a fresh attachment URL was obtained from a newly fetched #84 issue comment and successfully retrieved through the connected authorized GitHub work context. This is the concrete fresh-context access test required by #68/#78: the active source pixels can be recovered without relying on the old chat or another manual source upload.

Current state:

- **identity/provenance:** durable and PASS;
- **reproducible derivation:** durable and PASS;
- **controlled private-repository storage authority:** PASS / explicitly owner-authorized;
- **four private #84 baseline image attachments:** PRESENT;
- **fresh-context visual access via private #84 attachment route:** PASS / retrieval route tested 2026-08-30;
- **exact parent PDF binary at reserved repository path:** PENDING / preservation only, nonblocking for #64 Checkpoint B.

The four historical SHA-256 values above remain fingerprints of the exact locally reproduced Poppler baselines. The Issue attachments were not each independently re-hashed as part of the access test, so attachment availability must not be described as a fresh four-file byte-identity verification.

This demonstrates why the project distinguishes two layers:

```text
research-ready visual access
→ actual images openable by the current/fresh authorized research context

exact parent preservation
→ canonical parent binary retained and checksum-verifiable at the durable preservation location
```

The first now passes for fol. 61v–63r. The second remains open and must not block the active scholarly semantic-loss audit.

An identifier, repository path, README or render recipe alone is still not considered equivalent to actual inspectable source pixels.

## Derivative-byte identity

No generic canonical SHA-256 requirement is introduced for page renders. Exact derivative hashes are retained here only because the real recovery fixture demonstrated value in identifying whether the same historical working set had been re-created.

If later rendering uses another implementation/version while preserving the intended visual evidence, byte differences alone do not imply scholarly difference.

## Current scholarly use

The baselines support #64 Checkpoint A/B work. On 2026-08-30 they were used for the explicit source↔anchor structural validation recorded in `research/g2-checkpoint-a-physical-inventory.md`; the private #84 attachment route now supplies restartable visual access for the same active slice.

Processed crops/rotation/contrast derivatives are not part of this baseline record. If later source work uses such a transformation consequentially, #68 governs proportional provenance and the unprocessed representation remains available for critical comparison.
