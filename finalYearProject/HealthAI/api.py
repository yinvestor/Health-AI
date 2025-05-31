import requests

"""Simulate how St. Francis Hospital would use the API to predict heart disease risk."""

API_URL = "http://127.0.0.1:8000/api/predict/"
headers = {"Content-Type": "application/json"}

patient_data = {
    "age": 55,
    "sex": 1,
    "cp": 0,
    "trestbps": 130,
    "chol": 250,
    "fbs": 1,
    "restecg": 1,
    "thalach": 160,
    "exang": 1,
    "oldpeak": 1.2,
    "slope": 2,
    "ca": 1,
    "thal": 2
}

response = requests.post(API_URL, json=patient_data, headers=headers)

if response.status_code == 200:
    result = response.json()
    print("Prediction:", result["prediction"])
    print("Confidence:", result["confidence"])
    print("Message:", result["message"])
else:
    print("Error:", response.status_code, response.text)