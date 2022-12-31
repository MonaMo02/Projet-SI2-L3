from django.db import models

# Create your models here.


#Models de la section Tables
class TypeProduit (models.Model):
    CodeT = models.CharField(primary_key=True ,max_length=10)
    DesignationT = models.CharField(max_length=100)
    
class Fournisseur(models.Model):
    CodeF = models.CharField(primary_key=True, max_length=10)
    NomF = models.CharField
    PrenomF = models.CharField
    AdresseF = models.CharField
    TelephoneF = models.CharField

class Produit (models.Model):
    CodeP = models.CharField(primary_key=True, max_length=10)
    DesignationP = models.CharField(max_length=100)
    Type = models.ForeignKey(TypeProduit, on_delete=models.CASCADE)
    Fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)


class Client (models.Model):
    CodeC = models.CharField(primary_key= True, max_length=10)
    NomC = models.CharField
    PrenomC = models.CharField
    AdresseC = models.CharField
    TelephoneC = models.CharField
    Acheter = models.ManyToManyField(Produit, related_name="Client")




    #Models de la section Achat
