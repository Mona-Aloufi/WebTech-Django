from django import forms  # Import forms from Django
from . import models  # Import your models
class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['title','author','price','edition']
        title=forms.CharField(
            max_length=100,
            required=True,
            label="Title",
            widget=forms.TextInput(attrs={
                'placeholder':'Title',
                'class':"mycssclass",
                'id':'jsID'
            })
        )
        author=forms.CharField(
            max_length=100,
            required=True,
            label="author",
            widget=forms.TextInput(attrs={
                'placeholder':'author',
                'class':"mycssclass",
                'id':'jsID'
            })
        )
        price=forms.DecimalField(
            required=True,
            label="Price",
            initial=0,
            min_value=0,
            max_value=1000,
            widget=forms.NumberInput(attrs={
              'placeholder': "Current Price"})
        )
        edition=forms.IntegerField(
            required=True,
            label="edition",
            initial=0,
            min_value=0,
            max_value=5,
            
            widget=forms.NumberInput(attrs={ 'placeholder': "Edition"})
        )