""" Admin Dashboard View modifications """

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from cosmetics.models import User, Image, Checkout, Review, Product, Category, Tag


class UserCheckoutInline(admin.StackedInline):
    """ Userprofile display on Admin Dashboard """

    model = Checkout
    can_delete = True
    verbose_name_plural = 'checkout'


class ImageInline(admin.StackedInline):
    """ Referral Model display on User Model """

    model = Image
    can_delete = False
    extra = 2


class UserAdmin(admin.ModelAdmin):
    """ Customized User Model display to include user profile and checkout data"""

    list_display = ('username', 'first_name', 'email')
    inlines = (
        UserCheckoutInline,
    )


class ProductAdmin(admin.ModelAdmin):
    """ Product Model Admin """
    list_display = ('name', 'category', 'quantity')
    inlines = (
        ImageInline,
    )


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Review)
