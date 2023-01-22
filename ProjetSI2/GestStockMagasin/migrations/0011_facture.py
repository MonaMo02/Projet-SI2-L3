# Generated by Django 4.1.4 on 2023-01-05 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestStockMagasin', '0010_remove_bondecommande_list_p_remove_bondecommande_qte_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('Code_Fac', models.IntegerField(primary_key=True, serialize=False)),
                ('Date_creation', models.DateTimeField(auto_now=True)),
                ('Fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestStockMagasin.fournisseur')),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestStockMagasin.unecommande')),
            ],
        ),
    ]
