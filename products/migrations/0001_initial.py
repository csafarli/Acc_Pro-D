# Generated by Django 3.2.5 on 2021-11-30 12:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0003_auto_20211130_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_code', models.CharField(default='4487', max_length=4, unique=True)),
                ('product_model', models.CharField(max_length=100)),
                ('product_description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supplier_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(choices=[('kg', 'Kilogram'), ('l', 'Liter'), ('pcs', 'Pieces')], max_length=10)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]