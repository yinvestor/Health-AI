from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, PatientsForm, CheckUpForm
from .models import Patients, CheckUp
import joblib
import numpy as np
from django.contrib.auth.models import User

model = joblib.load('c:/Users/bigir/OneDrive/Desktop/Health-AI/finalYearProject/project-models/model_training/heart_disease_xgboost_model.pkl')
scaler = joblib.load('c:/Users/bigir/OneDrive/Desktop/Health-AI/finalYearProject/project-models/model_training/heart_disease_scaler.pkl')

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    parameters = [
    {
        "title": "CP (Chest Pain Type)",
        "description": "Type of chest pain experienced.",
        "values": [
            "0: Typical angina",
            "1: Atypical angina",
            "2: Non-anginal pain",
            "3: Asymptomatic"
        ],
        "note": "Chest pain type helps assess heart risk and whether pain is heart-related."
    },
    {
        "title": "Trestbps (Resting Blood Pressure)",
        "description": "Resting blood pressure in mm Hg at admission to the hospital.",
        "note": "A higher value may indicate hypertension and increase heart disease risk."
    },
    {
        "title": "Chol (Serum Cholesterol)",
        "description": "Serum cholesterol in mg/dl.",
        "note": "Total cholesterol includes LDL, HDL, and triglycerides. High levels can block arteries."
    },
    {
        "title": "FBS (Fasting Blood Sugar)",
        "description": "Fasting blood sugar > 120 mg/dl.",
        "values": [
            "1: True (high)",
            "0: False (normal)"
        ],
        "note": "High fasting blood sugar may indicate diabetes, a major heart disease risk factor."
    },
    {
        "title": "Restecg (Resting Electrocardiographic Results)",
        "description": "ECG results at rest.",
        "values": [
            "0: Normal",
            "1: Having ST-T wave abnormality",
            "2: Showing left ventricular hypertrophy"
        ],
        "note": "Used to identify irregular heartbeats, enlarged heart, or ischemia."
    },
    {
        "title": "Thalach (Maximum Heart Rate Achieved)",
        "description": "The highest heart  rate achieved during a stress test.",
        "note": "Low values may indicate poor heart performance."
    },
    {
        "title": "Exang (Exercise-Induced Angina)",
        "description": "Whether chest pain occurred during exercise.",
        "values": [
            "1: Yes",
            "0: No"
        ],
        "note": "Presence of angina during exercise may suggest blocked arteries."
    },
    {
        "title": "Oldpeak (ST Depression Induced by Exercise Relative to Rest)",
        "description": "Amount of ST depression observed during a stress test compared to rest.",
        "note": "Higher values suggest the heart isn’t getting enough blood during activity."
    },
    {
        "title": "Slope (Slope of the Peak Exercise ST Segment)",
        "description": "Slope of the ST segment during peak exercise.",
        "values": [
            "0: Upsloping",
            "1: Flat",
            "2: Downsloping"
        ],
        "note": "Flat or downsloping ST segments often indicate heart issues."
    },
    {
        "title": "CA (Number of Major Vessels Colored by Fluoroscopy)",
        "description": "Number of major vessels (0–3) showing blood flow in a dye test.",
        "note": "More blocked vessels means higher chance of heart disease."
    },
    {
        "title": "Thal (Thallium Stress Test Result)",
        "description": "Results of a nuclear imaging test for blood flow in the heart.",
        "values": [
            "1: Normal",
            "2: Fixed defect (previous myocardial infarction)",
            "3: Reversible defect (possible ischemia)"
        ],
        "note": "Used to determine areas of reduced blood flow in the heart."
    }
]

    return render(request, 'about.html', {"parameters": parameters})

def register(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        profile_form = PatientsForm(request.POST)
        if reg_form.is_valid() and profile_form.is_valid():
            user = reg_form.save(commit=False)
            user.set_password(reg_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('checkup')
    else:
        reg_form = RegistrationForm()
        profile_form = PatientsForm()

    return render(request, 'register.html', {'form': reg_form, 'profile_form': profile_form})

def prediction(request):
    return render(request, 'prediction.html')

# @login_required
# def checkup(request):
#     if request.method == 'POST':
#         form = CheckUpForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.patient = Patients.objects.get(user=request.user)

#             features = np.array([[ 
#                 instance.age, instance.sex, instance.cp, instance.trestbps, 
#                 instance.chol, instance.fbs, instance.restecg, instance.thalach, 
#                 instance.exang, instance.oldpeak, instance.slope, 
#                 instance.ca, instance.thal
#             ]])
#             scaled = scaler.transform(features)
#             prediction = model.predict(scaled)[0]

#             instance.save()

#             return render(request, 'prediction.html', {'prediction': prediction})
#     else:
#         form = CheckUpForm()

#     return render(request, 'checkup.html', {'form': form})

from sklearn.preprocessing import StandardScaler
import shap

@login_required
def checkup(request):
    if request.method == 'POST':
        form = CheckUpForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.patient = Patients.objects.get(user=request.user)

            features = np.array([[ 
                instance.age, instance.sex, instance.cp, instance.trestbps, 
                instance.chol, instance.fbs, instance.restecg, instance.thalach, 
                instance.exang, instance.oldpeak, instance.slope, 
                instance.ca, instance.thal
            ]])
            scaled = scaler.transform(features)
            prediction = model.predict(scaled)[0]
            probability = model.predict_proba(scaled)[0][1]  # Prob. of class=1

            instance.save()

            # SHAP or model feature importances
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(scaled)
            feature_importance = list(zip(
                ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 
                 'exang', 'oldpeak', 'slope', 'ca', 'thal'], shap_values[0]
            ))
            top_features = sorted(feature_importance, key=lambda x: abs(x[1]), reverse=True)[:3]

            # Risk category
            if probability >= 0.8:
                risk = "High"
            elif probability >= 0.5:
                risk = "Medium"
            else:
                risk = "Low"

            # Health advice map
            health_advice = {
                "chol": "High cholesterol detected. Consider reducing saturated fats and increasing physical activity.",
                "trestbps": "High blood pressure. Monitor regularly and reduce sodium intake.",
                "thalach": "Low max heart rate. Discuss with a cardiologist if you feel chest pain during activity.",
                "oldpeak": "ST depression indicates possible ischemia. Further testing may be necessary.",
                "age": "Increased age is a risk factor. Regular checkups are important."
            }
            advice = [health_advice[f[0]] for f in top_features if f[0] in health_advice]

            return render(request, 'prediction.html', {
                'prediction': prediction,
                'risk': risk,
                'probability': round(probability * 100, 2),
                'top_features': top_features,
                'advice': advice
            })
    else:
        form = CheckUpForm()

    return render(request, 'checkup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    # if request.method == "POST":
    logout(request)
    return redirect('index')
    # else:
    #     return redirect('index')