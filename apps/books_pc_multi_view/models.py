from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    review = models.TextField()

    def __str__(self):
        return "Review from: " + self.name
