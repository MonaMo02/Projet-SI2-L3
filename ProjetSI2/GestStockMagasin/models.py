from django.db import models
from datetime import datetime

# Create your models here

#Models de la section Tables
class TypeProduit (models.Model):
    CodeT = models.AutoField(primary_key=True)
    DesignationT = models.CharField(max_length=100)
    def __str__(self):         
        return str(self.DesignationT)

    
class Fournisseur(models.Model):
    CodeF = models.AutoField(primary_key=True)
    NomF = models.CharField(max_length=100,default="...")
    PrenomF = models.CharField(max_length=100,default="...")
    AdresseF = models.CharField(max_length=100,default="...")
    TelephoneF = models.CharField(max_length=100,default="...")
    def __str__(self):         
        return str(self.NomF)


class Produit (models.Model):
    CodeP = models.AutoField(primary_key=True)
    DesignationP = models.CharField(max_length=100)
    Type = models.ForeignKey(TypeProduit, on_delete=models.CASCADE)
    def __str__(self):         
        return str(self.DesignationP)


class Client (models.Model):
    CodeC = models.AutoField(primary_key= True)
    NomC = models.CharField(max_length=100,default="...")
    PrenomC = models.CharField(max_length=100,default="...")
    AdresseC = models.CharField(max_length=100,default="...")
    TelephoneC = models.CharField(max_length=100,default="...")
    def __str__(self):         
        return str(self.NomC)



    #Models de la section Achat
