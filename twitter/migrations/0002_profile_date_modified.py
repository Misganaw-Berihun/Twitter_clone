# Generated by Django 4.1.4 on 2023-01-04 17:54

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(
                auto_now=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
