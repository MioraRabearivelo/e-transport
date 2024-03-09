

import json
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    pseudo = models.CharField(primary_key=True, editable=True, unique=True, max_length=50)
    phone_number = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/user/')
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["pseudo", "first_name", "last_name", "image", "phone_number"]
    
    def __str__(self) :
        return self.pseudo
    

class Destination(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False)
    start_in = models.CharField(max_length=50, default="")
    end_in = models.CharField(max_length=50,default="")
    start_at = models.DateTimeField()
    costs = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    
    
    def __str__(self):
        return str(self.id)


   
class Message(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(default=0)
    message_content = models.TextField()
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    first_phone_number = models.IntegerField(primary_key=True, editable=True, unique=True)
    second_phone_number = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=150)
    cin = models.IntegerField(default=0)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.second_phone_number == self.first_phone_number:
            return 'The second phone number must be diffrent the first phone number'
        elif self.second_phone_number == 0 or None:
            return 'This fileds is required'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.first_phone_number)
    
    
class Bagages(models.Model):
    """
        When the weight of total bagages is set above 20kg,
        the customer gotta paid 1kg of each bagage to 500
    """
    id = models.UUIDField(primary_key=True, editable=False, unique=True, max_length=6, default=uuid.uuid4)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    weigth = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    costs = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    bagage_name = models.CharField(max_length=50, default="")
    description = models.TextField(null=True, blank=True, default="")
    
    @property
    def get_weight(self):
        if self.weigth <= 20:
            self.costs = 0.0
        else:
            self.costs = self.weigth * 500 
        return self.costs 
    
    def __str__(self):
        return str(self.id)
    
    
class Driver(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, max_length=6, unique=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=250)
    phone_number = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/driver/')
    
    def __str__(self):
        return self.first_name
    

class Car(models.Model):
    car_number = models.CharField(primary_key=True, editable=True, unique=True, max_length=30)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    seats_total = models.IntegerField(default=32)
    description = models.TextField(default="", null=True, blank=True)
    
    def __str__(self):
        return self.car_number
    

"""class Payment(models.Model):
    ref = models.CharField(primary_key=True, editable=False, max_length=100)
    payment_mode = models.CharField(max_length=30, default="")
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.ref)
"""

class Reservation(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bagages = models.ForeignKey(Bagages, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return str(self.customer)
    
    
class Registration(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, unique=True)
    user_validator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bagages = models.ForeignKey(Bagages, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.customer)
    
 

