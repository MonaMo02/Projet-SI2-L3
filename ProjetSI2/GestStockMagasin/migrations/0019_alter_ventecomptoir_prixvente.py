# Generated by Django 4.1.4 on 2023-01-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestStockMagasin', '0018_ventecomptoir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventecomptoir',
            name='PrixVente',
            field=models.FloatField(default=0),
        ),
    ]