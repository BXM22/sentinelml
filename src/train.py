import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

from features import extract_features

#Data loading
urls = pd.read_csv("data/urls.csv")
baseline = DummyClassifier(strategy="most_frequent")
#Data extraction
rows = []
for url in urls['url']:
    features = extract_features(url)
    rows.append(features)
X = pd.DataFrame(rows)

y = urls['label']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
#Baseline model training
baseline.fit(X_train, y_train)
baseline_pred = baseline.predict(X_test)
#Decision Tree model training
forest = RandomForestClassifier(random_state=42)
forest.fit(X_train, y_train)
forest_preds = forest.predict(X_test)
print('Baseline')
print(classification_report(y_test, baseline_pred))
print(confusion_matrix(y_test, baseline_pred))

print('Random Forest')
print(classification_report(y_test, forest_preds))
print(confusion_matrix(y_test, forest_preds))