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
from gestion import forms as gestion_forms
from gestion import mixins


# Dashboard del usuario
class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "gestion/dashboard.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["menus"] = models.Menu.objects.filter(usuario=self.request.user).annotate(
            plato_count=Count("categoria__plato"),
            acceso_count=Count("acceso", distinct=True),
        )
        data["breadcrumbs"] = [
            {
                "label": "Panel",
                "href": reverse_lazy("gestion:dashboard"),
                "active": True,
            }
        ]
        return data


# Menus section
class MenuCreateView(mixins.MessageMixin, LoginRequiredMixin, CreateView):
    form_class = gestion_forms.MenuCreateForm
    template_name = "gestion/crear_menu.html"
    success_url = reverse_lazy("gestion:dashboard")
    login_url = reverse_lazy("login")
    msg_desc = "Menú creado con éxito"

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


class MenuEditView(mixins.MessageMixin, LoginRequiredMixin, UpdateView):
    model = models.Menu
    form_class = gestion_forms.MenuUpdateForm
    template_name = "gestion/editar_menu.html"
    login_url = reverse_lazy("login")
    msg_desc = "Menú editado con éxito"

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


class MenuDeleteView(mixins.MessageMixin, LoginRequiredMixin, DeleteView):
    model = models.Menu
    success_url = reverse_lazy("gestion:dashboard")
    msg_desc = "Menú eliminado con éxito"

    def get_queryset(self):
        return models.Menu.objects.filter(usuario=self.request.user)


# Categories section
class CategoriaCreateView(mixins.MessageMixin, LoginRequiredMixin, UpdateView):
    model = models.Menu
    form_class = gestion_forms.CategoriaCreateForm
    template_name = "gestion/crear_categoria.html"
    login_url = reverse_lazy("login")
    msg_desc = "Categoría creada con éxito"

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


class CategoriaEditView(mixins.MessageMixin, LoginRequiredMixin, UpdateView):
    model = models.Categoria
    form_class = gestion_forms.CategoriaUpdateForm
    template_name = "gestion/editar_categoria.html"
    login_url = reverse_lazy("login")
    msg_desc = "Categoría editada con éxito"

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


class CategoriaDeleteView(mixins.MessageMixin, LoginRequiredMixin, DeleteView):
    model = models.Categoria
    msg_desc = "Categoría eliminada con éxito"

    def get_queryset(self):
        return models.Categoria.objects.filter(menu__usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy("gestion:editar-menu", args=[self.object.menu.pk])


# Plates section


class PlatoCreateView(mixins.MessageMixin, LoginRequiredMixin, UpdateView):
    model = models.Categoria
    form_class = gestion_forms.PlatoCreateForm
    template_name = "gestion/crear_plato.html"
    login_url = reverse_lazy("login")
    msg_desc = "Plato creado con éxito"

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


class PlatoEditView(mixins.MessageMixin, LoginRequiredMixin, UpdateView):
    model = models.Plato
    form_class = gestion_forms.PlatoUpdateForm
    template_name = "gestion/editar_plato.html"
    login_url = reverse_lazy("login")
    msg_desc = "Plato editado con éxito"

    def get_queryset(self):
        return models.Plato.objects.filter(
            categoria__menu__usuario=self.request.user
        ).select_related("categoria__menu__usuario")

    def get_success_url(self):
        return reverse_lazy("gestion:editar-categoria", args=[self.object.categoria.pk])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["breadcrumbs"] = [
            {
                "label": "Panel",
                "href": reverse_lazy("gestion:dashboard"),
                "active": False,
            },
            {
                "label": self.get_object().categoria.menu.nombre,
                "href": reverse_lazy(
                    "gestion:editar-menu", args=[self.get_object().categoria.menu.pk]
                ),
                "active": False,
            },
            {
                "label": self.get_object().categoria.nombre,
                "href": reverse_lazy(
                    "gestion:editar-categoria", args=[self.get_object().categoria.pk]
                ),
                "active": False,
            },
            {
                "label": self.get_object().nombre,
                "href": reverse_lazy(
                    "gestion:editar-plato", args=[self.get_object().pk]
                ),
                "active": True,
            },
        ]
        return data


class PlatoDeleteView(mixins.MessageMixin, LoginRequiredMixin, DeleteView):
    model = models.Plato
    msg_desc = "Plato eliminado con éxito"

    def get_queryset(self):
        return models.Plato.objects.filter(categoria__menu__usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy("gestion:editar-categoria", args=[self.object.categoria.pk])


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


# Menus states
class PublicarMenuView(
    mixins.MessageMixin,
    LoginRequiredMixin,
    generic.detail.SingleObjectMixin,
    generic.View,
):
    model = models.Menu
    login_url = reverse_lazy("login")
    msg_desc = "Menú publicado con éxito"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.estado = "publicado"
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get_queryset(self):
        return models.Menu.objects.filter(usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy("gestion:dashboard")


class OcultarMenuView(
    mixins.MessageMixin,
    LoginRequiredMixin,
    generic.detail.SingleObjectMixin,
    generic.View,
):
    model = models.Menu
    login_url = reverse_lazy("login")
    msg_desc = "Menú ocultado con éxito"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.estado = "oculto"
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get_queryset(self):
        return models.Menu.objects.filter(usuario=self.request.user)

    def get_success_url(self):
        return reverse_lazy("gestion:editar-menu")


# Categories States
class PublicarCategoriaView(
    mixins.MessageMixin,
    LoginRequiredMixin,
    generic.detail.SingleObjectMixin,
    generic.View,
):
    model = models.Categoria
    login_url = reverse_lazy("login")
    msg_desc = "Categoría publicada con éxito"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.estado = "publicada"
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get_queryset(self):
        return models.Categoria.objects.filter()

    def get_success_url(self):
        return reverse_lazy("gestion:editar-menu", args=[self.object.menu_id])


class OcultarCategoriaView(
    mixins.MessageMixin,
    LoginRequiredMixin,
    generic.detail.SingleObjectMixin,
    generic.View,
):
    model = models.Categoria
    login_url = reverse_lazy("login")
    msg_desc = "Categoría ocultada con éxito"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.estado = "oculta"
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

    def get_queryset(self):
        return models.Categoria.objects.all()

    def get_success_url(self):
        return reverse_lazy("gestion:editar-menu", args=[self.object.menu_id])
