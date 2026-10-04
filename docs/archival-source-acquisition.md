# Archival Source Acquisition MVP

This bounded MVP adds one existing-tool implementation for the Sächsisches
Staatsarchiv. It deliberately does not introduce a repository-wide skills
directory or create Corpus/Project state.

## Scope

- provider adapter: Sächsisches Staatsarchiv download and tested fullsize routes;
- generic core: deterministic naming, external package storage, JPEG checks,
  SHA-256 manifest and idempotent/no-overwrite behavior;
- offline fixtures for 20578 Nr. 632 (135 images) and Nr. 754 (61 images);
- no Project creation, Source-use creation, research-function assignment,
  automatic source search or Corpus mutation.

## Metadata input

The CLI expects a JSON file with at least:

- archive
- fonds
- signature
- title
- date_label
- guid
- page_url
- image_count

Optional fields include archive_code, name_key, classification_path and
rights_status. Date and name tokens must be supplied by the intake process;
the tool does not infer historical dating or archival identity from filenames.

## Commands

Dry-run planning:

    python tools/archival_source_acquisition.py \
      --metadata <metadata.json> \
      --output-root <external-literature-root> \
      --route download \
      --dry-run

Acquisition:

    python tools/archival_source_acquisition.py \
      --metadata <metadata.json> \
      --output-root <external-literature-root> \
      --route download

The output root is intentionally external to the repository. The tool writes a
package directory containing 0001.jpg...NNNN.jpg, QUELLENINFO.json,
QUELLENINFO.txt and SHA256SUMS.txt.

## Evidence and authority boundary

The tool records technical acquisition facts. It does not establish:

- Project existence or priority;
- Project-relative Source use;
- principal/comparison/context research functions;
- rights or access beyond the supplied status;
- historical provenance, reading or interpretation.

The generated manifest is an acquisition record, not a replacement for the
canonical Source/File contract. Corpus registration remains a separate,
explicit intake decision.

## Test contract

Offline tests cover both fixture counts, deterministic package separation,
download/fullsize route distinction, JPEG dimension checks, idempotent rerun,
and refusal to overwrite an existing different file.

Live extraction of the two archivalien is intentionally a separate execution
step against the configured external root. It must not be simulated by the
offline tests.
