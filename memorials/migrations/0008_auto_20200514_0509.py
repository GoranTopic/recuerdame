# Generated by Django 3.0.6 on 2020-05-14 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memorials', '0007_auto_20200514_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eulogy',
            name='memorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eulogy', to='memorials.Memorial'),
        ),
    ]
