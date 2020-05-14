# Generated by Django 3.0.6 on 2020-05-14 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memorials', '0002_auto_20200514_0043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memorial',
            old_name='date_of_death',
            new_name='date_of_passing',
        ),
        migrations.RenameField(
            model_name='memorial',
            old_name='first_names',
            new_name='second_first_name',
        ),
        migrations.RenameField(
            model_name='memorial',
            old_name='last_names',
            new_name='second_last_name',
        ),
        migrations.AddField(
            model_name='memorial',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='memorial',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='memorial',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='memorial',
            name='cover_image',
            field=models.ImageField(blank=True, db_index=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='memorial',
            name='profile_image',
            field=models.ImageField(blank=True, db_index=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Eulogy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(blank=True, max_length=200, null=True)),
                ('anecdote', models.TextField(blank=True, max_length=300, null=True)),
                ('writting', models.TextField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(blank=True, db_index=True, null=True, upload_to='')),
                ('memorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memorials.Memorial')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
