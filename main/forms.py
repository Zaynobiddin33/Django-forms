from django import forms
from .models import *

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'age']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your surname'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
        }