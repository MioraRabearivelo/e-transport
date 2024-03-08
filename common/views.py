

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Destination, Seats, Driver, Reservation, Registration
from .serializer import DestinationSerializer, SeatSerializer, DriverSerializer, ReservationSerializer,\
    RegistrationSerializer


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
            raise ValueError("Start date fields is required")
        serializer.save()
            
    def perform_update(self, serializer):
        start_date = serializer.validated_data.get('start_date')
        end_date =  serializer.validated_data.get('end_date')
        costs =  serializer.validated_data.get('costs')
        if start_date is None:
            raise ValueError("Start date fields is required")
        elif end_date is None:
            raise ValueError("End date fields is required")
        elif costs is None:
            raise ValueError("Cost fields is required")
        else:
            serializer.save()
            
    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)
    
    
class ListSeats(generics.ListCreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(*args, **kwargs)
    
    
class CreateSeats(generics.CreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        seats_total = serializer.validated_data.get('seats_total')
        if seats_total is None:
            raise ValueError("Seats total is required")
        serializer.save(seats_total=seats_total)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  
    
    
class UpdateSeats(generics.UpdateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        seats_total = serializer.validated_data.get('seats_total')
        seats_choices = serializer.validated_data.get('seats_choices')
        if seats_total  or seats_choices is None:
            raise ValueError("Seats total is required")
        serializer.save()
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


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
            raise ValueError("All fields is required") 
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
    

class ListDriver(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(*args, **kwargs)
    
    
class UpdateDriver(generics.ListCreateAPIView):
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
            raise ValueError("All fields is required") 
        serializer.save()
        
    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)
    
    
class ListReservation(generics.ListCreateAPIView):
    queryset = Reservation.objecty.all() 
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field =['id']
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(*args, **kwargs)
    

class CreateReservation(generics.CreateAPIView):
    queryset = Reservation.objecty.all() 
    serializer_class = ReservationSerializer
    lookup_field =['id']
    
    def perform_create(self, serializer):
        customer = serializer.validated_data.get('customer')
        destination = serializer.validated_data.get('destination')

        if customer or destination  is None:
            raise ValueError("All fields is required") 
        serializer.save()
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class UpdateResevation(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class =ReservationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']
    
    def perform_update(self, serializer):
        customer = serializer.validated_data.get('customer')
        destination = serializer.validated_data.get('destination')
        
        if customer or destination  is None:
            raise ValueError("All fields is required") 
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
    

class ListRegistration(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['id']
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.pk)
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(*args, **kwargs)
    
    
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
    
    
    