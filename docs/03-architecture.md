# Architecture

SentinelML is one pipeline that grows: each level swaps in a new data source or model while the later stages stay the same.

```mermaid
flowchart TD
    A["Ingest<br/>Public datasets first, then logs and live events<br/>(L1 URLs, L2 flows, L3 logs)"]
    B["Feature extraction<br/>Turn raw records into numbers<br/>(L1 URL features, L3 log windows)"]
    C["Model<br/>Random Forest first, then anomaly detection<br/>(L1-2 supervised, L3 anomaly)"]
    D["Score and explain<br/>Label, score and reason for every event<br/>(L4 REST endpoint)"]
    E["Store and monitor<br/>Postgres alerts, dashboard, drift checks<br/>(L4 store, L5 drift and retrain)"]
    A --> B --> C --> D --> E
    E -. retrain .-> C
```

The model stage is the one that changes most, and in Level 5 drift checks send it back for retraining.

**Stack:** Python, pandas, scikit-learn, pytest, FastAPI, PostgreSQL, Docker and GitHub Actions. Levels 1 to 3 run as scripts and notebooks; Level 4 adds the service.
