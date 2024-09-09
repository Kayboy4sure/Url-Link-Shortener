from .models import Urldata
from django import forms

class UrldataForm(forms.ModelForm):
    class Meta:
        model = Urldata
        fields = ['url']
        labels = {
            'url': 'Link'
        }
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the link here...'}),
        }