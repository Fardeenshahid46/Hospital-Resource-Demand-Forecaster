from fastapi import FastAPI
import joblib
import pandas as pd
import os

app = FastAPI(
    title="Hospital Resource Demand Forecaster",
    description="Predict next-day ICU admissions",
    version="1.0"
)

# ---- Load trained model ----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # -> src/
MODEL_PATH = os.path.join(BASE_DIR, "models", "rf_model.pkl")

model = joblib.load(MODEL_PATH)


@app.get("/predict")
def predict(hospital_id: str = "H001", icu_admissions_lag1: float = 0):
    """
    Predict next-day ICU admissions based on yesterday's ICU admissions.
    """
    X = pd.DataFrame([{"icu_admissions_lag1": icu_admissions_lag1}])
    y_pred = model.predict(X)[0]
    return {
        "hospital_id": hospital_id,
        "predicted_icu_admissions": float(y_pred)
    }
