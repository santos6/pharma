from django.shortcuts import render
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
    
 