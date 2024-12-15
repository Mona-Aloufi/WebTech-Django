
from django.shortcuts import redirect,render,get_object_or_404
from .models import Student,Student2,Address2
from django.db.models import Count
from .forms import StudentForm,Student2Form
from .models import Student2, Address2
from .forms import Student2Form
def students_by_city(request):
    # Count the number of students for each city
    city_counts = Student.objects.values('address__city') \
                                  .annotate(student_count=Count('id')) \
                                  .order_by('address__city')
    
    return render(request, 'usermodule/students_by_city.html', {'city_counts': city_counts})
def one_student(request,id):
    obj=Student.objects.get(id=id)
    return render(request,"usermodule/student_info.html",{"student":obj})
def list_Student(request):
    obj=Student.objects.all()
    return render(request,"usermodule/list.html",{"student":obj})
def add_student(request):
    student=None
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            obj=form.save()
            return redirect('one_student',id=obj.id)
    else:
        form=StudentForm()
    return render(request,"usermodule/add.html",{'form':form})

def update_student(request,id):
    obj=Student.objects.get(id=id)
    form=StudentForm(instance=obj)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=obj)
        if form.is_valid():
            obj.save()
            return redirect('one_student',id=obj.id)
    else:
        form=StudentForm(instance=obj)
    return render(request,"usermodule/update.html",{'form':form})

def DeleteStudent(request,Sid):
    obj=Student.objects.get(id=Sid)
    if request.method=="POST":
        obj.delete()
        return redirect("list_Student")
    return render(request,'usermodule/deleteStudent.html',{'student':obj})


def add_student_task2(request):
    if request.method == "POST":
        form = Student2Form(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)  # Save the student object but not the M2M relation
            obj.save()
            form.save_m2m()  # Save the many-to-many data
            new_address = form.cleaned_data.get('new_address')
            if new_address:
                address, created = Address2.objects.get_or_create(city=new_address)
                obj.address.add(address)  # Add the new address to the student
            return redirect('one_student_task2', id=obj.id)
    else:
        form = Student2Form()
    return render(request, "usermodule/add2.html", {'form': form})


def update_student_task2(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == "POST":
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            new_address = form.cleaned_data.get('new_address')
            if new_address:
                address, created = Address2.objects.get_or_create(city=new_address)
                obj.address.add(address)
            return redirect('one_student_task2', id=student.id)
    else:
        form = Student2Form(instance=student)

    # Pass the student object to the template
    return render(request, "usermodule/update2.html", {'form': form, 'student': student})


def list_Student_task2(request):
    students = Student2.objects.all()
    return render(request, "usermodule/list2.html", {"students": students})


def one_student_task2(request, id):
    student = get_object_or_404(Student2, id=id)
    return render(request, "usermodule/student_info2.html", {"student": student})


def DeleteStudent_task2(request, Sid):
    student = get_object_or_404(Student2, id=Sid)
    
    if request.method == "POST":
        student.delete()
        return redirect('list_Student_task2')
    
    return render(request, 'usermodule/deleteStudent2.html', {'student': student})
