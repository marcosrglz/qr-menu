from django.conf import settings
from django import forms

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
            usuario=self.user,
        )

    def clean(self):
        cleaned_data = super().clean()
        menus = models.Menu.objects.filter(usuario=self.user).count()

        if menus >= settings.MAX_MENUS and not self.user.is_superuser:
            raise forms.ValidationError("Has alcanzado el límite de menús")

        return cleaned_data
