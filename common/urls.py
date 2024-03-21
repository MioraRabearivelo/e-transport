

from django.urls import path

from .views import DestinationApiMixin, ListDriver, CreateDriver, UpdateDriver, DeleteDriver, UserRegistration,\
    UserLoginView, CreateReservation, ListReservation, UpdateResevation, DeleteReservation, CreateMessage, \
    ListMessage, DeleteMessage, ListRegistration, UpdateRegistration, DeleteRegistration

urlpatterns = [
    path('destiantion/<str:pk>/detail',   DestinationApiMixin.as_view()),
    path('destiantion/<str:pk>/update',   DestinationApiMixin.as_view()),
    path('destiantion/<str:pk>/delete',   DestinationApiMixin.as_view()),
    path('destiantion/list',   DestinationApiMixin.as_view()),
    path('destiantion/create',   DestinationApiMixin.as_view()),
    path('driver/list-drivers', ListDriver.as_view()),
    path('driver/detail-driver/<str:pk>', ListDriver.as_view(), name='detail-driver'),
    path('driver/create/', CreateDriver.as_view()),
    path('driver/<str:pk>/update', UpdateDriver.as_view()),
    path('driver/<str:pk>/delete', DeleteDriver.as_view()),
    path('user/register', UserRegistration.as_view()),
    path('user/login', UserLoginView.as_view()),
    path('reservation/create', CreateReservation.as_view()),
    path('reservation/list', ListReservation.as_view()),
    path('reservation/<str:pk>/update', UpdateResevation.as_view()),
    path('reservation/<str:pk>/delete', DeleteReservation.as_view()),
    path('registration/list', ListRegistration.as_view()),
    path('registration/<str:pk>/update', UpdateRegistration.as_view()),
    path('registration/<str:pk>/delete', DeleteRegistration.as_view()),
     path('message/create/', CreateMessage.as_view()),
    path('message/list', ListMessage.as_view()),
    path('message/<str:pk>/delete', DeleteMessage.as_view()),
]