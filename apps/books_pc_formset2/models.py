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


class Contributor(models.Model):
    AUTHOR = 1
    EDITOR = 2
    REVIEWER = 3
    CONTRIBUTION_CHOICES = (
        (AUTHOR, "Author"),
        (EDITOR, "Editor"),
        (REVIEWER, "Reviewer"),
    )
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    contribution = models.IntegerField(choices=CONTRIBUTION_CHOICES)

    def __str__(self):
        return "%s %s" % (self.contribution, self.person)

