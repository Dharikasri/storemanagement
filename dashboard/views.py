from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from category.models import Category
from product.models import Product
from order.forms import OrderForm
from order.models import Order
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
    return render(request, 'webpage/dashboard.html', {'categories': categories, 'products': products})


def product_list(request):
    return render(request, 'product/product_list.html')


def logout_view(request):
    logout(request)
    return redirect('dashboard:login_view')  # Redirect to the login view using namespace


@login_required
def accounts_view(request):
    users_with_customers = User.objects.filter(customer__isnull=False)
    return render(request, 'webpage/accounts.html', {'users_with_customers': users_with_customers})


def homepage_view(request):
    return render(request, 'webpage/Homepage.html')


@login_required
def add_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order:order_list')  # Redirect to the order list using namespace
    else:
        form = OrderForm()
    return render(request, 'order/add_order.html', {'form': form})


@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})
