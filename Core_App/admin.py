from django.contrib import admin
from .models import CustomUser, Customer

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_admin')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_father_name', 'customer_cnic_number', 'mobile_name', 'purchase_date')
    search_fields = ('customer_name', 'customer_cnic_number', 'mobile_name')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Customer, CustomerAdmin)
