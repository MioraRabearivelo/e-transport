

from django.urls import path

from .views import DestinationApiMixin, ListDriver

urlpatterns = [
    path('destiantion/<str:pk>/detail',   DestinationApiMixin.as_view()),
    path('destiantion/<str:pk>/update',   DestinationApiMixin.as_view()),
    path('destiantion/<str:pk>/delete',   DestinationApiMixin.as_view()),
    path('destiantion/list/',   DestinationApiMixin.as_view()),
    path('destiantion/create/',   DestinationApiMixin.as_view()),
    path('driver/list_drivers/', ListDriver.as_view())
]