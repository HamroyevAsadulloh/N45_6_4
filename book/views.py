from django.shortcuts import render
from .models import Book,Authors
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    books = Book.objects.all()[:5]
    return render(request, 'home.html', context={'books':books})



def books(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(title__icontains=search) | Book.objects.filter(author__first_name__icontains=search)
        if books:
            return render(request, 'books.html', {'books': books, 'value': search, 'message':"Successfully"})
        else:
            return render(request, 'books.html', {'message':"Not Fount"})

    books = Book.objects.all()
    context = {'all_books': books}
    return render(request, 'books.html', {'books':books})


@login_required()
def book_detail(request, slug):
    book = Book.object.get(slug=slug)
    if book:
        return render(request, 'book_detail.html', {'book': book, 'message': 'Successfully'})
    else:
        return render(request, 'book_detail.html', {'book': book, 'message': 'Not found'})























# def authors(request):
#     if request.method == 'POST':
#         search = request.POST['search']
#         authors = Authors.objects.filter(name__icontains=search)
#         if authors:
#             return render(request, 'authors.html', {'authors': books, 'value': search, 'message': "Successfully"})
#         else:
#             return render(request, 'authors.html', {'message': "Not Fount"})
#     authors = Authors.objects.all()
#     context = {'all_authors': authors}
#     return render(request, 'authors.html', {'authors':authors})
