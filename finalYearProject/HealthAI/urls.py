from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("base", views.base, name="base"),
    path("register", views.register, name="register"),
    # path("wewandiise", views.register_user, name="wewandiise"),
    path("prediction", views.prediction, name="prediction"),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("checkup", views.checkup, name="checkup"),
    path("login", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(next_page="index"), name="logout"),
    path("logout/", views.logout_view, name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='auth/password_reset_confirm.html',
             success_url=reverse_lazy('login')
         ),
         name='password_reset_confirm'),
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='auth/password_reset_complete.html'
         ), 
         name='password_reset_complete'),

]