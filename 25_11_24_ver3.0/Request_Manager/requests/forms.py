import re

from django import forms
from .models import  Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea,
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if "@" in name:
            raise forms.ValidationError("Имя не должно содержать '@'.")
        elif re.search(r'\d', name):
            raise forms.ValidationError("Имя не должно содержать цифры.")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        return email





