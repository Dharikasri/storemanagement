from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'address', 'mobile', 'created_at')
    search_fields = ('name', 'mobile')
    list_filter = ('created_at',)

admin.site.register(Customer, CustomerAdmin)
