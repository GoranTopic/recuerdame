# Generated by Django 3.0.6 on 2020-05-21 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memorials', '0012_auto_20200521_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memorial',
            old_name='image_de_fondo',
            new_name='imagen_de_fondo',
        ),
    ]