# Generated by Django 4.0.5 on 2022-07-19 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_insproduct_expiry_date_otcproduct_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pickupstat',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled'), ('Transaction Successful', 'Transaction Successful'), ('Confirmed', 'Confirmed')], default='Pending', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PickupStatus',
        ),
    ]
