from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

from core import models


# Menús
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


class MenuEditView(LoginRequiredMixin, DetailView):
    model = models.Menu
    template_name = "gestion/editar_menu.html"
    success_url = reverse_lazy("gestion:dashboard")
    login_url = reverse_lazy("auth:login")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_queryset(self):
        return models.Menu.objects.filter(usuario=self.request.user)


# Categoría
class CategoriaCreateForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ["nombre"]

    def __init__(self, *args, menu, **kwargs):
        self.menu = menu
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        return models.Categoria.objects.create(
            nombre=self.cleaned_data["nombre"],
            menu=self.menu
        )


class CategoriaCreateView(LoginRequiredMixin, UpdateView):
    model = models.Menu
    form_class = CategoriaCreateForm
    template_name = "gestion/crear_categoria.html"
    login_url = reverse_lazy("auth:login")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = models.Categoria()
        kwargs["menu"] = self.get_object()
        return kwargs

    def get_queryset(self):
        return models.Menu.objects.filter(usuario=self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["menu"] = self.get_object()
        return data

    def get_success_url(self):
        return reverse_lazy("gestion:editar-menu", args=[self.get_object().pk])


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
