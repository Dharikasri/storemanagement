from django.urls import path,include
from . import views
from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.product_list, name='product_list'),
     path('api4/', include(router.urls)),
]
