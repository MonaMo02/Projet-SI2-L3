# Generated by Django 4.1.4 on 2023-01-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestStockMagasin', '0022_alter_ventecomptoir_codevente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventecomptoir',
            name='CodeVente',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
