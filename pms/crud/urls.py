from django.urls import path
from .views import *

urlpatterns = [
    path('create/',employee_creation_view,name='create'),
    
]