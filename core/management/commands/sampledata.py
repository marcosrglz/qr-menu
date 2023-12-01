from decimal import Decimal as D

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from core.models import Categoria, Menu, Plato


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

        usuarioDemo, usuarioDemo_created = User.objects.get_or_create(
            username="Demo"
        )

        if usuarioDemo_created:
            usuarioDemo.is_superuser = False
            usuarioDemo.is_staff = False
            usuarioDemo.email = "demo@gmail.com"
            usuarioDemo.set_password("Demo123")
            usuarioDemo.save()

        menuDemo, _ = Menu.objects.get_or_create(
            nombre="Carta Demo",
            descripcion="Menú de Verano Demo",
            usuario=usuarioDemo,
        )

        categoriaDemo, _ = Categoria.objects.get_or_create(
            nombre="Bocadillos Calientes", menu=menuDemo
        )

        categoriaDemo2, _ = Categoria.objects.get_or_create(
            nombre="Bocadillos Fríos", menu=menuDemo
        )

        categoriaDemo3, _ = Categoria.objects.get_or_create(
            nombre="Hamburguesas", menu=menuDemo
        )

        plato1Demo, _ = Plato.objects.get_or_create(
            nombre="Perrito Bahíña",
            precio=D("6.99"),
            descripcion="Frankfurt 200gr, Champiñones, Cebolla Caramelizada, Queso Edam",  # noqa:E501
            categoria=categoriaDemo,
        )

        plato2Demo, _ = Plato.objects.get_or_create(
            nombre="Bocadillo Suculento",
            precio=D("7.50"),
            descripcion="Pechuga de pollo, Lomo adobado, Queso Edam, Salsa Alioli",  # noqa:E501
            categoria=categoriaDemo,
        )

        plato3Demo, _ = Plato.objects.get_or_create(
            nombre="Bocadillo de Tortilla",
            precio=D("7.50"),
            descripcion="Tortilla Española, Queso Edam",  # noqa:E501
            categoria=categoriaDemo2,
        )

        plato4Demo, _ = Plato.objects.get_or_create(
            nombre="Hamburguesa Completa",
            precio=D("4.50"),
            descripcion="200gr Ternera, Queso, Lechuga, Tomate, Cebolla",  # noqa:E501
            categoria=categoriaDemo3,
        )

        plato5Demo, _ = Plato.objects.get_or_create(
            nombre="Bocadillo Suculento 2",
            precio=D("7.50"),
            descripcion="Pechuga de pollo, Lomo adobado, Queso Edam, Salsa Alioli",  # noqa:E501
            categoria=categoriaDemo,
        )

        plato6Demo, _ = Plato.objects.get_or_create(
            nombre="Bocadillo Suculento 3",
            precio=D("7.50"),
            descripcion="Pechuga de pollo, Lomo adobado, Queso Edam, Salsa Alioli",  # noqa:E501
            categoria=categoriaDemo,
        )

        plato7Demo, _ = Plato.objects.get_or_create(
            nombre="Bocadillo Suculento 4",
            precio=D("7.50"),
            descripcion="Pechuga de pollo, Lomo adobado, Queso Edam, Salsa Alioli",  # noqa:E501
            categoria=categoriaDemo,
        )

        plato8Demo, _ = Plato.objects.get_or_create(
            nombre="Bocadillo Suculento 5",
            precio=D("7.50"),
            descripcion="Pechuga de pollo, Lomo adobado, Queso Edam, Salsa Alioli",  # noqa:E501
            categoria=categoriaDemo,
        )

        plato9Demo, _ = Plato.objects.get_or_create(
            nombre="Bocadillo Suculento 6",
            precio=D("7.50"),
            descripcion="Pechuga de pollo, Lomo adobado, Queso Edam, Salsa Alioli",  # noqa:E501
            categoria=categoriaDemo,
        )

        plato10Demo, _ = Plato.objects.get_or_create(
            nombre="Bocadillo Suculento 7",
            precio=D("7.50"),
            descripcion="Pechuga de pollo, Lomo adobado, Queso Edam, Salsa Alioli",  # noqa:E501
            categoria=categoriaDemo,
        )

        print("Sampledata Ejecutado")
