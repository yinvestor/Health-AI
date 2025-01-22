from django.shortcuts import render, redirect
from .forms import RegistrationForm, CheckUpForm

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def demo(request):
    return render(request, 'demo.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prediction')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def prediction(request):
    return render(request, 'prediction.html')

def checkup(request):
    if request.method == 'POST':
        form = CheckUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prediction')
    else:
        form = CheckUpForm()
    return render(request, 'checkup.html', {'form': form})
