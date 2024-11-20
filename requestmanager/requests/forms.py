from django import forms
from .models import Feedback

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100,label="Ваше имя")
    def clean_name(self):
        name = self.cleaned_data['name']
        if "@" in name:
            raise forms.ValidationError("Имя не должно содержать '@'.")
        return name
    email = forms.EmailField(label="Ваш email")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")



class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']