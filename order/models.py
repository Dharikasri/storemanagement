# order/models.py
import uuid
from django.db import models
from django.utils import timezone
from customer.models import Customer
from product.models import Product
from django.core.validators import MaxValueValidator

class Order(models.Model):
    order_no = models.CharField(max_length=100, unique=True, editable=False)
    order_date = models.DateField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    
    class Meta:
        ordering = ['-order_date']

    def save(self, *args, **kwargs):
        if not self.order_no:
            self.order_no = self.generate_unique_order_no()
        super().save(*args, **kwargs)

    def generate_unique_order_no(self):
        return str(uuid.uuid4())

    def __str__(self):
        return self.order_no 

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(20)])

    def __str__(self):
        return f"{self.product.name} (x{self.quantity}) in Order {self.order.order_no}"
