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


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from product.models import Product
from order.forms import OrderForm  
from order.models import Order, OrderProduct
@login_required
def add_order_view(request):
    if request.method == 'GET':
        # Assuming product_id and product_name are passed via GET request
        product_id = request.GET.get('product_id')
        product_name = request.GET.get('product_name')
        quantity = int(request.GET.get('quantity', 1))  # Ensure quantity is an integer
        
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
                
                # Get the current customer (assuming a relationship between User and Customer)
                customer = request.user.customer
                
                # Create a new order associated with the customer
                order = Order.objects.create(customer=customer)
                
                # Create an OrderProduct linking the product and quantity to the order
                OrderProduct.objects.create(order=order, product_id=product_id, quantity=quantity)
                
                messages.success(request, 'Order placed successfully!')
                return redirect('order_list')  # Replace 'order_list' with your actual URL name for order list view
            except Exception as e:
                messages.error(request, f'Failed to place order. Error: {str(e)}')
        else:
            messages.error(request, 'Form is invalid. Please check the form inputs.')
    else:
        form = OrderForm()
    
    return render(request, 'order/add_order.html', {'form': form, 'product_name': product_name})

from order.models import OrderProduct 

@login_required
def order_list(request):
    orders = Order.objects.all()  # Fetch all orders
    for order in orders:
        print(f"Order Number: {order.order_no}")
        for op in order.orderproduct_set.all():
            print(f"Product Name: {op.product.name}, Product ID: {op.product.id}, Quantity: {op.quantity}")
    
    return render(request, 'order/order_list.html', {'orders': orders})

def logout_view(request):
    logout(request)
    return redirect('dashboard:login_view')