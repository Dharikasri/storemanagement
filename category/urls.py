from django.urls import path
from . import views

urlpatterns = [
    path('category/list/', views.category_list, name='category_list'),
    path('category/create/', views.create_category, name='create_category'),
]
