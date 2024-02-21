from django.urls import path
from .views import youtube, details

urlpatterns = [
    path('', youtube, name='youtube_from'),
    path('details', details, name='youtube_details'),
]