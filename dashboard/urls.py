from django.urls import path
from .views import login_view, dashboard_view, add_order_view, order_list, logout_view, accounts_view, homepage_view

app_name = 'dashboard'

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('list/', order_list, name='order_list'),
    path('add/', add_order_view, name='add_order'),
    path('logout/', logout_view, name='logout'),
    path('accounts/', accounts_view, name='accounts'),
    path('homepage/', homepage_view, name='homepage'),
]
