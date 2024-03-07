

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Destination, Seats
from .serializer import DestinationSerializer, SeatSerializer 


class DestinationApiMixin(generics.GenericAPIView, 
        mixins.CreateModelMixin, 
        mixins.ListModelMixin, 
        mixins.UpdateModelMixin, 
        mixins.DestroyModelMixin, 
        mixins.RetrieveModelMixin):
    
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    lookup_field = 'id'
    
    def perform_create(self, serializer):
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
    
    
class ListSeatsAPiApi(generics.ListCreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class CreateSeats(generics.CreateAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        seats_total = serializer.validated_data.get('seats_total')
        if seats_total is None:
            raise ValueError("Seats total is required")
        serializer.save(seats_total=seats_total)
        

class UpdateSeatsApi(generics.UpdateAPIView):
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


