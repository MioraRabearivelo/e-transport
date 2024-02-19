

import uuid
from django.db import models
# from django.contrib.auth.models import AbstractUser


class Destination(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    start_at = models.CharField(max_length=50)
    end_at = models.CharField(max_length=50)
    costs = models.DecimalField(max_digits=15, decimal_places=2)


class Seats(models.Model):
    seats_total = models.IntegerField(default=32)
    seats_used = models.IntegerField(default=0)
    
    @property
    def seats_free(self):
        return self.seats_total - self.seat_free
    
    def __str__(self):
        return self.seats_total, self.seats_used, self.seats_free


class CustomerUser(models.Model):
    first_phone_number = models.IntegerField(primary_key=True, editable=True, unique=True)
    second_phone_number = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=150)
    cin = models.IntegerField(default=0)
    # seats = models.ManyToManyField(Seats)
    
    
    def save(self, *args, **kwargs):
        if self.second_phone_number == self.first_phone_number:
            return 'this fileds is required'
        elif self.second_phone_number == 0 or None:
            return 'null is not accepted'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.customer_name
    
    
class Bagages(models.Model):
    """
        When the weight of total bagages is set above 20kg,
        the customer gotta paid 1kg of all bagage to 500ar
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    customer = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, null=True)
    weigth = models.DecimalField(max_digits=5, decimal_places=2)
    costs = models.DecimalField(max_digits=15, decimal_places=2)
    bagage_name = models.CharField(max_length=50)
    descripion = models.TextField(null=True, blank=True)
    
    @property
    def get_weight(self):
        if self.weigth <= 20:
            self.costs = 0.0
        else:
            self.costs = self.weigth * 500 
        return self.costs 
    

            
class Driver(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=250)
    phone_number = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    

class Car(models.Model):
    car_number = models.CharField(primary_key=True, editable=True, unique=True, max_length=30)
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True)
    driver = models.ManyToManyField(Driver)
    seats = models.ManyToManyField(Seats)
    bagages = models.ManyToManyField(Bagages)
    customer = models.ManyToManyField(CustomerUser)
    
    
    