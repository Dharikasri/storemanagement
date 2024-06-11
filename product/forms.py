from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'categories', 'description', 'expiry_date', 'price']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }
