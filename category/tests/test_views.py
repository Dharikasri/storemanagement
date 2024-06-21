from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from category.models import Category
from category.serializers import CategorySerializer

class CategoryAPIViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.category1 = Category.objects.create(name='Test Category 1')
        self.category2 = Category.objects.create(name='Test Category 2')

    def test_category_list_create_api_view(self):
        url = reverse('category:category-list-create')
        response = self.client.get(url)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

        # Test creating a new category
        response = self.client.post(url, {'name': 'New Category'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Category.objects.filter(name='New Category').exists())

    def test_category_detail_api_view(self):
        url = reverse('category:category-detail', args=[self.category1.pk])
        response = self.client.get(url)
        serializer = CategorySerializer(self.category1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

        # Test updating the category
        response = self.client.put(url, {'name': 'Updated Category'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category1.refresh_from_db()
        self.assertEqual(self.category1.name, 'Updated Category')

        # Test deleting the category
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(pk=self.category1.pk).exists())

    def test_category_viewset_list(self):
        url = reverse('category:category-list')  # Using the default router name
        response = self.client.get(url)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_category_viewset_create(self):
        url = reverse('category:category-list')  # Using the default router name
        response = self.client.post(url, {'name': 'New Category'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Category.objects.filter(name='New Category').exists())

    def test_category_viewset_retrieve(self):
        url = reverse('category:category-detail', args=[self.category1.pk])  # Using the default router name
        response = self.client.get(url)
        serializer = CategorySerializer(self.category1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_category_viewset_update(self):
        url = reverse('category:category-detail', args=[self.category1.pk])  # Using the default router name
        response = self.client.put(url, {'name': 'Updated Category'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category1.refresh_from_db()
        self.assertEqual(self.category1.name, 'Updated Category')

    def test_category_viewset_delete(self):
        url = reverse('category:category-detail', args=[self.category1.pk])  # Using the default router name
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(pk=self.category1.pk).exists())
