from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class DashboardViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user.is_staff = True
        self.user.is_superuser = True  # Set the user as superuser if required
        self.user.save()
        login_successful = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login_successful)

    def test_dashboard_view(self):
        url = reverse('dashboard:dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) 

    def test_accounts_view(self):
        url = reverse('dashboard:accounts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  

    def test_login_view(self):
        url = reverse('dashboard:login_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  

    def test_add_order_view(self):
        url = reverse('order:add_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) 

    def test_order_list_view(self):
        url = reverse('order:order_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) 

    def test_admin_dashboard_view(self):
        url = reverse('dashboard:admin_dashboard')
        response = self.client.get(url)
        if response.status_code == 302:
            print(f"Redirection to: {response['Location']}")
        self.assertEqual(response.status_code, 200)
