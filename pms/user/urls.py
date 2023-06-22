from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',TrainerSignupView.as_view(),name='signup'),
]