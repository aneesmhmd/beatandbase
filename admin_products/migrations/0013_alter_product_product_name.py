# Generated by Django 4.1.7 on 2023-02-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_products', '0012_alter_product_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
