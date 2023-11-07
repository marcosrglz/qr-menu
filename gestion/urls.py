from django.urls import path

from gestion.views import (
    CategoriaCreateView,
    CategoriaDeleteView,
    CategoriaEditView,
    DashboardView,
    MenuCreateView,
    MenuDeleteView,
    MenuEditView,
    MenuPrintQrView,
    OcultarCategoriaView,
    OcultarMenuView,
    PlatoCreateView,
    PlatoDeleteView,
    PlatoEditView,
    PublicarCategoriaView,
    PublicarMenuView,
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
        "eliminar-categoria/<int:pk>/",
        CategoriaDeleteView.as_view(),
        name="eliminar-categoria",
    ),
    path(
        "plato/<int:pk>/",
        PlatoEditView.as_view(),
        name="editar-plato",
    ),
    path("eliminar-plato/<int:pk>/", PlatoDeleteView.as_view(), name="eliminar-plato"),
    path("menu/<int:pk>/qr/", MenuPrintQrView.as_view(), name="generar-qr"),
    path("menu/<int:pk>/publicar/", PublicarMenuView.as_view(), name="publicar-menu"),
    path("menu/<int:pk>/ocultar/", OcultarMenuView.as_view(), name="ocultar-menu"),
    path(
        "<int:pk>/publicar/", PublicarCategoriaView.as_view(), name="publicar-categoria"
    ),
    path("<int:pk>/ocultar/", OcultarCategoriaView.as_view(), name="ocultar-categoria"),
]
