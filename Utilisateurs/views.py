from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate
from django.contrib import messages

import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



# fonction pour creer un compte
def Creation_Compte(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # Verification des mots de passe

        if password != password_confirm:
            messages.error(request, "Les mots de passe ne sont pas identiques.Veuillez réesseyer ")
            return redirect("creation")
        
        # vérification de la longueur et des caractères du mot de passe
        
        if len (password) < 8 or not re.search(r'[A-Za-z]', password) or not re.search(r'\d',password) or not re.search(r'[!@#$%(),.?":{}`|<>]',password):
           messages.error(request,'Le mot de passe doit contenir au moins 8 caractères, incluant des lettres, des chiffres et des caratères spéciaux.')
           return redirect("creation")
        
        #verification du format de l'adresse mail
        
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request,"L'adresse e-mail invalide. Veuillez réessayer.")
            return redirect('creation')

        #vérification de l'existence de l'utilisateur et de l'adresse mail
        if User.objects.filter(username=username).exists():
            messages.error(request,"Ce nom d'utilisateur existe déjà. Veuillez réessayer.")
            return redirect('creation')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"Cette adresse e-mail est déjà utilisée. Veuiller en choisir une autre.")
            return redirect('creation')
        
        # Création de l'utilisateur
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Compte créée avec succès. Connectez-vous maintenant")
        return redirect('login')
    
    return render(request,"creation.html")

# fonction pour se connecter

def Connecter_Compte(request):
    if request.method =="POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('acc')
        else:
            messages.error(request,"Nom d'utilisateur ou  mot de passe incorrect")
            return redirect("login")
    return render(request,'login.html')