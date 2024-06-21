# tests.py

from django.test import TestCase
from django.utils import timezone
from decimal import Decimal
from order.models import Order, OrderProduct
from customer.models import Customer
from product.models import Product
import uuid

from order.serializers import OrderSerializer

class OrderSerializerTestCase(TestCase):
    def setUp(self):
        # Create a customer
        self.customer = Customer.objects.create(name='Sridhar')

        # Create a product
        self.product = Product.objects.create(
            product_id=3,
            name='Diary milk',
            description='Test Description',
            price=Decimal('10.00')
        )

        # Create an order
        self.order = Order.objects.create(
            order_no=uuid.uuid4(),
            order_date=timezone.datetime(2024, 6, 21).date(),
            customer=self.customer
        )

        # Create an order product
        self.order_product = OrderProduct.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )

    def test_order_serializer(self):
        serializer = OrderSerializer(instance=self.order)
        expected_data = {
            'id': self.order.id,
            'order_no': str(self.order.order_no),
            'order_date': '2024-06-21',  # Ensure date format matches the serializer output
            'customer': 'Sridhar',  # Customer name as string
            'products': [
                {
                    'product_name': 'Diary milk',
                    'product_id': 3,
                    'quantity': 1
                }
            ]
        }
        self.assertEqual(serializer.data, expected_data)
