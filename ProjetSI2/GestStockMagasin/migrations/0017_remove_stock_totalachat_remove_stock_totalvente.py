# Generated by Django 4.1.4 on 2023-01-22 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestStockMagasin', '0016_remove_stock_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='TotalAchat',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='TotalVente',
        ),
    ]
