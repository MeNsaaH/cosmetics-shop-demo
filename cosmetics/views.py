from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView
from cosmetics.models import Product, Category
from cosmetics.utils import Cart


class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "products"
    # TODO Return products with highest ratings or newly added
    queryset = Product.objects.all()


class ShopView(ListView):
    model = Category
    template_name = "shop.html"
    context_object_name = "categories"
    queryset = Category.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if kwargs.get('categories'):
            context['products'] = Product.objects.filter(category=kwargs['category'])
        else:
            context['products'] = Product.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product-details.html"
    context_object_name = "product"
    query_pk_and_slug = True

    def post(self, *args, **kwargs):
        product = self.get_object()
        quantity = int(self.request.POST.get('quantity', 0))
        cart = Cart(self.request)
        cart.add(product, quantity)
        messages.success(self.request, f'{product} has being added to cart')
        return redirect(reverse('cosmetics:product', args=(product.slug,)))


class CartView(TemplateView):
    template_name = "cart.html"


class CheckoutView(TemplateView):
    template_name = "checkout.html"

    def post(self, *args, **kwargs):
        cart = Cart(self.request)
        cart.checkout()
        messages.success(self.request, f'Your Order is on Your Way.\nThank You for shopping with us')
        return redirect(reverse('cosmetics:index'))
