from django.urls import path
from .views import *

urlpatterns = [
    path('create/',CreatePost.as_view(), name='create'),
    path('list/',ListAllPost.as_view(), name='list')
]