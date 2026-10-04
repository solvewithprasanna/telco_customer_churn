import joblib
import pandas as pd


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("telco_churn_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")


class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float
    numAdminTickets: int
    numTechTickets: int



@app.post("/predict")
def predict(data: CustomerData):
    input_data = data.model_dump()

    transformed_data = preprocessor.transform(pd.DataFrame([input_data]))

    probability = model.predict_proba(transformed_data)[0][1]

    prediction = 1 if probability >= 0.40 else 0

    return {
        "churn_probability": round(float(probability), 4),
        "churn_prediction": prediction,
        "threshold": 0.40
    }