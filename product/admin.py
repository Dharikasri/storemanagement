from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'price', 'expiry_date')
    search_fields = ('name', 'product_id')
    list_filter = ('expiry_date', 'categories')
    filter_horizontal = ('categories',)
    ordering = ('-expiry_date',)
    
admin.site.register(Product, ProductAdmin)
