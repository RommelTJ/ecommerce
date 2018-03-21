# Generated by Django 2.0.2 on 2018-03-19 15:27

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_productfile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/Users/rommel/Documents/github/play/python/ecommerce/static_cdn/protected_media'), upload_to=products.models.upload_product_file_loc),
        ),
    ]