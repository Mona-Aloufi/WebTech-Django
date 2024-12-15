from django.db import models



# Define the Address model
class Address(models.Model):
    city = models.CharField(max_length=100)  # City as a string

    def __str__(self):
        return self.city

# Define the Student model
class Student(models.Model):
    name = models.CharField(max_length=100)  # Name of the student
    age = models.IntegerField()  # Age of the student
    address = models.ForeignKey(Address, on_delete=models.CASCADE)  # Foreign key to Address

    def __str__(self):
        return self.name

# Task 2: Suppose the relation between students and addresses is many-to-many, in which a student can have multiple addresses, and one address can be associated with many students. In this task, the code in the previous task should be copied and modified to implement many-to-many relationships.
# Note: If needed, student or address models should be copied and renamed to, for example, student2 or address2.
class Address2(models.Model):
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.city
class Student2(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.ManyToManyField(Address2,related_name="students")
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name