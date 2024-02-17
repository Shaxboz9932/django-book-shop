from django.conf import settings

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART)
        if not cart:
            cart = self.session[settings.CART] = {}
        self.cart = cart

    def add(self, book, quantity):
        self.cart[book.title] = {
            'title': book.title,
            'quantity': quantity,
            'image': book.photo.url,
            'slug': book.slug,
            'price': float(book.price),
            'total_price': float('%.2f' % (book.price * int(quantity)))
        }
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, book):
        del self.cart[book.title]
        self.save()

    def get_total_price(self):
        return '%.2f' % sum(float(i['total_price']) for i in self.cart.values())
