from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from customer.models import Customer 


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customer = Customer.objects.create(user=self.user, name='Test Customer', address='Test Address', mobile='1234567890')
        self.admin_group = Group.objects.create(name='admin')
        self.admin_user = User.objects.create_user(username='adminuser', password='adminpassword')
        self.admin_user.groups.add(self.admin_group)

    def test_login_view(self):
        url = reverse('dashboard:login_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  


        login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(url, login_data)
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('dashboard:dashboard')) 

        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        self.client.force_login(self.user)
        url = reverse('dashboard:logout')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('dashboard:login_view'))  

       
        self.assertFalse(response.wsgi_request.user.is_authenticated)

  

