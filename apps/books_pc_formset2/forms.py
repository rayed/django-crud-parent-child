from django.forms import ModelForm

from .models import Book, Person

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pages']

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email']