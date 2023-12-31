# Generated by Django 4.2.3 on 2023-07-17 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="usuario",
            ),
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "creado",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha creada"
                    ),
                ),
                (
                    "modificado",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha modificada"
                    ),
                ),
                ("nombre", models.CharField(max_length=50, verbose_name="Nombre")),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.menu"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="plato",
            name="categoria",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.categoria",
            ),
            preserve_default=False,
        ),
    ]
