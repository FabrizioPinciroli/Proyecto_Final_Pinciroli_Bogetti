# Generated by Django 4.2.4 on 2023-10-14 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("AppClub", "0012_alter_comentario_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comentario",
            old_name="contenido",
            new_name="comentario",
        ),
    ]
