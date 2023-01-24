from django.shortcuts import render, redirect
from .models import TypeProduit,VenteComptoir, Stock, Produit, Fournisseur, Client
from .forms import ProduitForm, VentCForm, FournisseurForm,StockForm,UserForm ,ClientForm,TypeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



#login and register views

# def register(request):
#     form = UserForm()
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, "users/register.html", {'form': form})

# def login(request):
#     if request.method == 'POST':
#         name = request.POST.get('uname')
#         password = request.POST.get('pass')
#         user = authenticate(request, username=name, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('main-dashboard')
#         else:
#             return HttpResponse('Error, user does not exist')
#     return render(request, 'users/login.html', {})

#Vente views

def afficher_Vente(request):
    item = VenteComptoir.objects.all()
    vente_count = item.count()
    prods = Produit.objects.all()
    prod_count = prods.count()
    fours = Fournisseur.objects.all()
    fours_count = fours.count()
    types = TypeProduit.objects.all()
    type_count = types.count()
    users = User.objects.all()
    user_count = users.count()
    Clients = Client.objects.all()
    client_count = Clients.count()
    stock = Stock.objects.all()
    stock_count = stock.count()
    if request.method == 'POST':
        form = VentCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-vente')
    else:
        form = VentCForm()
    contexte = {
        'ventes':item,
        'form' : form,
        'P_count':prod_count,
        'F_count':fours_count,
        'C_count':client_count,
        'U_count': user_count,
        'T_count':type_count,
        'S_count':stock_count,
        'V_count':vente_count,
    }
    return render(request, 'Vente/vente.html', contexte)

# def editvente(request, pk):
#     item = VenteComptoir.objects.get(CodeVente=pk)
#     if request.method == 'POST':
#         form = VentCForm(request.POST, instance = item)
#         if form.is_valid():
#             form.save()
#             return redirect("dashboard-vente")
#     else: 
#             form = VentCForm(instance= item)
#             return render(request, 'dashboard/edit_vente.html', {"form": form})



def edit_vente(request, pk):
    vente = VenteComptoir.objects.get(CodeVente = pk)
    if request.method == 'POST':
        form = VentCForm(request.POST, instance= vente)
        if form.is_valid():
            form.save()
            return redirect('dashboard-vente')
    else:
        form = VentCForm(instance=vente)
        return render(request, 'Vente/edit_vente.html', {"form":form})


def deletevente(request,pk):
    item = VenteComptoir.objects.get(CodeVente=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-vente')
    else:
        form = VentCForm(instance=item)
        return render(request,'Vente/delete_vente.html',{"form":form})


#end vente views

#stock views

def afficher_Stock(request):
    prods = Produit.objects.all()
    prod_count = prods.count()
    fours = Fournisseur.objects.all()
    fours_count = fours.count()
    types = TypeProduit.objects.all()
    type_count = types.count()
    users = User.objects.all()
    user_count = users.count()
    Clients = Client.objects.all()
    client_count = Clients.count()
    stock = Stock.objects.all()
    stock_count = stock.count()
    item = VenteComptoir.objects.all()
    vente_count = item.count()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-stock")
    else:
        form = StockForm()
    contexte = {
        'stock':stock,
        'form' : form,
        'P_count':prod_count,
        'F_count':fours_count,
        'C_count':client_count,
        'U_count': user_count,
        'T_count':type_count,
        'S_count':stock_count,
        'V_count':vente_count,
    }
    return render(request, 'Stock/stock.html', contexte)



def editstock(request, pk):
    item = Stock.objects.get(CodeS=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-stock")
    else: 
            form = StockForm(instance= item)
            return render(request, 'Stock/edit_stock.html', {"form": form})



def deletestock(request,pk):
    item = Stock.objects.get(CodeS=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-stock')
    else:
        form = StockForm(instance=item)
        return render(request,'Stock/delete_stock.html',{"form":form})


#end stock views



#View de dashboard
def dashboard(request):
    item = VenteComptoir.objects.all()
    vente_count = item.count()
    prods = Produit.objects.all()
    prod_count = prods.count()
    fours = Fournisseur.objects.all()
    fours_count = fours.count()
    clients = Client.objects.all()
    client_count = clients.count()
    types = TypeProduit.objects.all()
    type_count = types.count()
    users = User.objects.all()
    user_count = users.count()
    stocks = Stock.objects.all()
    stock_count = stocks.count()
    context ={
        'P_count':prod_count,
        'F_count':fours_count,
        'C_count':client_count,
        'U_count': user_count,
        'T_count':type_count,
        'S_count':stock_count,
        'V_count':vente_count,
    }
    return render(request,"dashboard/dashboard.html", context)

def afficher_Types(request):
    prods = Produit.objects.all()
    prod_count = prods.count()
    item = VenteComptoir.objects.all()
    vente_count = item.count()
    fours = Fournisseur.objects.all()
    fours_count = fours.count()
    types = TypeProduit.objects.all()
    type_count = types.count()
    users = User.objects.all()
    user_count = users.count()
    Clients = Client.objects.all()
    client_count = Clients.count()
    stock = Stock.objects.all()
    stock_count = stock.count()
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            T_name = form.cleaned_data.get('DesignationT')
            messages.success(request, f'{T_name} has been added')
            return redirect("dashboard-types")
    else:
        form = TypeForm()

    contexte = {
        'types':types,
        'form' : form,
        'P_count':prod_count,
        'F_count':fours_count,
        'C_count':client_count,
        'U_count': user_count,
        'T_count':type_count,
        'S_count':stock_count,
        'V_count':vente_count,
    }
    return render(request, "Types/Types.html", contexte)

    ########################################################################

def afficher_Fournisseur(request):
    prods = Produit.objects.all()
    prod_count = prods.count()
    item = VenteComptoir.objects.all()
    vente_count = item.count()
    fours = Fournisseur.objects.all()
    fours_count = fours.count()
    types = TypeProduit.objects.all()
    type_count = types.count()
    users = User.objects.all()
    user_count = users.count()
    stock = Stock.objects.all()
    stock_count = stock.count()
    #Pour l'affichage des clients
    Clients = Client.objects.all()
    client_count = Clients.count()
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            F_name = form.cleaned_data.get('NomF')
            messages.success(request,f'{F_name} has been added')
            return redirect("dashboard-Fournisseur")
    else:
        form = FournisseurForm()

    contexte = {
        'form' : form,
        'fournisseur' : fours,
        'P_count':prod_count,
        'F_count':fours_count,
        'C_count':client_count,
        'U_count': user_count,
        'V_count':vente_count,
        'T_count':type_count,
        'S_count':stock_count,
    }
    return render(request, "Fournisseurs/Fournisseurs.html", contexte)

########################################################################

def afficher_Produits(request):
    Prods = Produit.objects.all()
    prod_count = Prods.count()
    item = VenteComptoir.objects.all()
    vente_count = item.count()
    fours = Fournisseur.objects.all()
    fours_count = fours.count()
    types = TypeProduit.objects.all()
    type_count = types.count()
    users = User.objects.all()
    user_count = users.count()
    stock = Stock.objects.all()
    stock_count = stock.count()
    #Pour l'affichage des clients
    Clients = Client.objects.all()
    client_count = Clients.count()
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-produits")
    else:
        form = ProduitForm()
    contexte = {
        'produits' : Prods,
        'form' : form,
        'P_count':prod_count,
        'F_count':fours_count,
        'C_count':client_count,
        'U_count': user_count,
        'V_count':vente_count,
        'T_count':type_count,
        'S_count':stock_count,
    }
    return render(request,"Produit/Produits.html",contexte)

######################################################################

def afficher_Client(request):
    prods = Produit.objects.all()
    prod_count = prods.count()
    fours = Fournisseur.objects.all()
    fours_count = fours.count()
    types = TypeProduit.objects.all()
    type_count = types.count()
    item = VenteComptoir.objects.all()
    vente_count = item.count()
    users = User.objects.all()
    user_count = users.count()
    #Pour l'affichage des clients
    Clients = Client.objects.all()
    client_count = Clients.count()
    stock = Stock.objects.all()
    stock_count = stock.count()
    #Pour l'insertion
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            C_name = form.cleaned_data.get('NomC')
            messages.success(request, f'{C_name} has been added')
            return redirect("dashboard-client")
    else:
        form = ClientForm()

    context = {
        'Clients': Clients,
        'form': form,
        'P_count':prod_count,
        'F_count':fours_count,
        'V_count':vente_count,
        'C_count':client_count,
        'U_count': user_count,
        'T_count':type_count,
        'S_count':stock_count,
    } 
    return render(request, 'Client/Clients.html', context)



#Les views des suppressions: 

def product_delete(request,pk):
    item = Produit.objects.get(CodeP=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-produits')
    else:
        form = ProduitForm(instance=item)
        return render(request,'Produit/delete_prod.html',{"form":form})

def client_delete(request,pk):
    item = Client.objects.get(CodeC=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-client')
    else:
        form = ClientForm(instance=item)
        return render(request,'Client/delete_client.html',{"form":form})


def type_delete(request,pk):
    item = TypeProduit.objects.get(CodeT=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-types')
    else:
        form = TypeForm(instance=item)
        return render(request,'Types/delete_type.html',{"form":form})


def fournisseur_delete(request,pk):
    item = Fournisseur.objects.get(CodeF=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Fournisseur')
    else:
        form = FournisseurForm(instance=item)
        return render(request,'Fournisseurs/delete_fournisseur.html',{"form":form})


#les views de modification

def product_edit(request, pk):
    item = Produit.objects.get(CodeP=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-produits")
    else: 
            form = ProduitForm(instance= item)
            return render(request, 'Produit/edit_prod.html', {"form": form})

def client_edit(request, pk):
    item = Client.objects.get(CodeC=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-client")
    else: 
            form = ClientForm(instance= item)
            return render(request, 'Client/edit_client.html', {"form": form})

def type_edit(request, pk):
    item = TypeProduit.objects.get(CodeT=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-types")
    else: 
            form = TypeForm(instance= item)
            return render(request, 'Types/edit_type.html', {"form": form})

def fournisseur_edit(request, pk):

    item = Fournisseur.objects.get(CodeF=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-Fournisseur")
    else: 
            form = FournisseurForm(instance= item)
            return render(request, 'Fournisseurs/edit_fournisseur.html', {"form": form})

