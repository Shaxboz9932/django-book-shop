from decimal import Decimal

from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from django.urls import reverse

from orders.models import Order

stripe.api_key = 'sk_test_51OLPmUHH8TPF8bosfTl718elKHVhXAci5G6BtgGmKgJ3BLG8dP4wnRr5FMYnVv2ITvkiPGY5FU6B35531eZaF7di00sMWLVagM'
stripe.api_version = '2023-10-16'


def payment_process(request, order_id):
    order = Order.objects.get(pk=order_id)
    if request.method == 'POST':

        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,
            'success_url': 'http://127.0.0.1:8000',
            'cancel_url': 'http://127.0.0.1:8000',
            'line_items': []
        }
        # add order items to the Stripe checkout session
        for item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.price/item.quantity * Decimal('100')),
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product,
                    },
                },
                'quantity': item.quantity,
            })
        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303)
    else:
        return render(request, 'payments/process.html', {'order_id': order.pk})

def payment_completed(request):
    return render(request, 'payments/completed.html')

def payment_canceled(request):
    return render(request, 'payments/canceled.html')
