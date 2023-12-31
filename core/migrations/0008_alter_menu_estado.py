# Generated by Django 4.2.3 on 2023-08-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_menu_estado"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="estado",
            field=models.CharField(
                choices=[("publicado", "Publicado"), ("oculto", "Oculto")],
                default="oculto",
                max_length=100,
                verbose_name="Estado",
            ),
        ),
    ]
