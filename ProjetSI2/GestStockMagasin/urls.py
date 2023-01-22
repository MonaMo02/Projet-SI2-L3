from django.urls import path                                                                 
from . import views

urlpatterns = [
    path('', views.dashboard, name='main-dashboard'),
    path('list_produits/',views.afficher_Produits,name="dashboard-produits"),
    path('list_Types/', views.afficher_Types,name="dashboard-types"),
    path('list_Client/',views.afficher_Client, name="dashboard-client"),
    path('list_Fournisseur/', views.afficher_Fournisseur,name="dashboard-Fournisseur"),
    path('list_produits/deleteP/<int:pk>/',views.product_delete,name='delete-product'),
    path('list_produits/deleteC/<int:pk>/',views.client_delete,name='delete-client'),
    path('list_produits/deleteF/<int:pk>/',views.fournisseur_delete,name='delete-fournisseur'),
    path('list_produits/deleteT/<int:pk>/',views.type_delete,name='delete-type'),
    path('list_produits/editP/<int:pk>/',views.product_edit,name='edit-product'),
    path('list_produits/editC/<int:pk>/',views.client_edit,name='edit-client'),
    path('list_produits/editT/<int:pk>/',views.type_edit,name='edit-type'),
    path('list_produits/editF/<int:pk>/',views.fournisseur_edit,name='edit-fournisseur'),
    # path('login/', views.login, name="dash-login"),
    # path('register/' , views.register, name="dash-register"),
    path('Stock/',views.afficher_Stock, name="dashboard-stock"),
    path('Stock/editS/<int:pk>/', views.editstock, name="edit-stock"),
    path('Stock/deleteS/<int:pk>/', views.deletestock, name="delete-stock"),
    path('Vente/', views.afficher_Vente, name="dashboard-vente"),
    path('Vente/editV/<int:pk>/', views.editvente, name="edit-vente"),
    path('Vente/deleteV/<int:pk>/', views.deletevente, name="delete-vente"),
]