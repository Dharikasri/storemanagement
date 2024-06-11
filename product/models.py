from decimal import Decimal
from django.db import models
from category.models import Category

class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, related_name='products')
    description = models.TextField()
    expiry_date = models.DateField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name
