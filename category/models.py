from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",  
        related_name="subcategories",  
        on_delete=models.CASCADE,  
        blank=True,  
        null=True,   
    )

    def __str__(self):
        return self.name
    
