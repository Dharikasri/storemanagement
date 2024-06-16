# order/forms.py
from django import forms
from .models import Order
from product.models import Product

class OrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label=None)
    quantity = forms.IntegerField(min_value=1, max_value=20, initial=1)

    class Meta:
        model = Order
        fields = ['product', 'quantity', 'customer']  # Include 'customer' field in the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adjust queryset for product field if needed
        self.fields['product'].queryset = Product.objects.all()  # Example: filter or order queryset as required
