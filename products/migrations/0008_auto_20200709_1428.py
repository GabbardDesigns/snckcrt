# Generated by Django 3.0.8 on 2020-07-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200709_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagepath',
            field=models.ImageField(default='', null=True, upload_to='documents/images'),
        ),
    ]
