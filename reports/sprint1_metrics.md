# Sprint 1 metrics

Dataset: `data/urls.csv` (109,596 URLs, 1 = phishing, 0 = benign). Features: the 8 starter features in `src/features.py`. Split: stratified 80/20, `random_state=42`, so the test set has 21,920 URLs (10,960 per class). Reproduce with `python src/train.py`.

## Results (phishing = class 1)

| Model | Phishing recall | Phishing precision | Phishing F1 | Accuracy |
| --- | --- | --- | --- | --- |
| Majority-class baseline | 0.00 | 0.00 | 0.00 | 0.50 |
| Random Forest (`random_state=42`, default parameters) | 0.98 | 1.00 | 0.99 | 0.99 |

Precision for the baseline is 0.00 because it never predicts phishing, so scikit-learn reports it as undefined and sets it to 0.

## Confusion matrices (rows = real, columns = predicted)

Baseline:

```
              pred benign   pred phishing
real benign      10960            0
real phishing    10960            0
```

Random Forest:

```
              pred benign   pred phishing
real benign      10938           22
real phishing      178        10782
```

The forest missed 178 of 10,960 phishing URLs (the costly error) and raised 22 false alarms on benign URLs.

## Acceptance check

The Random Forest beats the baseline on phishing recall (0.98 vs 0.00), so the Story 3 acceptance criterion is met. It also clears the Level 1 target of recall >= 0.90 early.

## Feature importances

`python src/train.py` now also prints `forest.feature_importances_` (they sum to 1.0):

| Feature | Importance |
| --- | --- |
| `url_length` | 0.365 |
| `domain_length` | 0.290 |
| `dot_count` | 0.152 |
| `digits_in_url` | 0.133 |
| `digits_in_domain` | 0.035 |
| `hyphen_count` | 0.023 |
| `has_at` | 0.001 |
| `has_ip` | 0.000 |

## Caveat: do not trust the score yet

Benign rows are bare domains (`https://domain`), while phishing URLs are longer. The importances confirm the worry: the two length features carry about 65% of the forest's decisions. The 0.98 recall therefore likely overstates real-world performance, because a real benign URL often has a path and would look "long". `has_at` and `has_ip` barely matter, since they are rare in this data.

Planned for Sprint 2: add path-based or otherwise less length-dependent features, and either give benign URLs realistic paths or evaluate on a test set where lengths are comparable.
