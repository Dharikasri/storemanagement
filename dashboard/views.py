from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from category.models import Category
from product.models import Product
from order.forms import OrderForm
from order.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.forms import OrderForm
from order.models import Order, OrderProduct
from product.models import Product
from customer.models import Customer
from .decorators import admin_required
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if username == 'user': 
                    return redirect('dashboard:admin_dashboard')
                else:
                    return redirect('dashboard:dashboard') 
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    
    return render(request, 'webpage/login.html', {'form': form})

@login_required
def dashboard_view(request):
    user_is_superuser = request.user.is_superuser
    
    user_belongs_to_user_group = request.user.groups.filter(name='user').exists()
    
    products = Product.objects.all()  
    
    quantity_range = range(1, 21)  
    
    context = {
        'user_is_superuser': user_is_superuser,
        'user_belongs_to_user_group': user_belongs_to_user_group,
        'products': products,
        'quantity_range': quantity_range,
    }   
    return render(request, 'webpage/dashboard.html',context)


@login_required
def accounts_view(request):
    try:
        customer = Customer.objects.get(user=request.user)
        user_with_customer = {
            'username': request.user.username,
            'customer': customer
        }
        context = {'user_with_customer': user_with_customer}
    except Customer.DoesNotExist:
        context = {'user_with_customer': None}

    return render(request, 'webpage/accounts.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from order.forms import OrderForm
from order.models import Order, OrderProduct
from product.models import Product  
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from order.forms import OrderForm
from order.models import Order, OrderProduct
from product.models import Product

@login_required
def add_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                product = form.cleaned_data['product']
                quantity = form.cleaned_data['quantity']
                
                # Assuming each user has one customer profile
                customer = request.user.customer
                
                # Create the order
                order = Order.objects.create(customer=customer)
                
                # Create the OrderProduct entry
                OrderProduct.objects.create(order=order, product=product, quantity=quantity)
                
                messages.success(request, 'Order placed successfully!')
                return redirect('order:order_list')
            except Exception as e:
                messages.error(request, f'Failed to place order. Error: {str(e)}')
        else:
            messages.error(request, 'Form is invalid. Please check the form inputs.')
    else:
        # Handle GET request to prepopulate form
        product_id = request.GET.get('product_id')
        quantity = request.GET.get('quantity')
        initial_data = {}
        
        if product_id and quantity:
            try:
                product = Product.objects.get(id=product_id)
                initial_data = {
                    'product': product,
                    'quantity': quantity,
                }
            except Product.DoesNotExist:
                messages.error(request, 'Product does not exist.')

        form = OrderForm(initial=initial_data)
    
    return render(request, 'order/add_order.html', {'form': form})

@login_required
def order_list(request):
    customer = request.user.customer
    orders = Order.objects.filter(customer=customer).prefetch_related('orderproduct_set__product')
    return render(request, 'order/order_list.html', {'orders': orders})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('dashboard:login_view')


# Admin restricted views
@admin_required
def admin_dashboard_view(request):
    return render(request, 'webpage/admin_dashboard.html')

@admin_required
def manage_orders(request):
    orders = Order.objects.all()
    return render(request, 'webpage/manage_orders.html', {'orders': orders})

@admin_required
def manage_products(request):
    products = Product.objects.all()
    return render(request, 'webpage/manage_products.html', {'products': products})

@admin_required
def manage_accounts(request):
    users_with_customers = User.objects.filter(customer__isnull=False)
    return render(request, 'webpage/manage_accounts.html', {'users_with_customers': users_with_customers})
