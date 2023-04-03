# Generated by Django 3.2.16 on 2023-03-31 10:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20230331_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='item',
            name='rear_image',
            field=cloudinary.models.CloudinaryField(default='no-image', max_length=255, verbose_name='image'),
        ),
    ]
