from django.urls import path
from .views import *

urlpatterns = [
    path('create_demo/',employee_creation_view,name='create_demo'),
    path('create/',em_create,name='create'),   
    path('list/',em_list,name='list'),   
]