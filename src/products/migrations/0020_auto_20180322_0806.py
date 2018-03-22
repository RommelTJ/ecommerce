# Generated by Django 2.0.2 on 2018-03-22 15:06

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20180321_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/Users/rommel/Documents/github/play/python/ecommerce/static_cdn/protected_media'), upload_to=products.models.upload_product_file_loc),
        ),
    ]
