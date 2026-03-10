from fastapi import FastAPI, HTTPException, Path
from schema.user_input import UserInput
from fastapi.responses import JSONResponse
from model.predict import MODEL_VERSION, predict_output,model
from schema.prediction_response import PredictionResponse
import os
import json
import pandas as pd

app = FastAPI(title = "House-Price-Prediction")

@app.get('/')
def home():
    return {'message':'Welcome to the house-price-prediction-api'}

@app.get('/health')
def health_check():
    return {
        'status':'OK',
        'version':MODEL_VERSION,
        'model_loaded':model is not None
    }

@app.post('/predict', response_model = PredictionResponse )
def predict_price(data: UserInput):
    try:
        user_input={
            'Area_Sq': data.Area_Sq,
            'Income': data.Income,
            'Bedrooms': data.Bedrooms,
            'Bathrooms':data.Bathrooms,
            'floors':data.floors,
            'House_age':data.House_age,
            'location_score':data.location_score,
            'Parking': data.Parking
        }
        
        prediction= predict_output(user_input)
        return JSONResponse(status_code = 200, content={'message':prediction})
    
    except Exception as e:
        return JSONResponse(status_code =500, content=str(e))
        

    