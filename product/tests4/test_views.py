from django.test import TestCase
from django.urls import reverse
from datetime import date
from product.models import Product
from category.models import Category
from product.forms import ProductForm  

class AddProductViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='TestCategory')

    def test_add_product_post_valid(self):
        url = reverse('add_product')  
        product_data = {
            'product_id': '1',
            'name': 'Test Product',
            'categories': [self.category.pk],  
            'description': 'This is a test product.',
            'expiry_date': date.today(),
            'price': '10.50',
        }
        response = self.client.post(url, product_data)
        self.assertEqual(response.status_code, 302)  

    def test_add_product_post_invalid(self):
        url = reverse('add_product')
        invalid_product_data = {}
        response = self.client.post(url, invalid_product_data)
        self.assertEqual(response.status_code, 200)  

    def test_add_product_get(self):
        url = reverse('add_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'product/add_product.html') 
        

from django.test import TestCase
from django.urls import reverse
from datetime import date
from product.models import Product

class ProductListViewTest(TestCase):

    def setUp(self):
        # Create a few products for testing
        Product.objects.create(product_id='1', name='Product 1', price=10.0, description='Description for product 1', expiry_date=date.today())
        Product.objects.create(product_id='2', name='Product 2', price=20.0, description='Description for product 2', expiry_date=date.today())
        Product.objects.create(product_id='3', name='Product 3', price=30.0, description='Description for product 3', expiry_date=date.today())

    def test_product_list_get(self):
        url = reverse('product_list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_list.html')
        self.assertIn('products', response.context)
        self.assertEqual(len(response.context['products']), 3)
        

        actual_product_names = [product.name for product in response.context['products']]
        
    
        expected_product_names = ['Product 1', 'Product 2', 'Product 3']
        
    
        self.assertCountEqual(actual_product_names, expected_product_names)

