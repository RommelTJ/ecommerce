# Generated by Django 2.0.1 on 2018-03-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20180317_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfile',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
