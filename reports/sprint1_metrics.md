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

## Caveat: do not trust the score yet

Benign rows are bare domains (`https://domain`), while phishing URLs are longer, so the forest may be learning "long URL means phishing". Not yet checked: `forest.feature_importances_`. If `url_length` and `domain_length` dominate, the 0.98 overstates real-world performance. Planned for Sprint 2: inspect the importances and add path-based or otherwise less length-dependent features.
