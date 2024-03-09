

from rest_framework import serializers

from .models import Destination,  Customer, Bagages, Driver,  \
    Reservation, Registration, Message, Car


class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        fields = ['id', 'start_at', 'end_at', 'costs']
        


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['first_phone_number', 'second_phone_number', 'customer_name', 'cin', 'seats']
        

class BagagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bagages
        fields = ['customer', 'weigth', 'costs', 'bagage_name', 'description']


class DriverSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'phone_number', 'image']
        

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['car_number', 'destination', 'driver',  'description', 'bagages', 'customer']


"""class Paymentserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = ['ref', 'payment_mode', 'status']
        """
        
class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fileds = ['customer', 'bagages', 'destination', 'car', 'created_at', 'updated_at']
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Registration
        fields = ['user_validator', 'reservation', 'customer', 'bagages', 'seats', 'car', 'create_at', 'upated_at']
        

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['name', 'contact', 'message_content']