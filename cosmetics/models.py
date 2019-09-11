""" Shop Cosmetics Models """
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ User Model """
    country = models.CharField(max_length=127)
    address = models.TextField()
    city = models.CharField(max_length=127)

    def __str__(self):
        return f"{self.username}"


class Review(models.Model):
    """ Reviews about specific products """
    rating = models.PositiveSmallIntegerField(default=3)
    title = models.CharField(max_length=64, blank=True)
    comment = models.TextField(null=True)

    def __str__(self):
        return f"{self.rating}"


class Category(models.Model):
    """ Category Model """
    name = models.CharField(max_length=64)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    """ Tags to add more details to Product """
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


def get_product_dir(instance, filename):
    """ Return the dir to safe an image in. The dir is usually the product id """
    ext = filename.split(".")[-1]
    return f"product_{instance.id}/picture.{ext}"

def get_images_product_dir(instance, filename):
    """ Return the dir to safe an image in. The dir is usually the product id """
    no_images = Image.objects.filter(product=instance.product).count()
    ext = filename.split(".")[-1]
    return f"product_{instance.product.id}/images/{no_images+1}.{ext}"

class Product(models.Model):
    """ The Product Model """
    name = models.CharField(max_length=256)
    picture = models.ImageField(upload_to=get_product_dir)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    review = models.ManyToManyField(Review, related_name="reviews", blank=True)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return f"{self.name} - {self.amount}"

class Image(models.Model):
    """ Stores extra image about a particular product """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    # TODO Refactor to save in product id folder
    image = models.FileField(upload_to=get_images_product_dir)
    description = models.TextField()


class Checkout(models.Model):
    """ Checkout Model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    
