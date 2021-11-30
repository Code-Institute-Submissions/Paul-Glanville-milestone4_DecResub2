from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Product(models.Model):
    name = models.CharField(max_length=255)
    product = models.ManyToManyField(Product, related_name='products')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


class ItemWishlist(models.Model):

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    header = models.CharField(max_length=60, null=False, blank=False)
    comment = models.CharField(max_length=1000, null=False, blank=False)
    rating = models.IntegerField(choices=options)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header
