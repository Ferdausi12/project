
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    buyer_name = forms.CharField(max_length=100)
    buyer_email = forms.EmailField()
    quantity = forms.IntegerField()

    class Meta:
        model = Order
        fields = ['quantity']  # Include only fields from the model


