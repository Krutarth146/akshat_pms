from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('equipment/',equipment,name='equipment'),
    path('contact/',contact,name='contact'),
]