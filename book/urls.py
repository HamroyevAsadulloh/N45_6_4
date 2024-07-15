from django.urls import path
from .views import home, books,book_detail

urlpatterns = [
    path('', home, name='home'),
    path('books/', books, name='books'),
    path('book/<slug:slug>', book_detail, name='book_detail'),
]
















