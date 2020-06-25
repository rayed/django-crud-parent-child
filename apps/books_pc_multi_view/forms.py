from django.forms import ModelForm

from .models import Book, Review

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pages']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review']