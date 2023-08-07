from django.urls import path

from core.views import MenuView

app_name = "core"
urlpatterns = [
    path("<uuid:codigo>/", MenuView.as_view(), name="menu-detail"),
]
