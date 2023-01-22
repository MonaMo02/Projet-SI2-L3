from django.db.models import fields   
from django import forms  
from .models import Produit, VenteComptoir, Fournisseur,Stock, Client, TypeProduit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


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



class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Produit', 'Type', 'qte', 'PrixHT', 'PrixVente']


class VentCForm(forms.ModelForm):
    class Meta:
        model = VenteComptoir
        fields = ['CodeVente','Client', 'Produit','Qte','PrixVente','MontantPaye']