from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from books_pc_multi_view2.models import Person, Book, Review

# ========== Forms =========

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


# ========== Home =========

def home(request, template_name='books_pc_multi_view2/home.html'):
    books = Book.objects.all()
    persons = Person.objects.all()
    ctx = {}
    ctx['books'] = books
    ctx['persons'] = persons
    return render(request, template_name, ctx)
    

# ========== Book CRUD =========

def book_view(request, pk, template_name='books_pc_multi_view2/book_view.html'):
    book= get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book)
    ctx = {}
    ctx["book"] = book
    ctx["reviews"] = reviews
    return render(request, template_name, ctx)

def book_create(request, template_name='books_pc_multi_view2/book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books_pc_multi_view2:home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def book_update(request, pk, template_name='books_pc_multi_view2/book_form.html'):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books_pc_multi_view2:home')
    ctx = {}
    ctx["form"] = form
    ctx["book"] = book
    return render(request, template_name, ctx)

def book_delete(request, pk, template_name='books_pc_multi_view2/book_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('books_pc_multi_view2:home')
    ctx = {}
    ctx["object"] = book
    ctx["book"] = book
    return render(request, template_name, ctx)


# ========== Review CRUD =========

def review_create(request, parent_pk, template_name='books_pc_multi_view2/review_form.html'):
    book = get_object_or_404(Book, pk=parent_pk)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.save()
        return redirect('books_pc_multi_view2:book_view', parent_pk)
    ctx = {}
    ctx["form"] = form
    ctx["book"] = book
    return render(request, template_name, ctx)

def review_update(request, pk, template_name='books_pc_multi_view2/review_form.html'):
    review = get_object_or_404(Review, pk=pk)
    parent_pk = review.book.pk
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('books_pc_multi_view2:book_view', parent_pk)
    ctx = {}
    ctx["form"] = form
    ctx["book"] = review.book
    return render(request, template_name, ctx)

def review_delete(request, pk, template_name='books_pc_multi_view2/review_confirm_delete.html'):
    review = get_object_or_404(Review, pk=pk)    
    parent_pk = review.book.pk
    if request.method=='POST':
        review.delete()
        return redirect('books_pc_multi_view2:book_view', parent_pk)
    ctx = {}
    ctx["object"] = review
    ctx["book"] = review.book
    return render(request, template_name, ctx)


# ============ Person CRUD ===============

def person_create(request, template_name='books_pc_multi_view2/person_form.html'):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books_pc_multi_view2:home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def person_update(request, pk, template_name='books_pc_multi_view2/person_form.html'):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('books_pc_multi_view2:home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def person_delete(request, pk, template_name='books_pc_multi_view2/person_confirm_delete.html'):
    person= get_object_or_404(Person, pk=pk)    
    if request.method=='POST':
        person.delete()
        return redirect('books_pc_multi_view2:home')
    ctx = {}
    ctx["person"] = person
    return render(request, template_name, ctx)
