# Research milestones — Knau

## Purpose

These milestones define **verifiable scholarly maturity states**, not task lists or a fixed waterfall process. They exist to keep work directed toward a reliable edition of `ThHStAW, EGA, Reg. Ii 5, fol. 61v–63r` and to prevent isolated problem-solving or tooling work from replacing research progress.

A milestone is reached only when its requirements are satisfied. Later evidence may reopen an earlier milestone, but any consequential revision must remain traceable.

### Operating rule

> Every substantive activity must address an unmet requirement of the active milestone, repair a prerequisite exposed as invalid, or be explicitly justified as necessary evidence for doing so.

Uncertainty is not failure. A milestone may be complete while individual readings remain `variant` or `unresolved` if the milestone's requirements for documenting and testing that uncertainty have been met.

---

## M1 — Source and transmission basis secured

### Target state

The principal witness and the already available comparison/control sources relevant to this project can be identified, recovered and related without relying on chat history, while archival metadata, digital instantiation and demonstrated textual relationships remain distinct.

### Requirements

- The principal witness has an unambiguous canonical source identity.
- Its archive/fonds/signature, archival record, relevant locus and available persistent/digital record identity are recorded.
- The project locus is mapped independently of portal/export/PDF numbering.
- Consequential external/digital files used for research are represented in `corpus/files.tsv` with the available identity/checksum/coverage/storage/rights information.
- Project crosswalks distinguish archival folio, portal/export image, PDF/file position and working identifiers.
- Existing comparison/control records have independent canonical identities and stated research roles.
- Relationships such as extract/parallel/correspondence are stated only at the evidential level actually supported.
- Catalogue/finding-aid claims are distinguishable from claims established by manuscript inspection/collation.
- The principal project scope and current source basis can be reconstructed from the repository alone.

### Evidence/method allowed

Archival/catalogue metadata, persistent identifiers, inspected digital files/images, project crosswalks and direct source inspection. Textual dependence may only be strengthened by actual textual comparison.

### Canonical outputs

`corpus/sources.tsv`, `corpus/files.tsv`, `corpus/relationships.tsv`, `corpus/events.tsv`, project `sources/`, `project.yml`, relevant `STATUS.md` state.

### Exit gate

A new competent researcher/agent can answer: **What exactly is the principal source, which locus is being worked on, which concrete digital instantiation underlies the work, what comparison sources are already available, and what is actually known about their relationships?**

### Permitted residual uncertainty

Exact textual dependence, scribal relationship, chronology within an archival process or unclear catalogue relationships may remain unresolved if labelled accordingly.

### Reopen when

A source identity, folio mapping, digital-file identity, provenance claim, project boundary or consequential inter-source relationship is shown to be wrong or materially incomplete.

### Current project assessment

**Substantially reached.** Later milestones may still strengthen relationship claims through collation.

---

## M2 — Principal witness completely represented

### Target state

Every relevant physical text area of `Reg. Ii 5, fol. 61v–63r` is represented in a conservative diplomatic working transcription. Completeness means complete **representation of the source**, not complete resolution of every sign.

### Requirements

- Every physical line/text unit belonging to the Knau entry is represented in the transcription.
- No prose summary such as `[unresolved ... passage]` substitutes for a visible multi-line source passage.
- Line/region order and page/folio location remain reconstructable.
- Visible numerals, abbreviations, punctuation/separators and other materially relevant signs are represented conservatively according to the transcription method.
- Illegible/uncertain spans are localized as narrowly as the evidence permits rather than silently omitted.
- `observed`, `working`, `variant` and `unresolved` are used according to their defined meaning.
- Diplomatic reading is not silently normalized to modern spelling, known place/person names, expected syntax, currencies or measures.
- Historical identification and semantic interpretation remain outside the diplomatic reading layer.
- Every unresolved/variant locus that can affect the later edition is discoverable from the structured transcription rather than hidden in prose notes.
- Entry boundaries at 61v and 63r are represented sufficiently to establish the project text's physical extent.

### Evidence/method allowed

Direct inspection of the principal witness and same-image technical enhancement that does not introduce external textual content. Internal same-hand comparison may help segment/recognize signs, but semantic/contextual completion must not substitute for visible evidence.

### Canonical outputs

`transcription/132.tsv` through `transcription/135.tsv`, with consequential corrections logged in `apparatus/decisions.tsv`.

### Exit gate

A reviewer can move from fol. 61v to 63r and find a transcription representation for every relevant visible line/text unit, including explicitly unresolved material, without encountering paragraph-level placeholders that merely describe missing text.

### Permitted residual uncertainty

Individual letters, words, abbreviations, numerals, measures, names and syntax may remain `variant` or `unresolved`. M2 does **not** require W1–W6 or other difficult tokens to be solved.

### Reopen when

Later inspection shows omitted source text, incorrect line segmentation, an entry-boundary error, or a supposed transcription unit is actually semantic reconstruction rather than source representation.

### Current project assessment

**Active milestone. Not reached.** Known gaps include paragraph-level placeholders and unresolved multi-line spans, especially on fol. 62v, plus incomplete representation on 61v/62r.

---

## M3 — Internal palaeographic and notational analysis completed

### Target state

Consequential uncertainties in the principal witness have been systematically tested against relevant internal evidence before stronger reliance is placed on external textual parallels.

### Requirements

- All consequential `variant`/`unresolved` loci from M2 are inventoried as research problems.
- For each problem, the relevant evidence class is identified: letterform, abbreviation, numeral, currency, measure, grain/natural due, formula, syntax/segmentation or other.
- Relevant same-hand/same-record comparanda are sought where they can discriminate between candidates.
- Repeated forms are compared by graphematic/structural features, not merely semantic expectation.
- Numeral/measure/currency anchors are documented with exact locations and evidential status.
- Competing readings are preserved where internal evidence does not discriminate.
- Rejected readings remain traceable when they were consequential.
- Historical/domain knowledge is used to generate candidate tests, never as proof of the manuscript reading.
- The distinction between sign reading, abbreviation expansion, normalization and identification remains explicit.
- Every promoted reading has an evidence note sufficient to understand why its status changed.
- Problems that internal evidence cannot solve are explicitly handed forward to M4 rather than forced closed.

### Evidence/method allowed

Principal-witness images, same-hand/same-record material already available, documented grapheme/notation concordances, and domain knowledge used only for hypothesis generation. Existing C2 material may be used as a **comparative notation control** only when its independence/different evidential role is explicit; it does not become same-hand evidence without demonstration.

### Canonical outputs

Project `palaeography/`, transcription statuses, `apparatus/decisions.tsv`, and `STATUS.md` for active unresolved problems.

### Exit gate

For every consequential uncertain locus, a reviewer can tell **what internal evidence was relevant, what was actually compared, what conclusion followed, and what remains unresolved**. No important uncertainty remains merely because nobody systematically tested the available internal evidence.

### Permitted residual uncertainty

Any reading may remain unresolved after adequate testing. A documented negative result is a valid scholarly result.

### Reopen when

New same-hand/internal evidence becomes available, an anchor used for comparison is invalidated, or later collation exposes a likely misreading requiring renewed palaeographic inspection.

---

## M4 — Existing comparison witnesses/controls independently assessed and collated

### Target state

The already available comparison sources are used according to their demonstrated evidential roles, and the relevant Reg. Ii 4 Bd. II parallel is independently read and systematically collated with the principal witness without witness contamination.

### Requirements

- Each comparison/control source remains independently identified and its role explicitly stated.
- Relevant comparison loci are located by archival folio/locus, not only export/image number.
- Reg. Ii 4 Bd. II `306v–309r` is read independently enough to support local collation with Reg. Ii 5 `61v–63r`.
- A reading from one witness is never silently copied into the transcription of the other.
- Corresponding textual units are mapped explicitly.
- Material agreements and differences are recorded: wording, spelling, numerals, measures, additions, omissions, ordering and structurally significant divergence where present.
- C2 notation evidence is labelled as comparative/control evidence and not treated as proof of textual dependence or same-hand identity.
- Catalogue-supported extract relationships remain distinguishable from relationships demonstrated through collation.
- Any upgrade of `corpus/relationships.tsv` is justified by the observed textual evidence.
- External comparison may strengthen, weaken or leave unchanged an M2/M3 reading; consequential changes are logged rather than silently overwritten.
- The resulting evidence is sufficient to state the limits of what the parallel witness can legitimately support.

### Evidence/method allowed

Independent manuscript inspection of the already available witnesses/controls, structured collation, archival metadata at its proper evidential level and the results of M2/M3.

### Canonical outputs

Independent transcription/notes for the comparison locus as needed, collation record/apparatus, `apparatus/decisions.tsv`, relevant project source audit, and `corpus/relationships.tsv` when evidential status changes.

### Exit gate

A reviewer can distinguish **what Reg. Ii 5 says, what Reg. Ii 4 says, where they correspond/diverge, what C2 contributes as control, and which conclusions about transmission are actually warranted**.

### Permitted residual uncertainty

The exact genetic relationship between witnesses may remain unresolved. Individual variants may remain unreadable. Collation need not prove verbatim copying or complete line equivalence.

### Reopen when

A comparison witness is materially re-read, a locus mapping changes, a supposed correspondence fails, or new evidence changes the inferred transmission relationship.

---

## M5 — Critically consolidated text state

### Target state

The principal witness has a coherent, complete and evidence-auditable transcription state incorporating the results of internal analysis and controlled comparison, with all consequential uncertainty and revision history preserved. This is the research state from which an edition can responsibly be produced.

### Requirements

- M1–M4 requirements relevant to the final text state are satisfied or explicitly reopened.
- The principal transcription is complete at the M2 level and internally consistent in conventions.
- Every consequential reading has an appropriate status; no known uncertainty is disguised as certainty.
- Important `working` readings have been subjected to an adversarial attempt to falsify them, with priority proportional to consequence.
- Previously rejected fluent/semantic reconstructions have not re-entered the text without new evidence.
- Consequential changes caused by palaeographic analysis or collation are traceable in the decision apparatus.
- Source relationships used as evidence are stated at their demonstrated level.
- Names/places/historical identifications remain separate from diplomatic forms and carry their own evidential basis.
- Numeral/currency/measure readings used in substantive interpretation have been checked against the strongest available relevant evidence.
- Residual unresolved readings are explicitly enumerated or mechanically discoverable and have notes explaining the evidential limit where consequential.
- A bounded consistency pass confirms that transcription, apparatus, palaeographic evidence, source audit, corpus relationships and `STATUS.md` do not contradict the consolidated state.
- A competent third party can audit the path from a consequential edited reading back to the source locus and evidence/decision history.

### Evidence/method allowed

All evidence properly admitted and classified in M1–M4, plus adversarial reinspection and consistency checking. No new certainty may be created merely to make the text look finished.

### Canonical outputs

Frozen/versioned transcription checkpoint, apparatus, palaeographic evidence, source/collation audit, updated `STATUS.md` and any necessary corpus relationship updates.

### Exit gate

The question is no longer “have we transcribed and tested the source adequately?” but “how should this established research state be represented editorially?” A third party could produce an edition without reconstructing missing research decisions from chat.

### Permitted residual uncertainty

Explicitly documented unresolved readings, ambiguous expansions and unresolved transmission questions are permitted. They must be represented honestly in the eventual edition.

### Reopen when

A material source-reading error, provenance error, invalid comparison anchor or consequential undocumented decision is discovered.

---

## M6 — Scholarly edition produced and quality-controlled

### Target state

A usable scholarly edition of the Knau text is produced from the critically consolidated state without erasing the distinction between source text, editorial intervention, normalization/identification and historical commentary.

### Requirements

- The edition declares its scope, principal witness and relevant comparison witnesses/controls.
- Editorial/transcription conventions actually used are stated compactly and consistently.
- The edited/diplomatic text is derived from the M5 consolidated state; it does not introduce unlogged manuscript readings.
- Editorial expansions, supplied text, uncertain readings, illegible material and other interventions are distinguishable according to the adopted conventions.
- Material variants from the relevant parallel witness are represented in an apparatus or equivalent transparent form.
- Normalized names/places and historical identifications are not presented as if they were diplomatic manuscript readings.
- A concise source/transmission note distinguishes archival metadata from findings of textual collation.
- Historical/sachliche commentary is evidence-based and separable from transcriptional claims.
- Every consequential editorial claim can be traced to source locus and/or documented decision evidence.
- Residual uncertainty from M5 remains visible rather than being resolved for readability alone.
- The edition undergoes a final source-to-output sample audit, including difficult/uncertain passages and at least one adversarial check.
- Publication/export format is chosen for actual use; TEI or other additional infrastructure is introduced only if a concrete dissemination/interchange requirement justifies it.

### Evidence/method allowed

The M5 consolidated research state plus clearly labelled editorial normalization/commentary and any publication-specific verification required by the chosen output.

### Canonical outputs

Edition text, critical/variant apparatus, source/editorial note and any user-facing export justified by the actual dissemination need.

### Exit gate

A reader can use the edition while a specialist can independently distinguish manuscript evidence, editorial intervention, variant evidence, normalization/identification and historical interpretation, and can trace consequential claims back to their evidential basis.

### Permitted residual uncertainty

Scholarly uncertainty remains permitted and visible. Publication does not convert `unresolved` into certainty.

### Reopen when

Post-publication/source review reveals a material error, newly available evidence changes a consequential reading/relationship, or a new edition version intentionally incorporates additional research.

---

## Milestone progression and iteration

These milestones express dependency, not a one-way waterfall:

`M1 source basis → M2 complete representation → M3 internal analysis → M4 controlled comparison → M5 critical consolidation → M6 edition`

Later evidence may reopen earlier states. The rule is **controlled revision with provenance**, not immutability.

Do not advance merely because work has been performed. Advance when the milestone requirements are demonstrably met.

## STATUS relationship

`STATUS.md` should state only:

- overall research goal;
- reached milestone(s);
- active milestone;
- unmet requirements/known blockers of that milestone;
- exact `NEXT ACTION` chosen because it advances one of those unmet requirements.

Detailed milestone requirements live here and should not be duplicated in `STATUS.md`.
