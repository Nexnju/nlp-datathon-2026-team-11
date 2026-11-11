import json
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# 1. Load the workbook
df = pd.read_excel(
    "data/Team_11_Dholuo_Sentiment_Dataset.xlsx",
    sheet_name="Dataset Records"
)

# 2. Clean and normalise text
df["Text"] = df["Text"].fillna("").astype(str).str.strip()
df["Label"] = df["Label"].str.lower().str.strip()

df["Normalised"] = (
    df["Text"]
    .str.normalize("NFC")
    .str.casefold()
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

df = df[df["Normalised"] != ""].copy()

# 3. Remove duplicate sentences
df = df.drop_duplicates(subset="Normalised").reset_index(drop=True)

print("Unique dataset size:", len(df))
print("\nClass distribution:")
print(df["Label"].value_counts())

# 4. Prepare data
X = df["Text"]
y = df["Label"]

# 70% training, 15% development, 15% testing
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

X_dev, X_test, y_dev, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.50,
    random_state=42,
    stratify=y_temp
)

print("\nSplit sizes:")
print("Training:", len(X_train))
print("Development:", len(X_dev))
print("Testing:", len(X_test))

print("\nTraining class distribution:")
print(y_train.value_counts())

print("\nDevelopment class distribution:")
print(y_dev.value_counts())

print("\nTesting class distribution:")
print(y_test.value_counts())

# 5. Convert text into character-level TF-IDF features
vectorizer = TfidfVectorizer(
    analyzer="char",
    ngram_range=(2, 5),
    min_df=1,
    max_features=50000,
    sublinear_tf=True
)

X_train_vectorized = vectorizer.fit_transform(X_train)
X_dev_vectorized = vectorizer.transform(X_dev)
X_test_vectorized = vectorizer.transform(X_test)

# 6. Train Logistic Regression
model = LogisticRegression(
    max_iter=2000,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train_vectorized, y_train)

# 7. Evaluate on development and test sets
dev_predictions = model.predict(X_dev_vectorized)
test_predictions = model.predict(X_test_vectorized)

print("\nDEVELOPMENT RESULTS")
print("Accuracy:", accuracy_score(y_dev, dev_predictions))
print("Macro F1:", f1_score(y_dev, dev_predictions, average="macro"))

print("\nTEST RESULTS")
accuracy = accuracy_score(y_test, test_predictions)
macro_f1 = f1_score(y_test, test_predictions, average="macro")

print("Accuracy:", accuracy)
print("Macro F1:", macro_f1)

print("\nClassification Report:")
report = classification_report(
    y_test,
    test_predictions,
    labels=["negative", "neutral", "positive"],
    zero_division=0
)
print(report)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        test_predictions,
        labels=["negative", "neutral", "positive"]
    )
)

# 8. Compare with a majority-class baseline
majority_label = y_train.value_counts().idxmax()
majority_predictions = [majority_label] * len(y_test)

print("\nMAJORITY BASELINE")
print("Majority class:", majority_label)
print("Accuracy:", accuracy_score(y_test, majority_predictions))
print(
    "Macro F1:",
    f1_score(y_test, majority_predictions, average="macro")
)

# 9. Save exploratory results
output_dir = Path("exploratory_artifacts")
output_dir.mkdir(exist_ok=True)

pd.DataFrame({
    "Text": X_test.values,
    "Actual": y_test.values,
    "Predicted": test_predictions
}).to_csv(output_dir / "test_predictions.csv", index=False)

results = {
    "unique_records": len(df),
    "training_records": len(X_train),
    "development_records": len(X_dev),
    "testing_records": len(X_test),
    "test_accuracy": accuracy,
    "test_macro_f1": macro_f1,
    "majority_baseline_accuracy": accuracy_score(
        y_test, majority_predictions
    ),
    "majority_baseline_macro_f1": f1_score(
        y_test, majority_predictions, average="macro"
    )
}

with open(output_dir / "metrics.json", "w") as file:
    json.dump(results, file, indent=4)

print("\nResults saved in:", output_dir)
print("Experiment complete.")
