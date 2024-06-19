from django.urls import path
from .views import login_view,manage_accounts, dashboard_view, add_order_view, order_list, logout_view, accounts_view, homepage_view,manage_products,manage_orders,admin_dashboard_view

app_name = 'dashboard'

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('homepage/',homepage_view, name='homepage'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('admin/',admin_dashboard_view, name='admin_dashboard'),
    path('list/', order_list, name='order_list'),
    path('add/', add_order_view, name='add_order'),
    path('logout/', logout_view, name='logout'),
    path('accounts/', accounts_view, name='accounts'),
    path('manage-products/',manage_products, name='manage_products'),
    path('manage-orders/',manage_orders, name='manage_orders'),
    path('manage-accounts/',manage_accounts, name='manage_accounts'),
]
    


