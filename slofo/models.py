from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    publishers = models.ManyToManyField("Publisher", through="Book")

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)