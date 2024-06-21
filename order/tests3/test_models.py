from django.test import TestCase
from customer.models import Customer
from product.models import Product
from order.models import Order, OrderProduct
from decimal import Decimal

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Test Customer')
        self.product1 = Product.objects.create(
            product_id=1,
            name='Test Product 1',
            description='Description 1',
            price=Decimal('100.00')
        )
        self.product2 = Product.objects.create(
            product_id=2,
            name='Test Product 2',
            description='Description 2',
            price=Decimal('200.00')
        )

    def test_create_order(self):
        order = Order.objects.create(customer=self.customer)
        self.assertIsNotNone(order.order_no)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(str(order), order.order_no)

    def test_add_products_to_order(self):
        order = Order.objects.create(customer=self.customer)
        order_product1 = OrderProduct.objects.create(order=order, product=self.product1, quantity=2)
        order_product2 = OrderProduct.objects.create(order=order, product=self.product2, quantity=1)

        self.assertEqual(order.products.count(), 2)
        self.assertIn(order_product1, OrderProduct.objects.filter(order=order))
        self.assertIn(order_product2, OrderProduct.objects.filter(order=order))
        self.assertEqual(order_product1.quantity, 2)
        self.assertEqual(order_product2.quantity, 1)
        self.assertEqual(str(order_product1), f"{self.product1.name} (x2) in Order {order.order_no}")
        self.assertEqual(str(order_product2), f"{self.product2.name} (x1) in Order {order.order_no}")
