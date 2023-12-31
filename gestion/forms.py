from django import forms
from django.conf import settings

from core import models


# Menú section
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


class MenuUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = ["nombre", "descripcion"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["descripcion"].widget = forms.Textarea()


# Categories section
class CategoriaCreateForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ["nombre", "descripcion"]

    def __init__(self, *args, menu, **kwargs):
        self.menu = menu
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        return models.Categoria.objects.create(
            nombre=self.cleaned_data["nombre"],
            descripcion=self.cleaned_data["descripcion"],
            menu=self.menu,
        )


class CategoriaUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ["nombre", "descripcion"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Plates section
class PlatoCreateForm(forms.ModelForm):
    class Meta:
        model = models.Plato
        fields = ["nombre", "descripcion", "precio"]
        widgets = {"precio": forms.NumberInput(attrs={"min": 0})}

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


class PlatoUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Plato
        fields = ["nombre", "descripcion", "precio"]
        widgets = {"precio": forms.NumberInput(attrs={"min": 0})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
