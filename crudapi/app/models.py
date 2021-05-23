from django.db import models
from twilio.rest import Client
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

class Score(models.Model):
    result = models.PositiveIntegerField()
    def __str__(self):
        return str(self.result)

    def save(self, *args , **kwargs):
        if self.result < 70:
            account_sid = 'account_sid'
            auth_token = 'auth_token'
            client = Client(account_sid , auth_token)

            message = client.messages \
                .create(
                     body=f'Hi test message from pytho .The result - {self.result}',
                     from_='+18566198893',
                     to='+91 '
                 )
            print(message.sid)
        return super().save(*args , **kwargs)
