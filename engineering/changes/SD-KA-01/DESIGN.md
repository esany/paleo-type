# SD-KA-01 WP1 design

WP1 uses the admitted hybrid representation: central TSV registries for cross-artifact identity, coverage, findings and relations; JSON for configuration and bounded change state; Markdown remains the natural content owner. Paths are locators, never stable identity.

The validator resolves `artifact:`, `finding:`, `change:`, `decision:`, `adr:`, `github-issue:`, `github-pr:`, `git:` and `path:` references. It checks structural semantics only. It does not infer findings from prose, decide applicability, accept architecture or replace scholarly/specialist/Human review.

The baseline is deliberately representative rather than a bulk inventory. WP2 may extend classification and current/query derivation after this contract slice is reviewed.
