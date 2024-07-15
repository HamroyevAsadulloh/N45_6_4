from django.contrib import admin
from .models import Book,Authors,Comments
from import_export.admin import ImportExportModelAdmin

@admin.register(Authors)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "email", "gender")
    list_display_links = ("first_name", "last_name")
    search_fields = ('first_name', 'last_name')
    # ordering = ('gender')


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "slug", "description", "author", "image", "count", "price", "created_date")
    list_display_links = ("id", "title", "slug", "description", "author", "image", "count", "price", "created_date")
    prepopulated_fields = {'slug': ('title',)}