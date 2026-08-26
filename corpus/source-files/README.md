# Source files — exact original exports

This directory is the repository location for byte-identical original archive exports **when public repository storage is lawful/authorised for the intended use**.

Canonical intended layout:

`<source_id>/original/<original-filename>`

Rules:

- the original file is stored unchanged;
- its SHA-256, coverage, rights state and repository path are recorded in `../files.tsv`;
- OCR, renders, crops, rotations or other derivatives never overwrite the original;
- persistent identifiers such as URNs/stable archival URLs are retained as first-class provenance and working identifiers;
- a persistent identifier and the exact export have different functions: the former identifies/re-locates the archive-side object, while the latter preserves the concrete byte sequence actually used in research;
- neither is a substitute for the other;
- if public redistribution authority is not established, do not place the binary here and record the specific preservation blocker in `../files.tsv`.

## Current InC/1.0 exports

The current central Knau source-group exports carry the RightsStatements `InC/1.0` marker. That is a **known protected-rights state**, not an unknown-rights state. The statement indicates copyright and/or related-rights protection, notes that uses permitted by applicable law remain possible, and that further uses may require permission. It also warns that additional rights/permissions may matter and that the statement itself is **not a licence**.

Accordingly, `InC/1.0` is preserved verbatim in the file manifest while public redistribution of the PDF bytes is treated as a separate question. In the absence of a documented additional licence, permission, contract or other adequate basis for public repository redistribution, the central exports remain `preservation-blocked-public-redistribution`.

This does not reduce the importance of the originals: their filenames, SHA-256 values, source coverage and intended repository paths remain canonical preservation metadata until a lawful/authorised storage route is established.