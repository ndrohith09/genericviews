from .serializers import BookSerializer
from django.shortcuts import render
from rest_framework import generics , viewsets
from .models import Book , Employee
from .serializers import BookSerializer , EmployeeSerializer
# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book
    serializer_class = BookSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer