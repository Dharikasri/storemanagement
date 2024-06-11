from django.urls import path
from .views import (
    customer_list,
    customer_detail,
    customer_create,
    customer_update,
    customer_delete,
)

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('customer/<int:pk>/', customer_detail, name='customer_detail'),
    path('customer/create/', customer_create, name='customer_create'),
    path('customer/<int:pk>/update/', customer_update, name='customer_update'),
    path('customer/<int:pk>/delete/', customer_delete, name='customer_delete'),
]
