# Generated by Django 4.2.3 on 2023-07-17 10:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_menu_usuario_categoria_plato_categoria"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="plato",
            name="menu",
        ),
    ]
