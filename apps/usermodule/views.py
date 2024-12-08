
from django.shortcuts import render
from .models import Student
from django.db.models import Count
def students_by_city(request):
    # Count the number of students for each city
    city_counts = Student.objects.values('address__city') \
                                  .annotate(student_count=Count('id')) \
                                  .order_by('address__city')
    
    return render(request, 'usermodule/students_by_city.html', {'city_counts': city_counts})
