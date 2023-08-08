from uuid import uuid4

from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    creado = models.DateTimeField("Fecha creada", auto_now_add=True)
    modificado = models.DateTimeField("Fecha modificada", auto_now=True)

    class Meta:
        abstract = True


class Menu(BaseModel):
    codigo = models.UUIDField("Codigo", default=uuid4, null=False)
    nombre = models.CharField("Nombre", max_length=50)
    descripcion = models.TextField("Descripción")
    estado = models.CharField(
        "Estado",
        max_length=100,
        default="oculto",
        choices=[("publicado", "Publicado"), ("oculto", "Oculto")],
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="usuario", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nombre


class Categoria(BaseModel):
    nombre = models.CharField("Nombre", max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Plato(BaseModel):
    nombre = models.CharField("Nombre", max_length=100)
    precio = models.DecimalField("Precio", decimal_places=4, max_digits=8)
    descripcion = models.TextField("Descripción")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField("Imagen", null=True)

    def __str__(self):
        return self.nombre


# Analytics
class Acceso(BaseModel):
    user_agent = models.CharField("User Agent", max_length=200)
    ip = models.CharField("IP", max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.creado
