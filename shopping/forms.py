from django.forms import ModelForm
from .models import *
class ItemForm(ModelForm):
    class Meta:
        model = ShoppingList
        fields = '__all__'