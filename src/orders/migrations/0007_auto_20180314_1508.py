# Generated by Django 2.0.2 on 2018-03-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_productpurchase_productpurchasemanager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpurchase',
            name='user',
        ),
        migrations.AddField(
            model_name='productpurchase',
            name='order_id',
            field=models.CharField(default='abc123', max_length=120),
            preserve_default=False,
        ),
    ]