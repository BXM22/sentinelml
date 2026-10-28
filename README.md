# SentinelML

**An AI/ML + cybersecurity project that starts simple and grows over five levels.**

SentinelML begins as a small phishing-URL classifier and, sprint by sprint, grows into a real-time threat-detection system with a scoring API, a database, a dashboard, and tests against attacks on the model itself. Each level ships a working, tested release before the next one begins.

> **Status: planning.** This repository currently contains the planning documents only (SDLC, requirements, architecture, sprint plan). Code will be added level by level, starting with Sprint 1 on **Nov 2, 2026**.

## The five levels

```
Level 1            Level 2              Level 3             Level 4              Level 5
Phishing URL  ──►  Network intrusion ─► Log anomaly   ───►  Live pipeline   ───► Attack the
classifier         detection            detection           + dashboard          model itself
(supervised ML)    (multi-class ML)     (unsupervised)      (API + Postgres)     (adversarial ML)
```

| Level | Release | What it detects | Technique | Skills practiced |
| --- | --- | --- | --- | --- |
| 1 | v0.1 | Phishing URLs | Supervised classification (scikit-learn) | Feature engineering, precision vs. recall |
| 2 | v0.2 | Network intrusions | Multi-class classification on imbalanced data | Class weights, per-class metrics, confusion matrices |
| 3 | v0.3 | Anomalies in logs | Unsupervised anomaly detection (Isolation Forest) | Log parsing, thresholds, evaluation without labels |
| 4 | v0.4 | Live events | FastAPI scoring service, Postgres, dashboard | Deployment, Docker, CI |
| 5 | v1.0 | Attacks on the model itself | Adversarial testing, drift monitoring, retraining | Robustness, monitoring, optional LLM alert triage |

## Documentation

Start with the roadmap, then read the others as needed.

| # | Document | What it covers |
| --- | --- | --- |
| 1 | [SDLC approach](docs/01-sdlc-approach.md) | Eight lifecycle phases and working agreements |
| 2 | [Requirements](docs/02-requirements.md) | Functional requirements FR-1 to FR-12 and non-functional requirements |
| 3 | [Architecture](docs/03-architecture.md) | The five-stage pipeline and tech stack |
| 4 | [Quality and security gates](docs/04-quality-and-security-gates.md) | Testing, ML evaluation rules, security scans |
| 5 | [Release roadmap](docs/05-release-roadmap.md) | Ten one-week sprints with exit criteria |
| 6 | [Sprint 1 backlog](docs/06-sprint-1-backlog.md) | Stories, tasks and acceptance criteria for the first sprint |
| 7 | [Sprint ceremonies](docs/07-sprint-ceremonies.md) | Planning, check-ins, review, retro, definitions of ready and done |
| 8 | [Risks](docs/08-risks.md) | What could go wrong and the mitigation for each |

## Planned tech stack

Python, pandas, scikit-learn, pytest, FastAPI, PostgreSQL, Docker, GitHub Actions. Quality and security tooling: `ruff`, `bandit`, `pip-audit`, `gitleaks`.

## Planned data sources

All public and labeled; no real credentials, personal data or live malicious payloads are ever committed.

- **Level 1:** UCI Phishing Websites dataset, PhishTank (phishing URLs), Tranco list (benign domains)
- **Level 2:** NSL-KDD or CIC-IDS2017 network-flow data
- **Level 3:** public authentication or web-server log samples, with injected anomalies for testing

## Level 1 dataset

`python src/build_dataset.py` builds `data/urls.csv` (1 = phishing, 0 = benign) from the raw downloads in `data/raw/` (not committed). Raw sources: PhishTank `online-valid.csv` and the Tranco top-1M list, both downloaded Oct 27, 2026.

| Class | Rows |
| --- | --- |
| Phishing (1) | 54,797 |
| Benign (0) | 54,799 |
| **Total** | **109,596** |

No duplicate URLs. The classes are balanced because the benign side was randomly sampled (seed 42) to match the phishing count; the full Tranco list is 1M domains.

**Known caveat:** Tranco gives bare domains, so benign rows are `https://domain` with no path, while phishing URLs are longer (median 37 vs 21 characters). A model could score well just by learning "short means benign". Keep this in mind when reading Story 3 results.

## How the project is run

- One-week sprints, one sprint goal each, tagged releases at the end of every level.
- `main` always runs; work happens on short-lived feature branches and merges only with green tests.
- Every model release records its dataset, parameters and metrics.
- In security, a missed attack costs more than a false alarm, so recall and false-positive rate are always reported side by side.

## Planned repository layout

```
sentinelml/
├── docs/          planning documents (this is all that exists today)
├── data/          datasets (not committed if large)
├── src/           feature extraction, training, scoring code
├── tests/         unit tests and data checks
├── notebooks/     exploration and EDA
└── reports/       metrics and evaluation write-ups per sprint
```

## Roadmap at a glance

| Sprints | Dates | Level | Outcome |
| --- | --- | --- | --- |
| 1-2 | Nov 2-15, 2026 | 1 | Phishing classifier, recall >= 0.90 |
| 3-4 | Nov 16-29, 2026 | 2 | Multi-class intrusion detector |
| 5-6 | Nov 30-Dec 13, 2026 | 3 | Log anomaly detector |
| 7-8 | Dec 14-27, 2026 | 4 | Scoring API, Postgres, dashboard, CI |
| 9-10 | Dec 28, 2026-Jan 10, 2027 | 5 | Adversarial tests, drift monitoring, v1.0 |

Dates assume about 10 to 12 focused hours a week and will slide if other priorities take over; exit criteria do not get lowered, only the dates.

## License

MIT (to be added with Sprint 1).
