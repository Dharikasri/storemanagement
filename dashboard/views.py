from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from category.models import Category
from product.models import Product
from order.forms import OrderForm
from order.models import Order
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.forms import OrderForm
from order.models import Order, OrderProduct
from product.models import Product

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:dashboard')  # Redirect to the dashboard using namespace
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'webpage/login.html', {'form': form})

@login_required
def dashboard_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    quantity_range = range(1, 21)
    return render(request, 'webpage/dashboard.html', {'categories': categories, 'products': products,'quantity_range': quantity_range})

def product_list(request):
    return render(request, 'product/product_list.html')

def logout_view(request):
    logout(request)
    return redirect('dashboard:login_view') 

@login_required
def accounts_view(request):
    users_with_customers = User.objects.filter(customer__isnull=False)
    return render(request, 'webpage/accounts.html', {'users_with_customers': users_with_customers})

def homepage_view(request):
    return render(request, 'webpage/Homepage.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from order.models import Order, OrderProduct
from order.forms import OrderForm 
from product.models import Product  
@login_required
def add_order_view(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        product_name = request.GET.get('product_name')
        quantity = request.GET.get('quantity', 1)  
        
        product = get_object_or_404(Product, id=product_id)
        
        initial_data = {
            'product': product,
            'quantity': quantity,
        }
        form = OrderForm(initial=initial_data)
    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                product_id = form.cleaned_data['product'].id
                quantity = form.cleaned_data['quantity']
                
                customer = request.user.customer
                
                order = Order.objects.create(customer=customer)
                OrderProduct.objects.create(order=order, product_id=product_id, quantity=quantity)
                
                messages.success(request, 'Order placed successfully!')
                return redirect('order_list') 
            except Exception as e:
                messages.error(request, f'Failed to place order. Error: {str(e)}')
        else:
            messages.error(request, 'Form is invalid. Please check the form inputs.')
    else:
        form = OrderForm() 

    return render(request, 'order/add_order.html', {'form': form, 'product': product_name})



@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})
