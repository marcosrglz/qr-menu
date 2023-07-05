from django.conf import settings
from django.db import models


class Restaurante(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name="Usuario", 
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nombre