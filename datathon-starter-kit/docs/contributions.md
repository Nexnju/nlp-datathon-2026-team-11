# Team Contributions and AI-Use Statement

**Project:** Dholuo Sentiment Classification  
**Team:** Team 11 – NLP Hub Datathon 2026  
**Primary language:** Dholuo  
**Document version:** Draft v1.0  
**Date:** 11 November 2026  
**Status:** Draft – requires team confirmation

## 1. Project overview

Team 11 developed an experimental Dholuo natural language processing demonstration focused on three-class sentiment classification.

The project combines dataset preparation, text classification, model evaluation and a Streamlit-based demonstration application.

The team also investigated intent classification and semantic parsing as additional task options in the demonstration interface. The status and readiness of these additional tasks should be documented separately from the sentiment contribution.

## 2. Team roles and responsibilities

The following responsibilities describe the current work allocation. Team member names and completed contributions should be confirmed by the team before submission.

| Role | Responsibilities / evidence | Completion status |
|---|---|---|
| Team coordination and data integration | Coordinate team work, integrate dataset changes and prepare submission materials | Individual contribution details require team confirmation |
| Negative data contribution | Initial allocation included 16 replacement negative examples | Individual completion and contributor attribution require confirmation |
| Neutral data contribution | Initial allocation included 29 replacement neutral examples | Individual completion and contributor attribution require confirmation |
| Positive data review | Review positive examples for linguistic quality and label consistency | Individual contribution details require confirmation |
| Independent reviewers | Review held-out test examples independently | 60 of 60 test records have independent-review metadata; reviewer identities and disagreements should be confirmed |
| Model and application development | Implement the sentiment classification pipeline and Streamlit interface | Experimental implementation available |
| Documentation and evaluation | Prepare dataset documentation, quality reports and evaluation outputs | Reports and evaluation artifacts prepared; final team approval pending |

## 3. Dataset contributions

The final 300-record dataset derives from Sindhi sentiment material. Google Translate produced the initial Dholuo drafts for all 300 records. The final metadata records 276 as `machine_translated` (output used largely as produced) and 24 as `human_localised` (subsequently human-localised).

The initial duplicate audit identified 45 redundant occurrences. The final dataset has 300 unique record IDs and no normalized duplicate texts. The final dataset is split into train, development and test sets, with all 60 test records independently reviewed.

The initial team replacement allocation was:

| Contribution category | Planned records |
|---|---:|
| New negative examples | 16 |
| New neutral examples | 29 |
| **Total planned replacements** | **45** |

These replacements are intended to improve text uniqueness and reduce duplicate leakage across dataset splits.

The final contribution counts must be calculated from the accepted dataset and must distinguish original translated material from newly authored, human-localised or corrected examples.

## 4. Linguistic review and annotation

The team intends to use Dholuo-proficient contributors or reviewers to assess:

- Whether sentences are genuinely Dholuo.
- Whether wording is natural and understandable.
- Whether the assigned sentiment label is appropriate.
- Whether translation or contextual errors affect meaning.
- Whether ambiguous examples should be corrected, disputed or excluded.

Independent test review should be carried out by people who did not contribute the records they review.

Only completed reviews should be reported as completed contributions.

## 5. Technical contributions

The technical work includes:

- Preparing data inspection and duplicate-audit scripts.
- Developing an exploratory data-cleaning workflow.
- Implementing character-level TF-IDF features.
- Training a Logistic Regression sentiment classifier.
- Evaluating preliminary model performance.
- Developing a Streamlit demonstration application.
- Preparing reproducible environment and installation instructions.
- Documenting limitations and experimental results.

The current implementation is experimental and must not be represented as a fully validated multilingual or multi-task NLP system without evidence.

## 6. Tools and AI-use disclosure

The project used the following tools and technologies:

| Tool or technology | Purpose |
|---|---|
| Mozilla Data Collective | Original Sindhi dataset source |
| Google Translate | Machine translation from Sindhi to Dholuo |
| Python | Data processing and model development |
| pandas | Dataset manipulation and inspection |
| scikit-learn | TF-IDF feature extraction and Logistic Regression |
| Streamlit | Interactive demonstration interface |
| Git and GitHub | Version control and collaboration |
| Visual Studio Code / PowerShell | Development environment |
| AI assistance tools | Development support, documentation assistance and technical troubleshooting, where applicable |

The team must disclose any additional use of AI systems to generate, rewrite, classify or correct dataset sentences.

Machine-translated examples must not be represented as original human-authored Dholuo text.

AI-assisted documentation or code development should also be distinguished from human linguistic validation and annotation.

## 7. Individual contribution record

Complete this table with the actual names and contributions before submission.

| Team member | Data contribution | Review contribution | Technical/documentation contribution |
|---|---|---|---|
| Member 1 | TO COMPLETE | TO COMPLETE | TO COMPLETE |
| Member 2 | TO COMPLETE | TO COMPLETE | TO COMPLETE |
| Member 3 | TO COMPLETE | TO COMPLETE | TO COMPLETE |

Add additional rows if the team has more members.

## 8. Evidence of contributions

The team should retain evidence supporting its contribution claims, including:

- Dataset contribution records.
- Contributor and reviewer codes.
- Independent review sheets.
- Documented correction decisions.
- Git commit history.
- Code and notebook files.
- Model evaluation outputs.
- Application screenshots or recordings.
- Team task allocation and handover records.

Personal information should be handled responsibly and should not be published unnecessarily.

## 9. Outstanding work

The following items remain to be confirmed or completed before submission:

- Confirm each team member's name, role and actual contribution against the work and Git history.
- Confirm contributor and reviewer identities and the accuracy of the associated metadata.
- Obtain broader linguistic review from proficient Dholuo speakers; independent review metadata alone does not establish language proficiency.
- Confirm the upstream source's exact version, attribution requirements, derivative-data terms and redistribution permissions.
- Obtain team approval of the final dataset, model results and documentation.

## 10. Declaration

Team 11 aims to provide an accurate account of the data sources, human contributions, AI-assisted processes, technical work and remaining limitations associated with this project.

All final contribution and review claims must be supported by actual work and retained evidence.

**Team confirmation:** PENDING  
**Date of confirmation:** PENDING