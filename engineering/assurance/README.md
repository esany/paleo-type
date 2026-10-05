# Engineering fitness assurance

This directory owns the bounded, machine-readable WP4 engineering-fitness contract for SD-KA-01.

`fitness.json` maps the admitted ENG-FIT-01..ENG-FIT-09 checks to stable owners and regression fixtures. `tools/engineering_fitness.py` validates that mapping and executes the repository-owned structural checks that can be evaluated deterministically.

The shared developer/CI entrypoint remains:

```text
python tools/check.py
```

A PASS establishes only the deterministic properties actually checked. It does not establish scholarly truth, specialist validity, Human material acceptance, evidential independence, external runtime fitness, preservation of external source packages, or whole-system closure.

WP4 does not implement a runtime/orchestration layer. Repo-testable execution-control safeguards admitted separately under the outcome-preserving execution-control D-016 change may be exercised here only where the repository can actually falsify them. External/platform/runtime properties remain with their own acceptance owners.
