from io import BytesIO

import qrcode
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from core import models


# Dashboard del usuario
class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "gestion/dashboard.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["menus"] = models.Menu.objects.filter(usuario=self.request.user).annotate(
            plato_count=Count("categoria__plato"), acceso_count=Count("acceso")
        )
        data["breadcrumbs"] = [
            {
                "label": "Panel",
                "href": reverse_lazy("gestion:dashboard"),
                "active": True,
            }
        ]
        return data


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
    login_url = reverse_lazy("login")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {
                "label": "Panel",
                "href": reverse_lazy("gestion:dashboard"),
                "active": False,
            },
            {
                "label": "Crear Menú",
                "href": reverse_lazy("gestion:crear-menu"),
                "active": True,
            },
        ]
        return context


class MenuUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = ["nombre", "descripcion"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["descripcion"].widget = forms.Textarea()


class MenuEditView(LoginRequiredMixin, UpdateView):
    model = models.Menu
    form_class = MenuUpdateForm
    template_name = "gestion/editar_menu.html"
    login_url = reverse_lazy("login")

    def get_queryset(self):
        return models.Menu.objects.filter(usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy("gestion:editar-menu", args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["breadcrumbs"] = [
            {
                "label": "Panel",
                "href": reverse_lazy("gestion:dashboard"),
                "active": False,
            },
            {
                "label": self.get_object().nombre,
                "href": reverse_lazy(
                    "gestion:editar-menu", args=[self.get_object().pk]
                ),  # noqa: E501
                "active": True,
            },
        ]
        return data


class MenuDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Menu
    success_url = reverse_lazy("gestion:dashboard")

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
            nombre=self.cleaned_data["nombre"], menu=self.menu
        )


class CategoriaCreateView(LoginRequiredMixin, UpdateView):
    model = models.Menu
    form_class = CategoriaCreateForm
    template_name = "gestion/crear_categoria.html"
    login_url = reverse_lazy("login")

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
        data["breadcrumbs"] = [
            {
                "label": "Panel",
                "href": reverse_lazy("gestion:dashboard"),
                "active": False,
            },
            {
                "label": self.get_object().nombre,
                "href": reverse_lazy(
                    "gestion:editar-menu", args=[self.get_object().pk]
                ),
                "active": False,
            },
            {
                "label": "Crear categoría",
                "href": reverse_lazy(
                    "gestion:crear-categoria", args=[self.get_object().pk]
                ),
                "active": True,
            },
        ]
        return data

    def get_success_url(self):
        return reverse_lazy("gestion:editar-menu", args=[self.get_object().pk])


class CategoriaUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ["nombre"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CategoriaEditView(LoginRequiredMixin, UpdateView):
    model = models.Categoria
    form_class = CategoriaUpdateForm
    template_name = "gestion/editar_categoria.html"
    login_url = reverse_lazy("login")

    def get_queryset(self):
        return models.Categoria.objects.filter(
            menu__usuario=self.request.user
        ).select_related("menu__usuario")

    def get_success_url(self):
        return reverse_lazy("gestion:editar-categoria", args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["breadcrumbs"] = [
            {
                "label": "Panel",
                "href": reverse_lazy("gestion:dashboard"),
                "active": False,
            },
            {
                "label": self.get_object().menu.nombre,
                "href": reverse_lazy(
                    "gestion:editar-menu", args=[self.get_object().menu.pk]
                ),
                "active": False,
            },
            {
                "label": self.get_object().nombre,
                "href": reverse_lazy(
                    "gestion:editar-categoria", args=[self.get_object().pk]
                ),
                "active": True,
            },
        ]
        return data


# Platos
class PlatoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Plato
        fields = ["nombre", "descripcion", "precio"]

    def __init__(self, *args, categoria, **kwargs):
        self.categoria = categoria
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        return models.Plato.objects.create(
            nombre=self.cleaned_data["nombre"],
            descripcion=self.cleaned_data["descripcion"],
            precio=self.cleaned_data["precio"],
            categoria=self.categoria,
        )


class PlatoCreateView(LoginRequiredMixin, UpdateView):
    model = models.Categoria
    form_class = PlatoCreateForm
    template_name = "gestion/crear_plato.html"
    login_url = reverse_lazy("login")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = models.Plato()
        kwargs["categoria"] = self.get_object()
        return kwargs

    def get_queryset(self):
        return models.Categoria.objects.filter(
            menu__usuario=self.request.user
        ).select_related("menu__usuario")

    def get_success_url(self):
        return reverse_lazy("gestion:editar-categoria", args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["breadcrumbs"] = [
            {
                "label": "Panel",
                "href": reverse_lazy("gestion:dashboard"),
                "active": False,
            },
            {
                "label": self.get_object().menu.nombre,
                "href": reverse_lazy(
                    "gestion:editar-menu", args=[self.get_object().pk]
                ),
                "active": False,
            },
            {
                "label": self.get_object().nombre,
                "href": reverse_lazy(
                    "gestion:editar-categoria", args=[self.get_object().pk]
                ),
                "active": False,
            },
            {
                "label": "Crear plato",
                "href": reverse_lazy(
                    "gestion:editar-categoria", args=[self.get_object().pk]
                ),
                "active": False,
            },
        ]
        return data


# QR
class MenuPrintQrView(LoginRequiredMixin, generic.DetailView):
    model = models.Menu
    login_url = reverse_lazy("login")

    def get_queryset(self):
        return models.Menu.objects.filter(usuario=self.request.user)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        img = qrcode.make(
            request.build_absolute_uri(
                reverse_lazy("core:menu-detail", args=[self.object.codigo])
            )
        )  # noqa:501
        image_buffer = BytesIO()
        img.save(image_buffer, format="PNG")

        response = HttpResponse(content_type="image/jpeg")
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{ slugify(self.object.nombre) }.png"'  # noqa:501

        response.write(image_buffer.getvalue())
        return response


# Estado del menú
class PublicarMenuView(
    LoginRequiredMixin, generic.detail.SingleObjectMixin, generic.View
):
    model = models.Menu
    login_url = reverse_lazy("login")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.estado = "publicado"
        self.object.save()
        print(self.object.estado)
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get_queryset(self):
        return models.Menu.objects.filter(usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy("gestion:dashboard")


class OcultarMenuView(
    LoginRequiredMixin, generic.detail.SingleObjectMixin, generic.View
):
    model = models.Menu
    login_url = reverse_lazy("login")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.estado = "oculto"
        self.object.save()
        print(self.object.estado)
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get_queryset(self):
        return models.Menu.objects.filter(usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy("gestion:dashboard")
