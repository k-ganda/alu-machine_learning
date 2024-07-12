from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the model and scalers
model = joblib.load('linear_regression_model.pkl')
scaler_bmi = joblib.load('scaler_bmi.pkl')
scaler_charges = joblib.load('scaler_charges.pkl')

class InsuranceData(BaseModel):
    age: int
    sex: int
    bmi: float
    children: int
    smoker: int
    region: int
    
@app.get("/")
def get_hello():
    return {"message": "Hello World"}

@app.post("/predict")
def predict(data: InsuranceData):
    # Convert the input data to a DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Standardize the 'bmi' value
    input_df['bmi'] = scaler_bmi.transform(input_df[['bmi']])

    # Make prediction
    prediction_scaled = model.predict(input_df)
    prediction = scaler_charges.inverse_transform(prediction_scaled.reshape(-1, 1)).flatten()

    return {"predicted_charges": prediction[0]}
