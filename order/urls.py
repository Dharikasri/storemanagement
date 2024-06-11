from django.urls import path,include
from . import views
from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet, OrderProductViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order-products', OrderProductViewSet)

urlpatterns = [
    path('add/', views.add_order, name='add_order'),
    path('list/', views.order_list, name='order_list'),
    path('api3/', include(router.urls)),
]
