

from rest_framework import serializers

from .models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'start_at', 'end_at', 'costs']