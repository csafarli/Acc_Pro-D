# Generated by Django 3.2.5 on 2021-12-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(default='1604', max_length=4, unique=True),
        ),
    ]