from django.urls import path,include
from rest_framework import routers
from . import views
from .views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,CategoryViewSet

app_name = 'category'

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('category/list/', views.category_list, name='category_list'),
    path('category/create/', views.create_category, name='create_category'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
     path('api1/', include(router.urls)),
    
]