from django.http import request
from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.
def base(request):
    return render(request, template_name='base.html')

def index(request):
    return render(request, template_name='index.html')

def demo(request):
    return render(request, template_name='demo.html')

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
    return render(request, 'checkup.html')