# Generated by Django 4.1.4 on 2023-01-04 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestStockMagasin', '0007_alter_fournisseur_codef_alter_typeproduit_codet'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonDeCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QTE', models.IntegerField()),
                ('List_P', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestStockMagasin.produit')),
            ],
        ),
    ]
