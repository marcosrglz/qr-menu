from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    creado = models.DateTimeField("Fecha creada", auto_now_add=True)
    modificado = models.DateTimeField("Fecha modificada", auto_now=True)

    class Meta:
        abstract = True


class Restaurante(BaseModel):
    nombre = models.CharField("Nombre", max_length=50)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="Usuario", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nombre


class Menu(BaseModel):
    nombre = models.CharField("Nombre", max_length=50)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Plato(BaseModel):
    nombre = models.CharField("Nombre", max_length=100)
    precio = models.DecimalField("Precio", decimal_places=4, max_digits=8)
    descripcion = models.TextField("Descripción")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
