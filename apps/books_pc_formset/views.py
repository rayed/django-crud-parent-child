from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from books_pc_formset.models import Book, Tag

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pages']

def book_list(request, template_name='books_pc_formset/book_list.html'):
    book = Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

def book_create(request, template_name='books_pc_formset/book_form.html'):
    InlineFormSet = inlineformset_factory(Book, Tag, fields=('name', 'weight'))
    form = BookForm(request.POST or None)
    formset = InlineFormSet(request.POST or None, instance=Book())
    if form.is_valid():
        book = form.save()
        formset.instance = book
        if formset.is_valid():
            formset.save()
            return redirect('books_pc_formset:book_list')
    return render(request, template_name, {'form':form, 'formset':formset})

def book_update(request, pk, template_name='books_pc_formset/book_form.html'):
    InlineFormSet = inlineformset_factory(Book, Tag, fields=('name', 'weight'))
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    formset = InlineFormSet(request.POST or None, instance=book)
    if form.is_valid():
        book = form.save()
        formset.instance = book
        if formset.is_valid():
            formset.save()
            return redirect('books_pc_formset:book_list')
    return render(request, template_name, {'form':form, 'formset':formset})

def book_delete(request, pk, template_name='books_pc_formset/book_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('books_pc_formset:book_list')
    return render(request, template_name, {'object':book})
