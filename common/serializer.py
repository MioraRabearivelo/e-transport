

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Destination,  Customer, Bagages, Driver,  \
    Reservation, Registration, Message, Car, CustomUser


class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password', 'confirm_password',  'image')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs 

    def create(self, validated_data):
        user = CustomUser.objects.create(
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
        fields = ['id', 'start_in', 'start_at', 'end_in', 'costs']     


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['first_phone_number', 'second_phone_number', 'customer_name', 'cin', 'seats']
        

class BagagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bagages
        fields = ['customer', 'weigth', 'costs', 'bagage_name', 'description']


class DriverSerializer(serializers.ModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(view_name='detail-driver', lookup_field='id')
    
    class Meta:
        model = Driver
        fields = ['id', 'url', 'first_name', 'last_name', 'phone_number', 'image']


class CarSerializer(serializers.ModelSerializer):
    
    drivers = DriverSerializer(many=True, read_only=True)
    description = serializers.HyperlinkedIdentityField(view_name='detail-car' , read_only=True)
    
    class Meta:
        model = Car
        fields = ['car_number', 'destinations', 'drivers',  'description', 'bagages', 'customer']
        

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