**🏥 Hospital Resource Demand Forecaster**

A **FastAPI + Streamlit** application that predicts **next-day ICU admissions** for hospitals  
based on historical ICU admission data.

---

## 📁 Project Structure
```
src/
 ├─ api/                  # FastAPI backend
 │   └─ main.py           # Prediction API
 ├─ dashboard/            # Streamlit frontend
 │   └─ app.py            # Interactive UI for predictions
 ├─ data/                 # (optional) data utilities and database helpers
 ├─ features/             # (optional) feature engineering scripts
 ├─ model/                # Training scripts
 │   ├─ train_sklearn.py
 │   └─ train_pytorch.py  # (if needed for deep learning)
 ├─ models/               # Saved models (.pkl)
 └─ requirements.txt      # Python dependencies
```

---

## 🚀 Features
- **Machine Learning model**: RandomForestRegressor trained on ICU admission lag data.
- **FastAPI backend**: Provides an endpoint to predict next-day ICU demand.
- **Streamlit dashboard**: Simple and attractive web UI to input hospital data and view predictions.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/hospital-resource-demand-forecaster.git
cd hospital-resource-demand-forecaster
```

### 2️⃣ Create & activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Run the FastAPI Backend
Start the API server:
```bash
uvicorn src.api.main:app --reload
```
The API will be available at:
- Swagger UI: **http://127.0.0.1:8000/docs**
- Predict endpoint: **http://127.0.0.1:8000/predict**

### Run the Streamlit Frontend
In a new terminal:
```bash
streamlit run src/dashboard/app.py
```
Open your browser at **http://localhost:8501** to access the dashboard.

---

## 📡 Example API Request
```bash
GET http://127.0.0.1:8000/predict?hospital_id=H001&icu_admissions_lag1=10
```
Example response:
```json
{
  "hospital_id": "H001",
  "predicted_icu_admissions": 12.5
}
```

---

## 🧩 Training the Model
To retrain the RandomForest model:
```bash
python src/model/train_sklearn.py
```
This will:
- Perform time-series cross-validation
- Train the final model
- Save the model to **src/models/rf_model.pkl**

---

## 📌 Requirements
- Python 3.10+
- FastAPI
- Streamlit
- scikit-learn
- pandas
- numpy
- joblib
- uvicorn

*(All listed in `requirements.txt`)*

