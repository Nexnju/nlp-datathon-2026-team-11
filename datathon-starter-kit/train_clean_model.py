
import pandas as pd
import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix
)

DATA = Path("exploratory_artifacts/cleaned_experimental_dataset.csv")
OUT = Path("exploratory_artifacts/clean_model")

OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)

train = df[df["Split"] == "train"]
dev = df[df["Split"] == "dev"]
test = df[df["Split"] == "test"]

X_train = train["Text"].astype(str)
y_train = train["Label"]

X_dev = dev["Text"].astype(str)
y_dev = dev["Label"]

X_test = test["Text"].astype(str)
y_test = test["Label"]

# Character-level TF-IDF
vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(2, 5),
    min_df=1,
    max_features=50000,
    sublinear_tf=True
)

X_train_vec = vectorizer.fit_transform(X_train)
X_dev_vec = vectorizer.transform(X_dev)
X_test_vec = vectorizer.transform(X_test)

# Logistic Regression
model = LogisticRegression(
    max_iter=2000,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train_vec, y_train)

# Evaluate on development and test sets.
for name, X, y in [
    ("DEVELOPMENT", X_dev_vec, y_dev),
    ("TEST", X_test_vec, y_test)
]:
    predictions = model.predict(X)

    print("\n" + "=" * 50)
    print(name, "RESULTS")
    print("=" * 50)

    print("Accuracy:", accuracy_score(y, predictions))
    print("Macro-F1:", f1_score(
        y, predictions, average="macro"
    ))

    print("\nClassification report:")
    print(classification_report(
        y,
        predictions,
        labels=["negative", "neutral", "positive"],
        zero_division=0
    ))

    print("Confusion matrix:")
    print(confusion_matrix(
        y,
        predictions,
        labels=["negative", "neutral", "positive"]
    ))

    if name == "TEST":
        results = pd.DataFrame({
            "Text": test["Text"].values,
            "Actual": y.values,
            "Predicted": predictions
        })

        results.to_csv(
            OUT / "test_predictions.csv",
            index=False
        )

        metrics = {
            "accuracy": accuracy_score(y, predictions),
            "macro_f1": f1_score(
                y, predictions, average="macro"
            ),
            "test_records": len(y)
        }

        with open(OUT / "metrics.json", "w") as f:
            json.dump(metrics, f, indent=4)

print("\nSaved test predictions and metrics in:", OUT)
