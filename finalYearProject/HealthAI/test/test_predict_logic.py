from django.test import TestCase
from HealthAI.ml_model import predict_cad

class ModelPredictionTest(TestCase):
    def test_model_predicts_with_valid_data(self):
        data = {
            "age": 60, "sex": 1, "cp": 3, "trestbps": 130, "chol": 250,
            "fbs": 0, "restecg": 1, "thalach": 150, "exang": 0,
            "oldpeak": 1.2, "slope": 1, "ca": 0, "thal": 2
        }
        result = predict_cad(data)
        self.assertIn("prediction", result)
        self.assertIn("confidence", result)
        self.assertIn("message", result)
