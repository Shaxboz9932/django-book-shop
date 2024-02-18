import stripe
from django.shortcuts import redirect


def checkout(request):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': 'price_1OMmeJHH8TPF8bos3UKaElRM',
                'quantity': 1,
            },
        ],
        mode='subscription',
        success_url='http://127.0.0.1:8000',
        cancel_url='http://127.0.0.1:8000',
    )
    return redirect(checkout_session.url, code=303)