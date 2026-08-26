# Source files — exact original exports

This directory is the repository location for byte-identical original archive exports **when rights/authority permit committing them to this public repository**.

Canonical intended layout:

`<source_id>/original/<original-filename>`

Rules:

- the original file is stored unchanged;
- its SHA-256, coverage, rights state and repository path are recorded in `../files.tsv`;
- OCR, renders, crops, rotations or other derivatives never overwrite the original;
- a URL/URN is provenance, not an equivalent backup;
- if public redistribution authority is not established, do not place the binary here and keep `storage_status = preservation-blocked-rights` in `../files.tsv`.

The current Knau source-group exports are checksum-identified and have intended paths in `../files.tsv`, but their binary preservation here remains blocked because the source exports are marked `InC/1.0` and no public-redistribution authority has yet been recorded.
