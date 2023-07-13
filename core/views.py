from django.views import generic

from core import models


class MenuView(generic.DetailView):
    model = models.Menu
    template_name = "core/menu_detail.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related("usuario")
        return queryset
