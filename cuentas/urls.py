from django.urls import path

from . import views

urlpatterns = [
    path("registrarse/", views.SignUpView.as_view(), name="registrarse"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
]
