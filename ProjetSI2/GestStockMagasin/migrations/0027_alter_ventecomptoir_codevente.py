# Generated by Django 4.1.4 on 2023-01-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestStockMagasin', '0026_alter_ventecomptoir_codevente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventecomptoir',
            name='CodeVente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
