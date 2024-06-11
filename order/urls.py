from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_order, name='add_order'),
    path('list/', views.order_list, name='order_list'),
]
