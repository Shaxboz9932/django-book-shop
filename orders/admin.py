from django.contrib import admin

from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'paid']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
