from django.shortcuts import render, redirect
from django.urls import reverse
from cosmetics.models import Product, Category
from django.views.generic import DetailView, ListView, TemplateView


# TODO Switch all implementations to slugs
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
        print(kwargs)
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
        print(product, self.request.POST)
        return redirect(reverse('cosmetics:product', args=(product.slug,)))


class CartView(TemplateView):
    template_name = "cart.html"
    # TODO return items in session


class CheckoutView(TemplateView):
    template_name = "checkout.html"

