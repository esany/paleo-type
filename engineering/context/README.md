# Engineering context products

This surface is the admitted SD-KA-01/WP3 owner for **derived engineering context behavior**. It does not own Project scholarship, accepted architecture, work priority or Human authority. Canonical facts remain in `engineering/configuration.json`, `engineering/changes/SD-KA-01/STATE.json`, the engineering catalogs, accepted decisions and the applicable Requirement/METHOD owners.

## Core rule

Context is a rebuildable view over current owners:

```text
canonical owners + explicit work scope + applicability provenance
→ role-specific derived context
→ expandable provenance/history
```

No generated context file is committed as current truth.

## Human-visible current work

A generic invocation may be used to request the current work, and currentness may be scoped to an active work context. The visible result must nevertheless be semantically explicit:

```text
invocation may be generic
→ resolution may be context-relative
→ visible resolved work is a meaningful action/claim with scope and authority basis
```

A bare Issue number, work-package token or unexplained status is not an adequate Human-facing result. If more than one candidate remains applicable, the derived view reports ambiguity and the candidates instead of silently selecting one repository-global cursor.

## Profiles

`tools/engineering_context.py` provides these derived profiles:

- `human-system-overview` — accepted state, active/next bounded work, readiness, residuals, decision need and deeper provenance pointers;
- `system-development-execution` — bounded Agent/Senior-Developer execution packet with authority reads, applicability, non-goals, acceptance/return boundary and the full-check command;
- `architecture-review` — accepted/proposed/change context plus an explicit review-evidence-basis surface;
- `human-material-decision` — plain-language decision need/non-need and exact authority boundary without audit replay;
- `maintenance-review` — changed-owner/propagation review context with review-evidence-basis semantics.

All profiles expose applicability basis rather than maintaining an opaque reading list.

## Review evidence basis

Consequential review profiles carry these meanings explicitly:

```text
review target
material premise
basis actually inspected
inherited premises
premises re-tested
independence claim
remaining evidence-depth limitation
```

The generated starting state is `unknown/not-established`: a fresh context or second model is not independent evidence merely because it is new. Reviewers may strengthen the claim only from the evidence basis actually inspected.

## Senior Developer entry path

For current system-development work, use:

```text
README.md
→ engineering/README.md
→ python tools/engineering.py current
→ python tools/engineering_context.py --profile system-development-execution
→ active bounded work/Issue and applicable owners
→ python tools/check.py
→ deeper provenance only when needed
```

This path is navigation, not authority. `tools/check.py` is technical assurance only and never creates scholarly/specialist/Human acceptance.

## Human cursor rendering

For a concise Human-readable current/next-work rendering:

```bash
python tools/engineering_context.py --profile human-system-overview --format text
```

The output includes the meaningful action statement, scope and authority/basis references. It must not leave the Human with only `WP3`, `#258` or another opaque cursor token.
