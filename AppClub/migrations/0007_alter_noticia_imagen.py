# Generated by Django 4.2.4 on 2023-10-11 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AppClub", "0006_merge_20231010_2311"),
    ]

    operations = [
        migrations.AlterField(
            model_name="noticia",
            name="imagen",
            field=models.ImageField(blank=True, null=True, upload_to="noticias"),
        ),
    ]
