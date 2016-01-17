from django.contrib import admin
from books_pc_formset2.models import Book, Person, Contributor


class ContributorInline(admin.TabularInline):
    model = Contributor

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ContributorInline,
    ]

admin.site.register(Book, BookAdmin)
admin.site.register(Person)
