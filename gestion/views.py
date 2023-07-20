from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView

from core import models


# Creación de menú
class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = ["nombre", "descripcion"]

    def __init__(self, *args, user, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        return models.Menu.objects.create(
            nombre=self.cleaned_data["nombre"],
            descripcion=self.cleaned_data["descripcion"],
            usuario=self.user,
        )


class MenuCreateView(LoginRequiredMixin, CreateView):
    form_class = MenuCreateForm
    template_name = "gestion/crear_menu.html"
    success_url = reverse_lazy("gestion:dashboard")
    login_url = reverse_lazy("auth:login")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


# Dashboard del usuario
class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "gestion/dashboard.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["menus"] = models.Menu.objects.filter(usuario=self.request.user).annotate(
            plato_count=Count("categoria__plato")
        )
        return data
