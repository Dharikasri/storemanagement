from django.test import TestCase
from django.contrib.auth.models import User
from customer.models import Customer

class CustomerModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
    
    def create_customer(self, name, address, mobile):
        return Customer.objects.create(
            user=self.user,
            name=name,
            address=address,
            mobile=mobile
        )

    def test_create_customer(self):
        name = 'Brindha'
        address = 'Mandhaveli'
        mobile = 'xxxxxxxxxx'
        
        customer = self.create_customer(name, address, mobile)
        
        self.assertEqual(customer.name, name)
        self.assertEqual(customer.address, address)
        self.assertEqual(customer.mobile, mobile)
        self.assertEqual(customer.user, self.user)
    
    def test_customer_str(self):
        name = 'Brindha'
        address = 'Mandhaveli'
        mobile = 'xxxxxxxxxx'
        
        customer = self.create_customer(name, address, mobile)
        
        self.assertEqual(str(customer), name)
