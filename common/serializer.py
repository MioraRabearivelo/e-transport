

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Destination,  Customer, Bagages, Driver,  \
    Reservation, Registration, Message, Car, User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'image')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs 

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


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