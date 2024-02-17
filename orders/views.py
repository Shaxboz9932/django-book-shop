from django.shortcuts import render

from book.models import Book
from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart.cart.values():
                OrderItem.objects.create(
                    order=order,
                    product=Book.objects.get(title=item['title']),
                    price=item['total_price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart.cart, 'form': form})
