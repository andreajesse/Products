# Generated by Django 4.0.5 on 2022-07-21 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_alter_order_pickup_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PickUp',
            new_name='OrderPickUp',
        ),
    ]
