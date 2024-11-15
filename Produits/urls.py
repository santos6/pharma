from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   #path('',home,name='home'),
   path('',Affichage.as_view(), name='home'),
   path('ajout/',AjoutProduits.as_view(), name='ajout'),
 #  path('ajout/',ajout_donnees, name='ajout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)