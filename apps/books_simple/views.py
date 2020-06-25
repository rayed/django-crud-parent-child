from django.shortcuts import render, redirect, get_object_or_404

from .models import Book
from .forms import BookForm

def home(request, template_name='books_simple/home.html'):
    books = Book.objects.all()
    ctx = {
        'books': books,
    }
    return render(request, template_name, ctx)

def book_create(request, template_name='books_simple/book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books_simple:home')
    ctx = {
        'form': form,
    }
    return render(request, template_name, ctx)

def book_update(request, pk, template_name='books_simple/book_form.html'):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books_simple:home')
    ctx = {
        'form': form,
        'book': book,
    }
    return render(request, template_name, ctx)

def book_delete(request, pk, template_name='books_simple/book_confirm_delete.html'):
    book = get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('books_simple:home')
    ctx = {
        'book': book,
    }
    return render(request, template_name, ctx)
