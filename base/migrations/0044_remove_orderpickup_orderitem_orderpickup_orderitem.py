# Generated by Django 4.0.5 on 2022-07-24 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0043_remove_order_order_pickup_orderpickup_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderpickup',
            name='orderitem',
        ),
        migrations.AddField(
            model_name='orderpickup',
            name='orderitem',
            field=models.ManyToManyField(to='base.orderitem'),
        ),
    ]