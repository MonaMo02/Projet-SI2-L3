from django.db import models
from datetime import datetime

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


class Client (models.Model):
    CodeC = models.CharField(primary_key= True, max_length=10)
    NomC = models.CharField
    PrenomC = models.CharField
    AdresseC = models.CharField
    TelephoneC = models.CharField
    def __str__(self):         
        return str(self.CodeC,self.NomC,self.PrenomC,self.AdresseC,self.TelephoneC) 



class Commande(models.Model):     
    Description_cmd = models.CharField(max_length=50)     
    Date_cmd = models.DateTimeField(default=datetime.now)     
    Produit_cmd = models.ForeignKey(Produit, on_delete=models.CASCADE)    
    
    def __str__(self):         
        return str(self.Description_cmd)
    


    #Models de la section Achat