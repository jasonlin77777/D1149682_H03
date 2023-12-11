from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('courts/', views.court_members, name='courts'),
    path('courts/details/<int:id>', views.court_details, name='details_court'),
]