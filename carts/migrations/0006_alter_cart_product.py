# Generated by Django 5.0.2 on 2024-03-15 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_delete_mymodel'),
        ('goods', '0006_alter_products_options_alter_products_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.products', verbose_name='Товар'),
        ),
    ]
