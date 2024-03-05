

from rest_framework import serializers

from .models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    start_at = serializers.DateTimeField(format="%d/%b/%Y")
    end_at  = serializers.DateTimeField(format="%d/%b/%Y")
    costs = serializers.DecimalField(max_digits=15, decimal_places=2)
    class Meta:
        model = Destination
        fields = ['id', 'start_at', 'end_at', 'costs']