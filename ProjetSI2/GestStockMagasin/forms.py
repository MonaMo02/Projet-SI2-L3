from django.db.models import fields   
from django import forms  
from .models import Produit, Fournisseur, Client, TypeProduit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__"



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields ='__all__'


class TypeForm(forms.ModelForm):
    class Meta:
        model = TypeProduit
        fields = "__all__"











