from django.urls import path
from . import views


urlpatterns = [
    path("base", views.base, name="base"),
    path("demo", views.demo, name="demo"),
    path("register", views.register, name="register"),
    path("prediction", views.prediction, name="prediction"),
    path("index", views.index, name="index"),
    path("checkup", views.checkup, name="checkup")
]