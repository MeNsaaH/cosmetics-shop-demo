""" Shop Cosmetics Models """
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.CharField(max_length=127)
    address = models.TextField()
    city = models.CharField(max_length=127)


class Review(models.Model):
    """ Reviews about specific products """
    rating = models.PositiveSmallIntegerField(default=3)
    name = models.CharField(max_length=64)


class Category(models.Model):
    """ Category Model """
    name = models.CharField(max_length=64)
    description = models.TextField()


class Tag(models.Model):
    """ Tags to add more details to Product """
    name = models.CharField(max_length=64)
    description = models.TextField()


class Product(models.Model):
    """ The Product Model """
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to=_get_product_dir)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    review = models.ManyToManyField(Review, related_name="reviews")
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name="tags")
    other_images = models.FileField(upload_to=_get_product_dir)

    def _get_product_dir(self, instance, filename):
        """ Return the dir to safe an image in. The dir is usually the product id """
        return 'product_{0}/{1}'.format(instance.id, filename)


class Checkout(models.Model):
    """ Checkout Model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    
