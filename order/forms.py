from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'products', 'quantity']

    def __init__(self, *args, **kwargs):
        # Extract the initial value for the customer field
        initial_customer = kwargs.pop('initial_customer', None)
        super().__init__(*args, **kwargs)
        # Set the initial value for the customer field
        if initial_customer:
            self.fields['customer'].initial = initial_customer
