from datetime import date
from django.test import TestCase
from product.models import Product, Category  
from product.forms import ProductForm

class ProductFormTest(TestCase):
    
    def setUp(self):
        # Create a Category object for testing
        self.category = Category.objects.create(name='TestCategory')

    def test_product_form_valid(self):
        form_data = {
            'product_id': 1,
            'name': 'Test Product',
            'categories': [self.category.pk], 
            'description': 'This is a test product.',
            'expiry_date': date.today(),
            'price': 10.50,
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors.as_data())
