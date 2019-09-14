""" Utility Functions and Classes """
from django.db.models import Sum
from cosmetics.models import Cart as CartModel, CartItem

class Cart:
    def __init__(self, request):
        cart_id = request.session.get('CART-ID', None)
        self.request = request
        if cart_id:
            self.cart, _  = CartModel.objects.get_or_create(id=cart_id, checked_out=False)
        else:
            self.cart = CartModel.objects.create(checked_out=False)
            request.session['CART-ID'] = self.cart.id

    def __iter__(self):
        return iter(self.cart.items.all())

    def add(self, product, quantity):
        item = CartItem.objects.get_or_create(
            product=product, 
            cart=self.cart, 
            defaults={'quantity': quantity}
        )
        return item
    
    def remove(self, product):
        CartItem.objects.get(product=product, cart=self.cart).delete()

    def length(self):
        return self.cart.items.all().count()

    def total(self):
        return self.cart.items.all().aggregate(Sum('product__amount'))['product__amount__sum']

    def checkout(self):
        self.cart.checked_out = True
        self.cart.save()
        del self.request.session['CART-ID']
#         self.request.session.flust()

