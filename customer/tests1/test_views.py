from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from customer.models import Customer
from customer.serializers import CustomerSerializer

class CustomerViewSetTestCase(APITestCase):
    def setUp(self):
  
        self.customer1 = Customer.objects.create(name='Rahul Sharma', address='Kodambakkam', mobile='xxxxxxxxxx')
        self.customer2 = Customer.objects.create(name='Priya Singh', address='Nungambakkam', mobile='xxxxxxxxxx')
        
        self.invalid_payload = {
            'name': '',  
            'address': 'T. Nagar',
            'mobile': 'xxxxxxxxxx'
        }
    
    def test_list_customers(self):
        url = reverse('customer-list')  
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Customer.objects.count())
    
    def test_retrieve_customer(self):
        url = reverse('customer-detail', args=[self.customer1.pk])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.customer1.name)
    
    def test_create_invalid_customer(self):
        url = reverse('customer-list')
        response = self.client.post(url, self.invalid_payload, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
   
        self.assertIn('name', response.data)  
    
    def test_update_customer(self):
        url = reverse('customer-detail', args=[self.customer1.pk])
        response = self.client.put(url, self.invalid_payload, format='json')  
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
       
        self.customer1.refresh_from_db()
        self.assertNotEqual(self.customer1.name, '')  
    
    def test_delete_customer(self):
        url = reverse('customer-detail', args=[self.customer1.pk])
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Customer.objects.filter(pk=self.customer1.pk).exists())

