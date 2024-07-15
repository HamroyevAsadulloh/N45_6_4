from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect


def login_views(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, "auth/login.html", context={'message':'Username or password invalid'})
    return render(request, 'auth/login.html')


def register_views(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            return render(request, "auth/register.html", context={'message_password': 'Error password'})
        else:
            if User.objects.filter(username=username).exists():
                return render(request, "auth/register.html", context={'message': 'User already exists'})
            new_user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            new_user.set_password(password)
            new_user.save()
            return redirect('login')

    return render(request, 'auth/register.html')

def logout_views(request):
    logout(request)
    return redirect('home')

def account_main_views(request):
    return render(request, 'account/main.html')

def account_about_views(request):
    return render(request, 'account/main.html')


def account_books_views(request):
    user_id = request.user.id
    active_books = UserBook.objects.filter(user=user_id)
    return render(request, 'account/active_books.html', {"active_books":active_books})