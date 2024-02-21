

from django.contrib import admin
from .models import CustomerUser, Destination, Seats, Bagages,\
    Driver, Car, Reservation, Validation, Payment

class CustomerUserAdmin(admin.ModelAdmin):
    model = CustomerUser
    ordering = ('first_phone_number',)
    search_fields = ('customer_name',)
    list_display = [
        'first_phone_number', 'second_phone_number',
        'customer_name',
    ]

admin.site.register(CustomerUser, CustomerUserAdmin)


class DestinationAdmin(admin.ModelAdmin):
    model = Destination
    ordering = ('id',)
    search_fields = ('end_at',)
    list_display = [
        'id', 'start_at','end_at','costs'
    ]

admin.site.register(Destination, DestinationAdmin)


class SeatsAdmin(admin.ModelAdmin):
    model = Seats
    ordering = ('seats_used',)
    search_fields = ('seats_used',)
    list_display = [
        'seats_used', 'seats_total', 'seats_free'
    ]

admin.site.register(Seats, SeatsAdmin)


class BagagesAdmin(admin.ModelAdmin):
    model = Bagages
    ordering = ('id',)
    search_fields = ('customer',)
    list_display = [
        'id', 'customer', 'weigth', 'costs', 'bagage_name', 'descripion'
    ]

admin.site.register(Bagages, BagagesAdmin)


class DriverAdmin(admin.ModelAdmin):
    model = Driver
    ordering = ('id',)
    search_fields = ('first_name',)
    list_display = [
        'id', 'first_name', 'last_name','phone_number', 
    ]

admin.site.register(Driver, DriverAdmin)


class CarAdmin(admin.ModelAdmin):
    model = Car
    ordering = ('car_number',)
    search_fields = ('car_number',)
    list_display = [
        'car_number', 'driver', 'destination', 'seats', 'bagages', 'customer'
    ]

admin.site.register(Car, CarAdmin)

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    ordering = ('id',)
    search_fields = ('customer',)
    list_display = [
        'id', 'customer', 'bagages', 'destination', 'customer', 
        'payment', 'car', 'created_at', 'updated_at'
    ]

admin.site.register(Reservation, ReservationAdmin)


class ValidationAdmin(admin.ModelAdmin):
    model = Validation
    ordering = ('id',)
    search_fields = ('customer',)
    list_display = [
        'id', 'reservation','car', 'seats', 'bagages', 'customer',
        'create_at', 'upated_at'
    ]

admin.site.register(Validation, ValidationAdmin)


class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    ordering = ('ref',)
    search_fields = ('payment_mode',)
    list_display = [
        'ref', 'payment_mode'
    ]

admin.site.register(Payment, PaymentAdmin)

