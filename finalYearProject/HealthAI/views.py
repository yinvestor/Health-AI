from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, PatientsForm, CheckUpForm
from .models import Patients, CheckUp
from django.contrib.auth.models import User
import joblib
import numpy as np
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CheckUpAPISerializer
from .ml_model import predict_cad
import shap

# Load model and scaler once
model = joblib.load('c:/Users/dell/OneDrive/Desktop/Health-AI/finalYearProject/project-models/model_training/heart_disease_xgboost_model.pkl')
scaler = joblib.load('c:/Users/dell/OneDrive/Desktop/Health-AI/finalYearProject/project-models/model_training/heart_disease_scaler.pkl')

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    parameters = [ ... ]  # keep your existing parameters data here
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
            probability = model.predict_proba(scaled)[0][1]
            instance.save()

            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(scaled)
            feature_importance = list(zip(
                ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 
                'exang', 'oldpeak', 'slope', 'ca', 'thal'], shap_values[0]
            ))
            top_features = sorted(feature_importance, key=lambda x: abs(x[1]), reverse=True)[:3]

            if probability >= 0.8:
                risk = "High"
            elif probability >= 0.5:
                risk = "Medium"
            else:
                risk = "Low"

            health_advice = {
                "chol": "High cholesterol detected. Reduce saturated fats and increase physical activity.",
                "trestbps": "High blood pressure. Monitor regularly and reduce sodium intake.",
                "thalach": "Low heart rate. Consider cardiologist consultation if chest pain occurs.",
                "oldpeak": "Possible ischemia. Further cardiac tests are recommended.",
                "age": "Age is a risk factor. Schedule regular heart checkups."
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
    logout(request)
    return redirect('index')

# API View
@api_view(['POST'])
def predict_cad_api(request):
    serializer = CheckUpAPISerializer(data=request.data)
    if serializer.is_valid():
        try:
            result = predict_cad(serializer.validated_data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    print(serializer.errors)  # Debugging
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)