from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email'] 

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()  

    class Meta:
        model = Customer
        fields = ['id', 'user', 'name', 'address', 'mobile', 'created_at']
