# Generated by Django 3.0.8 on 2020-07-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200720_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagepath',
            field=models.ImageField(default='', null=True, upload_to='media/documents/images', verbose_name='Image'),
        ),
    ]
