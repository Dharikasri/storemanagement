# tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from order.models import Order
from customer.models import Customer

class OrderURLsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name="Test Customer")  # Ensure Customer model has a 'name' field
        self.order = Order.objects.create(customer=self.customer)  # Ensure Order model has a 'customer' field

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

    def test_order_api_detail_url(self):
        url = reverse('order:order-detail', args=[self.order.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
