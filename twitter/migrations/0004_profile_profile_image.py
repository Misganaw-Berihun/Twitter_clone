# Generated by Django 4.1.4 on 2023-02-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_meep'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(
                blank=True, null=True, upload_to='images/'),
        ),
    ]
