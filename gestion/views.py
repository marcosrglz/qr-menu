from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from core import models


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
            usuario=self.user
        )


class MenuCreateView(LoginRequiredMixin, FormView):
    form_class = MenuCreateForm
    template_name = "gestion/crear_menu.html"
    success_url = "/"
    login_url = "cuentas/login"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
