from django.urls import path

from gestion.views import (  # noqa:E501
    CategoriaCreateView,
    DashboardView,
    MenuCreateView,
    MenuDeleteView,
    MenuEditView,
)

app_name = "gestion"
urlpatterns = [
    path("crear-menu/", MenuCreateView.as_view(), name="crear-menu"),
    path("editar-menu/<int:pk>/", MenuEditView.as_view(), name="editar-menu"),
    path(
        "editar-menu/<int:pk>/crear-categoria",
        CategoriaCreateView.as_view(),
        name="crear-categoria",
    ),  # noqa:E501
    path("", DashboardView.as_view(), name="dashboard"),
    path("eliminar-menu/<int:pk>", MenuDeleteView.as_view(), name="eliminar-menu"),
]
