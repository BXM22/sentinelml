# Risks and mitigations

The biggest risks are scope growth and misleadingly high scores, so each has a built-in check.

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| Scope creep: adding features before a level ships | High | Medium | A level is closed only when its exit criteria are met; new ideas go to a parking-lot list |
| Data leakage inflates scores | Medium | High | Split first, deduplicate across splits, review features for label giveaways |
| Imbalanced data hides missed attacks | High | High | Report per-class recall; use class weights or resampling |
| Dataset is too old or unrepresentative | Medium | Medium | State dataset limits in each README; add a fresher source when possible |
| Job search eats the schedule | High | Medium | One-week sprints can be paused; carry unfinished stories forward |
| Unsafe handling of malicious content | Low | High | Use labeled public datasets only; never fetch or execute URLs from the data |
| Level 5 LLM triage adds cost or unreliable output | Medium | Low | Keep it optional; show the raw alert beside the summary |
