from django.urls import path

from .views import SignUpView

urlpatterns = [
    path("registrarse/", SignUpView.as_view(), name="registrarse"),
]
