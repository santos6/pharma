from django.forms import ModelForm

from.models import Produits, Categories
from django import forms

class AjoutProduit(ModelForm):

    class Meta:
        model = Produits
        fields = [
            'name','category','price','quantite','description','date_expiration','image'
        ]

        widgets= {
            'name': forms.TextInput(
                attrs= {
                    'placehoder' : 'Entrez le nom du produit',
                    'class': 'form-control'
                }
            ),

            'category': forms.Select(
                attrs= {
                    'class': 'form-control'
                }
            ),

             'price': forms.NumberInput(
                attrs= {
                    'placehoder' : 'Entrez le prix du produit',
                    'class': 'form-control'
                }
            ),

            'quantite': forms.NumberInput(
                attrs= {
                    'placehoder' : 'Entrez la quantité',
                    'class': 'form-control'

                }
            ),

            'description': forms.Textarea(
                attrs= {
                    'placehoder' : 'Description',
                    'class': 'form-control',
                    'rows' : 4
                }
            ),

            'date_expiration': forms.DateInput(
                attrs= {
                    'placehoder' : 'Date d\'expiration',
                    'class': 'form-control',
                    'type' : 'date'
                }
            ),

            'image': forms.FileInput (
                attrs= {
                    'class': 'form-control-file'
                }
            ),
        }

        def __init__(self, *args, **kwargs):

            super(AjoutProduit, self).__init__(*args, **kwargs)

            self.fields['name'].error_messages = {
                'required': 'Le nom est obligatoire',
                'invalid': 'Veuillez renseignez le nom'
            }

            
            self.fields['category'].error_messages = {
                'required': 'La categorie est obligatoire',
                'invalid' : 'Veuillez sectionner une categorie'
            }

            self.fields['price'].error_messages = {
                'required': 'Le prix est obligatoire',
                'invalid' : 'Veuillez entrer le prix'
            }

            self.fields['quantite'].error_messages = {
                'required': 'La quantite est obligatoire',
                'invalid' : 'Veuillez entrer la quantite '
            }

            self.fields['description'].error_messages = {
                'required': 'La description est obligatoire',
                'invalid' : 'Veuillez entrer la description '
            }

            self.fields['date_expiration'].error_messages = {
                'required': 'La date est obligatoire',
                'invalid' : 'Veuillez entrer une date '
            }

            # self.fields['image'].error_messages = {
            #     'required': 'La date est obligatoire',
            #     'invalid' : 'Veuillez entrer une date '
            # }