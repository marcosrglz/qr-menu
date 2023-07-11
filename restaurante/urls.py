from django.urls import path

from restaurante.views import MenuCreateView, RestauranteDetailView

app_name = "restaurante"
urlpatterns = [
    path("<int:pk>/", RestauranteDetailView.as_view(), name="restaurante-detail"),
    path("crear-menu", MenuCreateView.as_view(), name="crear-menu"),
]
