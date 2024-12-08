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

