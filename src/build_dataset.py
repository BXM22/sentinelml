"""Merge PhishTank (phishing) and Tranco (benign) into data/urls.csv.

Label: 1 = phishing, 0 = benign.
"""

import pandas as pd  # tables and CSV reading/writing

SEED = 42  # fixed seed so the random sampling gives the same rows every run

phish = pd.read_csv("data/raw/phishtank.csv", usecols=["url"])  # keep only the url column
phish["label"] = 1  # every PhishTank row is phishing

# Tranco lists domains only, so turn them into URLs. Sample as many as
# there are phishing URLs so the classes start balanced.
tranco = pd.read_csv("data/raw/top-1m.csv", names=["rank", "domain"])  # file has no header row, so name the columns
benign = tranco.sample(n=len(phish), random_state=SEED)  # random pick, same count as phishing
benign["url"] = "https://" + benign["domain"]  # bare domain -> URL (this is why benign URLs are short)
benign = benign[["url"]].assign(label=0)  # keep url, add label 0 = benign

urls = pd.concat([phish, benign]).drop_duplicates(subset="url")  # stack both sets, drop repeated URLs
urls = urls.sample(frac=1, random_state=SEED).reset_index(drop=True)  # shuffle all rows, renumber from 0
urls.to_csv("data/urls.csv", index=False)  # save without the row-number column

print(f"rows: {len(urls)}")  # total rows after dedup
print(urls["label"].value_counts().rename({1: "phishing", 0: "benign"}))  # class counts to check balance
