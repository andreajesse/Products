# Generated by Django 4.0.5 on 2022-07-20 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_alter_order_pickupstat_delete_pickupstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='pickupstat',
            new_name='pickup_status',
        ),
    ]