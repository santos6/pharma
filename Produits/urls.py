from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from Utilisateurs.views import Connecter_Compte

urlpatterns = [
   path('',Acc,name='acc'),
   path('produit/',Affichage.as_view(), name='home'),
   path('ajout/',AjoutProduits.as_view(), name='ajout'),

   path('modification/<int:pk>/',update_donnees.as_view(), name='modifier'),
   path('supprimer/<int:id>/', supprimer, name="supprimer"),
   #path('detail/<int:id>/',detail,name='detail'),
  path('detail/<int:pk>/',edit.as_view(),name='detail'),
 # path('modification/<int:id>/',modifier,name='modifier'),
 # path('ajout/',ajout_donnees, name='ajout')
 path('recherche/',recherche,name='recherche'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)