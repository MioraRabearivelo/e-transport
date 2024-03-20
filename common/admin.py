

from django.contrib import admin
from .models import CustomUser, Customer, Destination, Bagages,\
    Driver, Car, Reservation, Registration, Message
    
    
class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    ordering = ('user',)
    search_fields = ('user',)
    list_display = [
        'user', 'phone_number','image'
    ]

admin.site.register(CustomUser, UserAdmin)


class CustomerUserAdmin(admin.ModelAdmin):
    model = Customer
    ordering = ('first_phone_number',)
    search_fields = ('customer_name',)
    list_display = [
        'first_phone_number', 'second_phone_number', 'customer_name', 'cin', 'destination', 'messages'
    ]
    
admin.site.register(Customer, CustomerUserAdmin)


class DestinationAdmin(admin.ModelAdmin):
    model = Destination
    ordering = ('id',)
    search_fields = ('end_at',)
    list_display = [
        'id', 'start_at', 'end_in', 'start_in', 'costs'
    ]

admin.site.register(Destination, DestinationAdmin)


class BagagesAdmin(admin.ModelAdmin):
    model = Bagages
    ordering = ('id',)
    search_fields = ('customer',)
    list_display = [
        'id', 'customer', 'weigth', 'costs', 'bagage_name', 'description'
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
        'car_number', 'chair_total', 'description'
    ]

admin.site.register(Car, CarAdmin)


class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    ordering = ('customer',)
    search_fields = ('customer',)
    list_display = [
        'id', 'customer', 'bagages', 'destination',
        'car', 'created_at', 'updated_at'
    ]

admin.site.register(Reservation, ReservationAdmin)


class RegistrationAdmin(admin.ModelAdmin):
    model = Registration
    ordering = ('id',)
    search_fields = ('customer',)
    list_display = [
        'id', 'reservation','car', 'bagages', 'user_validator',
        'create_at', 'upated_at'
    ]

admin.site.register(Registration,RegistrationAdmin)


class MessageAdmin(admin.ModelAdmin):
    model = Message
    ordering = ('name',)
    search = ('name',)
    list_display = ['name', 'contact', 'message_content']
admin.site.register(Message, MessageAdmin)