# Generated by Django 3.0.6 on 2020-05-18 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('memorials', '0009_auto_20200518_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorial',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.CustomUser'),
        ),
    ]
