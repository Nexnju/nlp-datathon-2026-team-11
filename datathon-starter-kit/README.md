# Team 11 – Dholuo NLP: Sentiment Classification

**Strathmore NLP Hub Datathon 2026**

An experimental African-language NLP project exploring three-class sentiment classification for Dholuo text.

> **Important disclosure:** The final contribution contains 300 Dholuo records derived from Sindhi source material. Google Translate produced the initial Dholuo drafts for all 300 records. Of these, 276 were used largely as translated (`machine_translated`) and 24 were subsequently human-localised (`human_localised`). The dataset passed structural validation and duplicate checks, and all 60 held-out test records have independent-review metadata. However, the dataset is small, broader linguistic validation remains necessary, and source-data redistribution rights remain subject to verification. Results should not be interpreted as validated performance across Dholuo speakers or dialects.

## 1. Project overview

Team 11 developed a sentiment-analysis demonstration for the Strathmore NLP Hub Datathon 2026.

The model classifies Dholuo text into three categories:

- **Positive**
- **Negative**
- **Neutral**

The project uses character-level TF-IDF features and Logistic Regression as a baseline classifier. A Streamlit interface allows users to enter a sentence and inspect its predicted sentiment and class probability scores.

The project demonstrates a baseline NLP workflow, including dataset preparation, annotation metadata, validation, model training, held-out evaluation and an interactive application.

## 2. Final project status

| Component | Status |
|---|---|
| Sentiment classification baseline | Implemented |
| Streamlit demonstration | Implemented |
| Final contribution dataset | 300 records |
| Required-field and duplicate checks | Passed |
| Dataset split integrity | Passed |
| Independent review of test set | 60 of 60 records |
| Official sentiment validator | Passed |
| Final model training | Completed |
| Held-out test evaluation | Completed |
| Source-data redistribution review | Requires confirmation |
| Broader Dholuo linguistic validation | Limitation remains |

The application is a research demonstration, not a production-ready Dholuo language system.

## 3. Repository structure

Main project files:

- `app.py` – Streamlit demonstration interface.
- `core.py` – Shared dataset checks, labels, scoring and utility functions.
- `train.py` – Model training workflow.
- `evaluate.py` – Held-out evaluation workflow.
- `validate.py` – Dataset structure and quality validator.
- `requirements.txt` – Python dependencies.
- `taxonomy.csv` – Starter-kit taxonomy reference.
- `sentiment_guidelines.md` – Sentiment annotation guidance.
- `data/contribution.csv` – Final contribution dataset used for training and evaluation.
- `artifacts/sentiment/` – Trained model and evaluation outputs.
- `docs/` – Annotation, contribution, dataset, quality, provenance and evaluation documentation.
- `submission/` – Submission manifest and package information.

The final source workbook and exploratory working files are not required to run the application. Check the submission manifest for the files included in the final package.

## 4. Requirements and installation

Python 3.10 or later is recommended. The project was tested in a Python 3.13 virtual environment.

Clone the repository and enter the starter-kit directory:

```bash
git clone https://github.com/Nexnju/nlp-datathon-2026-team-11.git
cd nlp-datathon-2026-team-11/datathon-starter-kit
```

Create and activate a virtual environment.

**Windows PowerShell:**

```powershell
py -3.13 -m venv .venv313
.venv313\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The principal dependencies are:

- scikit-learn
- pandas
- Streamlit
- joblib

## 5. Running the demonstration

The application loads the trained model from:

```text
artifacts/sentiment/model.joblib
```

If the model artefact is not present, train it using the final contribution dataset:

```bash
python train.py --data data/contribution.csv --track sentiment
```

Then launch the application:

```bash
python -m streamlit run app.py
```

Open the local address displayed in the terminal, normally:

```text
http://localhost:8501
```

Select the sentiment task, enter a Dholuo sentence and click **Analyse sentence** to inspect the predicted category and probability breakdown.

**Interpretation caution:** The displayed probabilities are model scores, not calibrated confidence estimates. They should not be interpreted as guaranteed correctness.

## 6. Model approach and final evaluation

### Model configuration

The final sentiment baseline uses:

- Character-level TF-IDF feature extraction.
- Character n-grams of lengths 2–5.
- Logistic Regression.
- Maximum iterations: 1,000.
- Random state: 42.

Character n-grams provide a simple baseline for text classification without requiring a large pretrained language model.

### Dataset split

| Split | Records |
|---|---:|
| Training | 180 |
| Development | 60 |
| Test | 60 |
| **Total** | **300** |

The dataset contains 100 positive, 100 negative and 100 neutral records.

### Development and test results

| Metric | Development | Test |
|---|---:|---:|
| Accuracy | 70.00% | 61.67% |
| Macro-F1 | 0.698 | 0.611 |

The held-out test evaluation produced the following per-class F1 scores:

| Sentiment | Test F1 | Support |
|---|---:|---:|
| Positive | 0.651 | 20 |
| Negative | 0.500 | 20 |
| Neutral | 0.683 | 20 |

The test majority-class baseline macro-F1 was approximately 0.167. The model outperformed this baseline, but its test macro-F1 was lower than its development macro-F1. Negative sentiment was the weakest-performing class.

The test set was evaluated separately after the model configuration was frozen. These results are specific to this dataset and do not establish general performance across Dholuo speakers, dialects or domains.

See `docs/evaluation_report.md` for the evaluation methodology, detailed results and limitations.

## 7. Data provenance and annotation

The final contribution dataset contains 300 Dholuo records derived from Sindhi source material.

The recorded contribution methods are:

| Source method | Records | Description |
|---|---:|---|
| `machine_translated` | 276 | Initial Dholuo drafts produced using Google Translate and used largely as translated |
| `human_localised` | 24 | Initial Google Translate drafts subsequently human-localised by the team |
| **Total** | **300** | |

The dataset is balanced across positive, negative and neutral sentiment labels, with 100 records per class.

### Final dataset checks

The final contribution CSV was checked for:

- 300 records and no missing required values.
- 300 unique record IDs.
- 300 unique normalised text entries.
- No duplicate groups spanning dataset splits.
- 180 training, 60 development and 60 test records.
- 60 independently reviewed test records, with reviewer codes different from contributor codes.
- Successful execution of the official sentiment validator.

Review metadata records 217 self-reviewed records and 83 independently reviewed records overall. All 60 held-out test records are marked as independently reviewed.

The validator completed successfully:

```text
PASS: 300 records; language quality, permission and semantic duplicate review remain human responsibilities.
```

Passing structural validation does not establish linguistic correctness, semantic fidelity or permission to redistribute source-derived data.

For more information, see:

- `docs/annotation_guide.md`
- `docs/contributions.md`
- `docs/dataset_card.md`
- `docs/data_quality_report.md`
- `docs/provenance_and_rights.md`

## 8. Responsible use and limitations

1. **Source dependence:** All 300 records derive from Sindhi source material. The two recorded contribution methods describe how the Dholuo text was produced; they do not remove the need to document the original source.
2. **Linguistic validation:** Structural checks cannot replace review by proficient Dholuo speakers. Broader validation across speakers and dialects remains necessary.
3. **Dataset size:** The dataset contains only 300 records and may not represent the diversity of naturally occurring Dholuo.
4. **Sentiment ambiguity:** Context, sarcasm, idioms, spelling variation and mixed sentiment can affect predictions.
5. **Model limitations:** Character-level TF-IDF and Logistic Regression are baseline methods, not comprehensive models of Dholuo language understanding.
6. **Class performance:** Negative sentiment had the lowest test F1 score (0.500).
7. **Source rights:** The original source listing identifies a CC BY-NC 4.0 licence. The applicable attribution, derivative-data and redistribution terms must be confirmed before public redistribution.

The application is intended for demonstration and experimentation. It should not be used to make consequential decisions about individuals or communities.

## 9. Reproducibility

To reproduce model training in a clean environment:

1. Install dependencies from `requirements.txt`.
2. Obtain the authorised final contribution dataset at `data/contribution.csv`.
3. Run the official validator:

   ```bash
   python validate.py --data data/contribution.csv --track sentiment
   ```

4. Train the model:

   ```bash
   python train.py --data data/contribution.csv --track sentiment
   ```

5. For a controlled reproduction of the held-out evaluation, use:

   ```bash
   python evaluate.py --data data/contribution.csv --track sentiment
   ```

The reported final evaluation was performed after the model configuration was frozen. The held-out test set should not be used for repeated model tuning or selection.

Keep the dataset version, model artefact, evaluation outputs and source-code commit consistent when reporting results.

## 10. Attribution and licensing

This project builds on the Strathmore NLP Hub Datathon starter kit. The team acknowledges the starter-kit code, documentation and baseline workflow.

The Sindhi source material is attributed to Ali Nawaz and is listed on Mozilla Data Collective:

https://mozilladatacollective.com/datasets/cmrlqkecf00jynu07k7fb90iv

The source listing identifies a CC BY-NC 4.0 licence. The team must confirm the applicable attribution requirements and whether the proposed publication or redistribution of the Dholuo-derived contribution is permitted under the source terms and any additional applicable conditions.

The presence of a licence record in the dataset metadata is not, by itself, proof that every redistribution question has been resolved. Do not assume that public availability of the source automatically authorises publication of derivative data.

## 11. Team and submission

- **Team:** 11
- **Project:** Dholuo NLP – Sentiment Classification
- **Event:** Strathmore NLP Hub Datathon 2026
- **Repository:** https://github.com/Nexnju/nlp-datathon-2026-team-11

Team member names, individual contributions, contact information, final commit, submission archive and approval details are recorded in `docs/contributions.md` and `submission/manifest.md`.

---

*This README describes the final documented dataset and evaluation state as of 11 November 2026. Outstanding linguistic validation and source-data rights questions are disclosed rather than treated as completed.*
