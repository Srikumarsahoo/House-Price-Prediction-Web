🏠 House Price Prediction API

A complete Machine Learning powered House Price Prediction system built with Python, Scikit-learn, FastAPI, and Streamlit.
The project predicts housing prices based on user-provided property details using an Ensemble Learning model (Stacking Regressor combining Random Forest and Gradient Boosting).

The model is deployed as a REST API using FastAPI, with an optional Streamlit frontend for interactive predictions. The project is fully containerized using Docker for easy deployment and reproducibility.

🚀 Features

• Machine Learning price prediction using Stacking Ensemble Model

• Backend API built with FastAPI

• Interactive frontend using Streamlit

• Feature engineering for improved prediction accuracy

• Model evaluation using RMSE

• Containerized deployment using Docker

• Easy setup using Docker pull or Git clone


🧠 Machine Learning Approach

The model uses ensemble learning to improve prediction accuracy.

Algorithms used:

• Random Forest Regressor

• Gradient Boosting Regressor

• Stacking Regressor (final model)


Feature engineering techniques applied:

• Rooms per household

• Bedrooms per room

• Population per household

Model performance is evaluated using Root Mean Squared Error (RMSE).

⚙️ Technologies Used

Python

Scikit-learn

FastAPI

Streamlit

Pandas

NumPy

Docker

REST API

Machine Learning

Feature Engineering


🐳 Run Using Docker (Recommended)
The easiest way to run the project is using Docker.

Pull the Docker Image

docker pull srikumarsahoo/house-price-prediction-api

Run the Container

docker run -p 8000:8000 srikumarsahoo/house-price-prediction-api

Open the API

After running the container, open:

http://127.0.0.1:8000/docs

This opens the FastAPI interactive Swagger UI where you can test the API.

💻 Run Locally (Without Docker)
Clone the Repository:
git clone https://github.com/Srikumarsahoo/house-price-prediction-api.git

Go to the project directory:
cd house-price-prediction-api

Install dependencies:
pip install -r requirements.txt

Run the API server:
uvicorn main:app --reload

Open API documentation:
http://127.0.0.1:8000/docs

🧾 API Request Example
POST /predict

Example request body:

{
  "Area_Sq": 2000,
  "Income": 8.5,
  "Bedrooms": 3,
  "Bathrooms": 2,
  "floors": 1,
  "House_age": 10,
  "location_score": 5,
  "Parking": 1
}
📊 Example API Response
{
  "predicted_price": 268000,
  "price_range": {
    "min": 222000,
    "max": 314000
  },
  "category": "Medium Price"
}
🖥 Streamlit Frontend (Optional)

Run the Streamlit UI:

streamlit run frontend/app.py

The frontend allows users to enter property details and receive predictions visually.

📦 Docker Deployment

This project is fully containerized and can be deployed on:

• Docker

• AWS EC2

• Render

• Railway

• Kubernetes

• Google Cloud Run
