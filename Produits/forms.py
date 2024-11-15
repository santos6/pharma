from django.forms import ModelForm

from.models import Produits, Categories

class AjoutProduit(ModelForm):

    class Meta:
        model = Produits
        fields = [
            'name','category','price','quantite','description','date_expiration','image'
        ]