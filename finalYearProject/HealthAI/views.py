from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, PatientsForm, CheckUpForm
from .models import Patients, CheckUp
import joblib
import numpy as np
from django.contrib.auth.models import User

model = joblib.load('c:/Users/User/Documents/Health-AI/finalYearProject/project-models/model_training/heart_disease_xgboost_model.pkl')
scaler = joblib.load('c:/Users/User/Documents/Health-AI/finalYearProject/project-models/model_training/heart_disease_scaler.pkl')

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

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

            instance.save()

            return render(request, 'prediction.html', {'prediction': prediction})
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
    if request.method == "POST":
        logout(request)
        return redirect('index')
    else:
        return redirect('index')