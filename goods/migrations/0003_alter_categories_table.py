# Generated by Django 5.0.2 on 2024-02-27 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categories',
            table='goods_category',
        ),
    ]