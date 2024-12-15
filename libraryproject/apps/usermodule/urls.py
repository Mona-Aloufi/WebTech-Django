from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
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
        #task3
        path('task3/create_product', views.create_product, name='create_product'),
        path('task3/products', views.product_list, name='product_list'),
        path('task3/product/<int:id>', views.product_detail, name='product_detail'),
        path('task3/update_product/<int:id>', views.update_product, name='update_product'),
        path('task3/delete_product/<int:id>', views.delete_product, name='delete_product'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
