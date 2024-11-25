import re

from django import forms
from .models import  Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


    def clean_name(self):
        name = self.cleaned_data['name']
        if "@" in name:
            raise forms.ValidationError("Имя не должно содержать '@'.")
        elif re.search(r'\d', name):
            raise forms.ValidationError("Имя не должно содержать цифры.")
        return name




