from django.contrib import admin
from .models import Produit, Fournisseur,Stock, Client, TypeProduit
# Register your models here.

admin.site.register(Produit)
admin.site.register(TypeProduit)
admin.site.register(Fournisseur)
admin.site.register(Client)
admin.site.register(Stock)