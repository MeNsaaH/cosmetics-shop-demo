""" Custom Context Processors """
from cosmetics.utils import Cart

def cart(request):
    """ Add Cart to context """
    cart = Cart(request)
    return {'cart': cart}

