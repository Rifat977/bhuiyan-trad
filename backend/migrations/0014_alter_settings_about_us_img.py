# Generated by Django 3.2.16 on 2022-11-09 13:28

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20221109_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='about_us_img',
            field=models.ImageField(upload_to=backend.models.settings_path),
        ),
    ]
