from django.conf import settings
from django.db import models


class Restaurante(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Usuario", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    precio = models.DecimalField("Precio", decimal_places=4, max_digits=8)
    descripcion = models.TextField("Descripción")
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
