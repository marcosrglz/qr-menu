from django.urls import path

from core.views import MenuView

app_name = "core"
urlpatterns = [
    path("<int:pk>/", MenuView.as_view(), name="menu-detail"),
]
