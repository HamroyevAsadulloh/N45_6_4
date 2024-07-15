from django.urls import path
from .views import login_views,register_views,logout_views,account_main_views,account_about_views,account_books_views

urlpatterns = [
    path('login/', login_views, name='login'),
    path('register/', register_views, name='register'),
    path('logout/', logout_views, name='logout'),
    path('account/', account_main_views, name='account'),
    path('account/about/', account_about_views, name='account-about'),
    path('account/books/', account_books_views, name='account-books')
]