from django.test import TestCase
from django import forms
from order.forms import OrderForm
from customer.models import Customer
from product.models import Product
from order.models import Order, OrderProduct
from decimal import Decimal

class OrderFormTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='Test Customer')
        self.product = Product.objects.create(
            product_id=1,
            name='Test Product',
            description='Test Description',
            price=Decimal('100.00')
        )

    def test_valid_order_form(self):
        form_data = {
            'customer': self.customer.pk,
            'product': self.product.pk,
            'quantity': 5
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())
        order = form.save()

        self.assertEqual(order.customer, self.customer)
        order_product = OrderProduct.objects.get(order=order)
        self.assertEqual(order_product.product, self.product)
        self.assertEqual(order_product.quantity, 5)

    def test_invalid_order_form_no_customer(self):
        form_data = {
            'product': self.product.pk,
            'quantity': 5
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('customer', form.errors)

    def test_invalid_order_form_no_product(self):
        form_data = {
            'customer': self.customer.pk,
            'quantity': 5
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('product', form.errors)

    def test_invalid_order_form_quantity_out_of_range(self):
        form_data = {
            'customer': self.customer.pk,
            'product': self.product.pk,
            'quantity': 21  # Quantity out of the allowed range
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors)
