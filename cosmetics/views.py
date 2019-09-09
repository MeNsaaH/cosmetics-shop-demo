from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def product(request):
    return render(request, 'product-details.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')
