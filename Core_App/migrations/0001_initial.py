# Generated by Django 5.1.2 on 2024-10-28 07:04

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_father_name', models.CharField(max_length=255)),
                ('customer_address', models.TextField()),
                ('customer_phone_number_1', models.CharField(max_length=15, unique=True)),
                ('customer_phone_number_2', models.CharField(blank=True, max_length=15, null=True)),
                ('customer_cnic_number', models.CharField(max_length=15, unique=True)),
                ('customer_cnic_front_image', models.ImageField(upload_to='cnic_front/')),
                ('customer_cnic_back_image', models.ImageField(upload_to='cnic_back/')),
                ('mobile_name', models.CharField(max_length=255)),
                ('mobile_model', models.CharField(max_length=255)),
                ('mobile_company', models.CharField(max_length=255)),
                ('mobile_color', models.CharField(max_length=50)),
                ('mobile_imei_1', models.CharField(max_length=15, unique=True)),
                ('mobile_imei_2', models.CharField(blank=True, max_length=15, null=True)),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('purchase_time', models.TimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core_App.customuser')),
            ],
        ),
    ]
