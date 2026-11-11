
import pandas as pd
import unicodedata
from pathlib import Path

file_path = Path("data/Team_11_Dholuo_Sentiment_Dataset.xlsx")

df = pd.read_excel(file_path, sheet_name="Dataset Records")

# Normalise text to identify exact duplicates despite
# differences in capitalisation, spacing or Unicode form.
def normalise(text):
    text = unicodedata.normalize("NFC", str(text))
    return " ".join(text.casefold().split())

df["normalised_text"] = df["Text"].apply(normalise)

# Find every sentence appearing more than once.
duplicate_mask = df["normalised_text"].duplicated(keep=False)
duplicates = df[duplicate_mask].copy()

# Count how many different splits contain each sentence.
split_counts = (
    duplicates.groupby("normalised_text")["Split"]
    .nunique()
    .rename("number_of_splits")
)

duplicates = duplicates.merge(
    split_counts,
    on="normalised_text",
    how="left"
)

# Keep useful columns for inspection.
columns = [
    "Record Id",
    "Text",
    "Label",
    "Split",
    "Group Id",
    "number_of_splits"
]

duplicates[columns + ["normalised_text"]].sort_values(
    ["normalised_text", "Split"]
).to_csv(
    "exploratory_artifacts/duplicate_audit.csv",
    index=False
)

print("Total records:", len(df))
print("Unique sentences:", df["normalised_text"].nunique())
print("Duplicate records:", len(duplicates))
print(
    "Duplicate sentence groups:",
    duplicates["normalised_text"].nunique()
)
print(
    "Duplicate groups crossing splits:",
    int((split_counts > 1).sum())
)
print("\nDuplicate audit saved to:")
print("exploratory_artifacts/duplicate_audit.csv")
