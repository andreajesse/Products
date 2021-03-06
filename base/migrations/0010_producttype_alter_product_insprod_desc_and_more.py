# Generated by Django 4.0.5 on 2022-07-13 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_product_is_active_alter_product_cat_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdType_Name', models.CharField(max_length=200, verbose_name='Product Type')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='insProd_Desc',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='product',
            name='ProdType_Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.producttype', verbose_name='Category'),
        ),
    ]
