from django.shortcuts import render


def index(request):
    # TODO Return products with highest ratings or newly added
    return render(request, 'index.html')

def shop(request):
    # TODO return Categories
    # TODO Random Products
    return render(request, 'shop.html')

def product(request):
    # TODO Return product specified by id
    return render(request, 'product-details.html')

def cart(request):
    # TODO return items in session
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')
