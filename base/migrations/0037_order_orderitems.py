# Generated by Django 4.0.5 on 2022-07-22 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_rename_pickup_date_orderpickup_pickup'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderitems',
            field=models.ManyToManyField(related_name='orders', to='base.orderitem'),
        ),
    ]