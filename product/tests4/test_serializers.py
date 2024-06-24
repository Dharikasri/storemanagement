from datetime import date
from django.test import TestCase
from category.models import Category 
from product.models import Product
from product.serializers import ProductSerializer

class ProductSerializerTest(TestCase):
    
    def setUp(self):
        # Create a Category object for testing
        self.category = Category.objects.create(name='TestCategory')

    def test_product_serializer_valid(self):
        product_data = {
            'product_id': '1',
            'name': 'Test Product',
            'categories': [{'id': self.category.pk, 'name': self.category.name}],
            'description': 'This is a test product.',
            'expiry_date': date.today(),
            'price': '10.50',
        }
        serializer = ProductSerializer(data=product_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
