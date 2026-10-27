# Release roadmap

Ten one-week sprints starting Nov 2, 2026 deliver five releases. The plan assumes about 10 to 12 focused hours a week and should be stretched, not squeezed, if job-search work takes priority.

| Sprint | Dates | Level | Goal | Exit criteria | Points |
| --- | --- | --- | --- | --- | --- |
| 1 | Nov 2-8 | 1 | Repo, data, baseline phishing classifier | Model trains; baseline and first metrics logged | 8 |
| 2 | Nov 9-15 | 1 | Better features, evaluation, write-up (v0.1) | Recall >= 0.90 on phishing class; README with confusion matrix | 8 |
| 3 | Nov 16-22 | 2 | Load and clean network-flow data | Clean train/test sets, no leakage, EDA charts | 8 |
| 4 | Nov 23-29 | 2 | Multi-class intrusion model (v0.2) | Per-class recall report; imbalance handled | 8 |
| 5 | Nov 30-Dec 6 | 3 | Log parser and Isolation Forest | Logs become feature rows; anomaly scores produced | 8 |
| 6 | Dec 7-13 | 3 | Tune thresholds and test with injected anomalies (v0.3) | Detects injected anomalies at a stated rate with a stated false-alarm rate | 8 |
| 7 | Dec 14-20 | 4 | FastAPI scoring service and Postgres schema | `POST /score` works; alerts persist | 8 |
| 8 | Dec 21-27 | 4 | Dashboard, Docker, CI (v0.4) | `docker compose up` runs everything; CI green | 8 |
| 9 | Dec 28-Jan 3 | 5 | Adversarial evasion tests and hardening | Evasion success rate measured before and after hardening | 8 |
| 10 | Jan 4-10 | 5 | Drift monitor, retraining job, optional LLM triage, final write-up (v1.0) | Drift alert fires on shifted data; case-study README published | 8 |

A sprint that runs over moves its unfinished stories to the top of the next one; the level's exit criteria never get lowered, only the date.
