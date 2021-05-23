from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100 , blank=True)
    author = models.CharField(max_length=100 , blank=True)
    isbn = models.CharField(max_length=100 , blank=True)
    pubhlisher = models.CharField(max_length=100 , blank=True)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=20)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length= 15)



