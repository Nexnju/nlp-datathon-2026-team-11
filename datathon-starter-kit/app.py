
from pathlib import Path

import joblib
import streamlit as st

from core import FRIENDLY, extract


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Dholuo NLP Demo",
    page_icon="🌍",
    layout="centered",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>
        .block-container {
            max-width: 900px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .main-heading {
            font-size: 2.5rem;
            font-weight: 750;
            margin-bottom: 0.2rem;
        }

        .subheading {
            color: #8b949e;
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }

        .result-card {
            padding: 1.4rem;
            border-radius: 12px;
            border: 1px solid rgba(128, 128, 128, 0.3);
            margin-top: 1rem;
            margin-bottom: 1rem;
        }

        .result-label {
            font-size: 1.7rem;
            font-weight: 700;
            margin-top: 0.3rem;
        }

        .small-note {
            color: #8b949e;
            font-size: 0.85rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.title("🌍 Dholuo NLP")
    st.caption("African-language NLP demonstration")

    st.divider()

    track = "sentiment"
    st.caption("Task: Sentiment analysis")

    st.divider()

    st.markdown("### About this demo")
    st.write(
        "This application demonstrates natural language "
        "processing for Dholuo text."
    )

    st.markdown("**Supported tasks**")
    st.write("- Sentiment analysis")

    st.divider()

    st.caption("Team 11 | NLP Hub Datathon 2026")


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

path = Path("artifacts") / track / "model.joblib"

st.markdown(
    '<div class="main-heading">African-language NLP Demo</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subheading">'
    'Explore how an NLP model processes Dholuo language.'
    '</div>',
    unsafe_allow_html=True
)

if not path.exists():
    st.info(
        f"No trained model was found for **{track.capitalize()}**. "
        "Train this task first, then try again."
    )
    st.stop()

try:
    pack = joblib.load(path)
except Exception as error:
    st.error(f"Could not load the model: {error}")
    st.stop()


# --------------------------------------------------
# MODEL INFORMATION AND WARNINGS
# --------------------------------------------------

if pack.get("practice", False):
    st.warning(
        "PRACTICE MODE: This model uses constructed English "
        "teaching examples."
    )

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.metric("Language", pack.get("language", "Not specified"))

with info_col2:
    st.metric("NLP task", track.capitalize())

st.divider()


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.subheader("Try the model")

st.write(
    "Enter a sentence in Dholuo and let the model analyse it."
)

user_text = st.text_area(
    "Your Dholuo sentence",
    placeholder="Type or paste a Dholuo sentence here...",
    height=130,
    key="user_text"
)

predict_clicked = st.button(
    "Analyse sentence",
    type="primary",
    use_container_width=True
)


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if predict_clicked:

    if not user_text.strip():
        st.info("Please enter a sentence before analysing it.")

    else:
        try:
            with st.spinner("Analysing your sentence..."):

                model = pack["model"]

                label = model.predict([user_text])[0]

                probabilities = model.predict_proba([user_text])[0]

                confidence = max(probabilities)

                friendly_label = FRIENDLY.get(label, label)

            st.divider()
            st.subheader("Analysis result")
            st.markdown("**Sentence analysed**")
            st.info(user_text)

            # SENTIMENT CLASSIFICATION
            if track == "sentiment":

                st.markdown(
                    f"""
                    <div class="result-card">
                        <div class="small-note">Predicted sentiment</div>
                        <div class="result-label">{friendly_label}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.caption(
                    "The model assigns one of its known sentiment labels "
                    "to the sentence."
                )

            # INTENT CLASSIFICATION
            elif track == "intent":

                st.markdown(
                    f"""
                    <div class="result-card">
                        <div class="small-note">Predicted intent</div>
                        <div class="result-label">{friendly_label}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.info(
                    "Simulated route only. No calendar, music, weather "
                    "or other external action has been executed."
                )

            # SEMANTIC PARSING
            elif track == "semantic":


                st.markdown(
                    f"""
                    <div class="result-card">
                        <div class="small-note">Predicted intent</div>
                        <div class="result-label">{friendly_label}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                slots = extract(user_text, pack["slot_memory"])

                st.markdown("### Extracted information")

                st.json({
                    "intent": label,
                    "slots": slots
                })

                st.caption(
                    "Training-only surface-value matcher: unseen slot "
                    "values may be missed. No date/time normalisation "
                    "or real action is performed."
                )

            # PROBABILITY BREAKDOWN
            st.markdown("### Class probability breakdown")

            # Match probabilities to their actual class labels
            classes = model.classes_

            probability_data = sorted(
                zip(classes, probabilities),
                key=lambda item: item[1],
                reverse=True
            )

            for class_label, probability in probability_data:
                friendly_class = FRIENDLY.get(class_label, class_label)

                st.write(f"**{friendly_class} — {probability:.1%}**")
                st.progress(float(probability))

            st.caption(
                "These probabilities represent the model's estimated scores "
                "for each available class. They are uncalibrated and should "
                "not be interpreted as guaranteed correctness."
            )

            # SENTIMENT-SPECIFIC LIMITATION
            if track == "sentiment":
                st.info(
                    "This is sentence-level opinion classification. "
                    "It is not emotion detection, sarcasm understanding "
                    "or a diagnosis."
                )

        except Exception as error:
            st.error(f"An error occurred during prediction: {error}")


# --------------------------------------------------
# ABOUT THE MODEL
# --------------------------------------------------

st.divider()


with st.expander("About the model and methodology"):

    st.markdown("### Dataset")

    st.write(
        "The final Dholuo sentiment dataset contains "
        "300 records, balanced across three sentiment classes."
    )

    dataset_col1, dataset_col2, dataset_col3 = st.columns(3)

    dataset_col1.metric("Positive", "100")
    dataset_col2.metric("Negative", "100")
    dataset_col3.metric("Neutral", "100")

    st.caption(
        "All 300 records are derived from Sindhi source material. "
        "Google Translate produced the initial Dholuo drafts for all 300 records. "
        "Of these, 276 were used largely as translated (machine_translated) and 24 were subsequently human-localised (human_localised)."
        " The dataset is split into 180 training, 60 development "
        "and 60 test records."
    )

    st.caption(
        "Review metadata: 217 self-reviewed records and 83 "
        "independently reviewed records. All 60 test records are "
        "marked independently reviewed in the supplied metadata."
    )

    st.markdown("### Model methodology")

    st.write(
        "**Feature extraction:** Character-level TF-IDF "
        "using 2–5 character n-grams."
    )

    st.write(
        "**Classification algorithm:** Logistic Regression "
        "with a maximum of 1,000 iterations."
    )

    st.write(
        "**Evaluation approach:** Training and development data "
        "were used for model fitting and development evaluation. "
        "The held-out test set was evaluated separately after "
        "the model was frozen."
    )

    st.markdown("### Final test evaluation")

    metric_col1, metric_col2 = st.columns(2)

    metric_col1.metric("Test accuracy", "61.67%")
    metric_col2.metric("Test macro-F1", "0.6111")

    st.caption(
        "Evaluation on 60 held-out test records. These results "
        "are specific to this dataset and should be interpreted "
        "with its size and language-quality limitations in mind."
    )

    st.markdown("### Development evaluation")

    st.write(
        "**Development accuracy:** 70.00%"
    )

    st.write(
        "**Development macro-F1:** 0.6984"
    )

    st.markdown("### Known limitations")

    st.write(
        "- The dataset is relatively small, with 300 records."
    )

    st.write(
        "- Independent review covers 83 records overall. All 60 "
        "held-out test records were independently reviewed; the "
        "remaining records have varying review status."
    )

    st.write(
        "- The model may struggle with dialect differences, "
        "sarcasm, mixed-language text and unfamiliar expressions."
    )

    st.write(
        "- Predictions are estimates and may not reflect the "
        "intended meaning of every Dholuo sentence."
    )

    st.warning(
        "This is a research demonstration, not a production-ready "
        "language system. Evaluation results should not be treated "
        "as proof of general performance across Dholuo speakers "
        "or dialects."
    )



# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "NLP Hub Datathon 2026 | Team 11 | Dholuo Sentiment Analysis"
)

st.caption(
    "Experimental research demonstration. Results should be "
    "interpreted with the model's data and evaluation limitations in mind."
)
