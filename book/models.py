from django.db import models
from .helpers import SaveMedia
from django.contrib.auth.models import User

class Authors(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, null=True)
    age = models.PositiveIntegerField()
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()


class Book(models.Model):
    title = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    description = models.TextField()
    author = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to=SaveMedia.save_book_image_path, null=True)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



























