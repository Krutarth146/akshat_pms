from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    salary = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name