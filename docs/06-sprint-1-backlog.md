# Sprint 1 backlog (Nov 2-8, 2026)

**Sprint goal:** a phishing-URL classifier trains end to end and beats a majority-class baseline.

## Story 1 (3 pts): Set up the project

As a developer, I want a clean repo so every later level builds on it.

- [x] Create folders `data/`, `src/`, `tests/`, `notebooks/`, `reports/`
- [x] Virtual environment and pinned `requirements.txt`
- [x] Pre-commit hooks for `ruff` and `gitleaks`
- [x] Add MIT license

*Acceptance:* a fresh clone runs `pytest` with zero failures.

## Story 2 (2 pts): Get and inspect the data

As an analyst, I want a labeled URL dataset so I can train a model.

- [x] Download a phishing set (UCI Phishing Websites or PhishTank) and a benign list (Tranco)
- [x] Merge, deduplicate and label (1 = phishing, 0 = benign)
- [x] Log class counts and check for imbalance

*Acceptance:* `data/urls.csv` exists, has no duplicate URLs, and counts are documented in the README.

## Story 3 (3 pts): Baseline model

As a developer, I want a first working model so I have a score to beat.

- [x] Write `extract_features()` with 8 starter features and 3 unit tests
- [x] Stratified 80/20 split with a fixed seed
- [x] Train a majority-class baseline and a Random Forest
- [x] Print precision, recall, F1 and the confusion matrix for both

*Acceptance:* Random Forest beats the baseline on phishing-class recall; results saved to `reports/sprint1_metrics.md`.

**Definition of done for the sprint:** all three stories merged to `main`, tests green, and a short demo (screenshot of metrics) added to the README.
