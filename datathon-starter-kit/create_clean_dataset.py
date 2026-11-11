
import pandas as pd
import unicodedata
from pathlib import Path
from sklearn.model_selection import train_test_split

SOURCE = Path("data/Team_11_Dholuo_Sentiment_Dataset.xlsx")
OUTPUT = Path("exploratory_artifacts/cleaned_experimental_dataset.csv")

# Load the original workbook.
df = pd.read_excel(SOURCE, sheet_name="Dataset Records")

# Normalise text for duplicate detection.
def normalise(text):
    text = unicodedata.normalize("NFC", str(text))
    return " ".join(text.casefold().split())

df["normalised_text"] = df["Text"].apply(normalise)

# Keep only the first occurrence of each sentence.
df = df.drop_duplicates(
    subset="normalised_text",
    keep="first"
).copy()

# Remove the temporary normalisation column.
df.drop(columns=["normalised_text"], inplace=True)

print("Records after deduplication:", len(df))
print("\nClass counts:")
print(df["Label"].value_counts())

# Create new experimental splits: 70% train, 15% dev, 15% test.
train, temporary = train_test_split(
    df,
    test_size=0.30,
    random_state=42,
    stratify=df["Label"]
)

dev, test = train_test_split(
    temporary,
    test_size=0.50,
    random_state=42,
    stratify=temporary["Label"]
)

train = train.copy()
dev = dev.copy()
test = test.copy()

train["Split"] = "train"
dev["Split"] = "dev"
test["Split"] = "test"

cleaned = pd.concat(
    [train, dev, test],
    ignore_index=True
)

# Verify that no sentence crosses splits.
normalised = cleaned["Text"].apply(normalise)

check = pd.DataFrame({
    "text": normalised,
    "split": cleaned["Split"]
})

cross_split = (
    check.groupby("text")["split"].nunique() > 1
).sum()

assert cleaned["Text"].apply(normalise).nunique() == len(cleaned)
assert cross_split == 0

# Save the experimental dataset separately.
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
cleaned.to_csv(OUTPUT, index=False)

print("\nNew split distribution:")
print(pd.crosstab(cleaned["Split"], cleaned["Label"]))

print("\nDuplicate sentences crossing splits:", cross_split)
print("Saved to:", OUTPUT)
