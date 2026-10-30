# pandas holds the data in tables (DataFrames)
import pandas as pd

# DummyClassifier: a "model" that ignores the features; our score to beat
from sklearn.dummy import DummyClassifier

# RandomForestClassifier: many decision trees that vote together
from sklearn.ensemble import RandomForestClassifier

# classification_report: precision/recall/F1; confusion_matrix: error counts
from sklearn.metrics import classification_report, confusion_matrix

# train_test_split: splits data into a training part and a test part
from sklearn.model_selection import train_test_split

# turns one URL into 8 numbers (see features.py)
from features import extract_features

# --- Data loading ---
urls = pd.read_csv("data/urls.csv")  # columns: url, label (1 = phishing, 0 = benign)
baseline = DummyClassifier(strategy="most_frequent")  # always predicts the most common class in training

# --- Feature extraction ---
rows = []  # one dict of 8 numbers per URL
for url in urls['url']:  # go through every URL in the file
    features = extract_features(url)  # {"url_length": ..., "has_ip": ..., ...}
    rows.append(features)  # collect it
X = pd.DataFrame(rows)  # X = the feature table: one row per URL, one column per feature

y = urls['label']  # y = the answers the model must learn to predict
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,  # 20% of the rows are held back for testing
    stratify=y,  # keep the phishing/benign ratio the same in both parts
    random_state=42,  # fixed seed so the split is the same on every run
)

# --- Baseline model ---
baseline.fit(X_train, y_train)  # "training" just records the most common class
baseline_pred = baseline.predict(X_test)  # predicts that one class for every test URL

# --- Random Forest model ---
forest = RandomForestClassifier(random_state=42)  # default settings, fixed seed for repeatable results
forest.fit(X_train, y_train)  # learn patterns from the training URLs only
forest_preds = forest.predict(X_test)  # predict labels for URLs the model has never seen

# --- Results ---
print('Baseline')
print(classification_report(y_test, baseline_pred))  # per-class precision, recall, F1
print(confusion_matrix(y_test, baseline_pred))  # rows = real class, columns = predicted class

print('Random Forest')
print(classification_report(y_test, forest_preds))
print(confusion_matrix(y_test, forest_preds))

# --- Feature importances (Sprint 1 caveat check) ---
# Shows how much each feature contributed to the forest's decisions (they add up to 1.0).
# If url_length and domain_length dominate, the model may just be learning "short = benign".
importances = pd.Series(forest.feature_importances_, index=X.columns)  # label each score with its feature name
print('Feature importances')
print(importances.sort_values(ascending=False).round(3))  # biggest contributors first
