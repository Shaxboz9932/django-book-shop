from django.shortcuts import render, redirect
from django.urls import reverse

from .cart import Cart
from book.models import Book
from .forms import CartAddForm

def cart(request):
    cart = Cart(request)
    return render(request, 'cart/index.html', {'cart': cart.cart, 'total_price': cart.get_total_price()})

def cart_add(request, book_slug):
    cart = Cart(request)
    get_book = Book.objects.get(slug=book_slug)
    if request.method == 'POST':
        form = CartAddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            quantity = cd['quantity']
        cart.add(book=get_book, quantity=quantity)
    else:
        form = CartAddForm()
    return redirect(reverse('cart:cart'))

def cart_remove(request, book_slug):
    cart = Cart(request)
    book = Book.objects.get(slug=book_slug)
    cart.remove(book)
    return redirect('cart:cart')

