from django.urls import path
from .views import order_create
from .checkout import checkout

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('checkout/', checkout, name='checkout')
]