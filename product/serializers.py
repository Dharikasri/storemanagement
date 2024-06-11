from rest_framework import serializers
from .models import Product
from category.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)  # Serialize ManyToManyField

    class Meta:
        model = Product
        fields = ['id', 'product_id', 'name', 'categories', 'description', 'expiry_date', 'price']
