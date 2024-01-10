import json

from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    data = Book.objects.all()
    return render(request, template, context={'books': data})


def books_on_date(request, dt):
    template = 'books/books_list.html'
    content = Book.objects.values('pub_date').filter('pub_date')
    paginator = Paginator(content, 1)
    context = {
        'page': paginator
    }
    return render(request, template, context={'books': content})