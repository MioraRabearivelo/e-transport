

from django.urls import path

from .views import DestinationMixin

urlpatterns = [
    path('destinantion/', DestinationMixin.as_view(), name='destination'),
]