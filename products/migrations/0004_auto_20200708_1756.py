# Generated by Django 3.0.8 on 2020-07-08 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200707_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagepath',
            field=models.FileField(blank=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]