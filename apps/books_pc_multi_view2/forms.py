from django.forms import ModelForm

from .models import Person, Book, Review

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pages']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['person', 'review']