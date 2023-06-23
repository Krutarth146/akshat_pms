from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/',TrainerSignupView.as_view(),name='signup'),
    path('signupc/',ClientSignupView.as_view(),name='signupc'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]