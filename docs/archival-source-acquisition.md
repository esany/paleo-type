# Archival source acquisition: SStA pilot

This bounded implementation acquires individual JPEGs from the Sächsisches Staatsarchiv. It uses the archive's actual `files.json` list and writes only to a configured external source destination. It does not create Corpus or Project records, search for sources, infer research roles, or treat CI artifacts as preservation.

## Human-facing Dresden skill contract — corrected 2026-10-27

The **`savesax` user-facing skill** applies to **Hauptstaatsarchiv Dresden** records at the exact HTTPS origin `https://www.archiv.sachsen.de`. The historical/provider test fixtures from other SStA branches are evidence of the shared adapter, **not** evidence that the Dresden-specific Human-facing skill has been validated or extended to those branches. An exact hostname and HTTPS-scheme check is required; an attacker-supplied URL merely containing that text is not authoritative.

For this known host, use ordinary direct archive HTTP, **not TinyFish or a metered browser agent** to discover the viewer, thumbnails, image IDs, `files.json` or fullsize paths. Browser mediation is not the default; a text extractor returning `empty_content` for a JPG does not test JPG bytes.

The viewer is already known. Thumbnail items (including the currently active `.digitalisat-viewer-thumbnail.loaded.active`) are **navigation**, not the preservation files. The OpenSeadragon display uses `.openseadragon-wrapper` / `.openseadragon-container` (initial page HTML may show only `#openseadragon`). A thumbnail preview `src` in the form:

```text
/digitalisate/<GUID>/fullsize/../preview/<LISTED-NAME>.jpg
```

identifies the displayed filename. Use the **verified same GUID and that exact filename** to form the true download target:

```text
https://www.archiv.sachsen.de/digitalisate/<GUID>/fullsize/<LISTED-NAME>.jpg
```

The existing `SaechsischesStaatsarchivProvider.image_url(guid, filename, "fullsize")` already constructs that target. Do not fetch the preview image, canvas image or screenshot as a substitute. The thumbnail's `active` class marks **one** selected item, not the complete list. For **completeness**, obtain `/digitalisate/<VERIFIED-DIGITALISAT-GUID>/files.json` and validate its actual `name`, `typ`, `istEinzelbild` entries, count, uniqueness and order. Never enumerate unlisted intermediate names or infer that catalogue GUID necessarily equals digitalisat GUID. Preserve uncertainty about unsupported `istEinzelbild=false`, tile and DZI entries; no silent filtering, and no blind reinterpretation.

The intended outcome is the **publicly downloadable high-resolution online JPEG**, exactly as a Human can download it manually. No extra archival master-on-request step or speculative rights/licence debate is a prerequisite for the ordinary acquisition. This does not decide subsequent publication permissions.

**Completion conditions:** use verified catalogue/source metadata and exact provider file list; preflight a controlled durable external target with observe/stop/restart fitness; dry-run against actual filenames; download complete JPEG **bytes** with an evidenced online high-resolution route; verify payload integrity and actual image pixels, not only URL construction; persist after each verified image; resume without replaying verified files; finalize `QUELLENINFO.json`, `QUELLENINFO.txt`, `SHA256SUMS.txt`, `ACQUISITION_STATE.json` before reporting `complete`. `status` is read-only. CI, fixture comparison, a single image and a remote URI are not a preserved source package. Missing access is a specific **runtime/HTTP resource limitation**, not authority to replace the original research outcome.

**Known real-list regression:** For Hauptstaatsarchiv Dresden, `10001 Ältere Urkunden, Nr. 01739` (`8bdce320-0ce6-4ddb-b37a-eed8fe52cb94`), the officially observed list on 2026-10-27 contains exactly two JPEG entries in provider order `0002`, `0001`; ordered download names are `0001.jpg`, `0002.jpg`. `0003.jpg` must not be invented. This is *file-list evidence*, not proof of successful image-byte acquisition. The existing Nr. 632, Nr. 754 and Oppurg fixtures remain valid **adapter** checks at their evidenced envelope, not proof of Dresden skill scope or external archival preservation.

## Observed SStA path

1. Read the GUID from the archive record URL or supplied metadata.
2. Fetch `https://www.archiv.sachsen.de/digitalisate/<GUID>/files.json`.
3. Validate every `name`, `typ` and `istEinzelbild` entry; sort by `name`.
4. Form one `download.jsp` or `fullsize/<name>.jpg` URL per listed image.
5. Acquire the images directly into the configured external root.
6. Persist restartable progress after each newly verified image.
7. Write the final manifest/checksum set only after every expected image is verified.

The JSON list, not a supplied image count or a Viewer canvas, determines the image names. A supplied `image_count` is an optional consistency check. The adapter fails on unsupported or duplicate entries; it does not silently skip them. Tile/DZI variants are not implemented by this single-image adapter.

The generic acquisition core sees only a normalized list of image specifications. SStA fields and routes stay in the provider adapter.

## Metadata input

Supply JSON with `archive`, `fonds`, `signature`, `title`, `date_label`, `guid` and `page_url`. Optional fields include `archive_code`, `name_key`, `classification_path`, `rights_status` and `image_count`.

For chat-driven runs, pass the same JSON on standard input with `--metadata -`. This avoids creating a metadata sidecar file. Source image files are still written only to the configured external root.

## Runtime / destination gate

A productive full acquisition starts only after an intended external destination/runtime is shown fit for the operation's durability and control needs. At minimum, successful task-relevant files plus `ACQUISITION_STATE.json` must persist across an ordinary process/network interruption. The executing context must have adequate observability and any material stop/containment limitation must be known before start.

`Can execute code` is not a runtime-fit result. Repository/worktree paths and disposable CI runner/artifact storage are not valid default preservation destinations. The former GitHub Actions live-acquisition workflow has been removed; repository CI remains for deterministic checks, not as the production acquisition path merely because it is available.

## Commands

Preview the plan using the live SStA list:

    python tools/archival_source_acquisition.py \
      --metadata <metadata.json> \
      --output-root <external-literature-root> \
      --route download \
      --dry-run

Use a previously captured `files.json` response for offline planning:

    python tools/archival_source_acquisition.py \
      --metadata <metadata.json> \
      --file-list <files.json> \
      --output-root <external-literature-root> \
      --dry-run

Read existing acquisition state without fetching or mutating anything:

    python tools/archival_source_acquisition.py \
      --metadata <metadata.json> \
      --output-root <external-literature-root> \
      --status

Omit `--dry-run` to acquire the listed images after the runtime/destination gate passes. `--route fullsize` selects the direct viewer image route. The default `download` route uses the archive's individual download endpoint. `--file-list` affects planning only; actual image retrieval still needs network access.

## Restartable progress and completion

The tool writes successful images directly into the external package and atomically maintains `ACQUISITION_STATE.json`.

A normal interrupted run remains explicitly `partial-restartable`; an operator interruption remains `cancelled-restartable`. On an authorized repeat/resume against the same source/GUID/provider-list hash/route plan, files already recorded as verified are revalidated locally and are not downloaded again. If a recorded file is missing, corrupt or has changed checksum/dimensions, the resume fails closed before a network retry can hide the mismatch.

An untracked pre-existing file is not trusted merely by filename. It is adopted only when a newly downloaded remote copy has the same SHA-256 and dimensions; otherwise the tool refuses to overwrite it.

The final package contains the JPEGs without recompression/renaming plus:

- `ACQUISITION_STATE.json` — restart/progress state;
- `QUELLENINFO.json` — complete technical manifest;
- `QUELLENINFO.txt` — Human-readable source/acquisition information;
- `SHA256SUMS.txt` — final image checksums.

`complete` is written only after the actual image sequence matches the provider list and every image has passed integrity checks. A file-list check, one inspected JPEG, CI PASS, running job or temporary artifact is not a secured package.

## Status/read boundary

A pure status request is read-only. The CLI `--status` path reads persisted package state only and does not fetch `files.json`, fetch images, create the package directory or resume a failed/cancelled operation.

A bounded retry inside one already-authorized active download is ordinary retry behavior. A persisted resume or a new top-level acquisition after terminal state is a distinct consequential action and must be authorized by the acquisition request/operation contract; `Fertig?` or `Status?` does not supply that authority.

## Evidence and authority

Technical acquisition does not establish Project existence, Source use, research function, historical provenance, archival master status, rights or scholarly acceptance. Corpus registration remains a separate intake decision. The external manifest is a technical acquisition record, not a canonical Source/File row.

The offline fixtures in `tests/fixtures/ssta-files-*.json` were captured from the public SStA endpoints for Nr. 632 (135 entries), Nr. 754 (61), and the Oppurg pilot GUID (139) on 2026-10-05. They test real unsorted entry shapes and fail-closed parsing. They do not prove that every image byte was downloaded. A separate live check fully read and verified only image 0001 of the 139-entry Oppurg list (4,311 × 3,891 pixels).

The CLI deliberately does not handle restricted browser or sandbox policies. A failed DNS lookup in a restricted execution environment is not evidence that the archive server is unavailable. Diagnose the environment before reporting a source-access failure.

## Chat skill

The repository-scoped ChatGPT/Codex skill is `.agents/skills/savesax/`. Its preferred short invocation is the bare word `savesax`; implicit selection is enabled. In ChatGPT's explicit skill selector, use `@savesax`; Codex also supports `$savesax`. The skill reuses one source URL already present in context and asks only for a genuinely missing record link or external destination.

The skill keeps status reads separate from acquisition/resume requests, applies the runtime/destination gate before a long productive run, and reports partial/restartable/failing state without laundering it into `secured`.
