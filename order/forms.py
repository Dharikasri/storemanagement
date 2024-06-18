from django import forms
from .models import Order, OrderProduct
from product.models import Product
from customer.models import Customer

class OrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label=None)
    quantity = forms.IntegerField(min_value=1, max_value=20, initial=1)

    class Meta:
        model = Order
        fields = ['customer']  # Only include fields directly from the Order model

    def __init__(self, *args, **kwargs):
        initial_data = kwargs.get('initial', {})
        super().__init__(*args, **kwargs)
        
        # Adjust queryset for product field if needed
        self.fields['product'].queryset = Product.objects.all()  # Example: filter or order queryset as required
        
        # Initialize product and quantity from initial_data if available
        if initial_data:
            self.fields['product'].initial = initial_data.get('product')
            self.fields['quantity'].initial = initial_data.get('quantity')

    def save(self, commit=True):
        order = super().save(commit=False)
        
        # Retrieve the customer object associated with the current user
        customer = self.cleaned_data['customer']
        
        # Save the order instance if commit is True
        if commit:
            order.customer = customer
            order.save()
        
        # Now create the OrderProduct instance
        product = self.cleaned_data['product']
        quantity = self.cleaned_data['quantity']
        OrderProduct.objects.create(order=order, product=product, quantity=quantity)
        
        return order
