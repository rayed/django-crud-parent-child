from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Book, Review
from .forms import BookForm, ReviewForm


# ========== Home =========

def home(request, template_name='books_pc_multi_view/home.html'):
    books = Book.objects.all()
    ctx = {
        'books': books,
    }
    return render(request, template_name, ctx)
    

# ========== Book CRUD =========

def book_view(request, pk, template_name='books_pc_multi_view/book_view.html'):
    book= get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book)
    ctx = {
        'book': book,
        'reviews': reviews,
    }
    return render(request, template_name, ctx)

def book_create(request, template_name='books_pc_multi_view/book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books_pc_multi_view:home')
    ctx = {
        'form': form,
    }
    return render(request, template_name, ctx)

def book_update(request, pk, template_name='books_pc_multi_view/book_form.html'):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books_pc_multi_view:home')
    ctx = {
        'form': form,
        'book': book,
    }
    return render(request, template_name, ctx)

def book_delete(request, pk, template_name='books_pc_multi_view/book_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('books_pc_multi_view:home')
    ctx = {
        'object': book,
        'book': book,
    }
    return render(request, template_name, ctx)


# ========== Review CRUD =========

def review_create(request, parent_pk, template_name='books_pc_multi_view/review_form.html'):
    book = get_object_or_404(Book, pk=parent_pk)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.save()
        return redirect('books_pc_multi_view:book_view', parent_pk)
    ctx = {
        'form': form,
        'book': book,
    }
    return render(request, template_name, ctx)

def review_update(request, pk, template_name='books_pc_multi_view/review_form.html'):
    review = get_object_or_404(Review, pk=pk)
    parent_pk = review.book.pk
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('books_pc_multi_view:book_view', parent_pk)
    ctx = {
        'form': form,
        'book': review.book,
    }
    return render(request, template_name, ctx)

def review_delete(request, pk, template_name='books_pc_multi_view/review_confirm_delete.html'):
    review = get_object_or_404(Review, pk=pk)    
    parent_pk = review.book.pk
    if request.method=='POST':
        review.delete()
        return redirect('books_pc_multi_view:book_view', parent_pk)
    ctx = {
        'object': review,
        'book': review.book,
    }
    return render(request, template_name, ctx)
