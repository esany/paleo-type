# Parallel ChatGPT coordination audit — 2026-09-12

Status: **analytical / planning evidence for #162; not normative METHOD, not a new truth owner, and not implementation admission for an external messenger, agent runtime or automation layer**.

Baseline audited: `main@15c225bffd9d13d817413c4a7de0c7b09f23e35d`.

Primary bounded owner: #162. Historical owners #71/#77 remain closed/completed; this audit treats the newly demonstrated human-courier problem as the bounded regression that #77's closure explicitly anticipated.

Canonical authority remains `GOVERNING_OBJECTIVE.md`, `AGENTS.md`, applicable `REQ-*`, `methodology/workflow.md`, `methodology/maintenance.md`, `methodology/ai-governance.md` and the owning Project/Corpus state. This file records the audit and capability snapshot so the reasoning does not remain only in chat.

## 1. Demonstrated problem

The repository already solves a large part of cross-chat work correctly:

```text
specialized chat/work context
→ reconstruct role/task from canonical repository state
→ perform bounded work
→ persist consequential durable state to its canonical owner
→ another capable context can resume without old chat
```

That is **restartability and handoff integrity**.

The newly demonstrated problem is different:

```text
Chat A develops a concept
→ asks Chat B for review
→ B returns an objection
→ A asks a follow-up
→ B refines the review
```

Today the Human Owner often carries those intermediate messages manually between parallel chats. Telling both chats to `document everything` or `read the repo freshly` does not remove that burden:

- durable facts can be recovered from the repository;
- the live request/reply itself may still be transient and not yet worthy of canonical persistence;
- a receiving chat does not automatically know that another chat has just sent it a bounded question;
- the owner therefore becomes the message transport even when no owner decision is involved.

This is a **live coordination transport gap**, not a failure of canonical research persistence and not evidence that a multi-agent runtime is required.

## 2. What the current repository already solves

### 2.1 Canonical state and restartability

`AGENTS.md` requires applicable context to be loaded from canonical owners, rejects chat as a durable research-state owner and requires persistable/restart-relevant research state to be written through the repository when an authorized path exists.

`README.md` defines the repository reading path and explicitly states that old chat must not be required to reconstruct durable research state.

`tools/project_context.py` provides a rebuildable read-only Project context from canonical owners and deliberately refuses to infer Project authority, `NEXT ACTION`, research function, evidence access or scholarly judgement.

Therefore a messenger must **not** become a second Project/Source/research-state store.

### 2.2 Cross-role work-context contract

`methodology/workflow.md` already owns the required semantics for consequential role/task execution:

- role/responsibility;
- task/Issue owner;
- current executable stage;
- first/next bounded action;
- prerequisites plus invalidation;
- evidence/access state;
- execution cursor;
- completion condition;
- out-of-scope/not-authorized work;
- handoff target;
- return/review condition.

These are semantic requirements, not mandatory field labels or a template serialization.

### 2.3 Prior #71/#77 result

#71 correctly framed specialization as a responsibility-routing/restartability problem rather than a reason to build a multi-agent architecture.

#77 then tested real handoffs, distinguished session continuation from later role-result handoff, established that a specialized chat is never the sole durable owner of consequential knowledge, and explicitly stated that the human should not act as courier for knowledge already stored in the workflow.

#77 closed on 2026-09-08 because `methodology/workflow.md` had absorbed the generic work-context/handoff semantics. Its closure states that a future concrete handoff omission should be handled as a **bounded regression against the workflow**, not by retaining a standing prompt/agent-framework programme.

The present case is exactly such a bounded regression, but at a different layer: the semantics of a handoff are present; the **transport for iterative parallel-chat exchange** is not.

## 3. Governing requirements activated by the new failure

No new Requirement family is justified by this audit.

| Existing requirement / invariant | Consequence for parallel-chat coordination |
|---|---|
| Governing Objective — human auditability | The owner must be able to inspect what each chat is doing and challenge consequential actions; a hidden agent conversation is a poor default. |
| Governing Objective — technical subsidiarity | Choose the least complex transport that removes the demonstrated courier burden; do not build orchestration because it is architecturally attractive. |
| Governing Objective — canonical/restartable state | Transport messages never become canonical truth merely because another chat asserted them. |
| REQ-AI-001 / REQ-AI-002 | The receiver still reconstructs applicable context from the repository; a sender message may narrow the question but may not replace governing context. |
| REQ-AI-003 | AI message/output remains distinct from evidence, inference and independent validation. |
| REQ-AI-007 | Analysis/coordination, canonical research write and material architecture change keep separate authority paths. |
| REQ-AI-010 | A role-to-role review request must not turn the non-specialist owner into a substitute specialist validator. |
| REQ-RSE-010 | Any automation that writes canonical research state must remain narrower than scholarly judgement and reviewable. A messenger should normally write only coordination/work metadata. |
| REQ-UX-011 | Deterministically resolvable mechanics should be handled by the system; the researcher should not become the repository operator or message courier for routine AI work. This is the strongest directly demonstrated usability requirement here. |
| REQ-UX-012 | Consequential actions remain explainable/challengeable in ordinary language; the owner should be able to see what was requested, returned and acted on. |
| `methodology/ai-governance.md` | Do not archive every prompt/routine exchange as AI provenance. Persist only consequential influence proportionally. External services require rights/confidentiality/data-handling review. |
| `methodology/maintenance.md` / D-016 | A new external bridge, workflow engine, webhook router or agent/orchestration layer is a material research-system choice if it changes shared workflow/ownership/automation semantics; analysis may proceed, implementation requires the established admission boundary. |

### Result

The actual requirement is **not** `make chats autonomous`.

It is:

> Remove the Human Owner as courier for ordinary role-to-role requests/replies while preserving visible chat work, fresh canonical rehydration, non-canonical transport semantics and existing authority/review boundaries.

## 4. Requirements derived for a transport

A candidate transport is adequate only if it satisfies the following properties in a real pilot.

### 4.1 Direct enough to remove content courier work

A participating chat must be able to place a bounded request where another participating chat can retrieve it, and the receiver must be able to return a response to the same shared surface.

The Human Owner may still need to **resume** a normal chat if the platform does not support background execution. Success does not require automatic wake-up. It does require that the owner no longer copies/paraphrases the substantive message.

### 4.2 Visible in each normal ChatGPT conversation

The shared transport is not a replacement for the user's ordinary ChatGPT inspection surface.

For consequential coordination, each chat should say in its own conversation, in ordinary language:

- that it sent or received a coordination message;
- which task/role it concerns;
- what actionable content/consequence it is using.

This preserves the user's ability to inspect the participating chats rather than moving the actual collaboration into an opaque external system.

### 4.3 Non-canonical by design

A transport message may contain a request, hypothesis, review objection or return question. It does not become research/method truth until the appropriate existing owner receives a normal consequential write/review transition.

Durable decisions, review outcomes and canonical research state remain in the owning repository surfaces: canonical files, task Issues/PR reviews/comments and Project research owners as applicable.

### 4.4 Sender narrative never outranks fresh repository state

A message may include a sender checkpoint such as `repo@SHA`, but the receiver must freshly establish current repository state before acting where staleness matters.

A stale message cannot resurrect an old `NEXT ACTION`, scope, evidence state or requirement.

### 4.5 Minimal message semantics

Do not freeze a message schema before the real pilot. The receiver must only be able to reconstruct, semantically:

```text
TARGET ROLE / CONTEXT
REPO + TASK / ISSUE OWNER
BASIS / sender checkpoint where relevant
REQUEST or RESPONSE
RETURN / FOLLOW-UP EXPECTATION
```

Stable Project/Source/File facts should be derived from canonical owners, not copied into every message.

### 4.6 Cross-repository sovereignty

A coordination message may reference more than one repository, but each repository remains the authority for its own state. The receiving chat must load each relevant repo's own default branch/HEAD and local instructions.

Cross-repository synthesis remains a work-context result until deliberately persisted through the relevant repository's owner/review path.

## 5. Capability snapshot — 2026-09-12

This section is intentionally dated. Product capabilities and regional availability are volatile and must not become permanent architectural truth.

### 5.1 GitHub — verified current path

The connected GitHub surface available to this normal ChatGPT context exposes Issue/comment read/write operations.

A live preflight was executed in #162:

1. this chat wrote issue comment `#issuecomment-5648045256` directly;
2. this chat then fetched the #162 comments and recovered the same content;
3. the Human Owner did not manually copy the test message into GitHub.

This proves **one-context read/write transport capability** on the exact surface already used by the repository.

Still unverified until the required pilot:

- second independent normal ChatGPT chat reads the message;
- second chat replies;
- first chat reads that reply;
- at least one follow-up round occurs without the owner relaying substantive content.

GitHub does not itself make a normal ChatGPT chat a background worker. Polling/resume remains a separate question.

### 5.2 Slack — earlier attractive concept, current feasibility not established

The earlier conversational hypothesis `Slack is the best bus` is **not currently strong enough to adopt**.

Current official OpenAI documentation distinguishes:

- **Slack in ChatGPT** — ChatGPT can search permitted Slack messages/threads/channels and, where enabled, perform a documented set of Slack actions;
- **ChatGPT in Slack** — ChatGPT conversations can run inside Slack and draft posts/replies there.

Official sources inspected:

- https://help.openai.com/en/articles/12525822-chatgpt-slack-app
- https://help.openai.com/en/articles/12462158-chatgpt-app-in-slack

Current constraints relevant to this project:

1. OpenAI currently states that the ChatGPT Slack app is **not available to Plus and Pro users in the EEA, Great Britain and Switzerland**; Business/Enterprise are not affected.
2. The documented `Slack in ChatGPT` action list includes operations such as joining/leaving conversations, reminders, file upload and profile updates, but the inspected documentation does **not establish an arbitrary `post message to channel` action from an existing normal ChatGPT chat** sufficient for the proposed A↔B bus.
3. The local ChatGPT plugin directory query on 2026-09-12 did return a Slack integration entry, but plugin-list presence is not proof that connection/action scope is usable for the current plan/region/workspace.
4. Slack event-triggered Work tasks exist in the current product, but that is a different execution mode and would change the current `normal chats without background agent/work runtime` premise.

Therefore Slack is **candidate/deferred pending an exact capability test**, not the current recommended transport.

### 5.3 Discord — no direct current path demonstrated

A current ChatGPT plugin-directory search for `Discord` did not return a Discord integration. A Discord webhook/bot could be built externally, but that would introduce a bridge/service and still require a return path for messages back into normal ChatGPT chats.

That is strictly more infrastructure than the demonstrated GitHub path and fails technical subsidiarity for the first pilot.

Disposition: **defer/reject for first pilot**.

### 5.4 Repo file / mailbox branch

A Git file/branch mailbox is technically possible but a poor fit for conversational transport:

- every message becomes commit/state noise;
- parallel writers risk merge/ref conflicts;
- transient coordination is encouraged to look like durable repository truth;
- human readability is worse than an Issue thread;
- cross-repo routing becomes awkward.

Disposition: **reject unless a later concrete failure makes Issue comments unusable**.

## 6. Candidate comparison

| Criterion | GitHub Issue/comments | Slack | Discord | Git file/mailbox |
|---|---|---|---|---|
| Normal-chat read in current environment | verified for this chat | documented search capability, but current plan/region may block | not demonstrated | via GitHub file read |
| Normal-chat write suitable for request/reply | verified for this chat; second-chat pilot pending | arbitrary channel-post action not established by inspected docs | not demonstrated without bridge | possible but commit-heavy |
| New external service required | no | yes | yes | no |
| Fits existing work/audit metadata semantics | strong | medium | medium | weak |
| Keeps canonical research truth separate | strong if explicitly non-canonical | possible | possible | weak / easy to blur |
| Human inspectability | strong | strong if available | strong for human UI | medium |
| Conversational fit | medium | potentially strong | potentially strong | poor |
| Cross-repo use | strong by reference | strong | strong | weak/fragmented |
| Automatic wake-up of normal chats | no | no under this normal-chat premise | no | no |
| Current first-pilot feasibility | **high** | **low/unverified** | **low** | **low** |

## 7. Recommended concept

### 7.1 First transport: task-owned GitHub Issue/comment thread

Use the **existing task/review Issue or PR thread whenever one clearly owns the work**. Avoid a universal `agent message board` by default.

Pattern:

```text
Chat A (visible normal chat)
  → posts bounded request to task Issue/PR

Chat B (visible normal chat)
  → on resume, checks task thread
  → freshly rehydrates relevant repo state
  → posts review/answer to same thread

Chat A
  → on resume, checks thread
  → handles answer/follow-up

consequential durable outcome
  → existing canonical owner / Issue / PR review path
```

A dedicated coordination Issue such as #162 is appropriate for the **pilot and cross-cutting transport evaluation**. It should not become a universal parallel truth store.

### 7.2 Human role

The owner remains supervisor/authority, not message bus.

Acceptable owner actions:

- resume a chat (`continue`, `check the task thread`) when normal chats cannot wake automatically;
- make genuinely owner-reserved purpose/scope/rights/publication/material-change decisions;
- inspect/challenge either chat and the GitHub exchange.

Failure condition:

- the owner must copy, paraphrase or reconcile ordinary role-to-role request/response content merely to keep the collaboration moving.

### 7.3 Chat visibility rule

The user asked specifically that the chats themselves remain transparent. Therefore a successful transport pilot must preserve two views at once:

```text
ChatGPT chat = local visible work / explanation / consequence
GitHub thread = shared role-to-role transport + durable work/review metadata where appropriate
canonical file owners = research/method truth
```

A chat may reference a transport comment rather than reprinting it in full, but it should make the send/receive event and substantive consequence visible in its own response.

## 8. Pilot protocol for #162

Use two already useful parallel normal ChatGPT contexts with genuinely different functions, preferably `concept/domain review` or `domain review/dev review`.

### Round 1

Chat A:

1. reads current repo state;
2. performs its bounded work;
3. posts one real review request to #162 or the actual owning task Issue;
4. states in its own ChatGPT response that the request was posted and what it asks.

### Round 2

Human only resumes Chat B; **does not paste A's message**.

Chat B:

1. reads the shared Issue/comment thread;
2. resolves current repository state independently;
3. performs the requested review;
4. posts the result to the thread;
5. states in its own ChatGPT response what it received and returned.

### Round 3

Human only resumes Chat A; **does not paste B's answer**.

Chat A:

1. reads the reply;
2. either incorporates it or posts a bounded follow-up;
3. a second B response completes the ping-pong fixture if useful.

### Pilot success

Pass only if:

- zero substantive message content is relayed by the Human Owner;
- both normal ChatGPT conversations remain inspectable;
- each receiving chat freshly respects canonical repo state;
- no transport assertion is auto-promoted to research truth;
- any durable review/decision lands in the correct existing owner;
- the process uses materially less owner effort than manual copying;
- Issue traffic remains tolerable.

Record at least:

```text
courier burden: removed | partial | not removed
owner resume/poll actions: count + nature
message rounds: count
stale-context problems: yes/no + consequence
issue-thread noise: low/medium/high
chat-level transparency: adequate/inadequate
second service needed: yes/no + demonstrated reason
```

## 9. What is explicitly not justified yet

This audit does **not** justify:

- Slack adoption;
- Discord bot/webhook work;
- a GitHub Action router;
- a message queue/database;
- autonomous agents;
- automatic wake-up/background execution;
- a universal role/address registry;
- a new METHOD file for coordination;
- mandatory message syntax;
- logging every prompt or every transient message as research provenance.

If the GitHub two-chat pilot fails because manual polling/resume itself remains a material bottleneck, that is new evidence. At that point re-evaluate an event-driven runtime or external transport under D-016 rather than assuming it in advance.

## 10. Cross-repository extension

No separate architecture is required for the first cross-repo case.

A message should identify the relevant repositories and task owner(s), e.g. conceptually:

```text
TARGET: development-review
REPOS: repo-A, repo-B
TASK OWNER: repo-A#123
SENDER BASIS: repo-A@sha-x; repo-B@sha-y
REQUEST: inspect interface consequence X
RETURN: comment on repo-A#123; persist repo-B change only if its own owner requires it
```

The receiver then freshly loads each repo's own instructions and current state. It must not treat one repo's message as authority to mutate the other.

If cross-repo work later becomes frequent enough that no single task Issue is a truthful coordination home, a neutral coordination surface may become justified. That trigger has not yet been demonstrated.

## 11. Disposition of the earlier conversational proposals

| Earlier proposal/claim | Audit disposition |
|---|---|
| `We already do this through repo-first restartability.` | **Partly true.** Durable restart/handoff is solved; iterative live role-to-role transport is not. |
| `Create a GitHub messenger board.` | **Refine.** Use task-owned Issue/PR threads first; dedicated board only where cross-cutting coordination actually needs one. |
| `Slack is the best solution.` | **Withdraw as current recommendation.** Attractive conversationally, but current plan/region availability and arbitrary post-action capability are not established for this use case. |
| `Discord is an easy free alternative.` | **Reject for now.** Cost is not the governing issue; lack of direct normal-chat integration means extra bridge infrastructure. |
| `This can all run with normal chats and no agent runtime.` | **Yes for asynchronous read/write ping-pong if the GitHub two-chat pilot passes.** No for automatic wake-up/background execution. |
| `The chats should keep their own visible conversation while using a shared bus.` | **Retain as requirement.** It directly supports human auditability and avoids hidden agent conversation. |
| `Important things remain in repo Issues/comments/canonical files.` | **Retain with ownership distinction.** Issue/PR comments are work/review metadata; canonical research/method truth stays in its existing owner. |

## 12. Stop boundary / next evidence

The audit is complete enough to stop designing.

Next evidence for #162 should be the **real two-chat A→B→A GitHub Issue/comment pilot**. Do not add workflow rules, Slack/Discord integration or automation before that fixture exists.

If the pilot passes, the likely smallest outcome is a bounded operational convention/reference in the existing workflow/AGENTS owners only if repeated use shows that the convention must be durable. It may be sufficient to keep #162 as the usage/audit fixture with no normative change.

If the pilot fails, record the exact failure class before proposing a larger mechanism:

- second chat cannot read/write the same Issue surface;
- user still has to relay content;
- polling/resume burden is material;
- transport creates unacceptable Issue noise;
- cross-repo routing is ambiguous;
- current product permission/connector surface blocks the required action.

Only that demonstrated failure should select the next technical layer.