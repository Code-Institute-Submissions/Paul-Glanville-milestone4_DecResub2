from django.db import models

from products.models import Product
from profiles.models import UserProfile


class ItemReviews(models.Model):

    options = [
        (1, 'poor'),
        (2, 'average'),
        (3, 'good'),
        (4, 'great'),
        (5, 'excellent')
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    header = models.CharField(max_lenght=60, null=False, blank=False)
    comment = models.CharField(max_lenght=1000, null=False, blank=False)
    rating = models.IntegerField(choices=options)
    date_posted = models.DateTimeField(auto_add_now=True)
