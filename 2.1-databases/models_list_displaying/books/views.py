import json

from django.shortcuts import render

from books.models import Book


def books_view(request):
    #with open('books.json') as file:
        #book = json.load(file)
        #for boo in book:
            #books1 = Book(id=boo['id'],
                           #name=boo['name'],
                           #price=boo['price'],
                           #image=boo['image'],
                           #release_date=boo['release_date'],
                           #lte_exists=boo['lte_exists'],
                           #)
            #books1.save()
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)
