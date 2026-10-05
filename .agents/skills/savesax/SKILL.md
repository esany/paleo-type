---
name: savesax
description: "Start or carry out acquisition of digitized images from a Sächsisches Staatsarchiv record. A bare “savesax” is a complete request; use the record URL already in context. Also applies to ordinary requests to save these archival images, not to transcription or historical interpretation."
---

# Save SStA digitalisat images

Treat `savesax` or `$savesax` by itself as the user's request to acquire the images for the Sächsisches Staatsarchiv record already present in the conversation. Do not make the user choose an internal workflow, provider, or atom, and do not ask for a full sentence.

## Run

1. **Resolve the record.** Reuse the single relevant archival record URL in the current conversation. If there is no URL, ask only for the archival record link. If multiple plausible records are in scope, ask which one. A digitalisat GUID URL is sufficient.
2. **Verify catalog metadata.** Read the linked record page and use its displayed archive, fonds, signature, official title, date, classification and GUID. Do not fill missing catalog facts from inference or chat memory; leave optional metadata unset and disclose unavailable fields. Keep the archive page URL as provenance.
3. **Resolve the real image list.** Use `tools/archival_source_acquisition.py`. Its SStA adapter fetches `/digitalisate/<GUID>/files.json`, validates each `name`, `typ` and `istEinzelbild`, rejects unsupported/duplicate entries and sorts actual names. Never fabricate a sequence from an image count. Do not use thumbnails, canvas screenshots or DOM class names as image sources for this supported single-JPEG mode. Tile/DZI records are unsupported; stop and explain if encountered.
4. **Choose external storage.** Reuse an explicitly configured external literature/source root from the current work context or host configuration. If none is available, ask one short question for the destination folder. Never default to the repository, worktree, project mirror, or a local workspace folder. Resolve the target and verify it is outside the repository/worktree before downloading. If the external destination is inaccessible, report that limitation; do not fall back to local storage.
5. **Plan without persisting source metadata.** Pass the verified metadata JSON to the CLI on standard input using `--metadata -`; do not create a metadata file. Run with `--dry-run` first and check the record identity, destination, actual image count, first/last filenames and route. Use the official individual `download.jsp` route by default; use `fullsize` only when appropriate for the requested output or when the download route fails for a diagnosed reason.
6. **Acquire and verify.** Once the plan is coherent and the user has requested acquisition, run the same command without `--dry-run`. The CLI writes original JPEG bytes, `QUELLENINFO.json`, `QUELLENINFO.txt` and `SHA256SUMS.txt` under the external root, without silently overwriting differing files. Verify the returned manifest says complete and that count, sorted sequence, dimensions and checksums are present. Report partial/failing results as such; do not call a file-list check a completed image download.
7. **Report plainly.** Give the source title/signature, destination, number of images, filename range, route and any failures. Distinguish live acquisition from planning/fixture checks. Do not claim that files are archival masters or that rights have been established.

The current CLI accepts metadata from standard input. A Python runner can pass `json.dumps(metadata)` as `subprocess.run(..., input=..., text=True)` to avoid shell-quoting problems and any metadata file. Pass the output root and flags as argument-list elements, not interpolated shell text.

## Boundaries

- Store image/source-package files only in the configured external destination; never commit them or leave copies in the repository/worktree.
- Do not create Projects, Corpus rows, Source uses, research functions, priorities, or historical interpretations.
- Do not search for more sources unless separately requested.
- A package directory is the current output; do not claim a ZIP exists unless one was explicitly requested, created externally, and verified.
- If a tool/network error occurs, identify the failing tool/environment separately from the archive server. A sandbox DNS error is not evidence that the source is unavailable.
