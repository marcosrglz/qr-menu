from django.views import generic
from core import models


class MenuView(generic.DetailView):
    model = models.Menu
