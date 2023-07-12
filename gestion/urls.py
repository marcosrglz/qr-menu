from django.urls import path

from gestion.views import MenuCreateView, DashboardView

app_name = "gestion"
urlpatterns = [
    path("crear-menu", MenuCreateView.as_view(), name="crear-menu"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]