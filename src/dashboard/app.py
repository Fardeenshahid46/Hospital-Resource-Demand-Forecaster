import streamlit as st
import requests

st.set_page_config(
    page_title="Hospital Resource Demand Forecaster",
    page_icon="🏥",
    layout="centered",
)

st.markdown("""
    <style>
        .main { padding-top: 2rem; }
       
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            border-radius: 10px;
        }
        div.stButton > button{
            background-color: #4CAF50;
            color: white;
            border-radius: 12px;
            padding: 0.6rem 1.2rem;
            font-size: 1.1rem;
            transition: background-color 0.3s ease;
        }
        div.stButton > button:first-child:hover {
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

st.markdown("</div>", unsafe_allow_html=True)

if st.button("🔮 Predict Next-Day ICU Demand"):
    try:
        resp = requests.get(
            "http://127.0.0.1:8000/predict",
            params={
                "hospital_id": hospital_id,
                "icu_admissions_lag1": icu_admissions_lag1
            },
            timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
        st.success(
            f"✅ **Predicted ICU admissions for {hospital_id}: "
            f"{data['predicted_icu_admissions']}**"
        )
    except requests.exceptions.RequestException:
        st.error("⚠️ Could not reach the prediction API. Make sure the backend is running.")
    except KeyError:
        st.error("⚠️ Unexpected response format from the API.")
