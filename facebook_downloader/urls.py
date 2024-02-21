from django.urls import path
from .views import facebook, details

urlpatterns = [
    path('', facebook, name='facebook_from'),
    path('details', details, name='facebook_details'),
]