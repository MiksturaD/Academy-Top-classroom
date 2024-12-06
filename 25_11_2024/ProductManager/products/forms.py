import re

from django import forms
from .models import  Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price']
        widgets = {
            'price': forms.NumberInput
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if "@" in name:
            raise forms.ValidationError("Имя не должно содержать '@'.")
        elif re.search(r'\d', name):
            raise forms.ValidationError("Имя не должно содержать цифры.")
        return name







