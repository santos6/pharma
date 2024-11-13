from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView

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
    
def ajout_donnees(request):
    if request.method == 'POST':
        name = request.POST['name']
        #category = request.POST['category']
        price = request.POST['price']
        quantite = request.POST['quantite']
        description = request.POST['description']
        date_expiration = request.POST['date_expiration']
        image = request.FILES['image']

        #Récupération des catégories en fonction de la clé primaire
        category = Categories.objects.get(pk = request.POST['category'])

        savedonnees = Produits(name= name, price= price, quantite= quantite, description= description , date_expiration= date_expiration, category= category, image= image)
        savedonnees.save()
        return redirect('home')
    
    else:
        category = Categories.objects.all

    return render(request,"ajout-donnees.html", {"category" : category}) 