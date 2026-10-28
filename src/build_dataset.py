"""Merge PhishTank (phishing) and Tranco (benign) into data/urls.csv.

Label: 1 = phishing, 0 = benign.
"""

import pandas as pd

SEED = 42

phish = pd.read_csv("data/raw/phishtank.csv", usecols=["url"])
phish["label"] = 1

# Tranco lists domains only, so turn them into URLs. Sample as many as
# there are phishing URLs so the classes start balanced.
tranco = pd.read_csv("data/raw/top-1m.csv", names=["rank", "domain"])
benign = tranco.sample(n=len(phish), random_state=SEED)
benign["url"] = "https://" + benign["domain"]
benign = benign[["url"]].assign(label=0)

urls = pd.concat([phish, benign]).drop_duplicates(subset="url")
urls = urls.sample(frac=1, random_state=SEED).reset_index(drop=True)
urls.to_csv("data/urls.csv", index=False)

print(f"rows: {len(urls)}")
print(urls["label"].value_counts().rename({1: "phishing", 0: "benign"}))
