from django import forms
from .models import CustomUser, Customer

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'customer_name', 'customer_father_name', 'customer_address', 
            'customer_phone_number_1', 'customer_phone_number_2', 
            'customer_cnic_number', 'customer_cnic_front_image', 
            'customer_cnic_back_image', 'mobile_name', 
            'mobile_model', 'mobile_company', 'mobile_color', 
            'mobile_imei_1', 'mobile_imei_2'
        ]
