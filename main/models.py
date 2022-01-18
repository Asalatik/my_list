from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    """
    table of products

    title - name of product
    link - link to online market
    price - price of product
    image - image of product
    money -
    created_at - date and time of createa product
    note - note of product
    product_type - type of product
    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='pic_folder/', null=True, blank=True)
    money = models.CharField(max_length=3, choices=(('EUR', 'EUR'), ('USD', 'USD'), ('RUB', 'RUB')), default='EUR')
    created_at = models.DateTimeField(default=timezone.now)
    note = models.TextField(max_length=1000, default='')
    product_type = models.CharField(max_length=8, choices=(('wh_p', 'wishing'), ('sh_p', 'shopping')), default='wh_p')

    def __str__(self):
        return self.title


class Wishlist(models.Model):
    """
    table for list of presents

    title - name of wishlist
    product - list of products
    is_hidden - hidden or not
    owner - owner of wishlist
    """

    title = models.CharField(max_length=120)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Shoplist(models.Model):
    """
    table for shopping list

    title - name of shopping list
    product - list of products
    is_hidden - hidden or not
    owner - owner of shopping list
    """
    title = models.CharField(max_length=120)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
