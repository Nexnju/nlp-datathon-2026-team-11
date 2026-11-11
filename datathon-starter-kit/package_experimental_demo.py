
import pandas as pd
import joblib

from pathlib import Path
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

DATA = Path("exploratory_artifacts/cleaned_experimental_dataset.csv")
OUTPUT = Path("artifacts/sentiment/model.joblib")

df = pd.read_csv(DATA)

train = df[df["Split"] == "train"]

# Build the same model pipeline used by the starter kit.
model = make_pipeline(
    TfidfVectorizer(
        analyzer="char",
        ngram_range=(2, 5)
    ),
    LogisticRegression(
        max_iter=1000,
        random_state=42
    )
)

model.fit(train["Text"], train["Label"])

# Package the model for the Streamlit app.
pack = {
    "model": model,
    "dummy": None,
    "language": "Dholuo",
    "practice": False,
    "experimental": True,
    "track": "sentiment",
    "data_sha256": "experimental_deduplicated_dataset",
    "slot_memory": {}
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(pack, OUTPUT)

print("Experimental Dholuo model packaged successfully.")
print("Saved to:", OUTPUT)
