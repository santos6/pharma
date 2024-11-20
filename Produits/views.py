from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.urls import reverse_lazy

from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView,UpdateView,DetailView
from .forms import AjoutProduit

from django.contrib import messages
from datetime import datetime

# La fonction 'home' permet d'afficher la page home.html
def home(request):
    return render(request,'home.html')

    #Récupération des données dans la base de données
   # donnees = Produits.objects.all()

   # context= {
   #     'donnees' :donnees
   # }

   # return render(request,'home.html',context)

def Acc(request):
    return render(request,'acc.html')

class Affichage(ListView):
    # Affichage du template
    template_name = 'home.html'
    #Récupération des données
    queryset = Produits.objects.all()


#Class  d'ajoutdes données 

class AjoutProduits(CreateView):
    #utilisation du model
    model = Produits
    #Specifier le formulaire à utiliser 
    form_class = AjoutProduit
    #Affichage du template
    template_name = 'ajout-donnees.html'
    #redirection après enregistrement
    success_url = reverse_lazy('home')


#class pour la modification
class update_donnees(UpdateView):

    #Récupération du model
    model = Produits
    #specifier le formulaire
    form_class = AjoutProduit
    #Précision du template
    template_name= 'modification.html'
    success_url = reverse_lazy('home')


#Fonction pour supprimer

def supprimer(request,id):
    if request.method == "POST":
        produit = get_object_or_404(Produits, id=id)
        produit.delete()
        return JsonResponse({'success':True, 'message':'Le produit a été supprimé avec succès'})
    return JsonResponse ( {'success':False,'message':'Methode non autorisé'})



    #fonction pour voir les details
def detail(request,id):

    n = Produits.objects.get(id=id)

    return render (request,'detail.html ',{'n':n})

#class pour voir les détails d'un produit
class edit(DetailView):
    model= Produits
    template_name= 'detail.html'
    context_object_name= 'n'

#fonction de recherche de produit
def recherche(request):

    query= request.GET.get('produit')
    donnees= Produits.objects.filter(name__icontains= query)
    context={
        'donnees': donnees
    }
    return render(request, 'resultat_recherche.html',context)


    #fonction pour modifier les donnees

# def modifier(request,id):
#     produit= get_object_or_404(Produits,id= id)
#     categories= Categories.objects.all()
#     errors = {}

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         category_id = request.POST.get('category')
#         price= request.POST.get('price')
#         quantite= request.POST.get('quantite')
#         description= request.POST.get('description')
#         date_expiration= request.POST.get('date_expiration')
#         image= request.FILES.get('image')
    
#         #validation des champs

#         if not name:
#             errors['name'] = "Le nom est requis"

#         if not category_id:
#             errors['category'] = "La categorie est requise"

#         if not price:
#             errors['price'] = "La prix est requise"

#         if not quantite:
#             errors['quantite'] = "La quantite est requise"

#         if not description:
#             errors['description'] = "La description est requise"

#         if not date_expiration:
#             try:
#                 datetime.strftime(date_expiration, '%Y-%m-%d')
#             except ValueError:
#                 errors['date_expiration'] = "Le format de ladate d'expiration est incorect. Utilisez le format AAAA-MM-JJ"

#         if not errors:
#             category = get_object_or_404(Categories, id=category_id)
#             produit.name = name
#             produit.category = category
#             produit.price = price
#             produit.quantite = quantite
#             produit.description = description
#             produit.date_expiration = date_expiration

#             if image:
#                 fs = FileSystemStorage()
#                 filname= fs.save(name.name,image)
#                 produit.image = fs.url(filname)
            
        
#         produit.save()
#         messages.success(request,"Le produit a été modifié avec succès !")
#         return redirect("home")
    
#     else:
#         for key, error in errors.items():
#             messages.error(request,error)

#     return render (request,"modification.html",{'produit':produit, 'categories':categories, 'errors':errors})




    
# def ajout_donnees(request):
#     #Creation de la variable pour la gestion des erreus
#     errors = {}
#     if request.method == 'POST':
#         name = request.POST['name']
#         #category = request.POST['category']
#         price = request.POST['price']
#         quantite = request.POST['quantite']
#         description = request.POST['description']
#         date_expiration = request.POST['date_expiration']
#         image = request.FILES['image']

#         #--- Validation de la date ---
#         #try :
#             #date_expiration= datetime.strftime(date_expiration, '%Y-%m-%d')
#         #except ValueError:
#             #errors ['date_expiration'] = "Le format de la date n'est pas bon. Essayez ceci: AAAA-MM-JJ"
        
#         #--- Validation du prix ---
#         try:
#             price = float(price)
            
#             if price < 0:
#                 errors['price'] = "Le prix ne peut pas être négatif"
#         except ValueError:
#             errors ['price'] = "Entrez un prix valide svp"

#         #Si aucune erreur n'est contatée
#         if not errors:
#             try:
#                 #Récupération des catégories en fonction de la clé primaire
#                 category = Categories.objects.get(pk = request.POST['category'])

#                 savedonnees = Produits(name= name, price= price, quantite= quantite, description= description , date_expiration= date_expiration, category= category, image= image)
#                 savedonnees.save()
#                 messages.success(request, "Le produit a été ajouté avec succès")
            
#             except Categories.DoesNotExist: 
#                 errors ['category'] = f'La catégorie spécifiée est introuvable.'
#             except KeyError as e:
#                 errors [str(e)] = f'Le champ {e} est manquant dans la requête'
#             except Exception as e:
#                 messages.error(request, f'Une erreur est survenu: {e}')

#         return redirect('home')
    
#     else:
#         category = Categories.objects.all

#     return render(request,"ajout-donnees.html", {"category" : category }) 
#     #return render(request,"ajout-donnees.html", {"category" : category, "errors" : errors })