from django.urls import path
from . import views

urlpatterns = [
    path('riders/create/', views.rider_create_view, name='rider-create'),
    path('riders/', views.rider_list_view, name='rider-list'),
    path('requesters/create/', views.requester_create_view, name='requester-create'),
    path('requesters/', views.requester_list_view, name='requester-list'),
]
