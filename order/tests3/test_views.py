from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from order.models import Order,OrderProduct
from customer.models import Customer
from product.models import Product
from category.models import Category
from decimal import Decimal

class OrderURLsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.category = Category.objects.create(name="Test Category")

    
        self.customer = Customer.objects.create(name="Test Customer")


        self.product = Product.objects.create(
            product_id=1,  
            name="Test Product", 
            description="Test Description",
            price=Decimal('10.00')
        )
        self.product.categories.add(self.category)  


        self.order = Order.objects.create(
            customer=self.customer,
        )

        self.order_product = OrderProduct.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )

    def test_add_order_url(self):
        url = reverse('order:add_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_order_list_url(self):
        url = reverse('order:order_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_order_api_list_url(self):
        url = reverse('order:order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
