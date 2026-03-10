import joblib
import pandas as pd

# Load model data
data = joblib.load("model/house_model.pkl")

model = data["model"]
features = data["features"]
rmse = data["rmse"]

MODEL_VERSION = "1.0.0"


def predict_output(user_input: dict):

    # Convert input to dataframe
    df = pd.DataFrame([user_input])

    # Feature engineering (same as training script)
    df["rooms_per_household"] = df["Area_Sq"] / df["floors"]
    df["bedrooms_per_room"] = df["Bedrooms"] / df["Area_Sq"]
    df["population_per_household"] = df["Bathrooms"] / df["floors"]

    # Ensure correct feature order
    df = df[features]

    # Prediction
    prediction = model.predict(df)[0]

    # Category classification
    if prediction < 150000:
        category = "Budget House"
    elif prediction < 300000:
        category = "Medium Price"
    elif prediction < 500000:
        category = "Premium"
    else:
        category = "Luxury"

    response = {
        "predicted_price": round(prediction, 2),
        "price_range": {
            "min": round(prediction - rmse, 2),
            "max": round(prediction + rmse, 2)
        },
        "category": category
    }

    return response