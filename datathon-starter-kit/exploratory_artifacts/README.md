# Dholuo Sentiment – Experimental Artifacts

This folder contains outputs from exploratory dataset auditing and model experimentation for Team 11's Dholuo sentiment track.

## Data provenance

The experimental dataset was derived from material originally in Sindhi and translated using Google Translate. Human review is incomplete. The data must not be treated as fully validated Dholuo material.

## Files

| File | Description |
|---|---|
| `duplicate_audit.csv` | Duplicate sentence audit of the original 300 records |
| `cleaned_experimental_dataset.csv` | Deduplicated experimental dataset containing 255 unique records |
| `metrics.json` | Results from the earlier exploratory experiment |
| `test_predictions.csv` | Predictions from the earlier experiment |
| `clean_model/metrics.json` | Development and test evaluation results for the cleaned experiment |
| `clean_model/test_predictions.csv` | Predictions from the cleaned experiment |
| `blinded_test_review.xlsx` | Separate review worksheet for human assessment; review completion must be recorded separately |

## Experimental model

The classifier uses character-level TF-IDF features and Logistic Regression.

The cleaned dataset contains:
- 178 training records
- 38 development records
- 39 test records

The test results are preliminary and based on a small dataset. They are not official competition results and do not establish reliable real-world Dholuo sentiment performance.

## Limitations

- Machine translation may introduce grammatical and semantic errors.
- Original labels have not all been independently verified.
- Human review is incomplete.
- Duplicate removal reduced the dataset below the competition's 300-record minimum.
- The resulting class distribution does not satisfy all minimum split requirements.

These artifacts are preserved for reproducibility and further experimentation, not as evidence of a competition-compliant final dataset.