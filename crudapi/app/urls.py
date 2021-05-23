from django.urls import path , include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee' , EmployeeViewSet)
#router.register('books' , BookList)

urlpatterns = [
    path('api/books' ,BookList.as_view()),
    path('api/books/<int:pk>', BookDetail.as_view()),
    path('' , include(router.urls)),
]
