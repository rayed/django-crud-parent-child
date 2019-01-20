from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_pc_formset2:person_edit', kwargs={'pk': self.pk})


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_pc_formset2:book_edit', kwargs={'pk': self.pk})


class Contributor(models.Model):
    AUTHOR = 1
    EDITOR = 2
    REVIEWER = 3
    CONTRIBUTION_CHOICES = (
        (AUTHOR, "Author"),
        (EDITOR, "EDITOR"),
        (REVIEWER, "REVIEWER"),
    )
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    contribution = models.IntegerField(choices=CONTRIBUTION_CHOICES)

    def __unicode__(self):
        return "%s %s" % (self.contribution, self.person)

