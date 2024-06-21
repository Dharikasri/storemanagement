from django.test import TestCase
from django.contrib.auth.models import User
from customer.forms import CustomerForm
from customer.models import Customer

class CustomerFormTest(TestCase):

    def setUp(self):
        # Create a User instance
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_customer_form_valid(self):
        # Create data to be used in the form
        form_data = {
            'name': 'Brindha',
            'address': 'Madhaveli',
            'mobile': 'xxxxxxxxxx'
        }
        
        form = CustomerForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_customer_form_save(self):
        form_data = {
            'name': 'Brindha',
            'address': 'Madhaveli',
            'mobile': 'xxxxxxxxxx'
        }
        
        form = CustomerForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        # Save the form data
        customer = form.save(commit=False)
        customer.user = self.user  # Assign the user to the customer
        customer.save()
        
        # Retrieve the saved customer object from the database
        saved_customer = Customer.objects.get(id=customer.id)
        
        # Check if the saved data matches the form data
        self.assertEqual(saved_customer.name, form_data['name'])
        self.assertEqual(saved_customer.address, form_data['address'])
        self.assertEqual(saved_customer.mobile, form_data['mobile'])
        self.assertEqual(saved_customer.user, self.user)
