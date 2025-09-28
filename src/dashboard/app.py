import streamlit as st
import joblib
import pandas as pd
import os

# --- Page Config ---
st.set_page_config(
    page_title="Hospital Resource Demand Forecaster",
    page_icon="🏥",
    layout="centered",
)

# --- Model load ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
MODEL_PATH = os.path.join(BASE_DIR, "models", "rf_model.pkl")
model = joblib.load(MODEL_PATH)

# --- UI Styling ---
st.markdown("""
    <style>
        .main { padding-top: 2rem; }
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            border-radius: 10px;
        }
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 12px;
            padding: 0.6rem 1.2rem;
            font-size: 1.1rem;
            transition: background-color 0.3s ease;
        }
        div.stButton > button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🏥 **Hospital Resource Demand Forecaster**")
st.write(
    "Predict next-day ICU admissions for your hospital. "
    "Enter hospital details below and click **Predict**."
)

col1, col2 = st.columns(2)
with col1:
    hospital_id = st.text_input("🏨 Hospital ID", "H001")
with col2:
    icu_admissions_lag1 = st.number_input(
        "📈 ICU admissions yesterday",
        min_value=0,
        value=10,
        step=1
    )

if st.button("🔮 Predict Next-Day ICU Demand"):
    X = pd.DataFrame([{"icu_admissions_lag1": icu_admissions_lag1}])
    y_pred = model.predict(X)[0]
    st.success(
        f"✅ **Predicted ICU admissions for {hospital_id}: {y_pred:.0f}**"
    )
