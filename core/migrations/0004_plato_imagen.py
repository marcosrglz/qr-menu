# Generated by Django 4.2.3 on 2023-07-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_remove_plato_menu"),
    ]

    operations = [
        migrations.AddField(
            model_name="plato",
            name="imagen",
            field=models.ImageField(null=True, upload_to="", verbose_name="Imagen"),
        ),
    ]
