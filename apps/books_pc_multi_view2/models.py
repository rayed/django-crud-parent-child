from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_pc_multi_view2:person_edit', kwargs={'pk': self.pk})


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_pc_multi_view2:book_edit', kwargs={'pk': self.pk})


class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    review = models.TextField()

    def __unicode__(self):
        return "Review from: " + self.person

    def get_absolute_url(self):
        return reverse('books_pc_multi_view2:review_edit', kwargs={'pk': self.pk})


