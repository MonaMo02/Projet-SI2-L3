# Generated by Django 4.1.4 on 2023-01-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestStockMagasin', '0008_bondecommande'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bondecommande',
            name='List_P',
        ),
        migrations.AddField(
            model_name='bondecommande',
            name='List_P',
            field=models.ManyToManyField(related_name='BonDeCommande', to='GestStockMagasin.produit'),
        ),
    ]
