from django.shortcuts import render, redirect
from .forms import UserRegisterForm, CheckUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('prediction')
#     else:
#         form = RegistrationForm()
#     return render(request, 'register.html', {'form': form})

def prediction(request):
    return render(request, 'prediction.html')

@login_required
def checkup(request):
    if request.method == 'POST':
        form = CheckUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prediction')
    else:
        form = CheckUpForm()
    return render(request, 'checkup.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'wewandiise.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form':form})

def logout_view(request):
    if request.method == "POST":  # Recommended security practice
        logout(request)
        return redirect('login')
    else:
        return redirect('index')  # Redirect elsewhere if accessed via GET