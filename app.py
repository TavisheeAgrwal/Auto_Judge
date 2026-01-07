import streamlit as st
import joblib
import numpy as np
import re
from scipy.sparse import hstack


@st.cache_resource
def load_models():
    clf = joblib.load('difficulty_classifier.pkl')
    reg = joblib.load('score_regressor.pkl')
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    le = joblib.load('label_encoder.pkl')
    return clf, reg, tfidf, le

try:
    clf, reg, tfidf, le = load_models()
except FileNotFoundError:
    st.error("Error: Model files not found. Make sure .pkl files are in the same folder as this script!")
    st.stop()

keywords = ['graph', 'tree', 'dp', 'modulo']

def predict_difficulty(title, desc, in_desc, out_desc):

    raw_text = title + " " + desc + " " + in_desc + " " + out_desc

    text_len = len(raw_text)

    math_density = raw_text.count('$') + raw_text.count('\\') + raw_text.count('{')

    keyword_flags = [1 if kw in raw_text else 0 for kw in keywords]

    manual_features = np.array([[text_len, math_density] + keyword_flags])

    tfidf_vector = tfidf.transform([raw_text])
    
    X_input = hstack([tfidf_vector, manual_features])
    
    pred_class_idx = clf.predict(X_input)[0]
    pred_class = le.inverse_transform([pred_class_idx])[0]
    pred_score = reg.predict(X_input)[0]
    
    return pred_class, pred_score

import streamlit as st

st.set_page_config(
    page_title="AutoJudge",
    page_icon="🤖",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align: center;'>🤖 AutoJudge</h1>
    <h4 style='text-align: center; color: gray;'>
    Automated Programming Problem Difficulty Prediction
    </h4>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    This tool predicts the **difficulty class** and **difficulty score** of a competitive programming
    problem using machine learning models trained on textual problem descriptions.
    """
)

st.divider()

st.subheader("📝 Problem Details")

title = st.text_input(
    "Problem Title",
    placeholder="e.g., Watermelon"
)

st.markdown("**Problem Description**")
desc = st.text_area(
    "",
    height=200,
    placeholder="Paste the complete problem statement here..."
)

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Input Description**")
    input_desc = st.text_area(
        "",
        height=120,
        placeholder="Describe input format and constraints..."
    )

with col2:
    st.markdown("**Output Description**")
    output_desc = st.text_area(
        "",
        height=120,
        placeholder="Describe expected output..."
    )

st.divider()

predict_btn = st.button("🚀 Predict Difficulty", use_container_width=True)

if predict_btn:
    if not desc.strip():
        st.warning("⚠️ Please provide at least the problem description.")
    else:
        with st.spinner("🔍 Analyzing problem text..."):
            category, score = predict_difficulty(
                title, desc, input_desc, output_desc
            )

        st.subheader("🎯 Prediction Results")

        res_col1, res_col2 = st.columns(2)

        with res_col1:
            st.markdown(
                f"""
                <div style='padding: 20px; border-radius: 10px; background-color: #f0f2f6; text-align: center;'>
                    <h4>Predicted Category</h4>
                    <h2>{category}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        with res_col2:
            st.markdown(
                f"""
                <div style='padding: 20px; border-radius: 10px; background-color: #f0f2f6; text-align: center;'>
                    <h4>Predicted Score</h4>
                    <h2>{int(score)}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        if category == "Easy":
            st.success("🌱 This problem appears beginner-friendly.")
        elif category == "Medium":
            st.warning("⚖️ This problem has moderate difficulty.")
        elif category == "Hard":
            st.error("🔥 This problem likely requires advanced concepts.")
