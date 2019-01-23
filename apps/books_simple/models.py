from django.db import models
from django.urls import reverse

class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_simple:book_edit', kwargs={'pk': self.pk})