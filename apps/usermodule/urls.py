from django.urls import path
from . import views
urlpatterns = [
    path('students_by_city/', views.students_by_city, name='students_by_city'),
]
