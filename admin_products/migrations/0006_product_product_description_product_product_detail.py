# Generated by Django 4.1.7 on 2023-02-24 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_products', '0005_alter_product_brand_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_detail',
            field=models.TextField(blank=True),
        ),
    ]