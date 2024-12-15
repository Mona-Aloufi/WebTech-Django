from django.urls import path
from . import views
urlpatterns = [
    path('students_by_city/', views.students_by_city, name='students_by_city'),
    path('add/', views.add_student, name='add_student'),
    path('one_student/<int:id>', views.one_student, name='one_student'),
    path('list_student', views.list_Student, name='list_Student'),
    path('update/<int:id>', views.update_student, name='update_student'),
    path('DeleteStudent/<int:Sid>', views.DeleteStudent, name='DeleteStudent'),
    #task2
        path('task2/one_student/<int:id>', views.one_student_task2, name='one_student_task2'),
        path('task2/list_student', views.list_Student_task2, name='list_Student_task2'),
        path('task2/add/', views.add_student_task2, name='add_student_task2'),
        path('task2/update/<int:id>', views.update_student_task2, name='update_student_task2'),
        path('task2/DeleteStudent/<int:Sid>', views.DeleteStudent_task2, name='DeleteStudent_task2'),
]
