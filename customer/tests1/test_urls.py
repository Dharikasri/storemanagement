from django.test import SimpleTestCase
from django.urls import reverse, resolve
from customer.views import (
    customer_list,
    customer_detail,
    customer_create,
    customer_update,
    customer_delete,
)

class TestCustomerUrls(SimpleTestCase):

    def test_customer_list_url(self):
        url = reverse('customer_list')
        self.assertEqual(resolve(url).func, customer_list)

    def test_customer_detail_url(self):
        url = reverse('customer_detail', args=[1]) 
        self.assertEqual(resolve(url).func, customer_detail)

    def test_customer_create_url(self):
        url = reverse('customer_create')
        self.assertEqual(resolve(url).func, customer_create)

    def test_customer_update_url(self):
        url = reverse('customer_update', args=[1]) 
        self.assertEqual(resolve(url).func, customer_update)

    def test_customer_delete_url(self):
        url = reverse('customer_delete', args=[1])  
        self.assertEqual(resolve(url).func, customer_delete)
