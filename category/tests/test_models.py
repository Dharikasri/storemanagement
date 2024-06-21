from django.test import TestCase
from category.models import Category

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Category 1")
        self.category2 = Category.objects.create(name="Category 2")
        self.category3 = Category.objects.create(name="Category 3", parent=self.category1)

    def test_category_creation(self):
        self.assertEqual(self.category1.name, "Category 1")
        self.assertEqual(self.category2.name, "Category 2")
        self.assertEqual(self.category3.name, "Category 3")

    def test_subcategories(self):
        self.assertTrue(self.category3.parent == self.category1)
