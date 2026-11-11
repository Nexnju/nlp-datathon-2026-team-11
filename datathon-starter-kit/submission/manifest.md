# NLP Hub Datathon 2026 – Submission Manifest

**Team:** Team 11  
**Project:** Dholuo NLP – Sentiment Classification  
**Primary language:** Dholuo  
**Submission date:** 11 November 2026  
**Manifest version:** 1.0  
**Submission status:** Draft – final verification pending

## 1. Team information

| Field | Value |
|---|---|
| Team number | 11 |
| Team name | Team 11 |
| Primary language | Dholuo |
| Main task | Sentiment classification |
| Additional demonstration options | Intent classification and semantic parsing |
| Team members | TO COMPLETE |
| Team contact | TO COMPLETE |

## 2. Project overview

This project demonstrates sentence-level sentiment classification in Dholuo.

The experimental system uses character-level TF-IDF features (2?5 character n-grams) and Logistic Regression (max_iter=1000, random_state=42) to classify text into positive, negative and neutral sentiment categories.

A Streamlit application provides an interface for entering Dholuo text and viewing the model's predicted sentiment and class probability breakdown.

The model and dataset remain experimental. Their limitations are documented in the accompanying reports.

## 3. Repository and frozen version

| Field | Value |
|---|---|
| GitHub repository | https://github.com/Nexnju/nlp-datathon-2026-team-11 |
| Branch | main |
| Submission tag | TO CREATE |
| Full commit SHA | TO COMPLETE |
| ZIP archive | TO CREATE |
| Freeze date and time | TO COMPLETE |

The submitted ZIP archive must correspond exactly to the recorded Git commit.

## 4. Dataset information

| Field | Value |
|---|---|
| Dataset name | Team 11 Dholuo Sentiment Dataset |
| Language | Dholuo |
| Task | Three-class sentiment classification |
| Target size | 300 records |
| Final positive count | 100 |
| Final negative count | 100 |
| Final neutral count | 100 |
| Final train split | 180 |
| Final development split | 60 |
| Final test split | 60 |
| Final accepted record count | 300 |
| Final unique normalized text count | 300 |
| Final normalized duplicate count | 0 |
| Independently reviewed test records | 60 of 60 (review metadata) |

### Original source

Sindhi Sentiment Analysis Dataset, stewarded by Ali Nawaz, hosted on Mozilla Data Collective.

https://mozilladatacollective.com/datasets/cmrlqkecf00jynu07k7fb90iv

The source page lists CC BY-NC 4.0. The team's machine translation and any redistribution of derived material require appropriate rights and attribution checks.

### Data files

| File | Description |
|---|---|
| `data/contribution.csv` | Final contribution dataset, subject to validation and publication clearance |
| `data/Team_11_Dholuo_Sentiment_Dataset.xlsx` | Working source workbook; do not publish unless cleared |
| `exploratory_artifacts/` | Preliminary exploratory outputs and model evidence |

Replace these paths if the final repository structure differs.

## 5. Documentation included

| File | Purpose |
|---|---|
| `docs/annotation_guide.md` | Sentiment annotation definitions and procedures |
| `docs/dataset_card.md` | Dataset description and limitations |
| `docs/data_quality_report.md` | Data-quality checks and audit findings |
| `docs/provenance_and_rights.md` | Source attribution, translation and rights |
| `docs/evaluation_report.md` | Model evaluation methodology and results |
| `docs/contributions.md` | Team contributions and AI-use disclosure |

The documentation has been updated to reflect the final dataset and known review limitations.

## 6. Model and evaluation

| Field | Value |
|---|---|
| Algorithm | Logistic Regression |
| Feature extraction | Character-level TF-IDF |
| Character n-gram range | 2–5 |
| Random seed | 42 |
| Majority baseline accuracy | 0.333 |
| Majority baseline macro-F1 | 0.167 |
| Final test accuracy | 0.617 |
| Final test macro-F1 | 0.611 |
| Positive F1 | 0.651 |
| Negative F1 | 0.500 |
| Neutral F1 | 0.683 |
| Confusion matrix | Recorded below in the evaluation report |

The metrics above are from the final accepted 300-record dataset. The test set contains 60 records; evaluation is experimental and should not be interpreted as broad validation of Dholuo sentiment understanding.

## 7. Running the demonstration

### Requirements

- Python 3.13
- pip
- Dependencies listed in `requirements.txt`

### Setup on Windows PowerShell

```powershell
py -3.13 -m venv .venv313
.\.venv313\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Launch the application

```powershell
python -m streamlit run app.py
```

Open the local Streamlit URL displayed in the terminal, normally:

`http://localhost:8501`

The model artefact must be available in the expected `artifacts/` directory. Follow the repository's model-packaging instructions if the artefact is not committed.

## 8. Demo evidence

| Evidence | Location |
|---|---|
| Application screenshots | TO COMPLETE |
| Demo recording | TO COMPLETE |
| Example inputs and predictions | TO COMPLETE |
| Presentation slides | TO COMPLETE |

The demonstration should show a Dholuo input, predicted sentiment, class probability breakdown and the model's experimental limitations.

## 9. Validation and reproducibility

| Check | Result |
|---|---|
| Official dataset validator | PASS (structural checks); output saved at `submission/evidence/validator_output.txt` |
| Duplicate audit | PASS: 0 normalized duplicate texts |
| Split leakage audit | PASS: no group IDs cross splits |
| Required-field audit | PASS: 0 missing required values |
| Independent test review | 60/60 records have independent-review metadata |
| Baseline evaluation | Completed: accuracy 0.333, macro-F1 0.167 |
| Final model evaluation | Completed: accuracy 0.617, macro-F1 0.611 |
| Clean environment installation | TO COMPLETE |
| Demo launch test | PASS: launched successfully in the existing virtual environment |

## 10. Known limitations and unresolved issues

Known limitations and outstanding checks:

- Google Translate produced the initial Dholuo drafts for all 300 records; 276 were used largely as translated and 24 were subsequently human-localised.
- The initial duplicate audit identified 45 redundant occurrences. The final dataset has 300 unique record IDs and 300 unique normalized texts; no group IDs cross dataset splits.
- All 60 test records have independent-review metadata. This does not establish full linguistic validation by proficient Dholuo speakers.
- Contextual references, linguistic naturalness and sentiment preservation still require broader Dholuo-speaker assessment.
- The upstream source's exact version, derivative-data terms and redistribution permissions remain unresolved.

## 11. AI-use and source disclosure

The initial dataset preparation used Google Translate to translate Sindhi material into Dholuo.

Additional AI-assisted work, if any, must be described accurately in `docs/contributions.md`.

The original source must be attributed, and the applicable licence and redistribution terms must be respected.

## 12. Submission checklist

- [ ] Final contribution CSV is complete and cleared for submission.
- [x] Final dataset counts and splits are verified.
- [x] Duplicate and leakage audits are complete.
- [x] Independent review status is accurately reported.
- [ ] Provenance and rights documentation is complete.
- [x] Annotation guide and dataset card are complete.
- [x] Final evaluation and majority baseline are recorded.
- [x] Official validator output is saved.
- [x] README and installation instructions are updated.
- [ ] Demo evidence is included.
- [ ] No unapproved private data or secrets are committed.
- [ ] Git submission tag is created.
- [ ] Full commit SHA is recorded.
- [ ] ZIP archive matches the frozen commit.
- [ ] Manifest is complete.
- [ ] Submission is made through the official datathon channel.

**Final submission approval:** TO COMPLETE

**Submission timestamp:** TO COMPLETE