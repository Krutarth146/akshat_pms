from django.urls import path
from . import views

urlpatterns = [
    path('first/',views.simple),
    path('aboutus/',views.aboutus),
    path('data/',views.data),
    path('contactus/',views.contactus),
    path('learnfor/',views.learnforloop),
    path('getdata/',views.getAllData),
    path('createorm/',views.createOrm),
    path('deleteorm/',views.deleteRecord),
    path('updateorm/',views.updateRecord),
]
