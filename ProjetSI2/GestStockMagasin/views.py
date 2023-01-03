from django.shortcuts import render, redirect
from .models import TypeProduit, Produit, Fournisseur, Client
from .forms import ProduitForm, FournisseurForm, ClientForm,TypeForm
from django.contrib import messages
#View de dashboard


def dashboard(request):
    return render(request,"dashboard.html")


def afficher_Types(request):
    #Pour l'affichage des types des produits 
    Types = TypeProduit.objects.all()
    #Pour l'insertion
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
        'types':Types,
        'form' : form,
    }
    return render(request, "Types.html", contexte)

    ########################################################################

def afficher_Fournisseur(request):
    #Pour l'affichage des fournisseurs
    Fours = Fournisseur.objects.all()
    #Pour l'insertion
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
        'fournisseur' : Fours,
    }
    return render(request, "Fournisseurs.html", contexte)

########################################################################

def afficher_Produits(request):
    Prods = Produit.objects.all()
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
    }
    return render(request,"Produits.html",contexte)

######################################################################

def afficher_Client(request):
    #Pour l'affichage des clients
    Clients = Client.objects.all()
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
    } 
    return render(request, 'Clients.html', context)



#Les views des suppressions: 

def product_delete(request,pk):
    item = Produit.objects.get(CodeP=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-produits')
    else:
        form = ProduitForm(instance=item)
        return render(request,'delete_prod.html',{"form":form})

def client_delete(request,pk):
    item = Client.objects.get(CodeC=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-client')
    else:
        form = ClientForm(instance=item)
        return render(request,'delete_client.html',{"form":form})


def type_delete(request,pk):
    item = TypeProduit.objects.get(CodeT=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-types')
    else:
        form = TypeForm(instance=item)
        return render(request,'delete_type.html',{"form":form})


def fournisseur_delete(request,pk):
    item = Fournisseur.objects.get(CodeF=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Fournisseur')
    else:
        form = FournisseurForm(instance=item)
        return render(request,'delete_fournisseur.html',{"form":form})


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
            return render(request, 'edit_prod.html', {"form": form})

def client_edit(request, pk):
    item = Client.objects.get(CodeC=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-client")
    else: 
            form = ClientForm(instance= item)
            return render(request, 'edit_client.html', {"form": form})

def type_edit(request, pk):

    item = TypeProduit.objects.get(CodeT=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-types")
    else: 
            form = TypeForm(instance= item)
            return render(request, 'edit_type.html', {"form": form})

def fournisseur_edit(request, pk):

    item = Fournisseur.objects.get(CodeF=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-Fournisseur")
    else: 
            form = FournisseurForm(instance= item)
            return render(request, 'edit_fournisseur.html', {"form": form})

