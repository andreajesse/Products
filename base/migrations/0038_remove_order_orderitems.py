# Generated by Django 4.0.5 on 2022-07-22 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_order_orderitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderitems',
        ),
    ]
