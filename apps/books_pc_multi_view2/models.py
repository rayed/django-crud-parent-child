from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    review = models.TextField()

    def __str__(self):
        return "Review from: " + self.person.name
