from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_pc_multi_view:book_edit', kwargs={'pk': self.pk})


class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    review = models.TextField()

    def __unicode__(self):
        return "Review from: " + self.name

    def get_absolute_url(self):
        return reverse('books_pc_multi_view:review_edit', kwargs={'pk': self.pk})


