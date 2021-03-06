# Generated by Django 4.0.5 on 2022-07-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_alter_order_pickup_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pickup_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled'), ('Transaction Successful', 'Transaction Successful'), ('Confirmed', 'Confirmed')], default='Pending', max_length=50),
        ),
    ]
