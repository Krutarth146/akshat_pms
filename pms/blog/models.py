from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'


class Account(models.Model):
    type = models.CharField(max_length=10)
    no = models.IntegerField()

    def __str__(self):
        return str(self.no)

    class Meta:
        db_table = 'Account'

class User(Account):
    uname = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.uname
    
    class Meta:
        db_table = 'User'


class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'author'

class Books(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    bname = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        return self.bname
    
    class Meta:
        db_table = 'books'


category = (('Primary', 'primary'), ('Secondary', 'secondary'))
class Product(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    category = models.CharField(max_length=20, choices=category)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'


class Cart(models.Model):
    name = models.ManyToManyField(Product)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.total)
    
    class Meta:
        db_table = 'cart'

# Question, Choices (Use Foreign Key)


