# Archival source acquisition: SStA pilot

This bounded implementation acquires individual JPEGs from the Sächsisches Staatsarchiv. It uses the archive's actual `files.json` list and writes only to a configured external source destination. It does not create Corpus or Project records, search for sources, infer research roles, or treat CI artifacts as preservation.

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

## Read-only list verification without acquisition metadata

For a **verified digitalisat GUID**, a runtime that can execute this repository can inspect the real provider list before resolving all catalog metadata or selecting a storage destination:

```sh
python tools/archival_source_acquisition.py --inspect-guid <DIGITALISAT-GUID>
```

The command requests `/digitalisate/<GUID>/files.json`, reports **exactly its actual entries in provider order**, `typ`, `istEinzelbild`, entry count and SHA-256, and writes no image, progress state or source package. To reproduce the list-only check against already captured bytes (without network):

```sh
python tools/archival_source_acquisition.py --inspect-guid <DIGITALISAT-GUID> --file-list <files.json>
```

**Do not treat a `bestand.jsp?guid=` catalogue GUID as the verified digitalisat GUID without checking the official catalog linkage.** The probe reports a provider *file list*, **not** successful image URL access, JPEG validity, resolution, or preservation. A `jpg` with `istEinzelbild=false` is surfaced in the report rather than silently excluded or assumed to be a valid direct JPEG. The acquisition plan retains its documented supported-mode checks until live provider evidence justifies a change. The probe is a diagnostic fallback, not a substitute for the normal `savesax` task.

**Skill registration is host-specific.** `.agents/skills/savesax/agents/openai.yaml` expresses invocation intent for a compatible host, but its presence in GitHub is not a runtime registration or functional test in an arbitrary ChatGPT session. If the skill is not in that session's installed/available skills, the assistant must still recognize the source-preservation request, freshly load these repo instructions, and attempt the existing authorized provider-native execution path where supported; otherwise it must name the actual platform/runtime or storage boundary. Neither the probe nor the repository-only skill configuration can certify automatic invocation.

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
