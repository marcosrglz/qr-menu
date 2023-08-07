from django.urls import path

from gestion.views import (
    CategoriaCreateView,
    CategoriaEditView,
    DashboardView,
    MenuCreateView,
    MenuDeleteView,
    MenuEditView,
    PlatoCreateView,
    MenuPrintQrView
)

app_name = "gestion"
urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("crear-menu/", MenuCreateView.as_view(), name="crear-menu"),
    path("editar-menu/<int:pk>/", MenuEditView.as_view(), name="editar-menu"),
    path(
        "editar-menu/<int:pk>/crear-categoria/",
        CategoriaCreateView.as_view(),
        name="crear-categoria",
    ),
    path("eliminar-menu/<int:pk>/", MenuDeleteView.as_view(), name="eliminar-menu"),
    path(
        "categoria/<int:pk>/",
        CategoriaEditView.as_view(),
        name="editar-categoria",
    ),
    path(
        "editar-categoria/<int:pk>/crear-plato/",
        PlatoCreateView.as_view(),
        name="crear-plato",
    ),
    path(
        "menu/<int:pk>/qr/",
        MenuPrintQrView.as_view(),
        name="generar-qr"
    )
]
