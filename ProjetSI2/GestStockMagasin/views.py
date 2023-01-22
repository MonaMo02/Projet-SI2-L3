from django.shortcuts import render, redirect
from .models import TypeProduit, Stock, Produit, Fournisseur, Client
from .forms import ProduitForm, FournisseurForm,StockForm,UserForm ,ClientForm,TypeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



#login and register views

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "users/register.html", {'form': form})

def login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('main-dashboard')
        else:
            return HttpResponse('Error, user does not exist')
    return render(request, 'users/login.html', {})


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
    }
    return render(request, 'dashboard/stock.html', contexte)



def editstock(request, pk):
    item = Stock.objects.get(CodeS=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-stock")
    else: 
            form = StockForm(instance= item)
            return render(request, 'dashboard/edit_stock.html', {"form": form})



def deletestock(request,pk):
    item = Stock.objects.get(CodeS=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-stock')
    else:
        form = StockForm(instance=item)
        return render(request,'dashboard/delete_stock.html',{"form":form})


#end stock views



#View de dashboard
@login_required(login_url='login')
def dashboard(request):
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
    }
    return render(request,"dashboard/dashboard.html", context)

@login_required(login_url='login/')
def afficher_Types(request):
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
    }
    return render(request, "dashboard/Types.html", contexte)

    ########################################################################

@login_required(login_url='dash-login')
def afficher_Fournisseur(request):
    prods = Produit.objects.all()
    prod_count = prods.count()
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
        'T_count':type_count,
        'S_count':stock_count,
    }
    return render(request, "dashboard/Fournisseurs.html", contexte)

########################################################################

@login_required(login_url='login/')
def afficher_Produits(request):
    Prods = Produit.objects.all()
    prod_count = Prods.count()
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
        'T_count':type_count,
        'S_count':stock_count,
    }
    return render(request,"dashboard/Produits.html",contexte)

######################################################################

@login_required(login_url='dash-login')
def afficher_Client(request):
    prods = Produit.objects.all()
    prod_count = prods.count()
    fours = Fournisseur.objects.all()
    fours_count = fours.count()
    types = TypeProduit.objects.all()
    type_count = types.count()
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
        'C_count':client_count,
        'U_count': user_count,
        'T_count':type_count,
        'S_count':stock_count,
    } 
    return render(request, 'dashboard/Clients.html', context)



#Les views des suppressions: 

@login_required(login_url='login')
def product_delete(request,pk):
    item = Produit.objects.get(CodeP=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-produits')
    else:
        form = ProduitForm(instance=item)
        return render(request,'dashboard/delete_prod.html',{"form":form})

def client_delete(request,pk):
    item = Client.objects.get(CodeC=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-client')
    else:
        form = ClientForm(instance=item)
        return render(request,'dashboard/delete_client.html',{"form":form})


def type_delete(request,pk):
    item = TypeProduit.objects.get(CodeT=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-types')
    else:
        form = TypeForm(instance=item)
        return render(request,'dashboard/delete_type.html',{"form":form})


def fournisseur_delete(request,pk):
    item = Fournisseur.objects.get(CodeF=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-Fournisseur')
    else:
        form = FournisseurForm(instance=item)
        return render(request,'dashboard/delete_fournisseur.html',{"form":form})


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
            return render(request, 'dashboard/edit_prod.html', {"form": form})

def client_edit(request, pk):
    item = Client.objects.get(CodeC=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-client")
    else: 
            form = ClientForm(instance= item)
            return render(request, 'dashboard/edit_client.html', {"form": form})

def type_edit(request, pk):

    item = TypeProduit.objects.get(CodeT=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-types")
    else: 
            form = TypeForm(instance= item)
            return render(request, 'dashboard/edit_type.html', {"form": form})

def fournisseur_edit(request, pk):

    item = Fournisseur.objects.get(CodeF=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("dashboard-Fournisseur")
    else: 
            form = FournisseurForm(instance= item)
            return render(request, 'dashboard/edit_fournisseur.html', {"form": form})



# def create_BDC(request):
#     item = UneCommande.objects.all()
#     if request.method == 'POST':
#         form = List_CMD_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("dashboard-BDC")
#     else:
#         form = List_CMD_Form()

#     contexte = {
#         'List':item,
#         'form' : form,
#     }
#     return render(request, "dashboard/create_BDC.html",contexte)
    




# def save_BDC(request):
#     buf = io.BytesIO()
#     c = canvas.Canvas(buf, pagesize = letter, buttomup =0 )
#     textOb = c.beginText()
#     textOb.setTextOrigin(inch , inch)
#     textOb.setFont("Helvatica", 14)
#     ListP = UneCommande.objects.all()
#     Lines = []
#     for u in ListP: 
#         Lines.append(u.product)
#         Lines.append(u.QTE)
#         Lines.append(" ")
#     for line in Lines:
#         textOb.textLine(line)
#     c.drawText(textOb)
#     c.showPage()
#     c.save()
#     buf.seek(0)
#     return FileResponse(buf, as_attachment=True, filename="BonDeCommande.pdf")



# def save_BDC(request):
#     item = UneCommande.objects.all()
#     return render(request,"dashboard/saved_BDC.html", {"List":item})


# def new_BDC(request):
#     item = UneCommande.objects.all()
#     item.delete()    
#     create_BDC(request)
#     return redirect(request, "dashboard/create_BDC.html")



# def rechercher_produits(request):  
#     if request.method =="GET": 
#         query=request.GET.get('recherche')   
#         if query: 
#             produits=Produit.objects.filter(name__contains = query)
#             return render(request, "search.html",{"products":produits})
#         else:
#             return render(request, "search.html")
        

# def create_facture(request):
#     item = Facture.objects.all()
#     if request.method == 'POST':
#         form = FactureForm(request.POST)
#         if form.is_valid():
#             form.save()
#             c = form.cleaned_data.get('commande')
#             p = c.get('product')
#             q = c.get('QTE')
#             prix = form.cleaned_data.get('Mont_HT')
#             pu = form.cleaned_data.get('Prix_unit')
#             prix = q * pu
#             return redirect("dashboard-BDC", {"produit":p, "Montant":prix, "QTE":q })
#     else:
#         form = FactureForm()

#     contexte = {
#         'facture':item,
#         'form' : form,
#     }
#     return render(request, "create_BDC.html",contexte)

