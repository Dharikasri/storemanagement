from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from category.models import Category

class CategoryViewsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.category1 = Category.objects.create(name='Test Category 1')
        self.category2 = Category.objects.create(name='Test Category 2')

    def test_category_viewset_api(self):
        url = reverse('category:category-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
