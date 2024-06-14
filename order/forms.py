from django import forms
from .models import Order
from product.models import Product

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        product_ids = kwargs.pop('product_ids', None)
        initial_customer = kwargs.pop('initial_customer', None)
        super().__init__(*args, **kwargs)

        # Filter products based on provided product_ids
        if product_ids:
            products = Product.objects.filter(id__in=product_ids)
            self.fields['products'].queryset = products
            if products:
                self.fields['products'].initial = products.first()

        # Set initial customer if provided
        if initial_customer:
            self.fields['customer'].initial = initial_customer

    class Meta:
        model = Order
        fields = ['customer', 'products', 'quantity']