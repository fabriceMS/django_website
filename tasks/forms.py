from django import forms
from django.forms import ModelForm

from .models import Item

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item    # For which model we are creating the form
        fields = '__all__'      # Which fields of the model are in the form