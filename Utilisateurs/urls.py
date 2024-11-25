from django.urls import path
from .views import *


urlpatterns = [
  path('connecter/',Connecter_Compte, name='login'),
  path('creation/',Creation_Compte, name='creation'),

]
