
import pandas as pd

df = pd.read_csv("exploratory_artifacts/duplicate_audit.csv")

cross_split = df[df["number_of_splits"] > 1].copy()

for sentence, group in cross_split.groupby("normalised_text"):
    print("\n" + "=" * 70)
    print("Sentence:", group["Text"].iloc[0])
    print("Labels:", group["Label"].unique())
    print("Records:")

    for _, row in group.iterrows():
        print(
            f"  {row['Record Id']} | "
            f"Label: {row['Label']} | "
            f"Split: {row['Split']} | "
            f"Group: {row['Group Id']}"
        )

print("\nTotal affected records:", len(cross_split))
print(
    "Total affected sentence groups:",
    cross_split["normalised_text"].nunique()
)
