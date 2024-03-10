

import pytest
from django.utils import timezone

from common.models import CustomUser, Destination


class TestDestinationModel:

    @pytest.mark.django_db
    def test_create_destination(self):
        id='ABC123',
        start_in='CityA',
        end_in='CityB',
        start_at=timezone.now(),
        costs=50.00
        
        Destination.objects.create(
            id=id,
            start_in=start_in,
            end_in=end_in,
            start_at=start_at,
            costs=costs,
        )
    
        assert Destination.objects.count() == 1


