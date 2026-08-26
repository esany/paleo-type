# Evidence policy

## Source-status codes

| code | status | what it can establish |
|---|---|---|
| P | primary source actually inspected | content visible in inspected passage plus provenance visible/verified |
| E | scholarly edition actually inspected | edited text/apparatus in inspected passage |
| F | research full text/relevant pages actually inspected | author's claims in inspected passage |
| K | catalogue/finding aid/metadata | existence, shelfmark, dates, descriptive metadata only |
| R | review | reviewer's report/assessment only |
| S | search result/snippet/TOC/abstract/marketing copy | discovery lead only unless the item itself is the object of the claim |
| H | hypothesis/inference | no independent evidential status |

## Audit requirements

For external sources record:
- bibliographic/archive identity;
- source-status code;
- access route;
- exact pages/folios/passages inspected when available;
- what the source actually supports;
- what it does **not** establish;
- date checked.

## Primary-source provenance

A primary image or file used for substantive transcription must become traceable independently of a transient chat session as soon as practical. Record what is actually known, such as:
- archive/repository and shelfmark;
- folio/page/image identifier;
- access route;
- stable/local filename or identifier;
- date inspected;
- relevant rights/access limitation.

Use a checksum/hash only when it solves a concrete identity or versioning problem. Do not invent archival metadata that has not been verified, and do not publish restricted binary sources merely to satisfy reproducibility.

## Promotion rule

A source may move from `K/S` to `P/E/F` only after the underlying material has actually been opened and the relevant passage inspected. Repetition of metadata never promotes status.

## Claim rule

Every consequential historical claim must be traceable to either:
- an inspected source (`P/E/F`), or
- an explicitly labeled inference (`H`) whose premises are themselves traceable.

AI/model output is never a source-status category and does not independently support a historical claim. Consequential AI use is documented as research provenance under `ai-governance.md`, not as evidence.

## Parallel-source rule

A finding aid saying that a record contains a relevant place/person/topic is not a textual parallel. It becomes a textual parallel only after the relevant manuscript/edition passage is inspected and compared.