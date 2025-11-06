
from django.urls import path
from firstapp.views import *

urlpatterns = [
    path('', popular_singers, name='home'),
    path('singer/',singer_card),
]
