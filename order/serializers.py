from rest_framework import serializers
from .models import Order, OrderProduct
from customer.serializers import CustomerSerializer
from product.serializers import ProductSerializer

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  

    class Meta:
        model = OrderProduct
        fields = ['id', 'order', 'product','quantity']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    products = OrderProductSerializer(many=True, source='orderproduct_set')  

    class Meta:
        model = Order
        fields = ['id', 'order_no', 'order_date', 'customer', 'products']
