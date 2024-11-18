from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   #path('',home,name='home'),
   path('',Affichage.as_view(), name='home'),
   path('ajout/',AjoutProduits.as_view(), name='ajout'),

   path('modification/<int:pk>/',update_donnees.as_view(), name='modifier'),
   path('supprimer/<int:id>/', supprimer, name="supprimer"),
   path('detail/<int:id>',detail,name='detail'),

 # path('modification/<int:id>/',modifier,name='modifier'),
 # path('ajout/',ajout_donnees, name='ajout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)