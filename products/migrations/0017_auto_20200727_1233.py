# Generated by Django 3.0.8 on 2020-07-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20200727_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='alt',
            field=models.CharField(blank=True, default='items', max_length=120, null=True, verbose_name='Alt Image Text'),
        ),
    ]
