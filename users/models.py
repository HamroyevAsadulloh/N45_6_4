from django.db import models
from book.models import Book
from django.contrib.auth.models import User


class UserBook(models.Model):
    book = models.ManyToManyField(Book, null=True)
    user = models.ManyToManyField(User, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class BasketBooks(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(default=0)
    total_price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_total_price(instance, obj):
        obj.total_price = obj.book.price * obj.count