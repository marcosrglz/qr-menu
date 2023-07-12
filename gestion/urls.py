from django.urls import path

from gestion.views import MenuCreateView

app_name = "gestion"
urlpatterns = [
    path("crear-menu", MenuCreateView.as_view(), name="crear-menu"),
]
