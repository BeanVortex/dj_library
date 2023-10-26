from django.db import models

# Create your models here.

class Shelf(models.Model):
    number=models.IntegerField(null=False)
    hall=models.CharField(null=False, max_length=200)

class Author(models.Model):
    first_name=models.CharField(null=False, max_length=200)
    last_name=models.CharField(null=False, max_length=200)
    nationality=models.CharField(null=True, max_length=200)
    

class Book(models.Model):
    title=models.CharField(null=False, max_length=200)
    year=models.IntegerField(null=True)
    publisher=models.CharField(null=False, max_length=200)
    isbn=models.IntegerField(null=True)
    language=models.CharField(null=False, max_length=200)
    author=models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    shelf=models.ForeignKey(Shelf, on_delete=models.CASCADE)
    