# Generated by Django 4.1.7 on 2023-03-14 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_products', '0023_remove_product_variant_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_sample',
            field=models.TextField(null=True),
        ),
    ]
