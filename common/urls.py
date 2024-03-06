

from django.urls import path

from .views import DestinationMixin

urlpatterns = [
    path('destination/', DestinationMixin.as_view(), name='destination'),
]