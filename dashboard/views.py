from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from category.models import Category
from product.models import Product
from order.forms import OrderForm
from order.models import Order

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
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from order.forms import OrderForm
from product.models import Product


@login_required
def add_order_view(request):
    if request.method == 'POST':
        print("POST request received")
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        print(f"Product ID: {product_id}, Quantity: {quantity}")
        
        try:
            product = Product.objects.get(id=product_id)
            print(f"Product found: {product.name}")
        except Product.DoesNotExist:
            print(f"Product with ID {product_id} does not exist")
            # Handle case where product does not exist, e.g., return an error response
        
        # Assuming you have a default customer or logic to determine customer
        initial_customer = request.user.customer
        print(f"Initial customer: {initial_customer}")
        
        # Prepare initial data for the order form
        initial_data = {
            'customer': initial_customer,
            'products': [product],
            'quantity': quantity,
            'product_name': product.name,  # Assuming 'name' is the attribute you want to prepopulate
        }
        print("Initial data prepared:", initial_data)
        
        # Create an instance of the OrderForm with initial data
        form = OrderForm(request.POST, initial=initial_data)
        
        if form.is_valid():
            print("Form is valid")
            form.save()
            messages.success(request, 'Order placed successfully!')
            return redirect('order_list')  # Redirect to order list page after successful submission
        else:
            print("Form is invalid")
            messages.error(request, 'Failed to place order. Please check the form.')
    else:
        print("GET request received")
    
    # If not a POST request or form is invalid, render the product list page again
    products = Product.objects.all()  # You might want to filter or order this differently
    quantity_range = range(1, 11)  # Example range for quantity selection
    
    return render(request, 'order/addorder.html', {'products': products, 'quantity_range': quantity_range})


@login_required
def order_list(request):
   orders = Order.objects.filter(customer=request.user.customer)
   return render(request, 'order/order_list.html', {'orders': orders})
