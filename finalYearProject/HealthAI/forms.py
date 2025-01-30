from django import forms
from django.contrib.auth.models import User
from .models import Patients, CheckUp

# class RegistrationForm(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
#
#     class Meta:
#         model = Patients
#         fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age', 'contact']
#         widgets = {
#             'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
#             'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
#             'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
#             'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
#             'age': forms.NumberInput(attrs={'placeholder': 'Enter Age'}),
#             'contact': forms.TextInput(attrs={'placeholder': 'Enter Contact'}),
#         }
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match")
#         return cleaned_data

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password do not match!')

        return password1


class CheckUpForm(forms.ModelForm):
    class Meta:
        model = CheckUp
        fields = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        widgets = {
            field: forms.NumberInput(attrs={'placeholder': f'Enter {field.capitalize()}'})
            for field in [
                'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                'restecg', 'thalach', 'exang', 'oldpeak', 'slope',
                'ca', 'thal'
            ]
        }
