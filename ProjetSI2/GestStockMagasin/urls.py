from django.urls import path                                                                 
from . import views

urlpatterns = [
    path('list_produits/',views.afficher_Produits),
    path('list_Types/', views.afficher_Types),
    path('list_Client/',views.afficher_Client, name="dashboard-client"),
    path('list_Fournisseur/', views.afficher_Fournisseur),
]