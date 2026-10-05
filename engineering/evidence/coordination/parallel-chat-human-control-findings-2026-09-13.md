# Parallel-chat human-control findings — 2026-09-13

Status: **analytical / evaluation evidence under #162, incorporating Pilot 2 (#171); not normative METHOD, not a new canonical research-state owner, not a frozen message schema, and not implementation admission for a bot/router/wake service, orchestration layer or other material research-system change**.

Baseline rechecked before this consolidation: `main@55bf9782c694282715f9a549be15c6fb0a721ca0`.

This record consolidates the coordination/human-control ideas, pilot observations, design approaches and limits that otherwise remain scattered across #162, #171, Slack and transient ChatGPT discussions. It supplements `requirements/parallel-chat-coordination-audit-2026-09-12.md`. In particular, the older audit's dated Slack capability uncertainty is historical: live Pilot 1/2 evidence subsequently demonstrated direct Slack read/write from the connected normal ChatGPT contexts used here. That capability correction does **not** establish Slack as accepted architecture.

Canonical authority remains `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, applicable `REQ-*`, `methodology/workflow.md`, `methodology/maintenance.md`, `methodology/ai-governance.md` and the owning Project/Corpus state.

## 1. Problem decomposition

The observed coordination problem is not one problem. At least six distinct burdens/failure modes must remain separate:

1. **Content-courier burden** — the Human Owner copies or paraphrases substantive requests/replies between parallel chats.
2. **Orientation burden** — the Human Owner must open many projects/chats merely to discover what happened, what is blocked and where a decision is needed.
3. **Activation burden** — a normal ChatGPT chat does not wake merely because another context or Slack posted something; the Human Owner may still have to resume it.
4. **Human-feedback continuity** — feedback written by the Human Owner on an external surface may not reach the intended normal ChatGPT context at all unless that context later polls/reads the surface.
5. **Conversation-topology/audit burden** — Slack creates its own top-level messages, threads and replies outside ChatGPT, so the Human Owner can lose the connection between a visible chat statement and the actual external object.
6. **Authority/staleness and premise-stack risk** — a sender message can be mistaken for current authority, and even a fresh independent review can repeat the same derived premise if it does not rehydrate the relevant primary canonical/evidence owners deeply enough.

Pilot evidence shows that removing content copy/paste is useful but insufficient. A coordination mechanism is not successful if it reduces courier work while increasing orientation/control burden or obscuring where authority and decisions live.

## 2. Human Owner role

The desired Human Owner role is **supervisor/editor/project owner, not routine dispatcher or message courier**.

The Human Owner should be able to:

- see what is running, blocked, answered or awaiting owner judgement without visiting every work context;
- inspect any consequential external action directly;
- intervene in a normal ChatGPT work context where actual work/reasoning is visible;
- make the genuinely owner-reserved purpose/scope/priority/material-change decisions;
- challenge or stop work without first reconstructing hidden inter-context traffic.

The Human Owner should **not** be required to:

- copy ordinary A→B→A review content;
- reconcile two parallel hidden conversation histories;
- monitor Slack merely to ensure that a chat did not silently act;
- infer whether feedback posted in Slack has actually reached a chat;
- approve every low-risk mechanical step merely to compensate for weak boundaries.

A useful operating principle is:

> The Human Owner does not need to watch everything, but everything consequential must remain observable, attributable and challengeable.

## 3. Layer model: control surface, transport, authority

The current evidence supports a strict three-layer distinction.

```text
ChatGPT normal chats
= visible work / reasoning / immediate Human-Owner steering surface

Slack coordination channel
= non-canonical transport / bulletin board / delivery journal

GitHub repository + owning Issues/PRs
= durable authority / restartable state / work-audit metadata
```

More precisely:

- **ChatGPT chats** are execution/work contexts. They are the primary human-facing place to inspect and steer the work performed in that context. They are not canonical research-state owners and are not historical evidence.
- **Slack** may transport bounded requests/replies, show human-readable status and expose links. It must not become a second truth/decision layer.
- **GitHub/repository owners** remain authoritative for durable Project, Corpus, METHOD and admitted work state. Issues/PRs remain work/audit metadata where appropriate; canonical files remain the owners of research/method truth.

This avoids calling ChatGPT a "primary source", which would collide with the repository's historical-source terminology.

## 4. Passive bulletin-board boundary

The useful Slack concept is a deliberately **passive bulletin board / wall newspaper / mailbox**, not an autonomous coordination agent.

Allowed transport/mechanical behavior may include, where the platform supports it:

- deliver/read a bounded request or response;
- retain a thread/permalink for human inspection;
- carry correlation/routing metadata;
- expose simple mechanical delivery states such as sent/received/answered when those states are actually known;
- link to the current task/Issue owner;
- present a short human-readable summary/status.

The channel must not independently:

- select or change Project/research priority;
- create or replace `NEXT ACTION`;
- expand scope;
- mark a scholarly/review result accepted merely because a reply exists;
- create a new research truth or evidence status;
- adjudicate palaeographic/philological/historical claims;
- treat a sender SHA or sender summary as current canonical state;
- become the durable memory from which future research state must be reconstructed.

A concise boundary is:

> The coordination channel may transport, display and perform deterministic delivery mechanics. It may not manufacture scholarly or project authority.

## 5. Machine block + human block concept

A two-layer message is a promising presentation approach, but the pilot does **not** justify freezing a schema.

### Machine-facing portion

The machine-facing part may be optimized aggressively for routing/correlation and token cost once actual stable needs are demonstrated. Candidate semantics include only what is required to locate and correlate the exchange, for example:

```text
id
from / to role-context
repo
current task / Issue owner pointer
kind = request | response | feedback | status
sender basis/checkpoint when relevant
reply/thread correlation
```

Stable Project/Source/File facts should still be derived from canonical owners rather than recopied into every packet.

### Human-facing portion

The human-facing part should remain deliberately readable rather than maximally compressed. In roughly five seconds the Human Owner should be able to answer:

- What happened?
- Who needs something from whom?
- What is being asked/returned?
- Does the Human Owner need to act?
- Where are the details?
- Has any durable consequence already been persisted to the correct repo owner?

The machine block routes; the human block explains. Neither becomes authority.

## 6. No silent external side effects: sender-side permalink rule

Pilot 2 established a concrete control requirement: **a normal ChatGPT context that performs a consequential external send must expose that action immediately in its own visible transcript**.

For every consequential Slack send, the sending ChatGPT transcript should expose:

1. the exact Slack permalink returned for the message;
2. a short human-readable statement of what was sent and why;
3. the relevant repo/task owner pointer when applicable;
4. whether the external send is transport/review only or whether a durable consequence was separately persisted to the canonical repo owner.

The same principle applies to other external coordination surfaces: a human must not have to trust the chat's claim that something was sent without an inspectable object pointer.

A stable correlation ID such as `PILOT-171-B1` is useful because it lets the Human Owner correlate ChatGPT, Slack and GitHub references without merging their separate conversation structures.

The permalink/correlation ID is an **audit and UX pointer only**. It is not Research-State-Authority.

## 7. Human feedback entered in Slack

Pilot 2 demonstrated a hard current platform boundary:

```text
Human Owner writes feedback in Slack
→ normal ChatGPT context is not automatically activated
→ feedback may remain orphaned until that context is explicitly resumed and reads Slack
```

Therefore, under the current normal-chat premise:

- Slack cannot be assumed to be the primary Human-Owner control surface;
- feedback written only in Slack must not be assumed to have changed any chat/task/canonical state;
- a chat that later consumes Human-Owner Slack feedback should state visibly in its own ChatGPT transcript that it received/used that feedback and should expose the source Slack permalink where practical.

There are only two coherent future boundaries:

1. **Slack remains bulletin/read surface only.** The Human Owner steers work in ChatGPT; Slack provides overview/delivery/history.
2. **Slack becomes an accepted input surface.** Then a separately analysed/admitted mechanism must reliably deliver/activate the addressed work context and make that feedback visibly acknowledged there.

Option 2 is materially different from passive transport. No bot, router, webhook, Work trigger, API/external orchestrator or other wake/dispatch architecture is admitted by this record.

## 8. Conversation topology: bounded transactions, not open autonomous dialogue

Slack's own thread structure is useful for transport but dangerous if it becomes a second place where the actual project conversation lives.

The preferred future interaction shape is therefore **bounded and transactional**, for example:

```text
request
→ independent rehydration/work
→ response
→ optional bounded follow-up if needed
→ close / persist durable consequence in existing owner
```

Avoid open-ended A↔B loops with no explicit completion condition. The objective is not to make chats talk indefinitely; it is to remove unnecessary Human-Owner courier work while preserving human control.

This also means that "one more message" should be justified by a material state/question/evidence delta, consistent with existing no-progress semantics in `methodology/workflow.md`.

## 9. Anti-"Eigenleben" control principles

The Human Owner's concern that parallel chats could develop hard-to-follow "Eigenleben" is a first-class usability/governance concern, not merely a comfort issue.

The following design heuristics are therefore retained for any future concept evaluation:

- **bounded delegation:** a chat may work autonomously only inside an already authorized bounded task;
- **no self-expanding authority:** a chat may not enlarge purpose/scope/priority merely because another chat suggested it;
- **no silent side effects:** consequential external writes/actions are surfaced locally with inspectable pointers;
- **explicit completion/stop conditions:** no open-ended inter-chat loop by default;
- **owner checkpoints at true decision boundaries:** request Human Owner judgement where owner-reserved meaning changes, not for every deterministic low-risk step;
- **avoid approval fatigue:** excessive approvals are not a substitute for clear boundaries and observability;
- **status before detail:** a bulletin view should make `what happened / human action needed? / where are details? / persisted?` immediately visible;
- **observable rather than continuously watched:** a human should be able to audit consequential behavior without personally following every routine exchange in real time;
- **no orchestrator by default:** do not introduce an agent manager, router, workflow engine or coordination database until a demonstrated need survives the simpler bounded model.

These are retained as evaluation principles, not promoted here to generic METHOD or executable schema.

## 10. Receiver freshness and anti-authority-laundering

Pilot 1 established the primary transport risk: **authority/staleness laundering through the messenger**.

A receiver must not treat sender-provided state as authoritative merely because it arrived in a structured packet. A sender SHA is useful only as a basis hint.

The stronger rule exposed by the pilot is:

> Fresh HEAD alone is not enough when task/owner/scope/evidence state can change independently. Before consequential use of an incoming request, the receiver must freshly resolve the applicable current canonical task/owner state needed for that request.

For cross-repository work, each repository remains sovereign over its own state and instructions.

## 11. Independence requires evidence depth, not merely a fresh context

Pilot 2 added an important epistemic learning that transport mechanics do not solve.

The B1 review freshly rehydrated repository state but did not explicitly inspect the strongest primary structural owners for the disputed unit relation. It therefore repeated a derived premise (`restored the cross-folio unit`) later challenged by a deeper owner/evidence re-read.

Consequences:

- separate ChatGPT contexts do not automatically provide independent evidence if both inherit the same derived premise stack;
- "fresh repo read" is necessary but not sufficient for high-value adversarial review;
- the review depth must match the concrete claim: inspect the relevant canonical/evidence owners, not merely current summaries/issues that already encode the disputed inference;
- messenger structure must never be mistaken for epistemic independence.

This is an evaluation finding about review quality, not a new specialist method rule.

## 12. What a human-facing bulletin should optimize

A central bulletin view is useful because it can reduce **orientation burden**, even if it cannot remove activation burden.

A useful human-facing item should privilege compact state such as:

```text
[REVIEW] source-understanding question
status: answer available
from / for: review → research
human action: none
repo owner: #...
chat/slack pointer: ...
durable consequence: none | persisted at ...
```

The Human Owner should not need to open every ChatGPT thread merely to learn status. But the bulletin must also make it clear when it is only reporting transport rather than authority.

The strongest usability test is not "did Slack carry the message?" but:

> Did total Human-Owner burden fall without reducing control, auditability or authority clarity?

## 13. Issue boundary

Current issue routing is now clear:

- **#171** is closed at the demonstrated Pilot 2 ceiling. It owns the bounded pilot history/evidence, not a future architecture.
- **#162** remains the broader deferred coordination owner. It is paused and not on the current scholarly critical path.

A new technical/process Issue is justified only when there is an **independently actionable desired system property**, not merely another observation. Example:

> Human Owner explicitly wants Slack to be a steering input, and feedback entered there must reliably reach the addressed work context and become visibly acknowledged in that ChatGPT transcript without Slack becoming authority.

At that point the new Issue should first own problem/requirements/concept analysis. It must not preselect Work, webhook, bot, API, plugin, external orchestrator or another implementation merely because one could provide wake-up.

A permalink/correlation convention or other small pilot acceptance criterion alone does not require its own architecture Issue while #162 remains the suitable deferred owner.

## 14. Future-pilot acceptance dimensions

If #162 is ever reactivated, a future bounded test should measure more than message transport.

At minimum evaluate:

- **courier burden:** zero substantive Human-Owner copy/paraphrase between participating contexts;
- **orientation burden:** Human Owner can understand current state without opening every chat;
- **activation burden:** measured separately rather than disguised as transport success;
- **feedback continuity:** no Human-Owner feedback is silently orphaned or assumed consumed when it was not;
- **local transparency:** every consequential external send is visible in the sending chat with exact permalink/correlation;
- **receiver freshness:** receiver re-resolves the applicable current canonical task/owner/evidence state;
- **authority boundary:** Slack/chat messages never auto-promote themselves to canonical truth or owner decisions;
- **persistence boundary:** durable consequence reaches the existing correct repo owner;
- **boundedness:** no open-ended no-delta inter-chat loop;
- **total owner burden:** the mechanism lowers total cognitive/control work, not only copy/paste;
- **human control:** owner can stop/challenge the process without having to reconstruct a second hidden control history;
- **review quality:** independent review reaches the evidence depth appropriate to the challenged claim.

## 15. Established, unestablished and deliberately not admitted

### Established by live project evidence

- direct Slack read/write from the connected normal ChatGPT contexts used in this workspace/channel works;
- bounded A→B→A transport can occur without substantive Human-Owner copy/paste;
- a real research→review message can be received, independently worked and returned through Slack;
- normal chats do not automatically wake from Slack messages;
- Human-Owner Slack feedback can remain ineffective until a chat explicitly reads it;
- Slack creates a separate conversation topology requiring explicit correlation for human auditability;
- sender-side exact permalinks materially improve inspectability/correlation;
- fresh independent context alone does not guarantee evidence-independent review.

### Not yet established

- that Slack is the preferred long-term transport;
- that a bulletin-board workflow sustainably reduces total Human-Owner burden;
- that the Human Owner can use Slack as a reliable primary steering input;
- automatic activation/wake-up of normal chats;
- cross-repository ergonomics at scale;
- that automation is needed at all after bounded passive transport/overview is optimized.

### Deliberately not admitted

- bot/router/bridge/webhook service;
- Slack→GitHub mirroring;
- coordination/prompt database;
- agent/orchestrator framework;
- mandatory machine-message schema;
- new METHOD/gate semantics;
- a second canonical state store;
- any architecture conclusion of the form `Slack is the answer`.

## 16. Evidence / restart pointers

Primary work/audit owners:

- #162 — deferred parent coordination question: https://github.com/esany/paleo-type/issues/162
- #171 — closed Pilot 2: https://github.com/esany/paleo-type/issues/171
- prior analytical audit: `requirements/parallel-chat-coordination-audit-2026-09-12.md`

Pilot 2 Slack pointers:

- A1 research→review parent: https://aixpost.slack.com/archives/C0C0ZDZL1B9/p1789286840251279
- B1 review reply: https://aixpost.slack.com/archives/C0C0ZDZL1B9/p1789287120416379?thread_ts=1789286840.251279&cid=C0C0ZDZL1B9
- Human-Owner feedback that exposed continuity/activation weakness: Slack message `1789287170.818759` in `#paleo-type-coordination`
- reply recording that weakness: https://aixpost.slack.com/archives/C0C0ZDZL1B9/p1789287499633169?thread_ts=1789287170.818759&cid=C0C0ZDZL1B9
- permalink-disclosure clarification: https://aixpost.slack.com/archives/C0C0ZDZL1B9/p1789322521347069?thread_ts=1789287170.818759&cid=C0C0ZDZL1B9

Relevant #171 comments include:

- `5652157537` — Human feedback does not automatically reach a normal ChatGPT context;
- `5655060872` — sender-side Slack permalink disclosure;
- `5655302434` — evidence-depth / shared-derived-premise learning from fresh primary-owner re-evaluation.

## 17. Current disposition

The transport hypothesis is partly demonstrated; the coordination/control hypothesis remains unresolved.

The correct current disposition is therefore:

```text
preserve evidence
→ keep #162 deferred
→ do not build coordination architecture from the pilot
→ return attention to the current scholarly critical path
→ reactivate only on a new explicit Human-Owner need and a bounded testable property
```

This record is intentionally comprehensive enough that a future capable context should not need the originating chats to recover the Pilot 1/2 control findings, while remaining non-normative and subordinate to the repository's canonical owners.