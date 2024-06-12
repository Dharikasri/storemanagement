from django.urls import path, include
from rest_framework import routers
from .views import OrderViewSet, OrderProductViewSet, add_order, order_list

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order-products', OrderProductViewSet)

app_name = 'order'  

urlpatterns = [
    path('add/', add_order, name='add_order'),
    path('list/', order_list, name='order_list'),
    path('api3/', include(router.urls)),
]
