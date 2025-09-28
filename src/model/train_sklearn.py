import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import TimeSeriesSplit
import numpy as np


def train_model(df, features, target):
    """Train RandomForest on ICU admissions lag feature."""
    # 1️⃣  Split
    X = df[features].fillna(0)
    y = df[target]

    # 2️⃣  Time-series CV
    tscv = TimeSeriesSplit(n_splits=5)
    model = RandomForestRegressor(n_estimators=200, random_state=42)

    maes, rmses = [], []
    for train_idx, val_idx in tscv.split(X):
        model.fit(X.iloc[train_idx], y.iloc[train_idx])
        preds = model.predict(X.iloc[val_idx])
        maes.append(mean_absolute_error(y.iloc[val_idx], preds))
        rmses.append(np.sqrt(mean_squared_error(y.iloc[val_idx], preds)))

    print("Average MAE :", np.mean(maes))
    print("Average RMSE:", np.mean(rmses))

    # 3️⃣  Train on full data
    model.fit(X, y)

    # 4️⃣  Save inside src/models
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # -> src/
    MODEL_DIR = os.path.join(BASE_DIR, "models")
    os.makedirs(MODEL_DIR, exist_ok=True)

    MODEL_PATH = os.path.join(MODEL_DIR, "rf_model.pkl")
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model successfully saved at: {MODEL_PATH}")
    return model


if __name__ == "__main__":
    # --- Replace with real data later ---
    # Dummy example with correct column name:
    data = pd.DataFrame({
        "icu_admissions_lag1": [1, 2, 3, 4, 5, 6],
        "target": [5, 7, 9, 11, 13, 15]
    })

    FEATURES = ["icu_admissions_lag1"]
    TARGET = "target"

    train_model(data, FEATURES, TARGET)
