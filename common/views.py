

from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login

from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import Destination, Driver, Reservation, Registration, Message, Car
from .serializer import DestinationSerializer,  DriverSerializer, ReservationSerializer,\
    RegistrationSerializer, MessageSerializer, CarSerializer, AccountSerializer
    

class UserRegistration(APIView):
    
    permission_classes = [IsAdminUser]
    
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            return serializer.save()
        return ValidationError('An error occured during registration')


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  
                token = Token.objects.create(user=user)
            return Response({'token': token.key, 'username': user.username})
        else:
            return Response({'message': 'Invalid username or password'})


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.headers) 
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()

        return Response({'detail': 'Successfully logged out.'})


class DestinationApiMixin(generics.GenericAPIView, 
        mixins.CreateModelMixin, 
        mixins.ListModelMixin, 
        mixins.UpdateModelMixin, 
        mixins.DestroyModelMixin, 
        mixins.RetrieveModelMixin):
    
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    lookup_field = ['id']
    
    def perform_create(self, serializer):
        start_date = serializer.validated_data.get('start_date')
        end_date =  serializer.validated_data.get('end_date')
        costs =  serializer.validated_data.get('costs')
        if start_date or end_date or costs is None:
            raise ValidationError("Start date fields is required")
        serializer.save()
            
    def perform_update(self, serializer):
        start_date = serializer.validated_data.get('start_date')
        end_date =  serializer.validated_data.get('end_date')
        costs =  serializer.validated_data.get('costs')
        if start_date is None:
            raise ValidationError("Start date fields is required")
        elif end_date is None:
            raise ValidationError("End date fields is required")
        elif costs is None:
            raise ValidationError("Cost fields is required")
        else:
            serializer.save()
            
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)
    
    
class CreateDriver(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAdminUser]
    
    def perform_create(self, serializer):
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        phone_number = serializer.validated_data.get('phone_number')
        image = serializer.validated_data.get('image')
        
        if first_name or last_name or phone_number or image is None:
            raise ValidationError("All fields is required") 
        serializer.save()
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class DeleteDriver(generics.DestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAdminUser]
    lookup_field = ['id']
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class ListDriver(generics.ListCreateAPIView, generics.RetrieveAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    
class UpdateDriver(generics.UpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAdminUser]
    lookup_field = ['id']
    
    def perform_update(self, serializer):
        first_name = serializer.validated_data.get('first_name')
        last_name = serializer.validated_data.get('last_name')
        phone_number = serializer.validated_data.get('phone_number')
        image = serializer.validated_data.get('image')
        
        if first_name or last_name or phone_number or image is None:
            raise ValidationError("All fields is required") 
        serializer.save()
        
    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)
    
    
class ListReservation(generics.ListCreateAPIView, generics.RetrieveAPIView):
    queryset = Reservation.objects.all() 
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field =['id']
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    

class CreateReservation(generics.CreateAPIView):
    queryset = Reservation.objects.all() 
    serializer_class = ReservationSerializer
    lookup_field =['id']
    
    def perform_create(self, serializer):
        customer = serializer.validated_data.get('customer')
        destination = serializer.validated_data.get('destination')

        if customer or destination  is None:
            raise ValidationError("All fields is required") 
        serializer.save()
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class UpdateResevation(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class =ReservationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']
    
    def perform_update(self, serializer):
        customer = serializer.validated_data.get('customer')
        destination = serializer.validated_data.get('destination')
        
        if customer or destination  is None:
            raise ValidationError("All fields is required") 
        serializer.save()
        
    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)
    

class DeleteReservation(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class ListRegistration(generics.ListCreateAPIView, generics.RetrieveAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    
class UpdateRegistration(generics.UpdateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']
    
    def perform_update(self, serializer):
        user_validator = serializer.validated_data.get('user_validator')
        reservation = serializer.validated_data.get('reservation')
        bagages = serializer.validated_data.get('bagages')
        
        if user_validator or reservation or bagages is None:
            raise ValueError("All fields is required") 
        serializer.save()
        
    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)


class DeleteRegistration(generics.DestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class CreateMessage(generics.CreateAPIView):
    queryset = Message.objects.all() 
    serializer_class =MessageSerializer
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        contact = serializer.validated_data.get('contact')
        message_content = serializer.validated_data.get('message_content')

        if name or contact or  message_content is None:
            raise ValueError("All fields is required") 
        serializer.save()
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class ListMessage(generics.ListCreateAPIView, generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


class DeleteMessage(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class =MessageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class ListCar(generics.ListCreateAPIView, generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = ['id']

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


class CreateCar(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        car_number = serializer.validated_data.get('car_number')
        seats = serializer.validated_data.get('seats')
        description = serializer.validated_data.get('description')

        if car_number or seats or  description is None:
            raise ValueError("All fields is required") 
        serializer.save()
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class DeleteCar(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser]
    lookup_field = ['id']

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
class UpdateCar(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']
    
    def perform_update(self, serializer):
        car_number = serializer.validated_data.get('car_number')
        destination = serializer.validated_data.get('destination')
        
        if car_number or destination is None:
            raise ValueError("All fields is required") 
        serializer.save()
        
    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)