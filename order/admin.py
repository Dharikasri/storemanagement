# order/admin.py
from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'order_date', 'customer')
    inlines = [OrderProductInline]

admin.site.register(Order, OrderAdmin)
