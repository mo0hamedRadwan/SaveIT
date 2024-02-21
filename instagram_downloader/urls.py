from django.urls import path
from .views import instagram, details

urlpatterns = [
    path('', instagram, name='instagram_from'),
    path('details', details, name='instagram_details'),
]