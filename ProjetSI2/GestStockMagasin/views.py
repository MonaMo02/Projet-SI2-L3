from django.shortcuts import render, redirect
from .models import TypeProduit, Produit, Fournisseur, Client
from .forms import ProduitForm, FournisseurForm, ClientForm,TypeForm
#View de dashboard


def dashboard(request):
    return render(request,"dashboard.html")


#Les views de l'affichage de la section Tables
def afficher_Types(request):
    Types = TypeProduit.objects.all()
    return render(request,"Types.html",{"Types":Types})

def afficher_Fournisseur(request):
    Fours = Fournisseur.objects.all()
    return render(request,"Fournisseurs.html",{"Fournisseurs":Fours})

def afficher_Produits(request):
    Prods = Produit.objects.all()
    if request.method == 'POST':
        form = ProduitForm(request.POST)

        if form.is_valid():
            form.save()
            form = ProduitForm()
            message = "Produit inseré"
            return render(request,"Produits.html",{"form":form, "message":message})
    else:
        form = ProduitForm()
        message = "Veuillez remplir tous les champs!"
        return render(request,"Produits.html",{"form":form, "message":message})

    return render(request,"Produits.html",{"Produits":Prods})

def afficher_Client(request):
    Clients = Client.objects.all()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClientForm()
            message = "Client inseré"
            return redirect("dashboard-client",{"message":message})
    else:
        form = ClientForm()
    context = {
        'Clients': Clients,
        'form': form,
    }
    return render(request, 'Clients.html', context)


#Les views des formulaires d'insertion:
