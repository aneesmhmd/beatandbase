# Generated by Django 4.1.7 on 2023-02-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_home', '0010_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='users'),
        ),
    ]
