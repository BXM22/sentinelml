# Quality and security gates

Nothing merges or releases until it clears these gates; the ML gates matter most because a model can pass every unit test and still be wrong.

| Gate | Check | Pass rule |
| --- | --- | --- |
| Code quality | `ruff` lint, `pytest` unit tests on feature code | All green |
| Data quality | No duplicate rows across train and test, no missing labels, class counts logged | No leakage found |
| Model quality | Recall on the attack class and F1 on the held-out test set | Beats the baseline; recall target set per level (start at 0.90) |
| Reproducibility | Re-run with the same seed | Metrics match within 0.5 points |
| Dependency security | `pip-audit` | No known high-severity issues |
| Code security | `bandit` static scan | No high-severity findings |
| Secrets | `gitleaks` or equivalent pre-commit hook | Nothing detected |
| Input safety (Levels 4+) | Validate and size-limit all API input; never execute or fetch submitted URLs | Tests for malformed input pass |

## ML-specific rules

1. Split data before any scaling or feature fitting, and fit transforms on the training set only.
2. Split by time or by source when the data allows it, so the test set looks like the future.
3. Always compare against a dumb baseline (majority class, simple rule) before celebrating a score.
4. In security, a missed attack costs more than a false alarm, so report recall and false-positive rate side by side.
