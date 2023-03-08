# Generated by Django 4.1.7 on 2023-02-21 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_image', models.ImageField(upload_to='advertisements')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_brand.brand')),
            ],
        ),
    ]