from django.test import TestCase
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from category.models import Category
from category.serializers import CategorySerializer
from io import BytesIO

class CategorySerializerTest(TestCase):
    def setUp(self):
        self.parent_category = Category.objects.create(name='Parent Category')
        self.subcategory1 = Category.objects.create(name='Subcategory 1', parent=self.parent_category)
        self.subcategory2 = Category.objects.create(name='Subcategory 2', parent=self.parent_category)
    
    def test_category_serializer(self):
        serializer = CategorySerializer(self.parent_category)
        json_data = JSONRenderer().render(serializer.data)
        
    
        stream = BytesIO(json_data)
        data = JSONParser().parse(stream)
        
        expected_data = {
            'id': self.parent_category.pk,
            'name': self.parent_category.name,
            'parent': self.parent_category.parent,  
            'subcategories': [self.subcategory1.pk, self.subcategory2.pk]
        }
        
        self.assertEqual(data, expected_data)
