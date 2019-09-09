"""cosmetics URL Configuration
"""

from django.urls import path
from cosmetics import views

app_name = 'cosmetics' 

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
