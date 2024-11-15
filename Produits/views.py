from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
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
    template_name = 'ajout.html'
    #redirection après enregistrement
    success_url = reverse_lazy('home')




    
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