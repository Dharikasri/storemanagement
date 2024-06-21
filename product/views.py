from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')  
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
