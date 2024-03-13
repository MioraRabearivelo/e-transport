

import uuid
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

User = settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    image = models.ImageField(upload_to='images/user/')

    def __str__(self):
        return self.user.username


class Destination(models.Model):
    id = models.CharField(primary_key=True, max_length=10, unique=True, editable=False)
    start_in = models.CharField(max_length=50, default="")
    end_in = models.CharField(max_length=50,default="")
    start_at = models.DateTimeField(auto_now_add=True)
    costs = models.DecimalField(max_digits=30, decimal_places=2, default=0.0)
    
    
    def __str__(self):
        return str(self.id)

   
class Message(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(default=0)
    message_content = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.message_content:
            raise ValidationError('message content is required')
        elif not self.contact:
            raise ValidationError('Contact field is required')
        elif not self.name:
            raise ValidationError('User name field is required')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_phone_number = models.IntegerField(primary_key=True, editable=True, unique=True)
    second_phone_number = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=150)
    cin = models.IntegerField(default=0)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    messages = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.second_phone_number == self.first_phone_number:
            raise ValidationError('The second phone number must be diffrent the first phone number')
        elif not self.second_phone_number:
            raise ValidationError('This fileds is required')
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
    id = models.CharField(primary_key=True, editable=False, max_length=15, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=250)
    phone_number = models.IntegerField(default=0, editable=True)
    image = models.ImageField(upload_to='images/driver/')
    
    def __str__(self):
        return self.first_name
    

class Car(models.Model):
    car_number = models.CharField(primary_key=True, editable=False, unique=True, max_length=15)
    destinations = models.ManyToManyField(Destination)
    drivers= models.ManyToManyField(Driver)
    chair_total = models.IntegerField(default=32)
    description = models.TextField(default="", null=True, blank=True)
    
    def __str__(self):
        return self.car_number
    

class Reservation(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bagages = models.ForeignKey(Bagages, on_delete=models.CASCADE, null=True, blank=True)
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
    bagages = models.ForeignKey(Bagages, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(id)
    
 

