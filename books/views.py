from django.shortcuts import render
from . import models

# Create your views here.

def all(req):
    books = models.Book.objects.all()
    return render(req, 'books.html', {'books': books, 'isAll': True})

def get_book_by_id(req, id):
    book = models.Book.objects.get(pk=id)
    return render(req, 'book_detail.html', {'book': book})

def get_author_by_id(req, id):
    author = models.Author.objects.get(pk=id)
    return render(req, 'author_detail.html', {'author': author})

def get_authors_books_by_id(req, id):
    author = models.Author.objects.get(pk=id)
    books = models.Book.objects.filter(author=id)
    return render(req, 'books.html', {'books': books, 'isAll': False, 'author': author})