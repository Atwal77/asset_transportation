from django.urls import path
from . import views

urlpatterns = [
    path('riders/create/', views.rider_create_view, name='rider-create'),
    path('riders/', views.rider_list_view, name='rider-list'),
    path('requesters/create/', views.requester_create_view, name='requester-create'),
    path('requesters/', views.requester_list_view, name='requester-list'),
    path('riders/match/<str:email_id>', views.rider_match_list_view, name='rider-match-list'),
    path('riders/<int:rider_id>/', views.rider_details_view, name='rider-details'),
    path('transportation-requests/create/', views.create_transportation_request, name='create-transportation-request')
]
