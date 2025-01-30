from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("base", views.base, name="base"),
    # path("register", views.register, name="register"),
    path("wewandiise", views.register_user, name="wewandiise"),
    path("prediction", views.prediction, name="prediction"),
    path("index", views.index, name="index"),
    path("checkup", views.checkup, name="checkup"),
    path("login", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]