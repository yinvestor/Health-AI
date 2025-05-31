from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CheckUpAPISerializer
import joblib
import numpy as np




import joblib
import numpy as np

model = joblib.load('c:/Users/dell/OneDrive/Desktop/Health-AI/finalYearProject/project-models/model_training/heart_disease_xgboost_model.pkl')
scaler = joblib.load('c:/Users/dell/OneDrive/Desktop/Health-AI/finalYearProject/project-models/model_training/heart_disease_scaler.pkl')


def predict_cad(data):
    features = np.array([[ 
        data['age'], data['sex'], data['cp'], data['trestbps'],
        data['chol'], data['fbs'], data['restecg'], data['thalach'],
        data['exang'], data['oldpeak'], data['slope'],
        data['ca'], data['thal']
    ]])
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][int(prediction)]

    return {
        'prediction': int(prediction),
        'confidence': round(prob * 100, 2),
        'message': "High risk of CAD" if prediction else "Low risk of CAD"
    }