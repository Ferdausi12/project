from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'description', 'price', 'condition', 'image','owner']
