from django.shortcuts import render
from .models import *


# La fonction 'home' permet d'afficher la page home.html
def home(request):
    return render(request,'home.html')
    
