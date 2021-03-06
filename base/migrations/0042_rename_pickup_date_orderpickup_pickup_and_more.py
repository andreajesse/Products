# Generated by Django 4.0.5 on 2022-07-22 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0041_rename_pickup_orderpickup_pickup_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderpickup',
            old_name='pickup_date',
            new_name='pickup',
        ),
        migrations.AddField(
            model_name='order',
            name='order_pickup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pickup_date', to='base.orderpickup'),
        ),
    ]
