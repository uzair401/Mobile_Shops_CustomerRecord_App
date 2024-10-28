from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_admin = models.BooleanField(default=True)

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_father_name = models.CharField(max_length=255)
    customer_address = models.TextField()
    customer_phone_number_1 = models.CharField(max_length=15, unique=True)
    customer_phone_number_2 = models.CharField(max_length=15, blank=True, null=True)
    customer_cnic_number = models.CharField(max_length=15, unique=True)
    customer_cnic_front_image = models.ImageField(upload_to='cnic_front/')
    customer_cnic_back_image = models.ImageField(upload_to='cnic_back/')
    mobile_name = models.CharField(max_length=255)
    mobile_model = models.CharField(max_length=255)
    mobile_company = models.CharField(max_length=255)
    mobile_color = models.CharField(max_length=50)
    mobile_imei_1 = models.CharField(max_length=15, unique=True)
    mobile_imei_2 = models.CharField(max_length=15, blank=True, null=True)
    purchase_date = models.DateField(auto_now_add=True)
    purchase_time = models.TimeField(auto_now_add=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.customer_name
