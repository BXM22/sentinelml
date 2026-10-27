# Requirements

The system must detect threats at five increasing levels of difficulty, with every detection explainable and every result reproducible.

| ID | Requirement | Level | Priority |
| --- | --- | --- | --- |
| FR-1 | Extract numeric features from a URL and classify it as phishing or benign | 1 | Must |
| FR-2 | Report precision, recall, F1 and a confusion matrix for every trained model | 1 | Must |
| FR-3 | Show the top feature importances for each model | 1 | Should |
| FR-4 | Load labeled network-flow data and classify normal vs. attack type | 2 | Must |
| FR-5 | Handle class imbalance (class weights or resampling) and report per-class recall | 2 | Must |
| FR-6 | Parse authentication or web-server logs into per-event or per-window features | 3 | Must |
| FR-7 | Score events for anomalies without labels and rank the most suspicious | 3 | Must |
| FR-8 | Expose a REST endpoint that scores an event and returns label, score and reason | 4 | Must |
| FR-9 | Store events and alerts in Postgres and show them on a dashboard | 4 | Must |
| FR-10 | Test the model against evasion attempts and record the results | 5 | Must |
| FR-11 | Detect data drift and trigger or recommend retraining | 5 | Should |
| FR-12 | Summarize an alert for an analyst using an LLM (optional) | 5 | Could |

## Non-functional requirements

- **Reproducibility:** fixed random seeds, pinned dependencies, and a one-command run (`make train`).
- **Performance:** the Level 4 endpoint scores a single event in under 200 ms on a laptop.
- **Safety of data:** use public datasets only; never commit real credentials, personal data or live malicious payloads.
- **Maintainability:** type hints, a README per level, and test coverage on feature code.
