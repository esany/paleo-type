# Archival source acquisition: SStA pilot

This bounded implementation acquires individual JPEGs from the Sächsisches
Staatsarchiv. It uses the archive's actual `files.json` list. It does not
create Corpus or Project records, search for sources, or infer research roles.

## Observed SStA path

1. Read the GUID from the archive record URL or supplied metadata.
2. Fetch `https://www.archiv.sachsen.de/digitalisate/<GUID>/files.json`.
3. Validate every `name`, `typ` and `istEinzelbild` entry; sort by `name`.
4. Form one `download.jsp` or `fullsize/<name>.jpg` URL per listed image.
5. Acquire the images into the configured external root and record checksums.

The JSON list, not a supplied image count or a Viewer canvas, determines the
image names. A supplied `image_count` is an optional consistency check. The
adapter fails on unsupported or duplicate entries; it does not silently skip
them. Tile/DZI variants are not implemented by this single-image adapter.

The generic acquisition core sees only a normalized list of image
specifications. SStA fields and routes stay in the provider adapter.

## Metadata input

Supply JSON with `archive`, `fonds`, `signature`, `title`,
`date_label`, `guid` and `page_url`. Optional fields include
`archive_code`, `name_key`, `classification_path`, `rights_status`
and `image_count`.

For chat-driven runs, pass the same JSON on standard input with
`--metadata -`. This avoids creating a metadata sidecar file. Source image
files are still written only to the configured external root.

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

Omit `--dry-run` to acquire the listed images. `--route fullsize` selects
the direct viewer image route. The default `download` route uses the
archive's individual download endpoint. `--file-list` affects planning only;
actual image retrieval still needs network access.

The tool writes the images without recompression or renaming, plus
`QUELLENINFO.json`, `QUELLENINFO.txt` and `SHA256SUMS.txt` in one package
directory under the external root. The manifest includes the `files.json`
URL and SHA-256, acquisition time, image URLs, dimensions and image checksums.
Existing images are downloaded again for hash comparison and never silently
overwritten; this is a repeatable check, not a network-free no-op.

## Evidence and authority

Technical acquisition does not establish Project existence, Source use,
research function, historical provenance, archival master status, or rights.
Corpus registration remains a separate intake decision. The manifest is an
external technical acquisition record, not a canonical Source/File row.

The offline fixtures in `tests/fixtures/ssta-files-*.json` were captured
from the public SStA endpoints for Nr. 632 (135 entries), Nr. 754 (61), and
the Oppurg pilot GUID (139) on 2026-10-05. They test real unsorted entry
shapes and fail-closed parsing. They do not prove that every image byte was
downloaded. A separate live check fully read and verified only image 0001
of the 139-entry Oppurg list (4,311 × 3,891 pixels).

The CLI deliberately does not handle restricted browser or sandbox policies.
A failed DNS lookup in a restricted execution environment is not evidence that
the archive server is unavailable. Diagnose the environment before reporting
a source-access failure.

## Chat skill

The repository-scoped ChatGPT/Codex skill is
`.agents/skills/savesax/`. Its preferred short invocation is the bare word
`savesax`; implicit selection is enabled. In ChatGPT's explicit skill
selector, use `@savesax`; Codex also supports `$savesax`. The skill reuses
one source URL already present in context and asks only for a genuinely
missing record link or external destination.

The skill and its CLI core are in this Draft PR. They become available only in
a ChatGPT/Codex environment that has loaded the repository skill. The live
full-image workflow is manual-dispatch only; a push or documentation change
must never launch an acquisition run.
