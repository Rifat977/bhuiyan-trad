# Generated by Django 3.2.16 on 2022-11-08 09:56

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_rename_stork_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featureimage',
            field=models.ImageField(upload_to=backend.models.product_path),
        ),
    ]
