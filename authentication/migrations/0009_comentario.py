# Generated by Django 4.2.4 on 2023-10-14 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("AppClub", "0010_alter_noticia_desarrollo"),
        ("authentication", "0008_alter_perfil_options_alter_perfil_fecha_nacimiento"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comentario",
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
                ("texto", models.TextField()),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "noticia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="AppClub.noticia",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]