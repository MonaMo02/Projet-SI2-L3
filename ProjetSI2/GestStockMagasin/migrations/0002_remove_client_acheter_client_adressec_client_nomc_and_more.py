# Generated by Django 4.1.4 on 2023-01-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestStockMagasin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='Acheter',
        ),
        migrations.AddField(
            model_name='client',
            name='AdresseC',
            field=models.CharField(default='...', max_length=100),
        ),
        migrations.AddField(
            model_name='client',
            name='NomC',
            field=models.CharField(default='...', max_length=100),
        ),
        migrations.AddField(
            model_name='client',
            name='PrenomC',
            field=models.CharField(default='...', max_length=100),
        ),
        migrations.AddField(
            model_name='client',
            name='TelephoneC',
            field=models.CharField(default='...', max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='CodeC',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Commande',
        ),
    ]
