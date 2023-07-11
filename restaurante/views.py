from django.views import generic
from django.views.generic.edit import CreateView

from core import models


class RestauranteDetailView(generic.DetailView):
    model = models.Restaurante
    template_name = "restaurante/restaurante_detail.html"


class MenuCreateView(CreateView):
    model = models.Menu
    fields = ["nombre"]
    template_name = "restaurante/crear_menu.html"
