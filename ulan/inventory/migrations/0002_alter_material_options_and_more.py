# Generated by Django 4.2.6 on 2023-12-07 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Материалы'},
        ),
        migrations.AlterModelOptions(
            name='materialtransaction',
            options={'verbose_name': 'Транзакция материалов'},
        ),
    ]