from decimal import Decimal
from django.test import TestCase
from django.utils import timezone
from product.models import Product
from category.models import Category

class ProductModelTestCase(TestCase):
    
    def setUp(self):
        # Set up initial categories for testing
        self.category1 = Category.objects.create(name="Electronics")
        self.category2 = Category.objects.create(name="Books")
    
    def test_create_product(self):
        product = Product.objects.create(
            product_id=1,
            name="Test Product",
            description="This is a test product.",
            expiry_date=timezone.now().date(),
            price=Decimal('99.99')
        )
        product.categories.set([self.category1, self.category2])
        
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "This is a test product.")
        self.assertEqual(product.price, Decimal('99.99'))
        self.assertEqual(product.categories.count(), 2)
        self.assertIn(self.category1, product.categories.all())
        self.assertIn(self.category2, product.categories.all())
    
    def test_default_price(self):
        product = Product.objects.create(
            product_id=2,
            name="Test Product Without Price",
            description="This product has no specified price."
        )
        
        self.assertEqual(product.price, Decimal('0.00'))
    
    def test_string_representation(self):
        product = Product.objects.create(
            product_id=3,
            name="String Representation Test",
            description="Testing string representation."
        )
        
        self.assertEqual(str(product), "String Representation Test")
