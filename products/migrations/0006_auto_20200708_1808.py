# Generated by Django 3.0.8 on 2020-07-08 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200708_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagepath',
            field=models.ImageField(upload_to='documents/%Y/%m/%d'),
        ),
    ]