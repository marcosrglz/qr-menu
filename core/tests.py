from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from core import models


class MenuDetailViewTests(TestCase):
    def test_menu_detail(self):
        """
        Comprueba si la vista de menu-detail se renderiza
        """
        call_command("sampledata")
        menu = models.Menu.objects.get(nombre="Carta Manduca")
        url = reverse("core:menu-detail", args=(menu.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
