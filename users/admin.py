from django.contrib import admin
from .models import UserBook,BasketBooks


admin.site.register([UserBook,BasketBooks])

# @admin.register(UserBook)
# class UserBooksAdmin(admin.ModelAdmin):
#     list_display = ('id', 'book', 'user')
#
# @admin.register(BasketBooks)
# class BasketBooksAdmin(admin.ModelAdmin):
#     list_display = ('id', 'book', 'user')
