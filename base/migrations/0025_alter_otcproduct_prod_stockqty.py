# Generated by Django 4.0.5 on 2022-07-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_alter_insproduct_prod_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otcproduct',
            name='Prod_stockQty',
            field=models.FloatField(verbose_name='Stock Quantity'),
        ),
    ]
