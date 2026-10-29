import pandas as pd
from sklearn.model_selection import train_test_split

from features import extract_features

urls = pd.read_csv("data/urls.csv")


rows = []
for url in urls['url']:
    features = extract_features(url)
    rows.append(features)
X = pd.DataFrame(rows)

y = urls['label']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

print(X_train.shape, X_test.shape)
print(y_train.value_counts(normalize=True))
print(y_test.value_counts(normalize=True))