# Cross-source research findings — 2026-09-14

Status: **non-normative comparative Research evidence for #185; not METHOD, not a Requirement owner, not Project priority, not capability admission, not architecture and not implementation authority.**

Research baseline: `main@3605453883dddfc88749366967b42ab9249478db`.

Parent programme: #183. Workstream: #185.

## 1. Purpose and comparison discipline

This record tests whether selected observations from the current Reg. Ii 5 research-system history remain meaningful when source structure, research purpose, evidence situation and materially implicated competencies change.

It does **not** attempt to validate the existing Concept Candidate. It does not assume that any internal construction-site category is generic.

The repository's Reg. Ii 3 and Reg. Ii 4 Projects were inspected first as possible comparison cases. They remain source-based work within closely related Thuringian archival/visitation structures and are therefore useful controlled comparators but insufficient by themselves for the intended heterogeneity test.

This pass therefore adds two narrowly bounded public external fixtures:

1. an individual correspondence item from the Darwin Correspondence Project;
2. a serial financial/accounting record from the Papers of George Washington / Founders Online, contextualized by the DEPCHA historical-accounts project.

For each fixture the analysis keeps separate:

- source type;
- research/editorial purpose;
- current knowledge state;
- evidence situation;
- concrete research question or uncertainty;
- materially implicated competencies.

No external fixture is imported as a model for `paleo-type` architecture.

## 2. External sources inspected

### 2.1 Darwin correspondence fixture

Primary/public source record:

- Darwin Correspondence Project, **Letter no. 5098, Charles Darwin to Japetus Steenstrup, 23 May [1874 or 1875?]**.
- Public record: https://www.darwinproject.ac.uk/letter/?docId=letters/DCP-LETT-5098.xml
- Source description in the edition: Det Kongelige Bibliotek, Copenhagen; autograph letter signed, one page.
- The edition explicitly marks the year as conjectural and explains the conjecture by relation to a later 1876 letter.

Editorial/project context used after the fixture observation:

- Darwin Correspondence Project, **Editorial policy and practice**: https://www.darwinproject.ac.uk/letters/editorial-policy-and-practice
- Darwin Correspondence Project, **Who we were**: https://www.darwinproject.ac.uk/about/who-we-were
- Darwin Correspondence Project, **Technical**: https://darwinproject.ac.uk/about/technical

Relevant editorial statements include that transcriptions are made from the original or facsimile where possible; original spelling is retained; correspondent identification may require inference from content, replies or archival provenance; and dating may require replies, content, postal-address history, paper/watermarks, handwriting style, publications/events or recipient endorsements.

### 2.2 Washington cash-account fixture

Primary/public source record:

- **Cash Accounts, December 1767**, George Washington.
- Founders Online / Papers of George Washington: https://founders.archives.gov/documents/Washington/02-08-02-0034
- Source description: autograph document in General Ledger A, Library of Congress, George Washington Papers, Series 5, Financial Papers, folios 262 and 267.
- The record contains dated receipt/payment entries, counterparties/descriptions, amounts and a balance.

Project context:

- Papers of George Washington overview: https://founders.archives.gov/about/Washington

Historical-account methodology used after the fixture observation:

- DEPCHA — Digital Edition Publishing Cooperative for Historical Accounts: https://gams.uni-graz.at/depcha
- Christopher Pollin, **Making Linkable Data from Account Books: Bookkeeping Ontology in the Digital Edition Publishing Cooperative for Historical Accounts**, TEI Conference 2019, DOI `10.5281/zenodo.3446143`: https://doi.org/10.5281/zenodo.3446143

DEPCHA explicitly describes historical financial records as highly structured administrative sources whose research significance often lies in aggregation of individual entries and states that transcription alone does not capture their textual, quantifiable and semantic dimensions. The DEPCHA work also names the Financial Papers of George Washington among its use cases.

## 3. Source-comparison matrix

| Dimension | Reg. Ii 5 current fixture | Darwin Letter 5098 fixture | Washington Cash Accounts Dec. 1767 fixture |
|---|---|---|---|
| source type | early modern visitation/administrative manuscript locus containing lists and prose rules | individual nineteenth-century correspondence item | serial eighteenth-century financial/accounting ledger record |
| immediate research/editorial situation | rich text-near source understanding with residual local uncertainty; no owner-selected next scope | short text is readable in edition, but year is explicitly uncertain | entries/amounts are transcribed; account meaning extends across structured receipts/payments/balance |
| salient uncertainty | paragraph/rule relationship, local object/notation residuals, appropriate analysis scale | date/year and correspondence relation; source/provenance context matters | transaction/category/currency/economic relation and aggregate significance |
| direct evidence form | manuscript images, physical lineation/layout, transcription, controlled witness comparison | letter text + source description + related correspondence/contextual evidence | ledger entries with dates, parties/descriptions, amounts, source locator |
| likely materially implicated competencies | palaeography, editing, diplomatics/source criticism, institutional/domain history, comparison discipline | documentary editing, archival provenance, correspondence chronology/network history, material evidence where available, history of science as question requires | documentary editing, accounting/financial history, historical currency/metrology, economic/social history, structured-data interpretation where research purpose requires |
| analytical-scale risk | physical line, paragraph, correspondence range and functional rule can be conflated | one letter may be insufficient to establish date/recipient/context; correspondence series can be evidentially necessary | one entry may be legible but research significance may lie in transactions/aggregates/periodic account structure |
| context timing | direct reading requires contamination control; later comparison/context may become necessary | external relational context may be constitutive evidence for dating/identification | aggregation and domain/accounting context may be necessary to establish transaction/economic meaning |

The table is descriptive. It does not assert one common workflow.

---

# Part A — fixture-level primary findings

## RF185-P01 — the correspondence fixture requires relational context for a claim the document alone does not settle

### Direct observation / evidence

Darwin Letter 5098 is published with the date `23 May [1874 or 1875?]`. The editorial note states that the year is conjectured from the relationship between this letter and a letter to Steenstrup dated 11 September 1876. The physical source is identified as an autograph one-page letter in Copenhagen.

The wider Darwin editorial policy states that years and even correspondents are often not directly supplied by the physical/textual item and may be inferred from replies, content, provenance, postal addresses, paper/watermarks, handwriting style, publications/events and recipient endorsements.

### Interpretation

For the **dating/identification claim**, relational and contextual evidence is not merely optional interpretation added after a self-contained source reading. It is part of the evidence needed to establish the claim at all.

This creates a strong counterexample to any universal research rule that external context should always remain outside primary analysis until the document has been fully interpreted in isolation.

### Alternative explanation

One could separate transcription from dating and say that only the transcription task requires source-local independence while chronology is a later editorial task. That distinction is valid, but it reinforces rather than removes the central observation: context timing is **claim-dependent**.

### Uncertainty / evidence ceiling

This fixture does not show that all correspondence research requires broad contextual loading. The correct amount of context depends on the specific question.

### Tentative generality

`cross-source counterexample to universal context-isolation sequencing; provisional claim-dependent-context hypothesis`.

---

## RF185-P02 — the letter's useful analysis unit can exceed the individual document without making the document boundary irrelevant

### Direct observation / evidence

The date of Letter 5098 is inferred through relation to another letter. The Darwin editorial policy likewise uses replies and correspondence series as dating evidence while retaining individual source descriptions and textual editions.

### Interpretation

The source object remains an individual letter, but the evidence-bearing **analysis relation** for some questions is a correspondence sequence/network rather than a single letter page.

This differs from simply declaring that a larger unit is intrinsically better. The larger relation is justified only by the question being asked.

### Alternative explanation

Dating could be treated as metadata curation rather than scholarly analysis. Even under that description, the evidence relation still exceeds the single document and therefore remains relevant to the source-address/analysis-unit distinction.

### Uncertainty / evidence ceiling

The fixture supports question-dependent enlargement for chronology/provenance, not a general principle that correspondence should be analysed at network scale.

### Tentative generality

`cross-source recurrence of address/object/analysis-relation distinction; provisional generic hypothesis only`.

---

## RF185-P03 — editorial source provenance remains part of the evidential state, not presentation metadata only

### Direct observation / evidence

The Darwin editorial policy distinguishes originals/facsimiles from substitute textual sources and explicitly reports when the best available source is a draft, published version or even a dealer-catalogue description. The individual letter record names the physical source and document type.

### Interpretation

For correspondence, the authority of a reading, date or identification depends partly on what kind of source survives and what the edition actually inspected. Provenance therefore constrains downstream claims.

### Alternative explanation

This may be an editorial-edition concern rather than a research-framing concern. It becomes framing-relevant when the available source form changes which questions can responsibly be answered.

### Uncertainty / evidence ceiling

No claim is made that `paleo-type` needs Darwin-style metadata fields.

### Tentative generality

`cross-source recurrence of provenance-sensitive claim limits; implementation form unconstrained`.

---

## RF185-P04 — the accounting fixture has a structured transactional logic that transcription alone does not exhaust

### Direct observation / evidence

The Washington December 1767 cash account presents dated cash entries with counterparties/descriptions and monetary amounts, divided into receipts and `Contra` payments, ending with a balance.

DEPCHA describes historical financial records as highly structured administrative sources and states that individual information is often not the central research interest; significance can lie in aggregation of entries. It explicitly distinguishes textual, quantifiable and semantic dimensions that pure transcription does not fully cover.

### Interpretation

A research question about the economic/social meaning of an account can require a shift from literal entry transcription to transaction structure, aggregation, currency interpretation and relationships among people/goods/payments.

The appropriate research object therefore depends on the question: an exact entry may be the right unit for editorial verification, while a transaction set or account period may be necessary for economic interpretation.

### Alternative explanation

DEPCHA is itself a digital-modelling project and may privilege structured/linked-data research questions. The primary Washington account still independently demonstrates a repeated tabular/transactional structure, but the claim that aggregation is normally central is supported by DEPCHA's methodological framing rather than proved by this one account page alone.

### Uncertainty / evidence ceiling

No Bookkeeping Ontology or RDF model is thereby justified for `paleo-type`.

### Tentative generality

`account-source-specific positive evidence; cross-source support for question-dependent analytical scale`.

---

## RF185-P05 — accounting interpretation activates different expertise from Reg. Ii 5 without implying a permanent competence pipeline

### Direct observation / evidence

The Washington fixture contains monetary notation, account-side structure, counterparties and descriptions of rents, weaving, purchases, loans, household payments and a carried balance. DEPCHA's historical-accounts work explicitly combines documentary editors, historians, developers/digital humanists and domain modelling of economic transfers.

### Interpretation

A serious account-book question can require accounting/financial history, currency/metrology and economic/social interpretation in addition to documentary editing. Those competencies are materially different from the palaeographic/diplomatic emphasis of a difficult manuscript-reading problem.

The fixture therefore supports a **problem-relative competence space** rather than one permanent disciplinary sequence.

### Alternative explanation

The breadth visible in DEPCHA could reflect the goals of a digital-edition project rather than the minimum expertise for all account-book research. The safe conclusion is that materially implicated competencies vary with source/question, not that every listed competence must participate.

### Uncertainty / evidence ceiling

No stable lead/contribute/review topology is demonstrated.

### Tentative generality

`cross-source recurrence of problem-relative expertise; organizational model unproven`.

---

## RF185-P06 — isolation of individual account entries can impoverish questions whose evidence is inherently aggregate

### Direct observation / evidence

The Washington account is a sequence of receipts/payments plus a balance. DEPCHA explicitly states that historical accounts often gain research significance through aggregation and that individual information may not be the core research interest.

### Interpretation

For some accounting questions, forcing each entry to be analysed independently before allowing aggregate context would remove part of the phenomenon under study. This is a concrete form of **decomposition bias** external to the Reg. Ii 5 history.

### Alternative explanation

Entry-level isolation may still be necessary for transcription verification or anomaly checking. The problem is therefore not isolation itself but using it for a question whose evidence is relational/aggregate.

### Uncertainty / evidence ceiling

The fixture does not establish when aggregation becomes sufficiently reliable for interpretation; currency normalization and category assignment can themselves introduce assumptions.

### Tentative generality

`cross-source support for question-dependent independence/interaction balance`.

---

# Part B — cross-source comparative findings

## RF185-C01 — context timing is claim-dependent across all three source structures

### Comparative evidence

- **Reg. Ii 5:** context/comparator wording is deliberately excluded from contamination-sensitive source reading, then controlled comparison becomes useful after source-side structure/function is localized.
- **Darwin correspondence:** relational evidence from other letters and contextual/provenance evidence can be necessary to establish date or correspondent identity.
- **Washington accounts:** aggregate/accounting context can be necessary for transaction/economic meaning that is not available from an isolated lexical reading of one entry.

### Research interpretation

The comparison does not support one universal rule `context first` or `context last`.

A better descriptive hypothesis is:

> The legitimacy and timing of context depend on the claim being established and on whether that context is evidence for the claim, a hypothesis generator, or a contamination risk.

This is a Research generalisation, not a new METHOD rule.

### Generality status

`cross-source recurrence / provisional generic hypothesis`.

### Falsifier / limitation

A source/question class in which context timing is fully irrelevant, or a case where the same context type has a stable role across all claims, would narrow the hypothesis.

---

## RF185-C02 — `source address != analysis relation/unit` recurs, but the larger object differs by source and question

### Comparative evidence

- Reg. Ii 5: physical lines are stable addresses; paragraph/rule/correspondence range differ from those addresses.
- Darwin letter: the individual letter is the source object, while a dating question may require a correspondence relation/sequence.
- Washington account: an entry is addressable, while economic meaning may require transaction structure or aggregation across entries/account periods.

### Research interpretation

The cross-source recurrence is not `larger unit = better analysis`. Instead:

> The evidential/analytical object can differ from the stable source address, and its appropriate scale is determined by the question and available evidence.

### Generality status

`cross-source recurrence / relatively strong provisional generic hypothesis within this small sample`.

### Limitation

The sample is intentionally heterogeneous but small. No universal object ontology follows.

---

## RF185-C03 — positive scholarly ability appears as controlled scale/context switching, not one fixed framing operation

### Comparative evidence

Across the fixtures, good work may require:

- holding semantic context back during a contamination-sensitive source reading;
- bringing another letter or provenance evidence in to establish chronology;
- aggregating account entries to see transactional/economic significance;
- returning from a larger relation to a smaller direct source block when comparison has overreached.

### Research interpretation

A recurring productive practice is the ability to **change analytical scale and context exposure when the question/evidence changes**, while preserving provenance and the limits of each inference.

This is more strongly supported than the idea that one fixed `research framing layer` or one fixed sequence is already empirically demonstrated.

### Generality status

`cross-source recurrence / provisional generic practice`.

### Limitation

How such switching should be represented or operationalized remains completely open.

---

## RF185-C04 — transdisciplinary interaction is sometimes constitutive of the evidence, not merely a final synthesis step

### Comparative evidence

- Darwin dating can depend on documentary editing, archival provenance, correspondence chronology and historical/contextual clues during claim formation.
- accounting interpretation can depend on editing plus accounting/economic/currency knowledge while defining meaningful transactions or aggregates.
- Reg. Ii 5 G2 and #166 show source reading, structural/diplomatic evidence and controlled comparison interacting at different stages.

### Research interpretation

The evidence does not support a research design in which all competencies must first produce isolated complete judgements and only then be combined.

It also does not support unrestricted early joint reasoning. The descriptive recurrence is narrower:

> Some claims are only responsibly formed through sequenced or joint use of evidence owned by different competencies.

### Generality status

`cross-source recurrence / provisional generic hypothesis`.

### Limitation

No generic interaction mode, routing rule or role topology is established.

---

## RF185-C05 — independent checking and isolation remain distinct across heterogeneous fixtures

### Comparative evidence

- An exact Reg. Ii 5 grapheme/visual claim may need insulation from comparator wording.
- A Darwin date claim cannot be established from the letter in isolation when the year is omitted; independent checking may require consulting related letters and material/provenance clues.
- An accounting interpretation may require aggregation while still independently validating individual entries/amounts.

### Research interpretation

`Independent judgement` is better described by what evidence and premises were independently tested than by absence of interaction.

### Generality status

`cross-source recurrence / provisional generic research-design finding`.

### Limitation

This study does not experimentally compare model performance under isolated versus interactive conditions.

---

## RF185-C06 — question formation differs materially by source structure and purpose

### Comparative evidence

The natural high-value uncertainties exposed by the fixtures are structurally different:

- Reg. Ii 5: source-unit/function/relationship questions and whether local residual readings matter to understanding;
- Darwin letter: dating, correspondent/provenance and relationship to a correspondence sequence can dominate even when the short text itself is readable;
- Washington account: transaction structure, aggregation, currency/economic meaning and relationships can dominate over unresolved lexical reading.

### Research interpretation

The evidence weakens any assumption that `good research question generation` is one homogeneous operation independent of source type and Project purpose.

A future synthesis may still identify generic support functions, but the actual scholarly question-generating practice appears source-/purpose-sensitive.

### Generality status

`cross-source recurrence of heterogeneity; evidence against overly uniform capability assumptions`.

---

## RF185-C07 — external fixtures do not reproduce the repository's specific authority failures, and that negative result matters

### Direct comparative observation

Neither the Darwin nor Washington public fixture directly demonstrates the internal `resource unavailable → task STOP` failure, stale GitHub planning surface, or default-branch enforcement gap.

### Interpretation

Those internal phenomena should not be relabelled `generic historical-source problems` merely because they occurred in a research repository. Some are repository/governance-specific support-system risks.

### Generality status

`cross-source negative evidence against collapsing scientific and infrastructure problem classes`.

### Limitation

Comparable digital-edition projects may have analogous workflow/governance failures that are not visible from their public source pages.

---

# Part C — implications for existing Research hypotheses, without normative promotion

## 4. What gains empirical support

The heterogeneous fixtures provide support for the following descriptive propositions:

1. **Question-dependent analytical scale** recurs across visitation manuscript, correspondence and accounting sources.
2. **Context timing is claim-dependent**: context can be contaminating for one claim and constitutive evidence for another.
3. **Transdisciplinary interaction can occur during inquiry**, not only after independent monodisciplinary outputs are complete.
4. **Independent checking is not equivalent to isolation**; the important question is which premises/evidence were independently tested.
5. **Research-question formation is source-/purpose-sensitive**, even if later work discovers generic support functions.
6. Stable source/provenance identity remains relevant across very different source types, but no shared universal source ontology has been demonstrated.

## 5. What remains weak or unsupported

This pass does **not** empirically establish:

- a single generic question-generation capability;
- a permanent claim-relative leadership table;
- a mandatory Domain Review function;
- a candidate-question object;
- a semantic-handoff schema;
- a deterministic control-plane architecture;
- a Human-Owner decision-surface design;
- an AI allocation model;
- a universal analysis-unit type system.

The external evidence is more supportive of **adaptive scholarly practice and explicit evidential boundaries** than of any one system representation.

## 6. Relation to Requirement-efficacy research

The external fixtures primarily test scientific/source heterogeneity rather than the repository's current Requirements.

They nevertheless constrain later Requirement reasoning:

- a Requirement that universally forced source-local isolation would be unsafe for correspondence dating or aggregate account interpretation;
- a Requirement that universally forced early contextual integration would be unsafe for contamination-sensitive reading;
- a Requirement that equated source address with analysis unit would fail across all three fixtures;
- a Requirement that made a fixed competence list mandatory would overfit the source/question combinations observed here.

These are **constraint observations for later synthesis**, not new Requirements created by this file.

## 7. External-source epistemic roles

| Source | Role in this Research |
|---|---|
| Darwin Letter 5098 public edition | bounded primary/source fixture and editorial metadata |
| Darwin Editorial policy and practice | methodological/editorial evidence explaining dating/identification/provenance practice |
| Darwin project overview/technical page | project/editing context; not authority over `paleo-type` method |
| Washington Cash Accounts Dec. 1767 | bounded primary/source fixture and source locator |
| Papers of George Washington overview | documentary-edition/project context |
| DEPCHA project page | methodological/digital-humanities evidence on historical account structure and aggregation |
| Pollin 2019 / DOI 10.5281/zenodo.3446143 | methodological/technical comparative evidence; not a mandatory ontology recommendation |

## 8. HCI / Human-Owner evidence boundary

The external fixtures provide no direct observation of the `paleo-type` Human Owner using a decision surface.

No claim about an empirically successful Owner UI/decision format follows.

At most, the source comparison shows that any future decision surface would need to preserve differences in source purpose, evidence type, uncertainty and analytical scale rather than flattening all candidate questions into one uniform object without evidence.

Evidence status: `scenario/inference only`, not `human-observed`.

## 9. Limits and threats to validity

- Only two external source fixtures were added.
- The Darwin and Washington materials are already scholarly edited/public interfaces rather than fresh independent manuscript examinations in this Research run.
- Editorial-project documentation can reflect the projects' own methodological commitments.
- The account aggregation argument is supported partly by DEPCHA, a project specifically interested in structured/linkable account data.
- No experimental comparison of isolated versus interactive AI/research contexts was performed.
- Cross-source recurrence in this small sample justifies only provisional generic hypotheses.
- These findings must remain distinguishable from #184's internal Requirement-efficacy evidence.

## 10. Frozen cross-source evidence package for #186

The main cross-source findings to carry forward are:

- **RF185-C01:** context timing is claim-dependent;
- **RF185-C02:** stable source address and useful analytical relation/unit are not identical;
- **RF185-C03:** controlled scale/context switching is more empirically visible than one fixed framing operation;
- **RF185-C04:** transdisciplinary interaction can be constitutive during inquiry;
- **RF185-C05:** independence does not imply isolation;
- **RF185-C06:** question formation is materially source-/purpose-sensitive;
- **RF185-C07:** infrastructure/governance failures must not be promoted into generic source-research problems without analogous evidence.

#186 may compare these findings with #184 and later challenge the Concept Candidate, but it must not rewrite the fixture-level findings to make them fit a preferred architecture.

No normative Capability/Requirement/Solution decision is made here.
