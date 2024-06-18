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


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:homepage')  # Redirect to the dashboard using namespace
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'webpage/login.html', {'form': form})

@login_required
def homepage_view(request):
       return render(request, 'webpage/Homepage.html', {'user': request.user.customer})


@login_required
def dashboard_view(request):
    products = Product.objects.all()
    quantity_range = range(1, 21)
    return render(request, 'webpage/dashboard.html', {'products': products,'quantity_range': quantity_range})

def product_list(request):
    return render(request, 'product/product_list.html')


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
    orders = Order.objects.filter(customer=customer).order_by('-order_date').prefetch_related('orderproduct_set__product')
    
    return render(request, 'order/order_list.html', {'orders': orders})

def logout_view(request):
    logout(request)
    return redirect('dashboard:login_view')