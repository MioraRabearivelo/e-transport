

from rest_framework import serializers

from .models import Destination, Seats

class DestinationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destination
        fields = ['id', 'start_at', 'end_at', 'costs']
        
class SeatSerkializer(serializers.ModelField):
    
    class meta():
        model = Seats
        fields = ['seats_total', 'seats_used', 'seats_free']