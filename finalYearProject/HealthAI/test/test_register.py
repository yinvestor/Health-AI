from django.test import TestCase
from HealthAI.forms import RegistrationForm

class RegistrationFormTest(TestCase):
    def test_registration_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'securepass123',
            'confirm_password': 'securepass123'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'securepass123',
            'confirm_password': 'wrongpass'
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("Passwords do not match", form.errors["__all__"])
