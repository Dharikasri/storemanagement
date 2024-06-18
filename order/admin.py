from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1  # Number of empty forms to display

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'order_date', 'customer')  # Fields to display in the admin list view
    inlines = [OrderProductInline]  # Inline for adding products to an order

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
