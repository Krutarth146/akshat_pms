from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    mobile = models.CharField(max_length=10,blank=True)   # for client
    diet_plan = models.CharField(max_length=100,blank=True)  # for Tariner


class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    class Meta:
        db_table = 'client'

class Trainer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    class Meta:
        db_table = 'trainer'


class Electronics(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to='uploads/')

    class Meta:
        db_table = 'electronics'
        