from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Book , Employee

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'