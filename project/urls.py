
# configuration for  project urls 
from django.urls import path
from .models import *

urlpatterns = [
    path('', home , name="home" ),
]
