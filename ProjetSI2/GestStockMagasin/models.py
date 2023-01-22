from django.db import models

# Create your models here

#Models de la section Tables
class TypeProduit (models.Model):
    CodeT = models.AutoField(primary_key=True)
    DesignationT = models.CharField(max_length=100)
    def __str__(self):         
        return str(self.DesignationT)

    
class Fournisseur(models.Model):
    CodeF = models.AutoField(primary_key=True)
    NomF = models.CharField(max_length=100,default="")
    PrenomF = models.CharField(max_length=100,default="")
    AdresseF = models.CharField(max_length=100,default="")
    TelephoneF = models.CharField(max_length=100,default="")
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
    NomC = models.CharField(max_length=100,default="")
    PrenomC = models.CharField(max_length=100,default="")
    AdresseC = models.CharField(max_length=100,default="")
    TelephoneC = models.CharField(max_length=100,default="")
    def __str__(self):         
        return str(self.NomC)



class Stock (models.Model):
    CodeS = models.AutoField(primary_key= True)
    Produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    Type = models.ForeignKey(TypeProduit, on_delete=models.CASCADE)
    qte = models.IntegerField(default=0)
    PrixHT = models.IntegerField(default=0)
    PrixVente = models.IntegerField(default=0)
    def __str__(self):         
        return str(self.PrixVente)
    @property
    def TotalAchat(self):
        TotalAchat = 0 
        if self.qte != 0:
            TotalAchat = (self.PrixHT * self.qte)
        return TotalAchat
    @property
    def TotalVente(self):
        TotalVente = 0
        if self.qte != 0:
            TotalVente = self.PrixVente * self.qte
        return TotalVente



#vente 

class VenteComptoir(models.Model):
    CodeVente = models.IntegerField(default=0, primary_key=True)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    Qte = models.IntegerField(default=0)
    PrixVente = models.FloatField(default= 0)
    MontantPaye = models.FloatField(default=0)
    @property
    def Montant(self):
        Montant = 0
        if self.Qte != 0 :
            Montant = self.Qte * self.PrixVente
            return Montant
    @property
    def Credit(self):
        Credit = 0
        Montant = (self.Qte * self.PrixVente)
        if self.MontantPaye < Montant :
            Credit = Montant - self.MontantPaye
            return Credit

