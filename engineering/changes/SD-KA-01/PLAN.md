# SD-KA-01 implementation plan

## WP1 — verified and returned

WP1 persisted the Human-Owner admission, established the in-place `engineering/` semantic owners and representative F01–F45 baseline, added deterministic structural validation and returned its exact result/whole-system consequence to #244. No physical migration or scholarly Project state changed.

## WP2 — verified and returned (#257)

Execution baseline: `main@2c683beaefa18bc07810bf91cbbe67a07ef81f6a`.

Completed bounded sequence:

1. advanced work ownership from completed #256/WP1 to #257/WP2 without changing D-016 admission or accepted architecture;
2. extended configuration/currentness semantics with explicit change state, focus/absence and applicability provenance;
3. implemented rebuildable current/query derivation in `tools/engineering.py` without committing a generated current-state clock;
4. added adversarial deterministic fixtures for proposed-as-current, work-metadata/currentness laundering, latest-wins pressure, explicit absence and invalid applicability/transition semantics;
5. ran exact-head repository CI and repository-first fresh-context/self-review on PR #278;
6. merged at `main@e10a51a56a6db1924d4500698d2dd2be2b222bc4` and passed exact post-merge `source-contract` run #527;
7. persisted the WP2 Result/whole-system return and downstream readiness without promoting the whole SD-KA-01 target to accepted architecture.

## WP3 — current implementation cursor (#258)

Execution baseline: `main@ddf289fdf69f3827f287665a2a8c8e4d137fcbba`.

Bounded sequence:

1. advance work ownership/current focus from returned WP2 to #258/WP3 under the existing D-016 admission while keeping accepted architecture/Requirement baselines unchanged;
2. implement rebuildable Human overview, system-development execution, architecture-review, Human material-decision and maintenance-review profiles over WP2 current/configuration owners;
3. make visible current/next work a semantically explicit action with scope and authority provenance; expose ambiguity rather than invent a repository-global cursor;
4. implement Senior Developer bootstrap and one documented `python tools/check.py` deterministic entrypoint shared with CI;
5. activate the bounded `.prompt` create/review/test capability without turning it into task execution, planning/current-state authority or a universal Skill framework;
6. operationalize review-evidence-basis/inherited-premise semantics without claiming that fresh context/model identity proves independence;
7. add context-starvation, history-growth, ambiguity, prompt simplicity/authority and self-review-independence regressions plus representative Human/Developer/Agent journey checks;
8. run exact-head CI/review, merge only after scoped technical assurance, run exact post-merge main assurance, then persist WP3 Result/whole-system return and actual WP4/WP5 readiness to #244.

## Later admitted work

WP4 adds the wider engineering-fitness/CI closure suite after WP3's context/prompt surfaces exist; WP5 performs controlled physical migration; WP6 performs adversarial qualification and terminal SD-KA-01 Result Review.

No later work package is started by WP3 technical PASS alone.
