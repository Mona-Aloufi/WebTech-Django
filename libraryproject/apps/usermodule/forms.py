from django import forms
from . import models
from .models import Student2, Address2, Student,Product

class StudentForm(forms.ModelForm):

    new_address = forms.CharField(
        max_length=100,
        required=False,
        label="New Address",
        widget=forms.TextInput(attrs={
            'placeholder': 'Add a new address (if not in list)',
            'class': 'form-control'
        })
    )

    class Meta:
        model = models.Student
        fields = ['name', 'age', 'address']

        name=forms.CharField(
            max_length=100,
            required=True,
            label="Name",
            widget=forms.TextInput(attrs={
                'placeholder':'Title',
                
            })
        )
        widgets = {
    'age': forms.NumberInput(attrs={
        'placeholder': 'Enter age',
        'class': 'form-control',
        'min': 18,
        'max': 75,
    }),
}

        address=forms.CharField(
            max_length=100,
            required=True,
            label="address",
            widget=forms.TextInput(attrs={
                'placeholder':'address',
                
            })
        )



class Student2Form(forms.ModelForm):
    new_address = forms.CharField(
        max_length=100,
        required=False,
        label="New Address",
        widget=forms.TextInput(attrs={
            'placeholder': 'Add a new address (if not in list)',
            'class': 'form-control',
        })
    )

    class Meta:
        model = Student2
        fields = ['name', 'age', 'address']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter age',
                'class': 'form-control',
                'min': 18,
                'max': 75,
            }),
            'address': forms.CheckboxSelectMultiple(),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']