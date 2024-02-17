from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import Book, Category
from .forms import UserRegisterForm, UserLoginForm
from cart.forms import CartAddForm


def index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books': books})

def get_books(request, book_slug):
    get_book = Book.objects.get(slug=book_slug)
    cart_add_form = CartAddForm()
    return render(request, 'book/detail.html', {'get_book': get_book, 'cart_add_form': cart_add_form})

def get_category(request, category_id):
    get_book = Book.objects.filter(category_id=category_id)
    category = Book.objects.get(pk=category_id)
    return render(request, 'book/category.html', {'category': category, 'get_book': get_book})

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:login')
    else:
        form = UserRegisterForm()
    return render(request, 'book/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book:home')
    else:
        form = UserLoginForm()
    return render(request, 'book/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('book:home')
