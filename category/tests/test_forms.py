from django.test import TestCase
from category.forms import categoryForm
from category.models import Category

class CategoryFormTestCase(TestCase):
    
    def test_category_form_with_parent(self):
        parent_category = Category.objects.create(name='Parent Category')
        form_data = {
            'name': 'Child Category',
            'parent': parent_category.pk  
        }
        form =categoryForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        category = form.save()
        self.assertEqual(category.name, 'Child Category')
        self.assertEqual(category.parent, parent_category)
