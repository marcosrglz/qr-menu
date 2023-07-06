from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Restaurante, Menu


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
            nombre="Corralito",
            usuario=usuario1
        )

        menu, _ = Menu.objects.get_or_create(
            nombre="Menú de Verano",
            restaurante=corralito
        )
        
        print("Sampledata Ejecutado")
