from django.urls import path
from .views import cart, cart_add, cart_remove

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<slug:book_slug>', cart_add, name='add'),
    path('remove/<slug:book_slug>/', cart_remove, name='remove')
]
