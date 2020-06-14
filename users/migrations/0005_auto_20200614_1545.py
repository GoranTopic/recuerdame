# Generated by Django 3.0.6 on 2020-06-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200614_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='imagen_image',
            new_name='profile_image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
