from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import inlineformset_factory

from .models import Book, Contributor, Person
from .forms import BookForm, PersonForm



# ============ Home ===============

def home(request, template_name='books_pc_formset2/home.html'):
    books = Book.objects.all()
    persons = Person.objects.all()
    ctx = {
        'books': books,
        'persons': persons,
    }
    return render(request, template_name, ctx)


# ============ Book CRUD ===============

def book_create(request, template_name='books_pc_formset2/book_form.html'):
    InlineFormSet = inlineformset_factory(Book, Contributor, fields=('person', 'contribution'))
    form = BookForm(request.POST or None)
    formset = InlineFormSet(request.POST or None, instance=Book())
    if form.is_valid() and formset.is_valid():
        book = form.save()
        formset.instance = book
        formset.save()
        return redirect('books_pc_formset2:home')
    ctx = {
        'form': form,
        'formset': formset,
    }
    return render(request, template_name, ctx)

def book_update(request, pk, template_name='books_pc_formset2/book_form.html'):
    InlineFormSet = inlineformset_factory(Book, Contributor, fields=('person', 'contribution'))
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    formset = InlineFormSet(request.POST or None, instance=book)
    if form.is_valid() and formset.is_valid():
        book = form.save()
        formset.instance = book
        formset.save()
        return redirect('books_pc_formset2:home')
    ctx = {
        'form': form,
        'formset': formset,
    }
    return render(request, template_name, ctx)

def book_delete(request, pk, template_name='books_pc_formset2/book_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)
    if request.method=='POST':
        book.delete()
        return redirect('books_pc_formset2:home')
    ctx = {
        'book': book,
    }
    return render(request, template_name, ctx)


# ============ Person CRUD ===============

def person_create(request, template_name='books_pc_formset2/person_form.html'):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books_pc_formset2:home')
    ctx = {
        'form': form,
    }
    return render(request, template_name, ctx)

def person_update(request, pk, template_name='books_pc_formset2/person_form.html'):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('books_pc_formset2:home')
    ctx = {
        'form': form,
    }
    return render(request, template_name, ctx)

def person_delete(request, pk, template_name='books_pc_formset2/person_confirm_delete.html'):
    person= get_object_or_404(Person, pk=pk)
    if request.method=='POST':
        person.delete()
        return redirect('books_pc_formset2:home')
    ctx = {
        'person': person,
    }
    return render(request, template_name, ctx)
