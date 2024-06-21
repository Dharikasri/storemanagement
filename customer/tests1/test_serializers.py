from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from customer.models import Customer
from customer.serializers import CustomerSerializer

class CustomerSerializerTestCase(APITestCase):
    def setUp(self):
        # Create a User object
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        
        # Create a Customer object associated with the User
        self.customer = Customer.objects.create(user=self.user, name='Brindha', address='Madhaveli', mobile='xxxxxxxxxx')
        
    def test_customer_serializer(self):
        serializer = CustomerSerializer(instance=self.customer)
        expected_fields = ['id', 'user', 'name', 'address', 'mobile', 'created_at']
        
        # Check if all fields are present in serialized data
        for field in expected_fields:
            self.assertIn(field, serializer.data)
        
        # Check specific values
        self.assertEqual(serializer.data['name'], 'Brindha')
        self.assertEqual(serializer.data['address'], 'Madhaveli')
        self.assertEqual(serializer.data['mobile'], 'xxxxxxxxxx')
        
        # Check nested UserSerializer data
        self.assertEqual(serializer.data['user']['username'], 'testuser')
        self.assertEqual(serializer.data['user']['email'], 'test@example.com')
