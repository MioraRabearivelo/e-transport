

import pytest
from django.db import IntegrityError
from django.utils import timezone

from common.models import CustomUser, Destination, Customer, Message


class TestDestinationModel:

    @pytest.mark.django_db
    def test_create_destination(self):
        id = 'ABC123'
        start_in = 'CityA'
        end_in = 'CityB'
        start_at = timezone.now()
        costs = 50.00
        
        Destination.objects.create(
            id=id,
            start_in=start_in,
            end_in=end_in,
            start_at=start_at,
            costs=costs,
        )
    
        assert Destination.objects.count() == 1


class TestMessageModel:
    
    @pytest.mark.django_db
    def test_create_message(self):
        user_name = 'Same'
        user_contact =  21545
        message_content = 'Hello world'

        Message.objects.create(
            name=user_name,
            contact=user_contact,
            message_content=message_content,
        )
        
        assert Message.objects.count() == 1
    
    @pytest.mark.django_db
    def test_invalid_message(self):
        with pytest.raises(IntegrityError):
            Message.objects.create(
                name='Same',
                contact=545
            )