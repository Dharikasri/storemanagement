from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from customer.models import Customer
from product.models import Product
from category.models import Category
from decimal import Decimal
from order.models import Order, OrderProduct
from order.serializers import OrderSerializer, OrderProductSerializer
from django.utils import timezone

class SerializerTestCase(TestCase):
    def setUp(self):
        # Set up a user, customer, category, and product
        self.user = User.objects.create_user(username='testuser', password='password')
        self.customer = Customer.objects.create(user=self.user, name='Test Customer', address='kk nagar', mobile='xxxxxxxxxx')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            product_id=1, 
            name='Test Product', 
            description='A test product', 
            expiry_date=None, 
            price=Decimal('9.99')
        )
        self.product.categories.add(self.category)
        
        self.order = Order.objects.create(customer=self.customer, order_date=timezone.now().date())
        self.order_product = OrderProduct.objects.create(order=self.order, product=self.product, quantity=2)

    def test_order_product_serializer(self):
        serializer = OrderProductSerializer(self.order_product)
        data = serializer.data
        
        self.assertEqual(data['product']['name'], self.product.name)
        self.assertEqual(data['quantity'], 2)

    