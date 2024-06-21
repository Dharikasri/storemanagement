from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order:order_list') 
    else:
        form = OrderForm()
    return render(request, 'order/add_order.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})


from rest_framework import viewsets
from .models import Order, OrderProduct
from .serializers import OrderSerializer, OrderProductSerializer 

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

