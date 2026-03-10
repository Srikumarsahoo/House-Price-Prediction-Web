import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="centered")

st.title("🏠 Housing Price Prediction")
st.markdown("### Enter your property details")

st.divider()

# Input fields
Area_Sq = st.number_input("Area per Square meter", min_value=100)

Income = st.number_input("Income (LPA)", min_value=1.0)

Bedrooms = st.number_input("Bedrooms", min_value=1, max_value=20)

Bathrooms = st.number_input("Bathrooms", min_value=1, max_value=20)

floors = st.number_input("Number of Floors required", min_value=1, max_value=20)

House_age = st.number_input("Enter the age of house", min_value=1, max_value=50)

location_score = st.number_input("Enter the location popularity", min_value=1, max_value=100)

Parking = st.number_input("Number of parkings required", min_value=0, max_value=10)

st.divider()

# Button
if st.button("Predict My House Price", use_container_width=True):

    input_data = {
        "Area_Sq": Area_Sq,
        "Income": Income,
        "Bedrooms": Bedrooms,
        "Bathrooms": Bathrooms,
        "floors": floors,
        "House_age": House_age,
        "location_score": location_score,
        "Parking": Parking
    }

    try:
        response = requests.post(API_URL, json=input_data)

        try:
            result = response.json()
        except:
            st.error("Invalid response from API")
            st.stop()

        if response.status_code == 200 and "response" in result:

            prediction = result["response"]

            st.success("Prediction Successful")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    label="Predicted House Price",
                    value=f"₹ {prediction['Predicted_price']}"
                )

            with col2:
                st.metric(
                    label="Category",
                    value=prediction["Category"]
                )

            st.markdown("### Price Range")
            st.info(prediction["Price_range"])

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")