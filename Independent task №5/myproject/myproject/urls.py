
from django.urls import path

from first_app.views import *

urlpatterns = [
    path('', table, name='home'),
    ]

