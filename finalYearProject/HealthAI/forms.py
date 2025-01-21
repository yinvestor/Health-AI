from django import forms
from .models import Patients
from .models import CheckUp

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Patients
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age', 'contact']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

class CheckUpForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.RadioSelect)
    cp = forms.ChoiceField(choices=[(0, 'Type 0'), (1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], widget=forms.RadioSelect)
    trestbps = forms.IntegerField()
    chol = forms.IntegerField()
    fbs = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], widget=forms.RadioSelect)
    restecg = forms.ChoiceField(choices=[(0, 'Normal'), (1, 'Abnormal')], widget=forms.RadioSelect)
    thalach = forms.IntegerField()
    exang = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], widget=forms.RadioSelect)
    oldpeak = forms.FloatField()
    slope = forms.ChoiceField(choices=[(0, 'Up'), (1, 'Flat'), (2, 'Down')], widget=forms.RadioSelect)
    ca = forms.ChoiceField(choices=[(0, 'None'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four')], widget=forms.RadioSelect)
    thal = forms.ChoiceField(choices=[(0, 'Normal'), (1, 'Fixed Defect'), (2, 'Reversible Defect'), (3, 'Unknown')], widget=forms.RadioSelect)

    class Meta:
        model = CheckUp