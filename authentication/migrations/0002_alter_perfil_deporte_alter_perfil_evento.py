# Generated by Django 4.2.4 on 2023-10-09 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("AppClub", "0001_initial"),
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perfil",
            name="deporte",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="AppClub.deporte",
            ),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="evento",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="AppClub.evento",
            ),
        ),
    ]
