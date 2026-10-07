---
name: savesax
description: "Start or carry out acquisition of digitized images from a Sächsisches Staatsarchiv record. A bare “savesax” is a complete request; use the record URL already in context. Also applies to ordinary requests to save these archival images, not to transcription or historical interpretation."
---

# Save SStA digitalisat images

Treat `savesax` or `$savesax` by itself as the user's request to acquire the images for the Sächsisches Staatsarchiv record already present in the conversation. Do not make the user choose an internal workflow, provider, or atom, and do not ask for a full sentence.

A status/read request is different from an acquisition request. `Fertig?`, `Status?`, `läuft es noch?` or equivalent wording is **read-only**: inspect/report the existing operation/package state and never infer a rerun, resume, push, workflow trigger or new acquisition from that read alone.

## Run

1. **Resolve the record.** Reuse the single relevant archival record URL in the current conversation. If there is no URL, ask only for the archival record link. If multiple plausible records are in scope, ask which one. A digitalisat GUID URL is sufficient.
2. **Verify catalog metadata.** Read the linked record page and use its displayed archive, fonds, signature, official title, date, classification and GUID. Do not fill missing catalog facts from inference or chat memory; leave optional metadata unset and disclose unavailable fields. Keep the archive page URL as provenance.

   **Keep this skill's access routing cost-aware.** When an available authorized non-metered read/fetch route can establish the needed catalogue or viewer fact, use it instead of starting a metered interactive browser/agent merely because that route is connected. If one bounded UI-only interaction is genuinely the simplest useful continuation and the Human has chosen the low-cost collaboration mode, ask only for that concrete click/result; do not make the Human choose provider/tool internals. If a metered browser/agent is materially necessary because the non-metered read path and the provider-native acquisition path cannot establish the needed fact, explain the information gain and obtain explicit Human approval before starting the metered route. Provider pricing is runtime information; do not hard-code current rates into this skill.

3. **Resolve the real image list.** Use `tools/archival_source_acquisition.py`. Its SStA adapter fetches `/digitalisate/<GUID>/files.json`, validates each `name`, `typ` and `istEinzelbild`, rejects unsupported/duplicate entries and sorts actual names. Never fabricate a sequence from an image count. Do not use thumbnails, canvas screenshots or DOM class names as image sources for this supported single-JPEG mode. Tile/DZI records are unsupported; stop and explain if encountered.
4. **Choose and preflight external storage/runtime.** Reuse an explicitly configured external literature/source root from the current work context or host configuration. If none is available, ask one short question for the destination folder. Never default to the repository, worktree, project mirror, disposable CI storage or a local workspace folder. Before a long run, verify that successful files and `ACQUISITION_STATE.json` persist at the intended destination across an ordinary process/network interruption and that the executing context has adequate observation/control for the run. If a material cancel/containment limitation remains, disclose it before starting rather than discovering it after `Stop`. GitHub Actions is not the default productive acquisition path merely because it can run code.
5. **Plan without persisting source metadata.** Pass the verified metadata JSON to the CLI on standard input using `--metadata -`; do not create a metadata file. Run with `--dry-run` first and check the record identity, destination, actual image count, first/last filenames and route. Use the official individual `download.jsp` route by default; use `fullsize` only when appropriate for the requested output or when the download route fails for a diagnosed reason.
6. **Acquire with durable progress.** Once the plan is coherent and the user has requested acquisition, run the same command without `--dry-run`. The CLI writes successful JPEGs directly under the external package and atomically updates `ACQUISITION_STATE.json` after each newly verified image. A normal interruption therefore leaves truthful `partial-restartable` or `cancelled-restartable` state instead of discarding prior progress. Re-running the authorized acquisition against the same provider-list/route plan verifies recorded files locally and resumes only missing work; changed/corrupt persisted bytes fail closed. Untracked pre-existing files are adopted only after a fresh remote copy hashes identically. Final `complete` status is written only after all expected images are verified.
7. **Verify final package.** On completion, verify `QUELLENINFO.json`, `QUELLENINFO.txt`, `SHA256SUMS.txt`, `ACQUISITION_STATE.json`, expected count, stable sequence, dimensions and checksums. Report partial/failing results as such; do not call a file-list check, a few JPEGs, CI progress or a temporary artifact a secured package.
8. **Report plainly.** Give the source title/signature, destination, operation state, number of images, filename range, route and any failures. Distinguish live acquisition from planning/fixture checks. Do not claim that files are archival masters or that rights have been established.

For a pure status question, use the CLI `--status` path (or equivalent direct state inspection) against the known metadata/output root. That path reads the existing progress state only; it must not fetch images or mutate the package. A terminal failure/cancelled state is reported as such. A new top-level acquisition/resume after terminal state requires an acquisition request or another already-authorized operation contract; a status read is not that authorization.

The current CLI accepts metadata from standard input. A Python runner can pass `json.dumps(metadata)` as `subprocess.run(..., input=..., text=True)` to avoid shell-quoting problems and any metadata file. Pass the output root and flags as argument-list elements, not interpolated shell text.

## Boundaries

- Store image/source-package files only in the configured external destination; never commit them or leave copies in the repository/worktree.
- Keep transient staging, controlled external preservation and CI artifacts semantically distinct. A disposable artifact is not the intended source-preservation destination.
- Do not create Projects, Corpus rows, Source uses, research functions, priorities, or historical interpretations.
- Do not search for more sources unless separately requested.
- A package directory is the current output; do not claim a ZIP exists unless one was explicitly requested, created externally, and verified.
- If a tool/network error occurs, identify the failing tool/environment separately from the archive server. A sandbox DNS error is not evidence that the source is unavailable.
- If the Human says `Stop`, start no new work. Use an available authorized cancel mechanism for the active operation when the executing context supports it; otherwise report the precise control limitation and preserve/contain the restartable external state.
