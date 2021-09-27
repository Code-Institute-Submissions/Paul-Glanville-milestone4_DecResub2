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

    user =
    product =
    header =
    comment =
    rating =
    date_posted =
