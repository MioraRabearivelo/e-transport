

from django.urls import path

from .views import DestinationApiMixin, ListDriverView, CreateDriverView, UpdateDriverView, DeleteDriverView, UserRegistrationView,\
    UserLoginView, CreateReservationView, ListReservationView, UpdateResevationView, DeleteReservationView, CreateMessageView, \
    ListMessageView, DeleteMessageView, ListRegistrationView, UpdateRegistrationView, DeleteRegistrationView, CreateCarView, \
    UpdateCarView, ListCarView, DeleteCarView, CreatePackagesView, ListPackagesView, DeletePackagesView

urlpatterns = [
    path('destiantion/<str:pk>/detail', DestinationApiMixin.as_view()),
    path('destiantion/<str:pk>/update', DestinationApiMixin.as_view()),
    path('destiantion/<str:pk>/delete', DestinationApiMixin.as_view()),
    path('destiantion/list',   DestinationApiMixin.as_view()),
    path('destiantion/create',   DestinationApiMixin.as_view()),
    path('driver/list-drivers', ListDriverView.as_view()),
    path('driver/detail-driver/<str:pk>', ListDriverView.as_view(), name='detail-driver'),
    path('driver/create/', CreateDriverView.as_view()),
    path('driver/<str:pk>/update', UpdateDriverView.as_view()),
    path('driver/<str:pk>/delete', DeleteDriverView.as_view()),
    path('user/register', UserRegistrationView.as_view()),
    path('user/login', UserLoginView.as_view()),
    path('reservation/create', CreateReservationView.as_view()),
    path('reservation/list', ListReservationView.as_view()),
    path('reservation/<str:pk>/update', UpdateResevationView.as_view()),
    path('reservation/<str:pk>/delete', DeleteReservationView.as_view()),
    path('registration/list', ListRegistrationView.as_view()),
    path('registration/<str:pk>/update', UpdateRegistrationView.as_view()),
    path('registration/<str:pk>/delete', DeleteRegistrationView.as_view()),
    path('message/create/', CreateMessageView.as_view()),
    path('message/list', ListMessageView.as_view()),
    path('message/<str:pk>/delete', DeleteMessageView.as_view()),
    path('car/create', CreateCarView.as_view()),
    path('car/list', ListCarView.as_view()),
    path('car/<str:pk>/update', UpdateCarView.as_view()),
    path('car/<str:pk>/delete', DeleteCarView.as_view()),
    path('packages/create', CreatePackagesView.as_view()),
    path('packages/list', ListPackagesView.as_view()),
    path('packages/<str:pk>/delete', DeletePackagesView.as_view()),
]