

from django.urls import path

from .views import DestinationApiMixin, ListDriver, CreateDriver, UpdateDriver, DeleteDriver

urlpatterns = [
    path('destiantion/<str:pk>/detail',   DestinationApiMixin.as_view()),
    path('destiantion/<str:pk>/update',   DestinationApiMixin.as_view()),
    path('destiantion/<str:pk>/delete',   DestinationApiMixin.as_view()),
    path('destiantion/list/',   DestinationApiMixin.as_view()),
    path('destiantion/create/',   DestinationApiMixin.as_view()),
    path('driver/list-drivers/', ListDriver.as_view()),
    path('driver/detail-driver/<str:pk>/', ListDriver.as_view(), name='detail-driver'),
    path('driver/create/', CreateDriver.as_view()),
    path('driver/update/<str:pk>/', UpdateDriver.as_view()),
    path('driver/delete/<str:pk>/', DeleteDriver.as_view()),
]