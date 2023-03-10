# Generated by Django 4.1.4 on 2022-12-31 16:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('CodeF', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeProduit',
            fields=[
                ('CodeT', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('DesignationT', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('CodeP', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('DesignationP', models.CharField(max_length=100)),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestStockMagasin.typeproduit')),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description_cmd', models.CharField(max_length=50)),
                ('Date_cmd', models.DateTimeField(default=datetime.datetime.now)),
                ('Produit_cmd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestStockMagasin.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('CodeC', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Acheter', models.ManyToManyField(related_name='Client', to='GestStockMagasin.produit')),
            ],
        ),
    ]
