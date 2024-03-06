

from django.urls import path

from .views import DestinationMixin

urlpatterns = [
    path('destiantion/<str:pk>/detail',   DestinationMixin.as_view()),
    path('destiantion/<str:pk>/update',   DestinationMixin.as_view()),
    path('destiantion/<str:pk>/delete',   DestinationMixin.as_view()),
    path('destiantion/list/',   DestinationMixin.as_view()),
    path('destiantion/create/',   DestinationMixin.as_view()),
]