# Generated by Django 4.0.5 on 2022-07-21 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_rename_pickup_orderpickup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderpickup',
            old_name='pickup',
            new_name='pickup_date',
        ),
    ]
