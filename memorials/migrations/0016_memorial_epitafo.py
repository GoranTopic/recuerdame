# Generated by Django 3.0.6 on 2020-05-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorials', '0015_auto_20200528_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='memorial',
            name='epitafo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
