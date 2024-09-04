from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI()

# Load the model and scalers
model = joblib.load('model.pkl')
scaler_bmi = joblib.load('scaler_bmi.pkl')
scaler_charges = joblib.load('scaler_charges.pkl')

class InsuranceData(BaseModel):
    age: int = Field(gt=17, lt=101, description='Age must be between 18 and 100')
    sex: int = Field(ge=0, le=1, description='Sex must be 0(male) or 1(female)')
    bmi: float = Field(gt=0, description="BMI must be greater than 0")
    children: int = Field(ge=0, description="Number of children must be a non-negative integer")
    smoker: int = Field(ge=0, le=1, description="Smoker must be 0 (no) or 1 (yes)")
    region: int = Field(ge=0, le=3, description="Region must be between 0 and 3")
    
@app.get("/", status_code=status.HTTP_200_OK)
async def get_hello():
    try:
        return {"message": "Hello World"}
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=err)

@app.post("/predict")
async def predict(data: InsuranceData):
    try:
        # Convert the input data to a DataFrame
        input_df = pd.DataFrame([data.dict()])

        # Standardize the 'bmi' value
        input_df['bmi'] = scaler_bmi.transform(input_df[['bmi']])

        # Make prediction
        prediction_scaled = model.predict(input_df)
        prediction = scaler_charges.inverse_transform(prediction_scaled.reshape(-1, 1)).flatten()

        return {"predicted_charges": prediction[0]}
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=err)
