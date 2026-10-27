# SDLC approach

SentinelML uses an iterative agile SDLC: every one-week sprint passes through all eight phases below, so each level ends as a tagged, working release (v0.1 to v1.0).

| Phase | What happens | Deliverable |
| --- | --- | --- |
| 1. Plan | Pick the sprint goal, size stories, check time available | Sprint backlog |
| 2. Requirements | Write user stories with acceptance criteria | Stories in the tracker |
| 3. Design | Sketch data flow, features, model choice, schema | Design note (half a page) |
| 4. Implement | Code on a feature branch, small commits | Pull request to `main` |
| 5. Test | Unit tests, data checks, model metrics against a threshold | Passing CI run and metrics report |
| 6. Secure | Dependency scan, secret scan, threat check on new inputs | Clean scan output |
| 7. Release | Merge, tag, update README and changelog | Version tag and release notes |
| 8. Review and monitor | Sprint review, retro, check model metrics and drift | Retro notes and next backlog |

Working agreements: one `main` branch that always runs, short-lived feature branches, no merge without green tests, and every model release records its dataset, parameters and metrics.
