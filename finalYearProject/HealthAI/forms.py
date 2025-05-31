from django import forms
from django.contrib.auth.models import User
from .models import Patients, CheckUp

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['first_name', 'last_name', 'email', 'age', 'contact']
        widgets = {
            'contact': forms.TextInput(attrs={'placeholder': 'Eg. 0744939399', type: 'tel'})
        
        }
from django import forms
from .models import CheckUp

class CheckUpForm(forms.ModelForm):
    class Meta:
        model = CheckUp
        fields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                  'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

        widgets = {
            'age': forms.NumberInput(attrs={
                'placeholder': 'e.g. 45', 'min': 18, 'max': 120
            }),
            'sex': forms.Select(choices=[(1, 'Female'), (2, 'Male')]),
            'cp': forms.Select(choices=[
                (0, 'Typical Angina(0)'), 
                (1, 'Atypical Angina(1)'), 
                (2, 'Non-anginal Pain(2)'), 
                (3, 'Asymptomatic(3)')
            ]),
            'trestbps': forms.NumberInput(attrs={
                'placeholder': 'e.g. 130 mm Hg(70 - 200)', 'min': 70, 'max': 200
            }),
            'chol': forms.NumberInput(attrs={
                'placeholder': 'e.g. 250 mg/dl(100 - 600)', 'min': 100, 'max': 600
            }),
            'fbs': forms.Select(choices=[(0, 'False (<120 mg/dl)'), (1, 'True (>=120 mg/dl)')]),
            'restecg': forms.Select(choices=[
                (0, 'Normal(0)'),
                (1, 'ST-T Abnormality(1)'),
                (2, 'Left Ventricular Hypertrophy(2)')
            ]),
            'thalach': forms.NumberInput(attrs={
                'placeholder': 'e.g. 150 bpm(60 - 220)', 'min': 60, 'max': 220
            }),
            'exang': forms.Select(choices=[(0, 'No(0)'), (1, 'Yes(1)')]),
            'oldpeak': forms.NumberInput(attrs={
                'placeholder': 'e.g. 1.4(ST depression from 1.0 to 6)', 'step': 0.1, 'min': 0, 'max': 6
            }),
            'slope': forms.Select(choices=[
                (0, 'Upsloping(0)'),
                (1, 'Flat(1)'),
                (2, 'Downsloping(2)')
            ]),
            'ca': forms.Select(choices=[(i, f'{i} major vessels') for i in range(5)]),
            'thal': forms.Select(choices=[
                (1, 'Normal(1)'),
                (2, 'Fixed Defect(2)'),
                (3, 'Reversible Defect(3)')
            ]),
        }

    # Optional: backend validation for one field
    def clean_trestbps(self):
        val = self.cleaned_data['trestbps']
        if not (70 <= val <= 200):
            raise forms.ValidationError("Resting blood pressure must be between 70 and 200 mm Hg.")
        return val

    def clean_oldpeak(self):
        val = self.cleaned_data['oldpeak']
        if not (0 <= val <= 6):
            raise forms.ValidationError("Oldpeak should be between 0.0 and 6.0.")
        return val

    def clean(self):
        cleaned_data = super().clean()
        # Add cross-field validation if needed here
        return cleaned_data
