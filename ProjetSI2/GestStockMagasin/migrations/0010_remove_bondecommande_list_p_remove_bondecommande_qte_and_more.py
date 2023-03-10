# Generated by Django 4.1.4 on 2023-01-04 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestStockMagasin', '0009_remove_bondecommande_list_p_bondecommande_list_p'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bondecommande',
            name='List_P',
        ),
        migrations.RemoveField(
            model_name='bondecommande',
            name='QTE',
        ),
        migrations.CreateModel(
            name='UneCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QTE', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestStockMagasin.produit')),
            ],
        ),
        migrations.AddField(
            model_name='bondecommande',
            name='List_Commande',
            field=models.ManyToManyField(related_name='BonDeCommande', to='GestStockMagasin.unecommande'),
        ),
    ]
