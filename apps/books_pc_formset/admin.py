from django.contrib import admin
from books_pc_formset.models import Book, Tag


class TagInline(admin.TabularInline):
    model = Tag

class BookAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]

admin.site.register(Book, BookAdmin)