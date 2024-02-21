from django.urls import path
from .views import tiktok, details

urlpatterns = [
    path('', tiktok, name='tiktok_from'),
    path('details', details, name='tiktok_details'),
]