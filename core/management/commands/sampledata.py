from decimal import Decimal as D

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from core.models import Menu, Plato, Restaurante


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

        usuario1, usuario1_created = User.objects.get_or_create(username="user1")

        if usuario1_created:
            usuario1.is_superuser = False
            usuario1.is_staff = False
            usuario1.email = "usuario1@fake.text"
            usuario1.set_password("usuario1")
            usuario1.save()

        corralito, _ = Restaurante.objects.get_or_create(
            nombre="Corralito", usuario=usuario1
        )

        menuVeranoCorralito, _ = Menu.objects.get_or_create(
            nombre="Menú de Verano Corralito", restaurante=corralito
        )

        plato1Corralito, _ = Plato.objects.get_or_create(
            nombre="Pasta Ardiente",
            precio=D("10.99"),
            descripcion="Pasta integral, Pollo Empanado, Tomate Natural, Queso fundido y Salchicha",  # noqa:E501
            menu=menuVeranoCorralito,
        )

        plato2Corralito, _ = Plato.objects.get_or_create(
            nombre="Miriam",
            precio=D("12.99"),
            descripcion="Cordon Bleu relleno de Queso gouda, Tomate Fresco con una capa de Pisto por encima",  # noqa:E501
            menu=menuVeranoCorralito,
        )

        plato3Corralito, _ = Plato.objects.get_or_create(
            nombre="Lasagna Boloñesa",
            precio=D("9.99"),
            descripcion="Lasagna rellena de boloñesa",
            menu=menuVeranoCorralito,
        )

        usuarioEnrique, usuarioEnrique_created = User.objects.get_or_create(
            username="Enrique Túnel"
        )

        if usuarioEnrique_created:
            usuarioEnrique.is_superuser = False
            usuarioEnrique.is_staff = False
            usuarioEnrique.email = "Enrique@Tunel.text"
            usuarioEnrique.set_password("EnriqueEnrique")
            usuarioEnrique.save()

        elTunel, _ = Restaurante.objects.get_or_create(
            nombre="El Túnel", usuario=usuarioEnrique
        )

        menuVeranoTunel, _ = Menu.objects.get_or_create(
            nombre="Menú de Verano Túnel", restaurante=elTunel
        )

        plato1Tunel, _ = Plato.objects.get_or_create(
            nombre="Cigalas 200gr",
            precio=D("69.00"),
            descripcion="",
            menu=menuVeranoTunel,
        )

        plato2Tunel, _ = Plato.objects.get_or_create(
            nombre="Paella de Mariscos 2p",
            precio=D("48.00"),
            descripcion="Paella de Mariscos (Bogavante, Cigalas, Langostinos, Zamburiñas, Mejillones) mínimo para 2 personas",  # noqa:E501
            menu=menuVeranoTunel,
        )

        usuarioManduca, usuarioManduca_created = User.objects.get_or_create(
            username="Manduca"
        )

        if usuarioManduca_created:
            usuarioManduca.is_superuser = False
            usuarioManduca.is_staff = False
            usuarioManduca.email = "Enrique@Tunel.text"
            usuarioManduca.set_password("EnriqueEnrique")
            usuarioManduca.save()

        manduca, _ = Restaurante.objects.get_or_create(
            nombre="manduca", usuario=usuarioManduca
        )

        menuManduca, _ = Menu.objects.get_or_create(
            nombre="Carta Manduca", restaurante=manduca
        )

        plato1Manduca, _ = Plato.objects.get_or_create(
            nombre="Perrito Bahíña",
            precio=D("6.99"),
            descripcion="Frankfurt 200gr, Champiñones, Cebolla Caramelizada, Queso Edam",  # noqa:E501
            menu=menuManduca,
        )

        plato2Manduca, _ = Plato.objects.get_or_create(
            nombre="Bocadillo Suculento",
            precio=D("7.50"),
            descripcion="Pechuga de pollo, Lomo adobado, Queso Edam, Salsa Alioli",  # noqa:E501
            menu=menuManduca,
        )

        print("Sampledata Ejecutado")
