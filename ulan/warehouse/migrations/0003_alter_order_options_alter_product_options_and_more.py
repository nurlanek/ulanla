# Generated by Django 4.2.6 on 2023-12-18 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_alter_order_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Заказ'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Продукция'},
        ),
        migrations.AlterModelTable(
            name='product',
            table=None,
        ),
    ]