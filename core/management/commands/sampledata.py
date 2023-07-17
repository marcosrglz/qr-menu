from decimal import Decimal as D

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from core.models import Menu, Categoria, Plato


class Command(BaseCommand):
    help = "Crea unos datos de ejemplo de la base de datos"

    def handle(self, *args, **options):
        superuser, superuser_created = User.objects.get_or_create(username="admin")

        if superuser_created:
            superuser.is_superuser = True
            superuser.is_staff = True
            superuser.email = "admin@admin.text"
            superuser.set_password("adminadmin")
            superuser.save()

        usuarioManduca, usuarioManduca_created = User.objects.get_or_create(
            username="Manduca"
        )

        if usuarioManduca_created:
            usuarioManduca.is_superuser = False
            usuarioManduca.is_staff = False
            usuarioManduca.email = "anduca@manduca.text"
            usuarioManduca.set_password("Manduca123")
            usuarioManduca.save()

        menuManduca, _ = Menu.objects.get_or_create(
            nombre="Carta Manduca",
            descripcion="Menú de Verano Manduca",
            usuario=usuarioManduca,
        )

        categoriaManduca, _ = Categoria.objects.get_or_create(
            nombre="Bocadillos Calientes",
            menu=menuManduca
        )

        plato1Manduca, _ = Plato.objects.get_or_create(
            nombre="Perrito Bahíña",
            precio=D("6.99"),
            descripcion="Frankfurt 200gr, Champiñones, Cebolla Caramelizada, Queso Edam",  # noqa:E501
            categoria=categoriaManduca
        )

        plato2Manduca, _ = Plato.objects.get_or_create(
            nombre="Bocadillo Suculento",
            precio=D("7.50"),
            descripcion="Pechuga de pollo, Lomo adobado, Queso Edam, Salsa Alioli",  # noqa:E501
            categoria=categoriaManduca
        )

        print("Sampledata Ejecutado")
