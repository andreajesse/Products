# Generated by Django 4.0.5 on 2022-07-13 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_producttype_alter_product_insprod_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProdType_Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.producttype', verbose_name='Product Type'),
        ),
    ]
