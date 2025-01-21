from django.db import models

# Create your models here.
class Patients(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    contact = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class CheckUp(models.Model):
    username = models.ForeignKey(Patients, on_delete=models.DO_NOTHING)
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    oldpeak = models.FloatField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()


class Predictions(models.Model):
    condition = models.IntegerField()

    def __str__(self):
        if self.condition == 1:
            return f'You have tested positive with Coronary Heart Disease.\n With a result of {self.condition}.'
        elif self.condition == 0:
            return f'You have tested negative with Coronary Heart Disease.\n With a result of {self.condition}.'
